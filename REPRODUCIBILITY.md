# Reproducibility and validation

Run commands from the extracted FINAL_PUBLIC_RELEASE_CANDIDATE root. Use fresh work directories OUTSIDE the candidate. Frozen sources/parameters are unchanged; this assignment ran only synthetic software verification and mocked fitting fixtures. It did not run scientific experiments or build either frozen submission ZIP.

## 1. Method, fitting and datasets

The exact interface is `predict(input, labeled)` in candidates/global_eb/submission/model.py. The target's full subject dictionary and anonymous benchmark ID filter evidence; other pairs are ignored. Each supplied matching labeled record contributes one observation. The zero-label probability is the fixed prior mean. No labeling.py is included, so acquisition is official random.

The prior was fitted once on 17 verified historical benchmark identifiers, 198 pairs and 211,256 item-group observations, by training-only equal-pair composite Beta-binomial marginal likelihood. The frozen objective, five starts, analytic-gradient optimizer, bounds and one-trial sampling rule are documented in HISTORICAL_TRAINING_PROVENANCE.md. The exact source identifiers, citations, original/export provenance and licensing uncertainties are in TRAINING_SOURCE_CITATION_REGISTER.md. Do not substitute current benchmarks or retune the constants.

## 2. Environment

The predictor and local contract/ZIP validation require Python 3.12 and standard-library modules. Research preparation/fixtures require the optional packages below. This completion verified Python 3.12.14 on the local Mac.

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements-research.txt --only-binary=:all: --index-url https://pypi.org/simple
```

A fresh isolated environment was created using the locally available Python 3.12.14 executable, avoiding an interpreter download. The exact dependency-install command above (with that environment path) succeeded: 21 packages installed/resolved. All five direct imports passed, and the original synthetic reproduction fixture passed in the fresh environment. Direct pins are numpy 2.5.1, scipy 1.18.0, pandas 3.0.3, pyarrow 25.0.0 and huggingface-hub 1.22.0. These are observed compatible versions, not a full historical/transitive platform lock. A CPU and modest RAM suffice for these small fixtures; full historical data replay has separate resource/access needs.

## 3. Official local validation

Obtain the organizer's official starting kit separately and extract it outside this candidate. Its prior verified archive hash is `a870970a7b9e82385929db37435aac29e3f0ee648cce7df143787b88ac4770f6`; exact expected member hashes are in provenance/official-kit-pins.json. This repository does not redistribute the separate kit. Stop on a hash mismatch rather than silently replace its version. Competition information: https://aimslab.stanford.edu/competition .

```sh
.venv/bin/python -B tools/verify_local.py --kit-dir /path/to/extracted-official-kit --work ../fresh-local-validation
```

This entry point checks pinned kit members and the frozen EB archive, runs the unchanged 11-test synthetic suite, two official ZIP validators, and sequential/requested-four-worker official smoke tests. It does not rebuild the archive. Verified: 11/11 tests, both validators and both smoke modes passed. The toy smoke only has two inputs; separate synthetic suite checks started actual one-/four-worker pools across all six budgets and verified 96 worker forecasts. Local success does not authenticate a hosted receipt or prove competitive performance.

## 4. Fabricated research-workflow fixtures

```sh
.venv/bin/python -B tools/verify_reproduction_fixtures.py --work ../fresh-synthetic-fixtures
```

The wrapper generates 23 entirely fabricated sources (3,680 responses), runs unchanged prepare.py on these generated tables, checks 24 training-pair count records, replaces the fit function with a mock, and invokes the existing summarize function on arbitrary synthetic loss values. Seven assertions passed, including correct family grouping despite repeated seeds. No optimizer or learned predictor is trained; no historical response file or protected outcome is opened. Network access is denied during synthetic preparation. Verified in both the existing and new dependency environments.

## 5. Authorized dataset access — no data bundled

Request your own access at https://huggingface.co/datasets/aims-foundations/measurement-db and comply with its terms and underlying source requirements. Configure authentication locally; never put a token in repository files or logs. Raw/export permissions are separate from MIT code and authorization to publish derived analyses.

```sh
.venv/bin/python -B tools/acquire_training_source.py --benchmark algotune --table subjects --work ../authorized-reproduction/research/phase4 --dry-run
```

Verified dry run: no authentication or network request. After independently authorized access, removing --dry-run invokes the original downloader for the chosen table at revision 54074453da7b9911be0f48e4c560be547bc84d21. The helper accepts only the 17 retained training names and subjects/items/responses tables, writes outside the repository, and retains the source size cap. Compare downloaded bytes to the historical receipts before use. An existing cache file is returned unchanged by the original downloader; independently checking hashes is essential. No dataset was downloaded in this assignment.

## 6. Historical fitting — conditional, not a turnkey public replay

An exact preparation depends on the original ordered full cohort, including sources used for cross-benchmark content/alias exclusion before coverage gates, not only the 17 retained fitting sources. The full private selection-plan.json and data-inventory.json, original protocol.json and protocol.sha256, and authorized source tables are not distributed. Original source manifests and hashes were previously located/verified; the sanitized training bridge and historical table receipts document that lineage without exposing protected identities.

A separately authorized researcher with those exact historical inputs can copy the existing research/phase4 layout into a NEW workspace, verify all code/config/source bindings, and execute:

```sh
cd /path/to/authorized-workspace/research/phase4
/path/to/environment/bin/python -B scripts/prepare.py
/path/to/environment/bin/python -B scripts/fit.py
```

These commands were NOT executed on real data. Fit.py also performs historical source-omission diagnostic fits. Do not replace the saved prior. Exact data/serialization and count equivalence must be established before claiming numerical reproduction. The 17-source acquisition helper alone is insufficient to reconstruct global duplicate exclusions. A training-only rerun would be a different analysis, not exact historical replication. Original common.py/run.py have only documented path-portability changes; prepare.py/fit.py are exact source copies.

## 7. Predictor construction and submission packaging

Use artifacts/global_eb_frozen.zip for the unchanged reviewed artifact; source is candidates/global_eb/submission/model.py. A future separately authorized packaging reproduction can write a distinct new destination:

```sh
.venv/bin/python -B candidates/global_eb/tools/build_zip.py --output /path/to/new-work/reproduced-global-eb.zip
```

The original builder was inspected and its CLI parsed through --help only. It writes exclusively, includes model.py and README.md, and introduces no acquisition override. No builder was invoked to create a predictor ZIP in this assignment. Do not substitute a rebuilt artifact silently. The archived independent builder expects its original layout and a comparison ZIP/outputs directory; it is provenance code, not the default release command. Preserve both Stanford and project MIT notices with any adapted-code distribution.

## 8. Local results and restricted experiments

The two results/*.json files are unchanged Phase 3 and Phase 4-development aggregate records. They concern different cohorts; do not pool them or treat them as hosted scores. Official budget weights are (.1,.2,.2,.2,.2,.1) at 0,1,3,7,15,31 labels, with equal pair weighting. Family uncertainty is not based on treating seeds or rows as independent families. Synthetic values are tests, not research results.

Historical run.py is included for transparency; its main evaluates development AND its old holdout, so it must not be blindly invoked as a development-only test. The safe fixture calls only its existing summarize function on fabricated losses. Reproducing a permitted historical comparison requires its original authorized pools/protocol; those are not supplied here. The protected eleven-family evaluation, individual forecasts/outcomes and private family identities are excluded. No public reproduction guarantee is made for them.
