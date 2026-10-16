"""Synthetic ZIP and official-runtime checks; no benchmark data or network."""
from pathlib import Path
import unittest,importlib.util,copy,json,math,sys,time,zipfile,tempfile,contextlib,ast,hashlib
ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'sources/starting_kit';MODEL=ROOT/'extracted-zip/model.py'
sys.path.insert(0,str(KIT/'tools'))
from streaming_ingestion import AcquisitionHook,run_streaming
from prediction_workers import parallel_predictions,group_prediction_inputs

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
PRED=module(MODEL,'packaged_beta').predict
RESEARCH=module(ROOT.parent/'phase6-online-acquisition-2026-10-11/policy/model.py','research_beta').predict
SUBJECT={k:'' for k in ['normalized_name','provider','release_date','access_date','harness','harness_version','reasoning_effort','subject_features_extra']}
SUBJECT.update(normalized_name='synthetic-system',harness='synthetic-harness')
ITEM=dict(item_content='Synthetic target',item_features='',interactors='',benchmark_id='benchmark_001')
INPUT=[SUBJECT,ITEM]
BUDGETS=[0,1,3,7,15,31]
def observation(y,i=0):return [[dict(SUBJECT),dict(ITEM,item_content='acquired '+str(i))],y]
def probability(v):
    assert type(v) is float and math.isfinite(v) and 0<=v<=1
    return v

