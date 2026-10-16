"""Check original research workflow on fabricated fixtures; fitting is mocked, never optimized."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,os,importlib.util
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--work',type=Path,required=True);args=ap.parse_args();work=args.work.resolve()
 if work==ROOT or ROOT in work.parents:raise ValueError('Work must be outside candidate')
 work.mkdir(parents=True,exist_ok=False)
 import pandas as pd
 import numpy as np
 r=work/'research/phase4';shutil.copytree(ROOT/'research/phase4/scripts',r/'scripts');(r/'outputs').mkdir()
 names=[f'synthetic_only_{i:02d}' for i in range(23)];plan={'train':names[:12],'development':names[12:15],'holdout':names[15:],'resource_cap_bytes':100_000_000,'per_table_cap_bytes':1_000_000};inventory=[]
 attrs=['normalized_name','provider','release_date','access_date','harness','harness_version','reasoning_effort','subject_features_extra']
 for name in names:
  d=r/'data'/name/'formatted_tables';d.mkdir(parents=True)
  subjects=[dict(subject_id=f's{i}',**{a:(f'synthetic_subject_{i}' if a=='normalized_name' else '') for a in attrs}) for i in range(2)]
  items=[dict(item_id=f'i{i}',content=f'fabricated {name} item {i}',raw_item_id=f'native{i}') for i in range(80)]
  responses=[dict(subject_id=f's{s}',item_id=f'i{i}',response_id=f'r{s}_{i}',response=i%2,trial=0,benchmark_id=name) for s in range(2) for i in range(80)]
  for table,records in [('subjects',subjects),('items',items),('responses',responses)]:pd.DataFrame(records).to_parquet(d/f'{table}.parquet',index=False)
  inventory.append(dict(directory=name,required_bytes=sum(p.stat().st_size for p in d.iterdir()),catalog={'benchmark_id':name,'domain':['synthetic']},source_family=name))
 for file,obj in [('selection-plan.json',plan),('data-inventory.json',inventory)]:(r/'outputs'/file).write_text(json.dumps(obj))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 # Explicit socket denial; the existing downloader returns pre-created synthetic files.
 harness="import sys,runpy; sys.path.insert(0,sys.argv[1]); sys.addaudithook(lambda event,args: (_ for _ in ()).throw(RuntimeError('network forbidden')) if event=='socket.connect' else None); runpy.run_path(sys.argv[2],run_name='__main__')"
 p=subprocess.run([sys.executable,'-B','-c',harness,str(r/'scripts'),str(r/'scripts/prepare.py')],env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120)
 (work/'prepare.log').write_text(p.stdout);assert p.returncode==0,p.stdout
 d=pd.read_parquet(r/'data/eligible-responses.parquet');assert len(d)==3680 and set(d.benchmark)==set(names)
 assert len(d[d.split=='train'])==1920
 protocol={'weights':[.1,.2,.2,.2,.2,.1],'synthetic_fixture_only':True};pb=json.dumps(protocol).encode();(r/'outputs/protocol.json').write_bytes(pb);(r/'outputs/protocol.sha256').write_text(hashlib.sha256(pb).hexdigest())
 sys.path.insert(0,str(r/'scripts'))
 def module(name):
  s=importlib.util.spec_from_file_location('fixture_'+name,r/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
 fit=module('fit');calls=[]
 def mock_fit(counts):
  assert all(x['items']==80 and x['successes']==40 for x in counts);calls.append(len(counts))
  return {'alpha':1.,'beta':1.,'mean':.5,'concentration':2.,'boundary':False,'starts':[],'fixture_optimizer_mocked':True}
 # Existing main executes grouping/count collection and output plumbing; optimizer entry point replaced.
 with patch.object(fit,'fit',side_effect=mock_fit):fit.main()
 assert calls==[24]+[22]*12
 counts=json.loads((r/'outputs/training-counts.json').read_text());assert len(counts)==24
 # Existing analysis function, arbitrary synthetic loss inputs; no predictions/scientific data.
 analysis=module('run');records=[];losses={'constant':.25,'empirical':.26,'beta':.24,'eb':.23}
 for b in range(4):
  for s in range(2):
   for seed in range(2):
    for budget in [0,1,3,7,15,31]:
     for method,value in losses.items():records.append(dict(benchmark=f'synthetic_stat_{b}',subject_key=f'fake_{s}',seed=seed,budget=budget,method=method,brier=value,ece=.1,endpoint=0))
 summary,pair,alc,bench=analysis.summarize(pd.DataFrame(records))
 assert all(np.isclose(summary['alc'][m],v) for m,v in losses.items());assert np.isclose(summary['primary_difference'],.01);assert summary['pairs']==8;assert summary['benchmark_clusters']==4
 result={'fixture_only':True,'prepare_rows':len(d),'training_count_pairs':len(counts),'fit_call_counts':calls,'optimizer_mocked':True,'model_training_performed':False,'scientific_predictions_performed':False,'analysis_pairs':8,'analysis_families':4,'checks':['original prepare.py completes on 23 synthetic sources','group identities and 3680 prepared rows preserved','training-only count construction uses 24 pairs','one trial per item yields 80 items and 40 successes per synthetic pair','fit main plumbing completes with optimizer replaced','original summarize yields expected equal-pair ALC and paired difference','family grouping retains four independent synthetic families despite repeated seeds'],'status':'PASS'}
 (work/'fixture-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
