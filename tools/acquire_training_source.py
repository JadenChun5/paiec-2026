"""Explicit authorized-data acquisition via original downloader; --dry-run never authenticates."""
from pathlib import Path
import argparse,json,importlib.util
ROOT=Path(__file__).resolve().parents[1]
def main():
 names=json.loads((ROOT/'provenance/training_sources.json').read_text())['training_benchmarks']
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--benchmark',choices=names,required=True);p.add_argument('--table',choices=['subjects','items','responses'],required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 work=a.work.resolve();rel=f'{a.benchmark}/formatted_tables/{a.table}.parquet'
 if work==ROOT or ROOT in work.parents:raise ValueError('Data must remain outside the release candidate')
 if a.dry_run:print(json.dumps({'revision':'54074453da7b9911be0f48e4c560be547bc84d21','relative_path':rel,'destination':str(work/'data'/rel),'network':False}));return
 spec=importlib.util.spec_from_file_location('original_download',ROOT/'research/phase4/scripts/common.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.ROOT=work
 result=m.download(rel);print('Authorized table saved outside release candidate:',result)
if __name__=='__main__':main()
