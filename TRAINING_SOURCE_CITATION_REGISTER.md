# Historical training-source citation register

Exactly **17 retained benchmark identifiers** contributed to the frozen empirical Bayes fit: 198 subject–benchmark pairs and 211,256 one-trial-per-item-group observations, from 285,454 eligible recorded training responses. Alpha = 1.1814007859059947; beta = 1.278451593031275. No refit or response-table access occurred during this recovery.

Identity is established by the original learned-prior training list, its frozen hash, the original retained-split bridge and the previously verified training-source list—not by present-day MDB availability. Dataset revision: `54074453da7b9911be0f48e4c560be547bc84d21`. Learned-prior SHA-256: `b0f63dde8905e101e1a03db613cbf679c76491e80e57d35ac8f1438f5b060979`. Original split-manifest SHA-256: `080372fcb66c241a2a8ac5a232991eed39e5944b6b5e19a57b78d18f054aabcc`.

The BibTeX file contains **21 distinct cited works**, not 17 independent papers: C-Eval cites benchmark and export; tau-bench cites benchmark and HAL; WorkBench cites original and revisited work; VisualWebArena and WorkArena each cite their task and share one AgentRewardBench export reference. Publication count is not independent-family count. The excluded candidate fewshot_ttt_bbh is not one of these 17 and is documented separately in HISTORICAL_TRAINING_PROVENANCE.md. Existing historical table receipts cover 18 candidates; only 51 of those table receipts belong to the 17 retained fitting sources.

## Evidence and permission scope

Original metadata citations, source links and declared terms were recovered from the previous pinned legal/citation receipt. Targeted primary-page checks filled abbreviated citation fields for C-Eval/export, MathConstraint, tau-bench/HAL, VisualWebArena, WorkArena and AgentRewardBench; LiveAoPSBench's publication URL/authors were checked. This is citation recovery, not a new universal legal audit. All 17 source identities are verified; bibliographic completeness and raw-export permission are separate fields.

AIMS-owned curation/citation adaptations retain attribution to AIMS Foundations and their existing [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) scope. Changes: selected the exact historical training sources, linked original works and exports, added provenance hashes and clearly labeled primary-source bibliographic completions. Underlying benchmark/task/export terms remain separate. No raw datasets, tasks, images, trajectories or individual predictions are redistributed. The Director reports explicit permission to publish derived MDB analyses with appropriate attribution and source-specific terms; that does not grant raw-data permission.

## algotune

