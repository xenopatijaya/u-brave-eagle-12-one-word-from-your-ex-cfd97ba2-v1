"""One-word entry for make.fun's "One Word From Your Ex" bounty.

The program writes exactly one word to /output/entry.txt: "rebound".

The word: the word your ex would use to describe you. "Rebound" is the
whole relationship demoted to a recovery phase in a single word — you were
never the destination, only the healing after the real one. It stings
because it is true rather than merely insulting: it does not call you
cruel or worthless, it says you were temporary by design, the person
someone dated to get over someone else. Everybody has been a rebound or
known one, so it lands instantly with no explanation, and no near
synonym keeps its edge — "placeholder" is colder, "fling" is lighter
and does not sting the same way. Seven letters, one word, no setup.
"""

import os
from pathlib import Path

WORD = "rebound"


def main() -> None:
    if not 1 <= len(WORD) <= 24:
        raise SystemExit(f"word is {len(WORD)} chars, must be 1-24")
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if not WORD.isalpha():
        raise SystemExit("entry must be a single plain word, letters only")
    if WORD != WORD.strip():
        raise SystemExit("word must not start or end with whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")
    print(WORD)


if __name__ == "__main__":
    main()
