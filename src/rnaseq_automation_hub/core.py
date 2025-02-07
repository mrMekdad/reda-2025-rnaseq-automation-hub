"""Core workflow for RNAseq Automation Hub by Red@."""

PROJECT_NAME = "RNAseq Automation Hub"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