- **Original identifier:** `algotune`; **benchmark name:** AlgoTune.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/oripress/AlgoTune.
- **Citation keys:** `press2025algotune`.
- **Stable citation URLs:** https://github.com/oripress/AlgoTune.
- **License/attribution recorded:** MIT
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit. Captured citation abbreviates the author list with others; it is not asserted complete.
- **Pinned citation metadata:** [algotune/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/algotune/metadata.yaml); historical SHA-256 `25f2d0e983ce96b44c604b08b396e72b2677655928788d64dd256b85049ec755`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `algotune/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@inproceedings{press2025algotune,
  title={AlgoTune: Can Language Models Speed Up General-Purpose Numerical Programs?},
  author={Press, Ori and Amos, Brandon and Zhao, Haoyu and Wu, Yikai and others},
  booktitle={NeurIPS 2025 Datasets and Benchmarks Track},
  year={2025},
  url = {https://github.com/oripress/AlgoTune}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- release: https://github.com/oripress/AlgoTune — `dff9914c10800c7a031c9e8c3d4d1c8cd1b38906`
- publication/source: https://huggingface.co/datasets/oripress/AlgoTune — `fc3744ffd7eebaa9e9b55427e2cda440955fdd2d`

## appworld

- **Original identifier:** `appworld`; **benchmark name:** AppWorld.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/StonyBrookNLP/appworld-leaderboard.
- **Citation keys:** `trivedi2024appworldcontrollableworldapps`.
- **Stable citation URLs:** https://arxiv.org/abs/2407.18901.
- **License/attribution recorded:** Apache-2.0
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [appworld/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/appworld/metadata.yaml); historical SHA-256 `cf9218801684b8625422d780db27d0a67cb12b30a13c5b69743ec1bf412d2a5e`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `appworld/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{trivedi2024appworldcontrollableworldapps,
      title={AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents},
      author={Harsh Trivedi and Tushar Khot and Mareike Hartmann and Ruskin Manku and Vinty Dong and Edward Li and Shashank Gupta and Ashish Sabharwal and Niranjan Balasubramanian},
      year={2024},
      eprint={2407.18901},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2407.18901},
}
```

Recorded upstream pins (not substituted for the MDB revision):

- results: https://github.com/StonyBrookNLP/appworld-leaderboard — `c1f56015cf7c3441ff1933f5bfbec879798d7bbe`
- publication/source: https://github.com/StonyBrookNLP/appworld — `0a749f16da0c516811fe58e59ec9e2217560f54d`

## ceval

- **Original identifier:** `ceval`; **benchmark name:** C-Eval.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/liyucheng09/Contamination_Detector.
- **Citation keys:** `huang2023ceval`, `li2024contamination`.
- **Stable citation URLs:** https://arxiv.org/abs/2305.08322; https://arxiv.org/abs/2310.17589v3.
- **License/attribution recorded:** Questions: CC-BY-NC-SA-4.0. The third-party prediction export declares no separate license.
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s). The export paper first appeared in 2023; its pinned v3 is 2024. Both original benchmark and export are credited.
- **Pinned citation metadata:** [ceval/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/ceval/metadata.yaml); historical SHA-256 `1b3e419103aa75ee424a3ead2a99fbfa7790d8d7b2c4693899878d80aad0d52a`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `ceval/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{huang2023ceval,
  title = {C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models},
  author = {Yuzhen Huang and Yuzhuo Bai and Zhihao Zhu and Junlei Zhang and Jinghan Zhang and Tangjun Su and Junteng Liu and Chuancheng Lv and Yikai Zhang and Jiayi Lei and Yao Fu and Maosong Sun and Junxian He},
  year = {2023},
  url = {https://arxiv.org/abs/2305.08322}
}
```

```bibtex
@misc{li2024contamination,
  title = {An Open Source Data Contamination Report for Large Language Models},
  author = {Yucheng Li and Frank Guerin and Chenghua Lin},
  year = {2024},
  url = {https://arxiv.org/abs/2310.17589v3}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- official_questions: https://huggingface.co/datasets/ceval/ceval-exam — `617524a00b307ff6f9933702f724131fe12ca7ce`
- analysis_code: https://github.com/liyucheng09/Contamination_Detector — `ffe3c249309da9a7ad7f42e9145e1f8e4d36c77e`

## financebench

- **Original identifier:** `financebench`; **benchmark name:** FinanceBench.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/patronus-ai/financebench/tree/22257c455f9f9ca9ca3dc67456d9a32e60c7ef08.
- **Citation keys:** `islam2023financebench`.
- **Stable citation URLs:** https://arxiv.org/abs/2311.11944.
- **License/attribution recorded:** unknown
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [financebench/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/financebench/metadata.yaml); historical SHA-256 `6c3372af624e9c5f5ad72970f09134c213bb42590b7fa09febc968d9666b9356`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `financebench/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{islam2023financebench,
  title={FinanceBench: A New Benchmark for Financial Question Answering},
  author={Pranab Islam and Anand Kannappan and Douwe Kiela and Rebecca Qian and Nino Scherrer and Bertie Vidgen},
  year={2023},
  eprint={2311.11944},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url = {https://arxiv.org/abs/2311.11944}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- provider_archive: https://codeload.github.com/patronus-ai/financebench/tar.gz/22257c455f9f9ca9ca3dc67456d9a32e60c7ef08 — `22257c455f9f9ca9ca3dc67456d9a32e60c7ef08`
- paper_v1: https://arxiv.org/pdf/2311.11944v1 — `v1`
- documents: https://github.com/patronus-ai/financebench — `22257c455f9f9ca9ca3dc67456d9a32e60c7ef08`

## liveaopsbench

- **Original identifier:** `liveaopsbench`; **benchmark name:** LiveAoPSBench.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/LiveMathBench/LiveMathBench.github.io.
- **Citation keys:** `mahdavi2025leveraging`.
- **Stable citation URLs:** https://arxiv.org/abs/2501.14275.
- **License/attribution recorded:** Task dataset: Apache-2.0 (author HF card); website result/source release: CC-BY-SA-4.0; evaluator code: Apache-2.0. Original notices are captured.
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s).
- **Pinned citation metadata:** [liveaopsbench/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/liveaopsbench/metadata.yaml); historical SHA-256 `d6a1ac2bd4de7153db8f5a14374ee186c6523e35dbe72ccc1f63b1427a6489b8`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `liveaopsbench/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@article{mahdavi2025leveraging,
  title={Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation},
  author={Mahdavi, Sadegh and Li, Muchen and Liu, Kaiwen and Thrampoulidis, Christos and Sigal, Leonid and Liao, Renjie},
  journal={International Conference on Machine Learning (ICML)},
  year={2025},
  url = {https://arxiv.org/abs/2501.14275}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- results_json: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/src/mocks/acc2024.json — `1fafd48912960842da0caa53a71e1d605a108246`
- questions_jsonl: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/public/data/LiveAoPSBench-2024.jsonl — `1fafd48912960842da0caa53a71e1d605a108246`
- earlier_results_json: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/src/mocks/acc.json — `1fafd48912960842da0caa53a71e1d605a108246`
- website_exporter_py: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/src/mocks/trans_json.py — `1fafd48912960842da0caa53a71e1d605a108246`
- website_index_tsx: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/src/index.tsx — `1fafd48912960842da0caa53a71e1d605a108246`
- website_readme_md: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/1fafd48912960842da0caa53a71e1d605a108246/README.md — `1fafd48912960842da0caa53a71e1d605a108246`
- source_questions_jsonl: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/f7e3b365cef3c0947199cb9872d525bb74764345/public/data/LiveAoPSbench-1224.jsonl — `f7e3b365cef3c0947199cb9872d525bb74764345`
- earlier_questions_jsonl: https://raw.githubusercontent.com/LiveMathBench/LiveMathBench.github.io/5a9a56b0bb14b028bc996e33dd3eb9a4d6f9e01f/public/data/LiveAoPSBench_v1.0.jsonl — `5a9a56b0bb14b028bc996e33dd3eb9a4d6f9e01f`
- evaluator_license: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/LICENSE — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_readme_md: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/README.md — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_license: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/LICENSE — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_readme_md: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/README.md — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_evaluate_py: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/evaluate.py — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_grader_py: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/grader.py — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_parser_py: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/parser.py — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_data_loader_py: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/data_loader.py — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- evaluator_eval_math_eval_py: https://raw.githubusercontent.com/DSL-Lab/aops/56f6bc1e670170e301f1c9ebc172124defd21e90/eval/math_eval.py — `56f6bc1e670170e301f1c9ebc172124defd21e90`
- task_dataset_card: https://huggingface.co/datasets/jojo23333/LiveAoPSBench-2024/resolve/3ff6280f4c1d75a035698524c26ee91c70e4e2b5/README.md — `3ff6280f4c1d75a035698524c26ee91c70e4e2b5`

## mathconstraint

- **Original identifier:** `mathconstraint`; **benchmark name:** MathConstraint.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/vireshpati/Math-Constraint.
- **Citation keys:** `pati2026mathconstraint`.
- **Stable citation URLs:** https://arxiv.org/abs/2605.08498.
- **License/attribution recorded:** cc-by-4.0
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s).
- **Pinned citation metadata:** [mathconstraint/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/mathconstraint/metadata.yaml); historical SHA-256 `0bc2f598b7243c49b562e7476e50909f3f8d220f7c0bacc2b417f82a3a4f72c2`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `mathconstraint/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{pati2026mathconstraint,
  title = {MathConstraint: Automated Generation of Verified Combinatorial Reasoning Instances for LLMs},
  author = {Viresh Pati and Zhengyu Li and Piyush Jha and Rahul Garg and Yatharth Sejpal and Vijay Ganesh},
  year = {2026},
  url = {https://arxiv.org/abs/2605.08498}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- benchmark: https://github.com/vireshpati/Math-Constraint — `687a6d5510f96afdfa7229fc04b230e434e0c792`

## medhelm_race_based_med

- **Original identifier:** `medhelm_race_based_med`; **benchmark name:** MedHELM RaceBasedMed.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://crfm.stanford.edu/helm/medhelm/.
- **Citation keys:** `bedi2025medhelm`.
- **Stable citation URLs:** https://crfm.stanford.edu/helm/medhelm/.
- **License/attribution recorded:** unknown
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit. Captured citation abbreviates the author list with others; it is not asserted complete. MedHELM is the verified export attribution; a separate underlying race-based-medicine task publication is not identified in the inspected citation field.
- **Pinned citation metadata:** [medhelm_race_based_med/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/medhelm_race_based_med/metadata.yaml); historical SHA-256 `e5a772d9a51afd45c94df5ae909155472b3115812a5b51ff82c6f210451ebdb2`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `medhelm_race_based_med/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@article{bedi2025medhelm,
  title={MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks},
  author={Bedi, Suhana and Cui, Hejie and Fuentes, Miguel and Unell, Alyssa and others and Shah, Nigam H.},
  journal={arXiv preprint arXiv:2505.23802},
  year={2025},
  url = {https://crfm.stanford.edu/helm/medhelm/}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- runs: https://storage.googleapis.com/crfm-helm-public — `v4.0.0`
- grader: https://github.com/stanford-crfm/helm — `63754d05db6f874e41a395880fb573890a13e791`

## naep_llm_students

- **Original identifier:** `naep_llm_students`; **benchmark name:** NAEP LLM-as-Student.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/kvadityasrivatsa/IRT-for-LLMs-as-Students.
- **Citation keys:** `srivatsa2025naepllm`.
- **Stable citation URLs:** https://github.com/kvadityasrivatsa/IRT-for-LLMs-as-Students.
- **License/attribution recorded:** MIT for the authors' recorded results and analysis code. NAEP source pages and illustrations retain their original attributions.
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [naep_llm_students/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/naep_llm_students/metadata.yaml); historical SHA-256 `210531fad5b4ade9b08fbb34be8cd7cd50e9baa05bf607b20018579bb2785c9f`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `naep_llm_students/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@article{srivatsa2025naepllm,
  title={Can LLMs Reliably Simulate Real Students' Abilities in Mathematics and Reading Comprehension?},
  author={Srivatsa, KV Aditya and Maurya, Kaushal Kumar and Kochmar, Ekaterina},
  journal={arXiv preprint arXiv:2507.08232},
  year={2025},
  url = {https://github.com/kvadityasrivatsa/IRT-for-LLMs-as-Students}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- recorded_results: https://github.com/kvadityasrivatsa/IRT-for-LLMs-as-Students — `c3105e17cb9f1e10ec5d9f939d0a336ad735e200`

## nyu_ctf_bench

- **Original identifier:** `nyu_ctf_bench`; **benchmark name:** NYU CTF Bench.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/NYU-LLM-CTF/NYU_CTF_Bench.
- **Citation keys:** `shao2024nyuctf`.
- **Stable citation URLs:** https://github.com/NYU-LLM-CTF/NYU_CTF_Bench.
- **License/attribution recorded:** GPL-2.0 for the NYU_CTF_Bench task repository, with original notices retained. The separate leaderboard_submissions repository and linked forensic input do not declare explicit redistribution terms; raw and formatted data remain local pending clarification. The previous blanket MIT attribution is unsupported.
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [nyu_ctf_bench/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/nyu_ctf_bench/metadata.yaml); historical SHA-256 `aa639d75c56df7fca87788b4f0e3ef85c3ea2e2f63fdc394b1e9740ed3d57937`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `nyu_ctf_bench/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@inproceedings{shao2024nyuctf,
  title={NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security},
  author={Shao, Minghao and Jancheska, Sofija and Udeshi, Meet and Dolan-Gavitt, Brendan and Xi, Haoran and Milner, Kimberly and Chen, Boyuan and Yin, Max and Garg, Siddharth and Krishnamurthy, Prashanth and Khorrami, Farshad and Karri, Ramesh and Shafique, Muhammad},
  booktitle={NeurIPS 2024 Datasets and Benchmarks Track},
  year={2024},
  url = {https://github.com/NYU-LLM-CTF/NYU_CTF_Bench}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- tasks: https://codeload.github.com/NYU-LLM-CTF/NYU_CTF_Bench/tar.gz/4c5744f55a31a58e03d6118c9dbb1c18e5bbdfa9 — `4c5744f55a31a58e03d6118c9dbb1c18e5bbdfa9`
- results: https://codeload.github.com/NYU-LLM-CTF/leaderboard_submissions/tar.gz/69def02a79e8b1d890e1e0d5c11106a9f40e11e1 — `69def02a79e8b1d890e1e0d5c11106a9f40e11e1`
- forensings: https://drive.usercontent.google.com/download — `sha256:d7754455afabf7d9778022a4f963e1e0ba81f9a003323458a52e33eb33268d89`

## perumedqa

- **Original identifier:** `perumedqa`; **benchmark name:** PeruMedQA.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/rodrigo-carrillo/PeruMedQA.
- **Citation keys:** `carrillolarco2025perumedqa`.
- **Stable citation URLs:** https://github.com/rodrigo-carrillo/PeruMedQA.
- **License/attribution recorded:** Apache-2.0
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [perumedqa/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/perumedqa/metadata.yaml); historical SHA-256 `48c73dccdde7ef47dca345804d8b1a7932577090c4ab9dd9ef25ab3b1a330484`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `perumedqa/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@article{carrillolarco2025perumedqa,
  title={PeruMedQA: Benchmarking Large Language Models (LLMs) on Peruvian Medical Exams -- Dataset Construction and Evaluation},
  author={Carrillo-Larco, Rodrigo M. and Lov\'on Melgarejo, Jesus and Castillo-Cara, Manuel and Bravo-Rocca, Gusseppe},
  journal={arXiv preprint arXiv:2509.11517},
  year={2025},
  url = {https://github.com/rodrigo-carrillo/PeruMedQA}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- release: https://github.com/rodrigo-carrillo/PeruMedQA — `709158accc32fed76e32b0c9b6c3b0ef759766ab`

## real_webagents

- **Original identifier:** `real_webagents`; **benchmark name:** REAL.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://realevals.xyz/api/getVerifiedModelData.
- **Citation keys:** `garg2025realbenchmarkingautonomousagents`.
- **Stable citation URLs:** https://arxiv.org/abs/2504.11543.
- **License/attribution recorded:** unknown
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [real_webagents/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/real_webagents/metadata.yaml); historical SHA-256 `07773643c7d995aca42aaa6135e135c7716323e4a749e4224cef683e505d1fb8`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `real_webagents/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{garg2025realbenchmarkingautonomousagents,
  title={REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites},
  author={Divyansh Garg and Shaun VanWeelden and Diego Caples and Andis Draguns and Nikil Ravi and Pranav Putta and Naman Garg and Tomas Abraham and Michael Lara and Federico Lopez and James Liu and Atharva Gundawar and Prannay Hebbar and Youngchul Joo and Jindong Gu and Charles London and Christian Schroeder de Witt and Sumeet Motwani},
  year={2025},
  eprint={2504.11543},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2504.11543},
}
```

Recorded upstream pins (not substituted for the MDB revision):

- tasks: https://github.com/agi-inc/REAL — `56d8f1643bdaa5e662086b1a357a9693c9ededf6`

## revolve

- **Original identifier:** `revolve`; **benchmark name:** REVOLVE.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/Peiyance/REVOLVE.
- **Citation keys:** `zhang2025revolve`.
- **Stable citation URLs:** https://github.com/Peiyance/REVOLVE.
- **License/attribution recorded:** MIT
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [revolve/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/revolve/metadata.yaml); historical SHA-256 `c001d565aa5e80c4240bdfd0b7d8be4031ae7bc44a429fcb7243e85bef61b065`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `revolve/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@inproceedings{zhang2025revolve,
  title={REVOLVE: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization},
  author={Zhang, Peiyan and Jin, Haibo and Hu, Leyang and Li, Xinnuo and Kang, Liying and Luo, Man and Song, Yangqiu and Wang, Haohan},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2025},
  url = {https://github.com/Peiyance/REVOLVE}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- predictions: https://github.com/Peiyance/REVOLVE — `63fa604d5df7c9c3262c77c9f58d4697cd7b0fbc`

## taubench

- **Original identifier:** `taubench`; **benchmark name:** tau-bench.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/sierra-research/tau-bench.
- **Citation keys:** `yao2024taubench`, `stroebl2026hal`.
- **Stable citation URLs:** https://arxiv.org/abs/2406.12045; https://github.com/princeton-pli/hal-harness.
- **License/attribution recorded:** Original Sierra code and tasks: MIT. HAL traces: public analysis release; no separate data license found in the captured export repository.
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s). HAL is a distinct result-export/harness reference; it is not a second fitting benchmark.
- **Pinned citation metadata:** [taubench/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/taubench/metadata.yaml); historical SHA-256 `39bd8ec34d06c3ad324cef462d63f35ae6633f6c6b0f42bf8678878aef059a9e`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `taubench/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{yao2024taubench,
  title = {tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains},
  author = {Shunyu Yao and Noah Shinn and Pedram Razavi and Karthik Narasimhan},
  year = {2024},
  url = {https://arxiv.org/abs/2406.12045}
}
```

```bibtex
@inproceedings{stroebl2026hal,
  title = {HAL: A Holistic Agent Leaderboard for Centralized and Reproducible Agent Evaluation},
  author = {Benedikt Stroebl and Sayash Kapoor and Arvind Narayanan},
  year = {2026},
  booktitle = {The International Conference on Learning Representations},
  url = {https://github.com/princeton-pli/hal-harness}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- sierra: https://github.com/sierra-research/tau-bench — `59a200c6d575d595120f1cb70fea53cef0632f6b`
- hal_runs: https://huggingface.co/datasets/agent-evals/hal_traces — `e7dcedc82b4f4bc819a170fd6616bdb44841c71e`
- hal_protocol: https://github.com/princeton-pli/hal-harness — `16bb03ebc11577fb5ea6dc8bb6c968387085e6aa`

## visual_riddles

- **Original identifier:** `visual_riddles`; **benchmark name:** Visual Riddles.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://huggingface.co/datasets/visual-riddles/visual_riddles.
- **Citation keys:** `bittonguetta2024visualriddlescommonsenseworld`.
- **Stable citation URLs:** https://arxiv.org/abs/2407.19474.
- **License/attribution recorded:** Apache-2.0 declared; see upstream card for commercial-training restriction and retained image rights
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [visual_riddles/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/visual_riddles/metadata.yaml); historical SHA-256 `4885d025d3ad6258d23b683ff8d7611ffd5a1b10bcaa39ddd572daf9346fd43c`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `visual_riddles/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{bittonguetta2024visualriddlescommonsenseworld,
      title={Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models},
      author={Nitzan Bitton-Guetta and Aviv Slobodkin and Aviya Maimon and Eliya Habba and Royi Rassin and Yonatan Bitton and Idan Szpektor and Amir Globerson and Yuval Elovici},
      year={2024},
      eprint={2407.19474},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2407.19474},
}
```

Recorded upstream pins (not substituted for the MDB revision):

- release: https://huggingface.co/datasets/visual-riddles/visual_riddles — `f944390e356887f91be078458ec492adb23a4e2a`

## visualwebarena

- **Original identifier:** `visualwebarena`; **benchmark name:** VisualWebArena.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://huggingface.co/datasets/McGill-NLP/agent-reward-bench.
- **Citation keys:** `koh2024visualwebarena`, `lu2025agentrewardbench`.
- **Stable citation URLs:** https://arxiv.org/abs/2401.13649; https://arxiv.org/abs/2504.08942.
- **License/attribution recorded:** AgentRewardBench custom dataset terms: use must be lawful and respect third-party rights and applicable third-party conditions; the source describes research use under applicable fair-use provisions. Derivatives must retain those terms, captured in raw/README.md. The VisualWebArena code's MIT license is not asserted to license these separately released trajectories.
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s).
- **Pinned citation metadata:** [visualwebarena/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/visualwebarena/metadata.yaml); historical SHA-256 `351871dfa87d05f7e7c7bea61e4eec6e271ef14e10991f650e26aca18d36cebe`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `visualwebarena/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{koh2024visualwebarena,
  title = {VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks},
  author = {Jing Yu Koh and Robert Lo and Lawrence Jang and Vikram Duvvur and Ming Chong Lim and Po-Yu Huang and Graham Neubig and Shuyan Zhou and Ruslan Salakhutdinov and Daniel Fried},
  year = {2024},
  url = {https://arxiv.org/abs/2401.13649}
}
```

```bibtex
@misc{lu2025agentrewardbench,
  title = {AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories},
  author = {Xing Han Lù and Amirhossein Kazemnejad and Nicholas Meade and Arkil Patel and Dongchan Shin and Alejandra Zambrano and Karolina Stańczak and Peter Shaw and Christopher J. Pal and Siva Reddy},
  year = {2025},
  url = {https://arxiv.org/abs/2504.08942}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- released_records: https://huggingface.co/datasets/McGill-NLP/agent-reward-bench — `b6d17e646009d6cb63d5dd7be78807b680693f61`
- task_images: https://github.com/web-arena-x/visualwebarena — `89f5af29305c3d1e9f97ce4421462060a70c9a03`
- libvisualwebarena: https://files.pythonhosted.org/packages/5c/de/321b533a7ec8538396addbc3206eef0ada4153208f783679e6091d94b2f7/libvisualwebarena-0.0.15-py3-none-any.whl — `sha256:02c2f66b6a7ccb98e11c6decd8b00e8fc262223b002b80a13464e20bcdfe2999`
- browsergym_visualwebarena: https://files.pythonhosted.org/packages/47/5a/5022fb0e073b51caa8190b839d2055743f2f645de52af3d6afd67d22a71b/browsergym_visualwebarena-0.13.3-py3-none-any.whl — `sha256:a42c200023497a4970290fce39b419a93aadfc9e92c02ae602704d2957e5e531`

## workarena

- **Original identifier:** `workarena`; **benchmark name:** WorkArena.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://huggingface.co/datasets/McGill-NLP/agent-reward-bench.
- **Citation keys:** `drouin2024workarena`, `lu2025agentrewardbench`.
- **Stable citation URLs:** https://arxiv.org/abs/2403.07718; https://arxiv.org/abs/2504.08942.
- **License/attribution recorded:** AgentRewardBench custom dataset terms: use must be lawful and respect third-party rights and applicable third-party conditions; the source describes research use under applicable fair-use provisions. Derivatives must retain those terms, captured in raw/README.md. The WorkArena code's Apache-2.0 license is not asserted to license these separately released trajectories.
- **Citation confidence / remaining uncertainty:** Primary bibliographic fields checked at the linked author/arXiv record(s).
- **Pinned citation metadata:** [workarena/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/workarena/metadata.yaml); historical SHA-256 `2a9212b994ba1a32cdf48e4c135e650dc787d6220afd4f1acbadb8d3f06defd7`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `workarena/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@misc{drouin2024workarena,
  title = {WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?},
  author = {Alexandre Drouin and Maxime Gasse and Massimo Caccia and Issam H. Laradji and Manuel Del Verme and Tom Marty and Léo Boisvert and Megh Thakkar and Quentin Cappart and David Vazquez and Nicolas Chapados and Alexandre Lacoste},
  year = {2024},
  url = {https://arxiv.org/abs/2403.07718}
}
```

```bibtex
@misc{lu2025agentrewardbench,
  title = {AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories},
  author = {Xing Han Lù and Amirhossein Kazemnejad and Nicholas Meade and Arkil Patel and Dongchan Shin and Alejandra Zambrano and Karolina Stańczak and Peter Shaw and Christopher J. Pal and Siva Reddy},
  year = {2025},
  url = {https://arxiv.org/abs/2504.08942}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- released_records: https://huggingface.co/datasets/McGill-NLP/agent-reward-bench — `b6d17e646009d6cb63d5dd7be78807b680693f61`
- protocol_reference: https://github.com/McGill-NLP/agent-reward-bench — `05899fcfe52c925978944a23920373b7a9c63740`

## workbench_revisited

- **Original identifier:** `workbench_revisited`; **benchmark name:** WorkBench Revisited.
- **Historical source identity:** VERIFIED in the frozen prior training list and retained split; it was not substituted.
- **Original publication/repository or export:** https://github.com/olly-styles/WorkBench.
- **Citation keys:** `styles2026workbenchrevisited`, `styles2024workbench`.
- **Stable citation URLs:** https://arxiv.org/abs/2606.13715; https://github.com/olly-styles/WorkBench.
- **License/attribution recorded:** MIT
- **Citation confidence / remaining uncertainty:** Citation retained from the hash-pinned MDB metadata receipt; no new independent publisher/complete-author-list audit.
- **Pinned citation metadata:** [workbench_revisited/metadata.yaml](https://huggingface.co/datasets/aims-foundations/measurement-db/resolve/54074453da7b9911be0f48e4c560be547bc84d21/workbench_revisited/metadata.yaml); historical SHA-256 `c3109e8b547fabb9cce4f8cece76e6c33d4634d5862ea29fd1a1375c300282bb`.
- **Training provenance reference:** `provenance/historical_cohort_bridge.json` retained_training; `provenance/historical_training_receipts.json` entries for `workbench_revisited/formatted_tables/{subjects,items,responses}.parquet`. These are historical hash receipts, not fresh raw-table reads.

```bibtex
@article{styles2026workbenchrevisited,
      title={WorkBench Revisited: Workplace Agents Two Years On},
      author={Styles, Olly and Miller, Sam},
      year={2026},
      eprint={2606.13715},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2606.13715},
}
```

```bibtex
@inproceedings{styles2024workbench,
      title={WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting},
      author={Styles, Olly and Miller, Sam and Cerda-Mardini, Patricio and Guha, Tanaya and Sanchez, Victor and Vidgen, Bertie},
      booktitle={Conference on Language Modeling (COLM)},
      year={2024},
  url = {https://github.com/olly-styles/WorkBench}
}
```

Recorded upstream pins (not substituted for the MDB revision):

- release: https://github.com/olly-styles/WorkBench — `da6f8ee8d9f8efc87b2f5f3cc9edc1befdac726e`
- verdicts: https://github.com/olly-styles/WorkBench — `7844e94c0a1f5c138699562830c37f37ede6d51b`

## Explicit limitations

Some legacy citations abbreviate authors or lack DOI/venue details; stable original repositories/publication links are supplied rather than invented fields. MedHELM's exact export is identified, but its underlying task attribution is not asserted exhaustively resolved by the MedHELM citation alone. Unknown raw/export license fields stay unknown. These limitations prohibit claiming universal raw redistribution or exhaustive primary bibliographic verification; they do not erase verified fitting-source identities or justify substituting new benchmarks. Supplementary original-work attribution may be enriched by the manuscript editor without changing the frozen scientific record.