class SubmissionTests(unittest.TestCase):
    def test_all_counts_equal_established_research_predictor(self):
        cases=0
        for n in range(32):
            for s in range(n+1):
                evidence=[observation(y,i) for i,y in enumerate([1]*s+[0]*(n-s))]
                p=PRED(INPUT,labeled=evidence);self.assertEqual(probability(p),(s+1)/(n+2));self.assertEqual(p,RESEARCH(INPUT,evidence));cases+=1
        self.assertEqual(cases,528)

    def test_full_subject_and_benchmark_isolation(self):
        ev=[observation(1),observation(0),observation(0)]
        for field in SUBJECT:
            other=copy.deepcopy(ev);other[0][0][0][field]='different'
            self.assertEqual(PRED(INPUT,ev+[other[0]]),2/5)
        other=observation(1);other[0][1]['benchmark_id']='benchmark_other'
        self.assertEqual(PRED(INPUT,ev+[other]),2/5);self.assertEqual(PRED(INPUT,[other]),.5)

    def test_no_mutation_or_checkpoint_state(self):
        ev=[observation(i%3==0,i) for i in range(31)];before=copy.deepcopy([INPUT,ev])
        for n in [31,0,7,1,15,3,0]:self.assertEqual(PRED(INPUT,ev[:n]),(sum(x[1] for x in ev[:n])+1)/(n+2))
        self.assertEqual([INPUT,ev],before);self.assertEqual(PRED(INPUT),.5);self.assertEqual(PRED(INPUT,None),.5)

    def test_input_guards_and_blank_fields(self):
        self.assertEqual(PRED([dict(SUBJECT),{}],[]),.5)
        with self.assertRaisesRegex(ValueError,'benchmark_id'):PRED([SUBJECT,{}],[observation(1)])
        ev=observation(1);ev[0][1].pop('benchmark_id')
        with self.assertRaisesRegex(ValueError,'benchmark_id'):PRED(INPUT,[ev])
        for bad in [float('nan'),float('inf'),-1,2,'1']:
            with self.assertRaisesRegex(ValueError,'binary'):PRED(INPUT,[observation(bad)])

    def test_zip_has_only_self_contained_files(self):
        with zipfile.ZipFile(ROOT/'dist/beta11_random.zip') as z:
            self.assertEqual(set(z.namelist()),{'model.py','README.md'});self.assertIsNone(z.testzip());self.assertEqual(z.read('model.py'),MODEL.read_bytes())
        tree=ast.parse(MODEL.read_text());self.assertFalse(any(isinstance(n,(ast.Import,ast.ImportFrom)) for n in ast.walk(tree)))
        self.assertFalse((ROOT/'extracted-zip/labeling.py').exists())

    def test_default_random_agrees_between_kit_and_latest_baseline(self):
        self.assertEqual(AcquisitionHook(None).mode,'random');self.assertFalse(AcquisitionHook(None).needs_prediction)
        paths=[KIT/'tools/streaming_ingestion.py',ROOT/'sources/official-baseline/tools/streaming_ingestion.py']
        bodies=[]
        for p in paths:
            tree=ast.parse(p.read_text());node=next(n for n in ast.walk(tree) if isinstance(n,ast.If) and ast.unparse(n.test)=="hook.mode == 'random'");bodies.append(ast.dump(ast.Module(body=node.body,type_ignores=[])))
        self.assertEqual(*bodies)

    def test_official_four_worker_fresh_checkpoints(self):
        inputs=[[dict(SUBJECT),dict(ITEM,item_content='worker target '+str(i))] for i in range(8)]
        evidence=[observation(i%2,i) for i in range(31)]
        for n in [31,0,7,1,15,3]:
            out=list(parallel_predictions(MODEL,inputs,evidence[:n],concurrency=4,deadline=time.monotonic()+30,per_call_timeout=5))
            self.assertEqual(len(out),8);self.assertEqual({i for i,_ in out},set(range(8)))
            for _,p in out:self.assertEqual(probability(p),(sum(x[1] for x in evidence[:n])+1)/(n+2))

    def test_official_streaming_random_and_six_checkpoints(self):
        budgets=[];chosen=[];queries=[];evaluated=[]
        targets=[{'input':[dict(SUBJECT),dict(ITEM,item_content='evaluation '+str(i%4))]} for i in range(5)]
        def events():
            reply=yield {'protocol':'streaming_alc_v1','type':'configure','event_id':'config'}
            self.assertEqual(reply['acquisition_mode'],'stream')
            def evaluate_event(n):return dict(protocol='streaming_alc_v1',type='evaluate',event_id=f'e{n}',budget=n,targets=targets,labeled=copy.deepcopy(chosen))
            reply=yield evaluate_event(0);self.assertEqual(reply['probabilities'],[.5]*5);budgets.append(0)
            for i in range(40):
                inp=observation(0,i)[0];ctx=dict(subject_id='subject_001',benchmark_id='benchmark_001',labels_acquired=len(chosen),labels_remaining=31-len(chosen),max_labels=31,items_remaining=40-i)
                reply=yield dict(protocol='streaming_alc_v1',type='acquire',event_id=f'a{i}',input=inp,context=ctx,labeled=copy.deepcopy(chosen))
                self.assertIs(type(reply['query']),bool)
                key=json.dumps([ctx,inp],sort_keys=True,separators=(',',':'));u=int.from_bytes(hashlib.sha256(key.encode()).digest()[:8],'big')/2**64
                self.assertEqual(reply['query'],u<min(1,ctx['labels_remaining']/ctx['items_remaining']));queries.append(i)
                if reply['query']:
                    chosen.append([inp,i%2]);n=len(chosen)
                    if n in BUDGETS:
                        reply=yield evaluate_event(n);expected=(sum(e[1] for e in chosen)+1)/(n+2);self.assertEqual(reply['probabilities'],[expected]*5);budgets.append(n)
                if len(chosen)==31:break
            yield dict(protocol='streaming_alc_v1',type='finished',predictions_csv='model_id,item_id,predicted_probability\n'+''.join('s,i,0.5\n' for _ in range(30)))
        gen=events();first=True
        def exchange(payload):
            nonlocal first
            if first:first=False;return next(gen)
            return gen.send(payload)
        def stream(model_path,inputs,labeled,**kwargs):
            # Each checkpoint uses a fresh module, as official workers do.
            fresh=module(model_path,'checkpoint_beta').predict
            for i,inp in enumerate(inputs):evaluated.append(inp);yield i,fresh(inp,labeled)
        with tempfile.TemporaryDirectory(dir=ROOT/'tmp') as temp:
            temp=Path(temp);config=temp/'config.json';config.write_text(json.dumps({'protocol':'streaming_alc_v1'}))
            stats=run_streaming(config_path=config,predict=PRED,acquisition_function=None,model_path=MODEL,output_dir=temp,concurrency=4,deadline=time.monotonic()+30,per_call_timeout=5,acquisition_timeout=5,call_window=lambda *a:contextlib.nullcontext(),validate_score=probability,prediction_stream=stream,group_inputs=group_prediction_inputs,log=lambda text:None,exchange=exchange)
        self.assertEqual(budgets,BUDGETS);self.assertEqual(len(chosen),31);self.assertEqual(stats['acquisition_mode'],'random');self.assertEqual(stats['acquisition_prediction_calls'],0);self.assertEqual(stats['prediction_calls_count'],24);self.assertEqual(stats['prediction_reuse_count'],6)
        self.assertEqual(len(set(queries)),len(queries))

if __name__=='__main__':unittest.main(verbosity=2)
