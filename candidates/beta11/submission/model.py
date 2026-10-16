"""Fixed Beta(1,1) posterior mean for each visible subject–benchmark pair.

Standard library only; no fitted parameters, cached labels or external access.
The platform's default random acquisition is selected by omitting labeling.py.
"""


def predict(input: list[dict], labeled: list | None = None) -> float:
    """Return (successes + 1) / (observations + 2), or 0.5 without evidence."""
    subject, item = input
    if not labeled:
        return 0.5

    benchmark = item.get("benchmark_id")
    if not isinstance(benchmark, str) or not benchmark:
        raise ValueError("The Beta predictor requires an anonymous item benchmark_id.")

    successes = 0
    count = 0
    for (observed_subject, observed_item), label in labeled:
        if observed_subject != subject:
            continue
        observed_benchmark = observed_item.get("benchmark_id")
        if not isinstance(observed_benchmark, str) or not observed_benchmark:
            raise ValueError("Acquired items must include an anonymous benchmark_id.")
        if observed_benchmark != benchmark:
            continue
        if label not in (0, 1):
            raise ValueError("Acquired responses must be binary (0 or 1).")
        successes += int(label)
        count += 1
    return float((successes + 1) / (count + 2))
