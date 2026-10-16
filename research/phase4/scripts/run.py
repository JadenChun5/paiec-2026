from common import *
import numpy as np,pandas as pd,importlib.util,itertools
METHODS=['constant','empirical','beta','eb']
def interval(matrix,counts):
 # Rows are whole benchmark clusters; supports vector-valued budget diagnostics.
 rng=np.random.default_rng(202610104);ix=rng.integers(len(counts),size=(10000,len(counts)))
 bs=np.asarray(matrix)[ix].sum(axis=1)/np.asarray(counts)[ix].sum(axis=1).reshape((-1,)+(1,)*(np.asarray(matrix).ndim-1))
 return np.quantile(bs,[.025,.975],axis=0).T.tolist()
def summarize(df):
 w=np.array(read('outputs/protocol.json')['weights']);budgets=[0,1,3,7,15,31]
 pair=df.groupby(['benchmark','subject_key','method','budget'],sort=True).agg(brier=('brier','mean'),ece=('ece','mean'),endpoint_mass=('endpoint','mean')).reset_index()
 pair['weighted_brier']=pair.brier*pair.budget.map(dict(zip(budgets,w)));pair['weighted_ece']=pair.ece*pair.budget.map(dict(zip(budgets,w)))
 alc=pair.groupby(['benchmark','subject_key','method']).agg(alc=('weighted_brier','sum'),ece_alc=('weighted_ece','sum')).reset_index()
 pivot=alc.pivot(index=['benchmark','subject_key'],columns='method',values='alc');diff=pivot.beta-pivot.eb
 sums=diff.groupby('benchmark').sum();counts=diff.groupby('benchmark').size();ci=interval(sums.values,counts.values)
 if len(sums)<=12:signs=np.array(list(itertools.product([-1,1],repeat=len(sums))))
 else:signs=np.random.default_rng(202610105).choice([-1,1],size=(100000,len(sums)))
 p=float(np.mean(np.abs(signs@sums.to_numpy())>=abs(sums.sum())-1e-14))
 effect=float(diff.mean());classification='NEGATIVE' if effect<=0 else 'SUPPORTED' if ci[0]>0 and p<.05 else 'SUGGESTIVE'
 perbench=pivot.groupby('benchmark').mean().reset_index();perbench['beta_minus_eb']=perbench.beta-perbench.eb;perbench['pairs']=perbench.benchmark.map(counts)
 bybudget=[]
 for budget in budgets:
  pp=pair[pair.budget==budget].pivot(index=['benchmark','subject_key'],columns='method',values='brier');dd=pp.beta-pp.eb;ss=dd.groupby('benchmark').sum();nn=dd.groupby('benchmark').size()
  bybudget.append({'budget':budget,**{m:float(pp[m].mean()) for m in METHODS},'beta_minus_eb':float(dd.mean()),'ci95':interval(ss.values,nn.values),'weighted_contribution':float(dd.mean()*w[budgets.index(budget)])})
 secondary={}
 for control in ['empirical','constant']:
  dd=pivot[control]-pivot.eb;ss=dd.groupby('benchmark').sum();nn=dd.groupby('benchmark').size();secondary[control+'_minus_eb']={'difference':float(dd.mean()),'ci95':interval(ss.values,nn.values)}
 return {'alc':{m:float(pivot[m].mean()) for m in METHODS},'primary_difference':effect,'ci95':ci,'signflip_p':p,'classification':classification,'benchmark_clusters':len(sums),'pairs':len(pivot),'benchmarks_improving':int((perbench.beta_minus_eb>0).sum()),'by_budget':bybudget,'secondary':secondary,'ece_alc':alc.groupby('method').ece_alc.mean().to_dict(),'leave_one_benchmark_out_difference':{b:float((diff.sum()-sums[b])/(len(diff)-counts[b])) for b in sums.index}},pair,alc,perbench

