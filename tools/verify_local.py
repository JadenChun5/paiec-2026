"""Run original synthetic tests and official validation; never rebuild or read research data."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a=argparse.ArgumentParser(description=__doc__);a.add_argument('--kit-dir',type=Path,required=True);a.add_argument('--work',type=Path,required=True);o=a.parse_args()
 work=o.work.resolve();kit=o.kit_dir.resolve()
 if work==ROOT or ROOT in work.parents:raise ValueError('Use a fresh work directory outside the candidate')
 pins=json.loads((ROOT/'provenance/official-kit-pins.json').read_text())
 for rel,h in pins.items():
  if sha(kit/rel)!=h:raise ValueError('Official kit pin mismatch: '+rel)
 archive=ROOT/'artifacts/global_eb_frozen.zip';expected='ec8906e3eeda8c1044899745ccaec9c948491ded74f021c7d83f1c62e396d3ef'
 assert sha(archive)==expected
 work.mkdir(parents=True,exist_ok=False);dest=work/'global_eb';shutil.copytree(ROOT/'candidates/global_eb',dest)
 for rel in ['outputs','logs','tmp','extracted-zip','sources/starting_kit','sources/official-baseline/tools']:(dest/rel).mkdir(parents=True,exist_ok=True)
 for rel in pins:
  target=dest/'sources/starting_kit'/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(kit/rel,target)
 for rel in ['check_submission_zip.py','tools/streaming_ingestion.py']:shutil.copyfile(ROOT/'third_party/paiec_baseline'/rel,dest/'sources/official-baseline'/rel)
 shutil.copyfile(archive,dest/'global_eb_frozen.zip')
 with zipfile.ZipFile(archive) as z:
  assert set(z.namelist())=={'model.py','README.md'}
  for name in z.namelist():
   assert z.read(name)==(dest/'submission'/name).read_bytes();(dest/'extracted-zip'/name).write_bytes(z.read(name))
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TMPDIR=str((dest/'tmp').resolve()),OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONHASHSEED='0')
 commands={
  'original_eb_synthetic_suite':[sys.executable,'-B','-m','unittest','discover','-s','tests','-v'],
  'baseline_validator':[sys.executable,'-B',str(dest/'sources/official-baseline/check_submission_zip.py'),str(archive)],
  'kit_validator':[sys.executable,'-B',str(dest/'sources/starting_kit/tools/check_submission_zip.py'),str(archive)],
  'kit_smoke_sequential':[sys.executable,'-B',str(dest/'sources/starting_kit/tools/run_smoke_test.py'),str(dest/'extracted-zip')],
  'kit_smoke_requested_four':[sys.executable,'-B',str(dest/'sources/starting_kit/tools/run_smoke_test.py'),str(dest/'extracted-zip'),'--concurrency','4']}
 results={}
 for name,cmd in commands.items():
  p=subprocess.run(cmd,cwd=dest,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
  (dest/'logs'/f'{name}.log').write_text(p.stdout);results[name]={'exit_code':p.returncode,'log':str(Path('global_eb/logs')/f'{name}.log')};print(name,p.returncode,flush=True)
  if p.returncode:break
 assert sha(archive)==expected
 (work/'validation.json').write_text(json.dumps(results,indent=2)+'\n')
 if not all(v['exit_code']==0 for v in results.values()) or len(results)!=len(commands):raise SystemExit(1)
if __name__=='__main__':main()
