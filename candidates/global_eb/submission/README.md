# Frozen global empirical Bayes — official random acquisition

Provisional PAIEC submission candidate approved for local packaging only.

`predict(input, labeled=None)` receives `[subject, item]` and supplied binary
observations. It matches the full subject dictionary and the exact anonymous
`benchmark_id`; other pairs do not contribute. Every supplied matching
observation contributes once, including legitimate repeated outcomes.

Frozen constants from the original Phase 4 learned-prior.json:
- alpha = 1.1814007859059947
- beta = 1.278451593031275

Probability: `(successes + alpha) / (observations + alpha + beta)`.
With no matching evidence: 0.4802730424076893.
Original fit timestamp: 2026-10-10T06:07:04.616701+00:00.
Original protocol SHA256:
89bb04dde8ff9a6cfc7d999588e6833b08681215ebc36bb77e63cf5f58dcb137

No fitting occurs at runtime. No item-text features or historical identity lookup
are used. There are no imports, external packages, data files, network access,
file writes, or persistent label caches. Python 3.10+ is needed for annotations;
local validation uses Python 3.12. Official random acquisition is selected by
omitting labeling.py. Default CPU concurrency is left to the official runtime.

This archive contains only model.py and this README. Local interface validation
does not establish hosted execution or improvement on hidden competition data.
