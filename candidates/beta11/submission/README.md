# Fixed Beta(1,1) with official random acquisition

`model.py` exposes `predict(input, labeled=None) -> float`.
For matching revealed responses, s successes out of n observations gives
p = (s + 1) / (n + 2). Zero matching labels gives 0.5.

Grouping uses equality of the complete visible subject dictionary and the
item's anonymous benchmark_id. Other subjects and benchmarks are excluded.
Only the current call's revealed evidence is used. Calls can arrive in any
budget order or in fresh worker processes. Missing benchmark IDs with supplied
labels raise an error instead of silently pooling benchmarks.

There is deliberately no labeling.py. The official PAIEC runtime therefore
uses its default sequential random acquisition at budgets 0, 1, 3, 7, 15, 31.
No diversity policy, learned prior, fitted state, public data or heldout labels
are included. No third-party packages, model downloads, API keys, GPU or network
access are required. Python 3.10 or later is supported by the annotations.

Derived from the official aims-foundations/paiec_baseline empirical_mean
predictor's interface and isolation guards, with its empirical mean replaced
by the established research Beta(1,1) formula. Official source commit:
82d330ddcdb16016a3ae9e048db7e588ba2c6a39.
Reference: https://aimslab.stanford.edu/competition

No training was performed for this package. Method selection was informed by
local public Measurement Data Bank development experiments, revision
54074453da7b9911be0f48e4c560be547bc84d21. No dataset is bundled.
Developed with assistance from OpenAI Codex. This ZIP is an inference artifact,
not a full competition technical report. It has not been submitted.
