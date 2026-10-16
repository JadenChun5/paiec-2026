# Current fitting-source index

The authoritative historical fitting list is the 17 retained identifiers in TRAINING_SOURCE_CITATION_REGISTER.md, with machine-readable BibTeX in TRAINING_SOURCE_CITATIONS.bib. The broader legacy register below includes previously scored development sources; it does NOT imply all listed sources were used to fit EB. Targeted citation completions in the new 17-source register supersede abbreviated legacy bibliographic fields without changing source identities or results.

# Data source citations and scope

Curation attribution: AIMS Foundations / Measurement Data Bank, pinned source revision linked below. The copied/adapted AIMS-owned citation and curation material in this document is provided under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Changes: selected previously used fitting/development sources, reorganized metadata into this register and added scope commentary. This license statement is confined to covered curation and its adaptation; it does not relicense original benchmark works or all project software.

Measurement Data Bank: https://huggingface.co/datasets/aims-foundations/measurement-db ; pinned revision `54074453da7b9911be0f48e4c560be547bc84d21`. Credit AIMS Foundations for curation and the original benchmark/export authors below. Citation strings are retained from the pinned public metadata as previously captured; metadata can contain incomplete bibliographic fields. This document does not redistribute tasks or responses.

## ai2d_test

Role in existing work: previously_scored_development. Public source: https://huggingface.co/datasets/VLMEval/OpenVLMRecords

Captured terms: AI2D diagrams: CC-BY-SA-4.0, linked by the AllenAI AWS Open Data registry. OpenVLMRecords and VLMEvalKit code: Apache-2.0, as declared upstream.

```text
Kembhavi, A. et al. (2016). A Diagram Is Worth A Dozen Images. ECCV. Duan, H. et al. (2024). VLMEvalKit: An Open-Source Toolkit for Evaluating Large Multi-Modality Models.
```

## algotune

Role in existing work: prior_fit. Public source: https://github.com/oripress/AlgoTune

Captured terms: MIT

```text
@inproceedings{press2025algotune,
  title={AlgoTune: Can Language Models Speed Up General-Purpose Numerical Programs?},
  author={Press, Ori and Amos, Brandon and Zhao, Haoyu and Wu, Yikai and others},
  booktitle={NeurIPS 2025 Datasets and Benchmarks Track},
  year={2025},
}
```

## appworld

Role in existing work: prior_fit. Public source: https://github.com/StonyBrookNLP/appworld-leaderboard

Captured terms: Apache-2.0

