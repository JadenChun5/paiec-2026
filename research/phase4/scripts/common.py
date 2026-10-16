from pathlib import Path
import json,hashlib,datetime,unicodedata
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'phase3-paiecreal-2026-10-09'
REV='54074453da7b9911be0f48e4c560be547bc84d21'
REPO='aims-foundations/measurement-db'
import sys
PYTHON=sys.executable
ATTRS=['normalized_name','provider','release_date','access_date','harness','harness_version','reasoning_effort','subject_features_extra']
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
def seed(x):return int(sha(x)[:16],16)
def norm(x):return ' '.join(unicodedata.normalize('NFKC',str(x)).casefold().split())
def read(name):return json.loads((ROOT/name).read_text())
def save(name,obj):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(obj,f,indent=2,default=str,allow_nan=False)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def download(name,limit=60_000_000):
 import urllib.request
 from huggingface_hub import get_token
 p=ROOT/'data'/name
 if p.exists():return p
 req=urllib.request.Request(f'https://huggingface.co/datasets/{REPO}/resolve/{REV}/{name}',headers={'Authorization':'Bearer '+get_token()})
 with urllib.request.urlopen(req,timeout=60) as r:b=r.read(limit+1)
 if len(b)>limit:raise RuntimeError('download limit exceeded')
 assert b[:4]==b'PAR1' and b[-4:]==b'PAR1'
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);return p
