# PAIEC frozen empirical Bayes predictor

A small, CPU-only PAIEC predictor for sparse binary outcomes. For the exact target subject and anonymous benchmark, it uses acquired successes s and observation count n to return `(s + 1.1814007859059947) / (n + 1.1814007859059947 + 1.278451593031275)`. With no matching observations it returns 0.4802730424076893. No model fitting, network access, language model or GPU is needed at inference. Omitting labeling.py preserves the organizer's random acquisition.

This repository contains the frozen predictor, its source code, validation tools and reproduction documentation for the accompanying Manuscript V4.3.

## Start here

- [REPRODUCIBILITY.md](REPRODUCIBILITY.md): environment setup, synthetic validation, authorized acquisition and conditional historical reproduction.
- [TRAINING_SOURCE_CITATION_REGISTER.md](TRAINING_SOURCE_CITATION_REGISTER.md) and [BibTeX](TRAINING_SOURCE_CITATIONS.bib): the exact 17 retained fitting identifiers and 21 distinct cited works, including result-export credits.
- [HISTORICAL_TRAINING_PROVENANCE.md](HISTORICAL_TRAINING_PROVENANCE.md): original frozen estimation and full-cohort exclusions. Exact public raw-to-fit replay is access-limited.
- [LICENSE_SCOPE.md](LICENSE_SCOPE.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [CITATION.md](CITATION.md): separate original-code and Stanford MIT grants, data-citation scope and attribution.
- [AI_ASSISTANCE_DISCLOSURE.md](AI_ASSISTANCE_DISCLOSURE.md): human/AI role boundaries.

## Files

`candidates/global_eb/` and `candidates/beta11/` contain the unchanged predictor, packaging and synthetic-test sources. `research/phase4/scripts/` contains the existing preparation, fitting and statistical code; read the restricted-input limitations before executing it. `tools/` contains the verified local validator, synthetic-fixture and explicit acquisition wrappers. `third_party/` contains only previously cleared Stanford baseline source/notices. `provenance/` contains source pins, frozen parameters and sanitized training hash receipts, not raw responses. `results/` contains two previously approved historical aggregate summaries, not a new leaderboard or protected final results.

`artifacts/global_eb_frozen.zip` is the unchanged frozen submission. SHA-256: ec8906e3eeda8c1044899745ccaec9c948491ded74f021c7d83f1c62e396d3ef. Preserve artifacts/LICENSE, artifacts/PROJECT_CODE_LICENSE.txt and artifacts/NOTICE.md with its distribution. The Beta fallback source is included; the original Beta ZIP is preserved separately with SHA-256 5450763794414ea95a0b457cbfdb4e9e3dcaa58a2a05bf9784dbb54548371f6d. Both competition ZIPs retain their validated bytes.

Original project code is MIT licensed by its sole human contributor; inherited Stanford code retains its own MIT notice and citation. This does not license raw benchmark data. This repository contains no gated datasets, protected item records, individual outcomes, private forecasts or credentials. The full protected evaluation is not publicly reproducible from this repository.