```text
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

## benger

Role in existing work: previously_scored_development. Public source: https://zenodo.org/records/20489788

Captured terms: CC BY 4.0 for data; quoted ZJS cases are restricted to the released permission-cleared subset. Author code: Apache-2.0.

```text
Nagl et al. (2026). BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law.
```

## bird_sql

Role in existing work: previously_scored_development. Public source: https://github.com/petavue/NL2SQL-Benchmark/tree/0637e2593739f82961d38a14d0d80df2b20e3060

Captured terms: MIT for the Petavue repository; its task inputs derive from BIRD.

```text
Li et al. (2023). Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs. NeurIPS Datasets and Benchmarks. Results: Petavue NL2SQL-Benchmark (2024).
```

## causal_axioms

Role in existing work: previously_scored_development. Public source: https://github.com/AniketVashishtha/Causal_Axioms

Captured terms: unknown

```text
@inproceedings{vashishtha2025teaching,
  title={Teaching Transformers Causal Reasoning through Axiomatic Training},
  author={Vashishtha, Aniket and Kumar, Abhinav and Pandey, Atharva and Reddy, Abbavaram Gowtham and Ahuja, Kabir and Balasubramanian, Vineeth N and Sharma, Amit},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2025}
}
```

## ceval

Role in existing work: prior_fit. Public source: https://github.com/liyucheng09/Contamination_Detector

Captured terms: Questions: CC-BY-NC-SA-4.0. The third-party prediction export declares no separate license.

```text
Huang et al. (2023), C-Eval, arXiv:2305.08322; Li, Guerin and Lin (2024), An Open-Source Data Contamination Report for Large Language Models, arXiv:2310.17589v3.
```

## clasheval

Role in existing work: previously_scored_development. Public source: https://github.com/kevinwu23/StanfordClashEval

Captured terms: unknown

```text
@article{wu2024clasheval,
  title={ClashEval: Quantifying the tug-of-war between an LLM's internal prior and external evidence},
  author={Wu, Kevin and Wu, Eric and Zou, James},
  journal={arXiv preprint arXiv:2404.10198},
  year={2024},
}
```

## dave

Role in existing work: previously_scored_development. Public source: https://huggingface.co/datasets/gorjanradevski/dave

Captured terms: MIT

```text
@inproceedings{radevski2025dave,
  title={DAVE: Diagnostic benchmark for Audio Visual Evaluation},
  author={Radevski, Gorjan and Popordanoska, Teodora and Blaschko, Matthew B. and Tuytelaars, Tinne},
  booktitle={NeurIPS 2025 Datasets and Benchmarks Track},
  year={2025},
}
```

## editbench

Role in existing work: previously_scored_development. Public source: https://github.com/waynchi/editbench/tree/b406cc5143feb91e9bda1edd01cbe37d84d185fd

Captured terms: Apache-2.0

```text
@misc{chi2025editbench,
  title={EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits},
  author={Wayne Chi and Valerie Chen and Ryan Shar and Aditya Mittal and Jenny Liang and Wei-Lin Chiang and Anastasios Nikolas Angelopoulos and Ion Stoica and Graham Neubig and Ameet Talwalkar and Chris Donahue},
  year={2025},
  eprint={2511.04486},
  archivePrefix={arXiv},
  primaryClass={cs.SE}
}
```

## edu_circuit_hw

Role in existing work: previously_scored_development. Public source: https://github.com/gt-learning-innovation/CIRCUIT_EDU_HW_ACL

Captured terms: Code: Apache-2.0. The Georgia Tech dataset record states In Copyright; its CC0 statement covers metadata only. No explicit CC-BY-NC dataset license was found in the captured release.

```text
Sun, W. et al. EDU-CIRCUIT-HW: Evaluating Multimodal Large Language Models on Real-World University-Level STEM Student Handwritten Solutions. arXiv:2602.00095 (2026).
```

## elicitation_game

Role in existing work: previously_scored_development. Public source: https://github.com/Felhof/sandbagging-elicitation

Captured terms: No explicit license file in the captured author repository; upstream WMDP terms also apply.

```text
Hofstätter, F., van der Weij, T., Teoh, J., Djoneva, R., Bartsch, H., and Ward, F. R. The Elicitation Game: Evaluating Capability Elicitation Techniques. ICML (2025).
```

## engdesign

Role in existing work: previously_scored_development. Public source: https://github.com/AGI4Engineering/EngDesign

Captured terms: MIT

```text
@inproceedings{guo2025engdesign,
  title={Toward Engineering AGI: Benchmarking the Engineering Design Capabilities of LLMs},
  author={Guo, Xingang and Li, Yaxin and Kong, XiangYi and others},
  booktitle={NeurIPS 2025 Datasets and Benchmarks Track},
  year={2025},
}
```

## fewshot_ttt_bbh

Role in existing work: previously_scored_development. Public source: https://github.com/adamzweiger/Fewshot-TTT

Captured terms: MIT

```text
Akyurek et al., The Surprising Effectiveness of Test-Time Training for Few-Shot Learning, ICML 2025
```

## financebench

Role in existing work: prior_fit. Public source: https://github.com/patronus-ai/financebench/tree/22257c455f9f9ca9ca3dc67456d9a32e60c7ef08

Captured terms: unknown

```text
@misc{islam2023financebench,
  title={FinanceBench: A New Benchmark for Financial Question Answering},
  author={Pranab Islam and Anand Kannappan and Douwe Kiela and Rebecca Qian and Nino Scherrer and Bertie Vidgen},
  year={2023},
  eprint={2311.11944},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

## healthadminbench

Role in existing work: previously_scored_development. Public source: https://github.com/som-shahlab/health-admin-bench

Captured terms: Apache-2.0

```text
Bedi et al. (2026). HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks. arXiv:2604.09937.
```

## liveaopsbench

Role in existing work: prior_fit. Public source: https://github.com/LiveMathBench/LiveMathBench.github.io

Captured terms: Task dataset: Apache-2.0 (author HF card); website result/source release: CC-BY-SA-4.0; evaluator code: Apache-2.0. Original notices are captured.

```text
@article{mahdavi2025leveraging,
  title={Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation},
  author={Mahdavi, Sadegh and Li, Muchen and Liu, Kaiwen and Thrampoulidis, Christos and Sigal, Leonid and Liao, Renjie},
  journal={International Conference on Machine Learning (ICML)},
  year={2025}
}
```

## mathconstraint

Role in existing work: prior_fit. Public source: https://github.com/vireshpati/Math-Constraint

Captured terms: cc-by-4.0

```text
MathConstraint: Automated Generation of Verified Combinatorial Reasoning Instances for LLMs (arXiv 2605.08498).
```

## medhelm_race_based_med

Role in existing work: prior_fit. Public source: https://crfm.stanford.edu/helm/medhelm/

Captured terms: unknown

```text
@article{bedi2025medhelm,
  title={MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks},
  author={Bedi, Suhana and Cui, Hejie and Fuentes, Miguel and Unell, Alyssa and others and Shah, Nigam H.},
  journal={arXiv preprint arXiv:2505.23802},
  year={2025},
}
```

## mtbbench

Role in existing work: previously_scored_development. Public source: https://github.com/bunnelab/MTBBench

Captured terms: MIT

```text
@inproceedings{jain2025mtbbench,
  title={{MTBBench}: A Multimodal Sequential Clinical Decision-Making Benchmark in Oncology},
  author={Jain, Eeshaan and others},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track},
  year={2025},
  url={https://openreview.net/forum?id=anzoPBV4jI}
}
```

## naep_llm_students

Role in existing work: prior_fit. Public source: https://github.com/kvadityasrivatsa/IRT-for-LLMs-as-Students

Captured terms: MIT for the authors' recorded results and analysis code. NAEP source pages and illustrations retain their original attributions.

```text
@article{srivatsa2025naepllm,
  title={Can LLMs Reliably Simulate Real Students' Abilities in Mathematics and Reading Comprehension?},
  author={Srivatsa, KV Aditya and Maurya, Kaushal Kumar and Kochmar, Ekaterina},
  journal={arXiv preprint arXiv:2507.08232},
  year={2025}
}
```

## nyu_ctf_bench

Role in existing work: prior_fit. Public source: https://github.com/NYU-LLM-CTF/NYU_CTF_Bench

Captured terms: GPL-2.0 for the NYU_CTF_Bench task repository, with original notices retained. The separate leaderboard_submissions repository and linked forensic input do not declare explicit redistribution terms; raw and formatted data remain local pending clarification. The previous blanket MIT attribution is unsupported.

```text
@inproceedings{shao2024nyuctf,
  title={NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security},
  author={Shao, Minghao and Jancheska, Sofija and Udeshi, Meet and Dolan-Gavitt, Brendan and Xi, Haoran and Milner, Kimberly and Chen, Boyuan and Yin, Max and Garg, Siddharth and Krishnamurthy, Prashanth and Khorrami, Farshad and Karri, Ramesh and Shafique, Muhammad},
  booktitle={NeurIPS 2024 Datasets and Benchmarks Track},
  year={2024},
}
```

## openbiorq

Role in existing work: previously_scored_development. Public source: https://huggingface.co/datasets/Minbyul/OpenBioRQ

Captured terms: CC-BY-4.0

```text
Minbyul Jeong. OpenBioRQ: Unsolved Biomedical Research Questions for Agents. arXiv:2606.21959, 2026.
```

## perumedqa

Role in existing work: prior_fit. Public source: https://github.com/rodrigo-carrillo/PeruMedQA

Captured terms: Apache-2.0

```text
@article{carrillolarco2025perumedqa,
  title={PeruMedQA: Benchmarking Large Language Models (LLMs) on Peruvian Medical Exams -- Dataset Construction and Evaluation},
  author={Carrillo-Larco, Rodrigo M. and Lov\'on Melgarejo, Jesus and Castillo-Cara, Manuel and Bravo-Rocca, Gusseppe},
  journal={arXiv preprint arXiv:2509.11517},
  year={2025},
}
```

## planbench

Role in existing work: previously_scored_development. Public source: https://github.com/karthikv792/LLMs-Planning

Captured terms: MIT

```text
@inproceedings{valmeekam2023planbench,
  title={PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change},
  author={Valmeekam, Karthik and Marquez, Matthew and Olmo, Alberto and Sreedharan, Sarath and Kambhampati, Subbarao},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track},
  year={2023}
}
Related result releases: Valmeekam et al. (2023), On the Planning Abilities of Large Language Models; Valmeekam et al. (2025), A Systematic Evaluation of the Planning and Scheduling Abilities of the Reasoning Model o1. See the original README for full citations.
```

## real_webagents

Role in existing work: prior_fit. Public source: https://realevals.xyz/api/getVerifiedModelData

Captured terms: unknown

```text
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

## reliancescope

Role in existing work: previously_scored_development. Public source: https://osf.io/27ec5/

Captured terms: Not specified in the captured dataset sources.

```text
Jin et al. RelianceScope: An Analytical Framework for Examining Students’ Reliance on Generative AI Chatbots in Problem Solving. L@S 2026. arXiv:2602.16251.
```

## revolve

Role in existing work: prior_fit. Public source: https://github.com/Peiyance/REVOLVE

Captured terms: MIT

```text
@inproceedings{zhang2025revolve,
  title={REVOLVE: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization},
  author={Zhang, Peiyan and Jin, Haibo and Hu, Leyang and Li, Xinnuo and Kang, Liying and Luo, Man and Song, Yangqiu and Wang, Haohan},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2025}
}
```

## sketchjudge

Role in existing work: previously_scored_development. Public source: https://github.com/yuhangsu82/SketchJudge

Captured terms: Apache-2.0 for the GitHub project. The external diagram archive has no separate license declaration; captured data remain local pending redistribution clarification.

```text
@article{su2026sketchjudge,
  title={SketchJudge: A Diagnostic Benchmark for Grading Hand-drawn Diagrams with Multimodal Large Language Models},
  author={Su, Yuhang and Wang, Mei and Zhong, Yaoyao and Li, Guozhang and Li, Shixing and Feng, Yihan and Huang, Hua},
  journal={arXiv preprint arXiv:2601.06944},
  year={2026}
}
```

## software_world_models

Role in existing work: previously_scored_development. Public source: https://huggingface.co/collections/JetBrains-Research/dl4c26-evaluation-of-software-world-model

Captured terms: unknown

```text
Bogomolov and Zharov. Towards Evaluation of Implicit Software World Models in Coding LLMs. 2026.
```

## statqa

Role in existing work: previously_scored_development. Public source: https://github.com/HKUSTDial/StatQA

Captured terms: GPL-3.0 as declared by the original repository LICENSE. This capture includes the released benchmark definitions and outputs, not unrelated upstream Kaggle datasets.

```text
@inproceedings{zhu2024statqa,
 author = {Zhu, Yizhang and Du, Shiyin and Li, Boyan and Luo, Yuyu and Tang, Nan},
 booktitle = {Advances in Neural Information Processing Systems},
 title = {Are Large Language Models Good Statisticians?},
 year = {2024}
}
```

## subjective_qa

Role in existing work: previously_scored_development. Public source: https://github.com/gtfintechlab/SubjECTive-QA

Captured terms: CC-BY-4.0

```text
@article{pardawala2024subjective,
  title={SubjECTive-QA: Measuring Subjectivity in Earnings Call Transcripts' QA Through Six-Dimensional Feature Analysis},
  author={Pardawala, Huzaifa and Sukhani, Siddhant and Shah, Agam and Kejriwal, Veer and Pillai, Abhishek and Bhasin, Rohan and DiBiasio, Andrew and Mandapati, Tarun and Adha, Dhruv and Chava, Sudheer},
  journal={arXiv preprint arXiv:2410.20651},
  year={2024}
}
```

## taubench

Role in existing work: prior_fit. Public source: https://github.com/sierra-research/tau-bench

Captured terms: Original Sierra code and tasks: MIT. HAL traces: public analysis release; no separate data license found in the captured export repository.

```text
Yao, Shinn, Razavi and Narasimhan. tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains. 2024. HAL run provenance: Stroebl, Kapoor and Narayanan, HAL: A Holistic Agent Leaderboard for Centralized and Reproducible Agent Evaluation, 2026.
```

## visual_riddles

Role in existing work: prior_fit. Public source: https://huggingface.co/datasets/visual-riddles/visual_riddles

Captured terms: Apache-2.0 declared; see upstream card for commercial-training restriction and retained image rights

```text
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

## visualwebarena

Role in existing work: prior_fit. Public source: https://huggingface.co/datasets/McGill-NLP/agent-reward-bench

Captured terms: AgentRewardBench custom dataset terms: use must be lawful and respect third-party rights and applicable third-party conditions; the source describes research use under applicable fair-use provisions. Derivatives must retain those terms, captured in raw/README.md. The VisualWebArena code's MIT license is not asserted to license these separately released trajectories.

```text
Koh et al. (2024), VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks, arXiv:2401.13649. Lu et al. (2025), AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories, arXiv:2504.08942.
```

## workarena

Role in existing work: prior_fit. Public source: https://huggingface.co/datasets/McGill-NLP/agent-reward-bench

Captured terms: AgentRewardBench custom dataset terms: use must be lawful and respect third-party rights and applicable third-party conditions; the source describes research use under applicable fair-use provisions. Derivatives must retain those terms, captured in raw/README.md. The WorkArena code's Apache-2.0 license is not asserted to license these separately released trajectories.

```text
Drouin et al. (2024), WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?, arXiv:2403.07718. Lu et al. (2025), AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories, arXiv:2504.08942.
```

## workbench_revisited

Role in existing work: prior_fit. Public source: https://github.com/olly-styles/WorkBench

Captured terms: MIT

```text
@article{styles2026workbenchrevisited,
      title={WorkBench Revisited: Workplace Agents Two Years On},
      author={Styles, Olly and Miller, Sam},
      year={2026},
      eprint={2606.13715},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2606.13715},
}
@inproceedings{styles2024workbench,
      title={WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting},
      author={Styles, Olly and Miller, Sam and Cerda-Mardini, Patricio and Guha, Tanaya and Sanchez, Victor and Vidgen, Bertie},
      booktitle={Conference on Language Modeling (COLM)},
      year={2024},
}
```

The 17 prior_fit sources contribute to the frozen EB estimator. Other listed sources are previously used public development sources; none is a disclosure of private final-family membership. No blanket third-party permission is inferred from MDB curation terms. No reviewed source-specific clause expressly prohibited publication of these two learned scalars or the selected aggregate comparisons; missing raw-export licenses are not asserted to ban non-reconstructive analysis. No source data, question text, image or trajectory is included.
