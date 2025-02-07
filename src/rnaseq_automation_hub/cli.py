import argparse
from rnaseq_automation_hub.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Automation hub for RNAseq task templates, checks, and release notes.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
