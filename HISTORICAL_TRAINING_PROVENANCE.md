# Historical training provenance — verified records and bounded reproduction

## Finding

The original historical cohort and exclusion records exist. Their current hashes match the frozen Phase 4 protocol's selection/split bindings, and all six original scientific source hashes match that protocol. This closes the missing-record identification problem. It does not make the public candidate a complete raw-to-fit replay: full historical cohort manifests and raw data remain outside this package, and exact duplicate exclusions depend on that full cohort. No training or evaluation was run.

## Frozen origin

- Dataset: aims-foundations/measurement-db, revision `54074453da7b9911be0f48e4c560be547bc84d21`.
- Original plan frozen 2026-10-10T06:03:00.285058+00:00; scientific protocol frozen 2026-10-10T06:06:10.396738+00:00; prior saved 2026-10-10T06:07:04.616701+00:00.
- Frozen alpha `1.1814007859059947`, beta `1.278451593031275`; no refitting or parameter change.
- Original selection: 18 training candidates, four development candidates, 12 historical holdout candidates. Retained: 17 / 4 / 11. The historical Phase 4 holdout is not the later reserved final-family evaluation. No final-family identity or data was read for this work.
- Training exclusion: `fewshot_ttt_bbh`, saved status COVERAGE_EXCLUDED (zero qualifying pairs after grouping/coverage). No replacement was selected. The other 17 training names are in provenance/training_sources.json.
- Saved training coverage: 198 subject–benchmark pairs, 189 visible subject profiles, 285,454 eligible response observations. Historical Phase 10A prior verification records 211,256 one-trial-per-group fitting observations. These are saved development-side facts, not recomputed outcomes.

## Source receipts and exact code

provenance/historical_training_receipts.json contains all 54 original SHA-256/size receipts for subjects/items/responses of the 18 training candidates. They are transcribed from the original Phase 4 file-manifest, not hashes of raw files reread today. Downloading at a pinned dataset commit is necessary but insufficient: check the exact receipt bytes, including files reused by prepare.py from Phase 3's cache. Existing files are trusted by the original downloader; reproducing without checking them could silently use stale content.

provenance/historical_cohort_bridge.json binds the original plan, retained split, inventory, preparation audit, protocol, saved verification and learned prior to their current hashes. Original manifests are retained privately; only training identities and non-outcome counts are exported here. Original prepared-data hash is a historical receipt only, not a new verification of protected or raw data.

## Exact preparation behavior (static inspection)

1. Use the original ordered train/development/holdout arrays and data-inventory lookup at the pinned revision. Catalog selection required public, binary, item-level, higher-is-better compatible releases, with named ambiguous-label exclusions and source-family grouping. Selection was purposive catalog/domain coverage, not fitted performance selection.
2. Use each source's subjects/items/responses tables; enforce unique subject/item IDs, foreign keys and the catalog benchmark ID. Repeated response IDs are dropped only if their entire rows agree; otherwise stop. Keep only responses in {0,1}; discard empty item content.
3. Subject key is SHA-256 of sorted JSON of eight visible attributes, missing values replaced by empty strings: normalized_name, provider, release_date, access_date, harness, harness_version, reasoning_effort, subject_features_extra.
4. Content key is SHA-256 of NFKC, case-folded, whitespace-collapsed text. Within each source, connect equal content or equal nonempty raw_item_id. Preserve original source row order and connected-component implementation; substituting a different canonical representative is not a verified equivalent.
5. Build the item-content index across ALL selected sources, including candidates subsequently excluded for coverage. If content occurs in more than one source, remove the entire linked item component from every affected source. This exclusion uses item content, but exact preparation still reads labels for binary filtering and coverage; it is not an outcome-blind public shortcut.
6. Keep subject–benchmark pairs with at least 80 distinct groups; keep sources with at least two such profiles. Enforce original no-replacement split-size gates. Preserve response aliases/trials in eligible-responses.parquet until fit-time selection.
7. Original output columns: subject_id, item_id, response_id, response, trial, benchmark, subject_key, item_group, content_group, split, family. Original preparation audit and split manifest record exclusions/coverage. An exact exported row-by-row removal list is not included; deterministic replay from full inputs is the supported reconstruction route.

## Estimation and separation

Only split=train enters the objective. For each benchmark/profile, sort item groups and response IDs, use PCG64 seeded by the first 16 hex characters of SHA-256 of `phase4-fit-trials-v1|benchmark|subject_key`, and select one recorded binary trial per group. Minimize the mean negative Beta-binomial marginal log likelihood over pairs, with alpha=sigmoid(u)*exp(v), beta=(1-sigmoid(u))*exp(v), u in [-6,6], concentration in [.05,1000]. The frozen protocol specifies five starts, analytic-gradient L-BFGS-B, ftol 1e-12, gtol 1e-8, maxiter 2000 and rejection of failed/boundary solutions. Source-omission fits are diagnostics, not a prior-selection procedure. Development and historical holdout labels do not enter fitting, though their content participated in cross-source duplicate exclusions.

The public common.py changes only interpreter portability; prepare.py and fit.py are exact original copies. run.py changes only its baseline lookup path. Neither run.py nor fit.py should be executed casually: fit.py includes diagnostic refits, run.py includes the old holdout evaluation. No protected final-evaluation procedure is offered here.

## Strongest supported reproduction procedure

A. Anyone can inspect the frozen formula/source and reproduce synthetic interface checks with the instructions in REPRODUCIBILITY.md. This requires no gated data or training.

B. An independently authorized researcher can request/access the exact historical preparation manifests and full selected source cohort, verify the manifest/code hashes and all recorded table hashes, place them in a NEW original-layout workspace, and run unchanged prepare.py followed by fit.py. Verify prepared-data hash where platform serialization matches, otherwise stop and diagnose rather than assert equivalence from file size; verify training counts/grouping and numerical tolerance before claiming reproduction. Never replace the frozen constants or overwrite research artifacts. Real-data execution is not authorized by this release-preparation task.

C. The included acquisition helper fetches only the 17 retained training sources. It is useful for authorized inspection but does NOT recreate exclusions computed across the full selected cohort. A training-only refit would be a different analysis, not exact historical reproduction.

## Limits and release claim

Historical parameter provenance is now documented and the original record chain verified. A turnkey public exact refit remains unavailable because the full private cohort/exclusion bootstrap is not bundled. No per-row outcome records, restricted content or original full membership manifest is exported. Direct dependency versions are recorded in requirements-research.txt; a complete historical transitive/platform lock is absent. This provenance-recovery record predates the final completion checks. REPRODUCIBILITY.md now records a successful fresh dependency installation and fabricated fixture run; no scientific rerun occurred. The saved 15/15 historical verification receipt is historical evidence, not 15 tests rerun today. An authorized exact replay remains a conditional procedure, not a public guarantee.
