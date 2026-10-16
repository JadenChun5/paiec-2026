# Reproducibility verification — Assignment 4

All execution was local and bounded to software tests, fabricated fixtures and environment setup. Neither frozen predictor ZIP was built or modified, no real-data fitting/scoring was performed, and no protected outcome or response file was opened.

| Check | Exact result |
|---|---|
| Isolated environment | Python 3.12.14, macOS arm64; new uv virtual environment created |
| Dependency install | 21 packages installed successfully using pinned direct requirements and binary wheels; 2 cache preparations, including a 3.4 MiB hf-xet download; no model weights |
| Dependency consistency | 21 packages checked; all compatible; all five direct imports pass |
| Original EB synthetic suite | 11/11 tests pass, including all 528 admissible count combinations, filtering/isolation, empty/repeated evidence and no-I/O interface checks |
| Official ZIP validation | Baseline validator PASS; starting-kit validator PASS |
| Official smoke | Sequential PASS; requested-four-worker PASS (toy case has two inputs) |
| Actual worker regression | Six one-worker and six four-worker pools at the six budgets; 96 synthetic worker predictions verified by original suite |
| Research preparation/statistics fixture | 7/7 checks: 23 fabricated sources, 3,680 prepared rows, 24 training pairs; fitting mocked, no optimization |
| Fresh dependency environment fixture | Same 7/7 assertions pass in freshly installed environment |
| Acquisition helper | Explicit dry run PASS; no auth or network data access |
| Predictor packaging instruction | Existing builder --help parses; source inspected; builder NOT used to rebuild any predictor ZIP |
| Reproduction boundary | Full historical fitting and historical comparisons require authorized original cohort/pool/protocol inputs; restricted final evaluation not offered as publicly reproducible |

Fresh direct versions: numpy 2.5.1, scipy 1.18.0, pandas 3.0.3, pyarrow 25.0.0, huggingface-hub 1.22.0. No new library was added to the declared research requirements. Existing source/tests are byte-identical to the approved private candidate; only documentation and attribution material changed.

Detailed local receipts are retained in the private publication-review evidence bundle. A sanitized summary is included at provenance/local_validation.json. Previous synthetic numerical findings are not new research findings. Source/version hashes, archive extraction and frozen artifact checks are recorded in the release review in the private review bundle. Local validation does not authenticate hosted Codabench receipts or prove competitiveness.
