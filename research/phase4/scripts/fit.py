from common import *
import numpy as np,pandas as pd
from scipy.special import betaln,digamma,expit,logit
from scipy.optimize import minimize

def fit(counts):
 s=np.array([r['successes'] for r in counts]);n=np.array([r['items'] for r in counts]);bounds=[(-6,6),(np.log(.05),np.log(1000))]
 def objective(z):
  mu=expit(z[0]);k=np.exp(z[1]);a=mu*k;b=(1-mu)*k
  val=-np.mean(betaln(s+a,n-s+b)-betaln(a,b))
  da=digamma(s+a)-digamma(n+a+b)-digamma(a)+digamma(a+b)
  db=digamma(n-s+b)-digamma(n+a+b)-digamma(b)+digamma(a+b)
  grad=-np.array([np.mean((da-db)*k*mu*(1-mu)),np.mean(da*a+db*b)])
  return val,grad
 results=[]
 for mu,k in [(.5,2),(.25,2),(.75,10),(.5,.5),(.5,20)]:
  r=minimize(objective,[logit(mu),np.log(k)],method='L-BFGS-B',jac=True,bounds=bounds,options={'ftol':1e-12,'gtol':1e-8,'maxiter':2000})
  results.append({'success':bool(r.success),'objective':float(r.fun),'x':r.x.tolist(),'iterations':int(r.nit)})
 valid=[r for r in results if r['success']];assert valid,'No successful optimizer'
 best=min(valid,key=lambda r:r['objective']);u,v=best['x'];mu=float(expit(u));k=float(np.exp(v))
 boundary=any(abs(x-lo)<1e-5 or abs(x-hi)<1e-5 for x,(lo,hi) in zip(best['x'],bounds))
 return {'alpha':mu*k,'beta':(1-mu)*k,'mean':mu,'concentration':k,'boundary':boundary,'starts':results,'pair_count':len(counts),'independent_item_count':int(n.sum())}
def main():
 p=read('outputs/protocol.json');assert sha((ROOT/'outputs/protocol.json').read_bytes())==(ROOT/'outputs/protocol.sha256').read_text().strip()
 d=pd.read_parquet(ROOT/'data/eligible-responses.parquet',filters=[('split','==','train')]);counts=[]
 for (b,s),q in d.groupby(['benchmark','subject_key'],sort=True):
  rng=np.random.default_rng(seed('phase4-fit-trials-v1|'+b+'|'+s));ys=[];ids=[]
  for g,f in q.groupby('item_group',sort=True):
   f=f.sort_values('response_id');row=f.iloc[int(rng.integers(len(f)))];ys.append(int(row.response));ids.append(row.response_id)
  counts.append({'benchmark':b,'subject_key':s,'successes':sum(ys),'items':len(ys),'selected_response_ids':ids})
 save('outputs/training-counts.json',counts);result=fit(counts);assert not result['boundary'],'STOP: boundary prior'
 result.update(fitted_utc=now(),training_benchmarks=sorted(d.benchmark.unique()),protocol_sha256=sha((ROOT/'outputs/protocol.json').read_bytes()))
 save('outputs/learned-prior.json',result)
 lobo={b:fit([r for r in counts if r['benchmark']!=b]) for b in sorted(d.benchmark.unique())};save('outputs/prior-stability.json',lobo)
 print(json.dumps({k:v for k,v in result.items() if k!='starts'},indent=2))
if __name__=='__main__':main()
