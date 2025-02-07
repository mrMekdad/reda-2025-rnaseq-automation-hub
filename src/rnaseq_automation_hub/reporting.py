"""Reporting helpers maintained by Red@."""


def to_markdown(rows: list[dict[str, str]]) -> str:
    return "\n".join(["# Red@ Report", "", f"- Rows: {len(rows)}"])
