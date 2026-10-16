"""Package the frozen global EB predictor without a data payload or API credentials."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def build_zip(output: Path | None = None) -> Path:
    root = Path(__file__).resolve().parents[1]
    output = output or root / "global_eb_frozen.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    # An explicit allowlist keeps local files and credentials out of the ZIP.
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        for name in ("model.py", "README.md"):
            entry = ZipInfo(name)
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (root / "submission" / name).read_bytes())
    return output


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    path = build_zip(args.output)
    print(f"Wrote {path} ({path.stat().st_size:,} bytes)")
