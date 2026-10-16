from common import *
import pandas as pd,numpy as np,shutil
from concurrent.futures import ThreadPoolExecutor

def main():
 plan=read('outputs/selection-plan.json');rows=read('outputs/data-inventory.json');lookup={r['directory']:r for r in rows}
 names=plan['train']+plan['development']+plan['holdout']
 total=sum(lookup[n]['required_bytes'] for n in names);assert total<plan['resource_cap_bytes'];print('Required source bytes:',total,flush=True)
 tasks=[(n,t) for n in names for t in ['subjects','items','responses']]
 def fetch(task):
  n,t=task;rel=f'{n}/formatted_tables/{t}.parquet';prev=OLD/'data'/rel;dest=ROOT/'data'/rel
  if prev.exists():dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(prev,dest)
  else:download(rel,plan['per_table_cap_bytes'])
 with ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(fetch,tasks))
 frames=[];audits=[];profiles={};item_index=[]
 for n in names:
  base=ROOT/'data'/n/'formatted_tables';s=pd.read_parquet(base/'subjects.parquet');i=pd.read_parquet(base/'items.parquet');r=pd.read_parquet(base/'responses.parquet')
  assert s.subject_id.is_unique and i.item_id.is_unique
  assert set(r.subject_id)<=set(s.subject_id) and set(r.item_id)<=set(i.item_id)
  assert set(r.benchmark_id)=={lookup[n]['catalog']['benchmark_id']}
  nraw=len(r);dups=int(r.response_id.duplicated().sum())
  if dups:
   assert all(len(x.astype(str).drop_duplicates())==1 for _,x in r[r.response_id.duplicated(False)].groupby('response_id'))
   r=r.drop_duplicates('response_id')
  missing=int(r.response.isna().sum());bad=int((r.response.notna()&~r.response.isin([0,1])).sum())
  r=r[r.response.isin([0,1])].copy()
  attrs={row.subject_id:{a:('' if pd.isna(getattr(row,a)) else str(getattr(row,a))) for a in ATTRS} for row in s.itertuples()}
  sk={sid:sha(json.dumps(v,sort_keys=True)) for sid,v in attrs.items()};profiles.update({sk[sid]:a for sid,a in attrs.items()})
  empty=i.content.isna()|i.content.fillna('').str.strip().eq('');i=i[~empty].copy();i['content_group']=i.content.map(lambda x:sha(norm(x)))
  # Connected components link matching content OR matching nonempty native raw item IDs.
  parent={x:x for x in i.content_group}
  def root(x):
   while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
   return x
  for _,g in i[i.raw_item_id.notna()&i.raw_item_id.fillna('').astype(str).str.strip().ne('')].groupby('raw_item_id'):
   keys=list(g.content_group);a=root(keys[0])
   for k in keys[1:]:parent[root(k)]=a
  i['item_group']=i.content_group.map(root)
  item_index.extend({'benchmark':n,'item_id':x.item_id,'content_group':x.content_group,'item_group':x.item_group} for x in i.itertuples())
  r=r[r.item_id.isin(i.item_id)].merge(i[['item_id','item_group','content_group']],on='item_id',validate='many_to_one');r['subject_key']=r.subject_id.map(sk);r['benchmark']=n
  r['split']='train' if n in plan['train'] else 'development' if n in plan['development'] else 'holdout'
  r['family']=lookup[n]['source_family']
  audits.append({'benchmark':n,'split':r['split'].iloc[0] if len(r) else None,'raw_rows':nraw,'missing_labels':missing,'nonbinary_labels':bad,'duplicate_response_ids_removed':dups,'empty_items_removed':int(empty.sum()),'duplicate_content_aliases':len(i)-i.content_group.nunique(),'content_or_rawid_aliases':len(i)-i.item_group.nunique(),'repeated_subject_item_rows':int(r.duplicated(['subject_key','item_id']).sum()),'repeated_subject_group_rows':int(r.duplicated(['subject_key','item_group']).sum()),'native_subjects':len(s),'full_visible_profiles':len(set(sk.values()))})
  frames.append(r[['subject_id','item_id','response_id','response','trial','benchmark','subject_key','item_group','content_group','split','family']])
  print('Prepared metadata',n,len(r),flush=True)
  del s,i,r
 allrows=pd.concat(frames,ignore_index=True);del frames
 idx=pd.DataFrame(item_index);cross=idx.groupby('content_group').benchmark.nunique();cross=set(cross[cross>1].index)
 # Drop complete linked components if any alias crosses benchmark boundaries.
 badgroups=set(map(tuple,idx[idx.content_group.isin(cross)][['benchmark','item_group']].to_numpy()))
 drop=np.array([(b,g) in badgroups for b,g in zip(allrows.benchmark,allrows.item_group)])
 dropped=int(drop.sum());allrows=allrows[~drop].copy()
 counts=allrows.groupby(['benchmark','subject_key']).item_group.nunique();ok=set(counts[counts>=80].index)
 allrows=allrows[[(b,s) in ok for b,s in zip(allrows.benchmark,allrows.subject_key)]].copy()
 pairs=allrows.groupby('benchmark').subject_key.nunique();kept=set(pairs[pairs>=2].index);allrows=allrows[allrows.benchmark.isin(kept)].copy()
 manifest={split:[n for n in plan[split] if n in kept] for split in ['train','development','holdout']}
 for a in audits:
  q=allrows[allrows.benchmark==a['benchmark']];a.update(eligible_rows=len(q),eligible_pairs=q.subject_key.nunique(),eligible_groups_across_pairs=len(q[['subject_key','item_group']].drop_duplicates()),status='INCLUDED' if len(q) else 'COVERAGE_EXCLUDED')
 save('outputs/preparation-audit.json',audits);save('outputs/subject-profiles.json',profiles)
 save('outputs/split-manifest.json',{'splits':manifest,'source_bytes':total,'excluded_candidates':[n for n in names if n not in kept],'cross_benchmark_content_groups':len(cross),'cross_benchmark_rows_removed':dropped,'families':{n:lookup[n]['source_family'] for n in names},'domains':{n:lookup[n]['catalog']['domain'] for n in names},'coverage':{split:{'benchmarks':len(ns),'pairs':sum(a['eligible_pairs'] for a in audits if a['benchmark'] in ns),'observations':sum(a['eligible_rows'] for a in audits if a['benchmark'] in ns),'unique_subject_profiles':allrows[allrows.benchmark.isin(ns)].subject_key.nunique()} for split,ns in manifest.items()}})
 if len(manifest['holdout'])<8 or len(manifest['development'])<3 or len(manifest['train'])<12:
  save('outputs/STOP.json',{'status':'INCONCLUSIVE','reason':'Frozen coverage gate failed'});return
 allrows.to_parquet(ROOT/'data/eligible-responses.parquet',index=False)
 print(json.dumps(read('outputs/split-manifest.json')['coverage'],indent=2))
if __name__=='__main__':main()
