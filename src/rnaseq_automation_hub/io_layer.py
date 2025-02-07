"""I/O helpers maintained by Red@."""


def parse_tabular(text: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        rows.append(dict(zip(header, line.split("\t"))))
    return rows