def main():
 assert not (ROOT/'outputs/results.json').exists()
 p=read('outputs/protocol.json');prior=read('outputs/learned-prior.json');profiles=read('outputs/subject-profiles.json');m=read('outputs/split-manifest.json')
 assert prior['protocol_sha256']==sha((ROOT/'outputs/protocol.json').read_bytes())
 spec=importlib.util.spec_from_file_location('official',str(ROOT.parents[1]/'third_party/paiec_baseline/empirical_mean/model.py'));official=importlib.util.module_from_spec(spec);spec.loader.exec_module(official)
 assert sha(Path(spec.origin).read_bytes())==p['official_baseline_sha256']
 data=pd.read_parquet(ROOT/'data/eligible-responses.parquet');assert sha((ROOT/'data/eligible-responses.parquet').read_bytes())==p['data_sha256']
 trainkeys=set(data[data.split=='train'].subject_key);trainnames={norm(profiles[k]['normalized_name']) for k in trainkeys if profiles[k]['normalized_name']}
 lookup={(b,s):q for (b,s),q in data.groupby(['benchmark','subject_key'])};records=[];trajectories=[];memberships=[];calls=0
 a,beta=prior['alpha'],prior['beta']
 for pool in read('outputs/frozen-pools.json'):
  b,s=pool['benchmark'],pool['subject_key'];q=lookup[b,s];target=q[q.item_group.isin(pool['evaluation_groups'])];y=target.response.to_numpy();rate=float(y.mean());groups={g:f.sort_values('response_id') for g,f in q[q.item_group.isin(pool['acquisition_groups'])].groupby('item_group')}
  attrs=profiles[s];item={'benchmark_id':'anonymous::'+b,'item_content':'','item_features':'','interactors':''}
  memberships.append({'benchmark':b,'subject_key':s,'split':pool['split'],'source_subject_ids':sorted(q.subject_id.unique()),'profile':attrs,'eligible_responses':len(q),'target_responses':len(y),'target_groups':target.item_group.nunique(),'familiar_profile':s in trainkeys,'familiar_model_name':bool(attrs['normalized_name']) and norm(attrs['normalized_name']) in trainnames,'target_rate':rate,'family':m['families'][b]})
  for rep in p['seeds']:
   rng=np.random.default_rng(seed(f'phase4-acquisition-v1|{b}|{s}|{rep}'));order=rng.permutation(sorted(groups))[:31];chosen=[groups[g].iloc[int(rng.integers(len(groups[g])))] for g in order];ys=[int(x.response) for x in chosen];ids=[x.response_id for x in chosen]
   trajectories.append({'benchmark':b,'subject_key':s,'seed':rep,'groups':list(order),'response_ids':ids,'labels':ys})
   labels=[[[attrs,item],v] for v in ys]
   for n in p['budgets']:
    success=sum(ys[:n]);emp=float(official.predict([attrs,item],labels[:n]));calls+=1;assert emp==(success/n if n else .5)
    probs=[.5,emp,(success+1)/(n+2),(success+a)/(n+a+beta)]
    for method,prob in zip(METHODS,probs):
     loss=float(prob*prob-2*prob*rate+rate)
     assert np.isclose(loss,np.mean((prob-y)**2),rtol=0,atol=1e-14)
     records.append({'split':pool['split'],'benchmark':b,'subject_key':s,'seed':rep,'budget':n,'method':method,'probability':prob,'brier':loss,'ece':abs(prob-rate),'endpoint':int(prob in [0.,1.]),'target_rate':rate,'target_count':len(y)})
  print('Scored pair',b,s[:8],flush=True) if len(memberships)%30==0 else None
 df=pd.DataFrame(records);df.to_parquet(ROOT/'outputs/forecasts.parquet',index=False)
 save('outputs/acquisition-trajectories.json',trajectories);save('outputs/included-subjects.json',memberships)
 results={};reliability=[]
 for split in ['development','holdout']:
  dd=df[df.split==split];result,pair,alc,perbench=summarize(dd);mm=[r for r in memberships if r['split']==split];result['target_responses']=sum(r['target_responses'] for r in mm);result['target_groups_across_pairs']=sum(r['target_groups'] for r in mm);result['unique_subject_profiles']=len({r['subject_key'] for r in mm})
  pair.to_parquet(ROOT/f'outputs/{split}-pair-budget.parquet',index=False);alc.to_parquet(ROOT/f'outputs/{split}-pair-alc.parquet',index=False);save(f'outputs/{split}-benchmark-results.json',perbench.to_dict('records'))
  result['familiarity']={}
  for field in ['familiar_profile','familiar_model_name']:
   result['familiarity'][field]={}
   for flag in [True,False]:
    keys={(r['benchmark'],r['subject_key']) for r in mm if r[field]==flag};sub=alc[[(b,s) in keys for b,s in zip(alc.benchmark,alc.subject_key)]];pv=sub.pivot(index=['benchmark','subject_key'],columns='method',values='alc')
    result['familiarity'][field][str(flag)]={'pairs':len(pv),'alc':pv.mean().to_dict(),'beta_minus_eb':float((pv.beta-pv.eb).mean()) if len(pv) else None}
  result['domain_results']={}
  for domain in sorted({d for r in mm for d in m['domains'][r['benchmark']]}):
   benches={r['benchmark'] for r in mm if domain in m['domains'][r['benchmark']]};sub=alc[alc.benchmark.isin(benches)];pv=sub.pivot(index=['benchmark','subject_key'],columns='method',values='alc');result['domain_results'][domain]={'benchmarks':sorted(benches),'pairs':len(pv),'alc':pv.mean().to_dict(),'beta_minus_eb':float((pv.beta-pv.eb).mean())}
  result['subject_results_note']='Every subject configuration has per-pair ALC and budget results in saved parquet; included-subjects maps full attributes and native IDs. Source-family results coincide with benchmark results on final holdout, one benchmark per family.'
  results[split]=result
  dd=dd.copy();dd['bin']=np.minimum((dd.probability*10).astype(int),9)
  for (method,n,binid),g in dd.groupby(['method','budget','bin']):reliability.append({'split':split,'method':method,'budget':int(n),'bin':int(binid),'pair_seed_count':len(g),'mean_probability':float(g.probability.mean()),'observed_rate':float(g.target_rate.mean()),'pair_seed_mass':len(g)/(result['pairs']*30)})
 save('outputs/calibration-bins.json',reliability);save('outputs/results.json',{'completed_utc':now(),'official_baseline_calls':calls,**results});print(json.dumps(results,indent=2))
if __name__=='__main__':main()
