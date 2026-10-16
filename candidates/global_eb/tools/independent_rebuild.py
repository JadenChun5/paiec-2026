"""Second build implementation; does not import or invoke the primary builder.

Rebuilds from reviewed sources, not the original ZIP. Fixed ZIP metadata removes
source paths and filesystem timestamp differences. Exclusively creates output.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'rebuild/global_eb_frozen.zip');args=p.parse_args()
args.output.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(args.output,mode='x') as archive:
    for filename in ['model.py','README.md']:
        payload=(ROOT/'submission'/filename).read_bytes()
        info=zipfile.ZipInfo(filename=filename,date_time=(1980,1,1,0,0,0))
        info.create_system=3
        info.create_version=20
        info.extract_version=20
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644 << 16
        info.internal_attr=0
        with archive.open(info,mode='w') as member:
            member.write(payload)
original=(ROOT/'global_eb_frozen.zip').read_bytes();rebuilt=args.output.read_bytes()
assert original==rebuilt,'Independent rebuild is not byte-identical'
result={'original_sha256':hashlib.sha256(original).hexdigest(),'rebuilt_sha256':hashlib.sha256(rebuilt).hexdigest(),'byte_identical':True,'bytes':len(rebuilt),'builder':'separate implementation using zipfile streaming writes; primary uses writestr','scope':'independent build path, not a separate human reviewer or different compression toolchain'}
(ROOT/'outputs/rebuild-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
