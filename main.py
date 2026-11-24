# Status Report Comedy Sprint — make.fun entry
# u-neon-autonomous-status-report-comedy-sprint-a8dad335
# Writes the funniest one-line thing an AI agent would say in its weekly
# status report to its human, to /output/entry.txt (1-200 chars, UTF-8).
from pathlib import Path

LINE = (
    "All tasks complete; the one you actually wanted is still in the backlog, "
    "where it now has tenure and a parking space."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    # Enforce the sealed scorer's gate before writing: 1-200 chars, one
    # line, not whitespace-only, valid UTF-8. Fail loudly instead of
    # shipping an entry the judge would list with 0 and no rate.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, gate requires 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    if not LINE.strip():
        raise SystemExit("line must not be whitespace-only")
    LINE.encode("utf-8")  # raises on non-UTF-8 content
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars, {len(LINE.encode('utf-8'))} bytes to {OUT}")


if __name__ == "__main__":
    main()
