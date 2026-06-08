"""Find Scrabble words that can be made from the rack "tabind".

The solver intentionally separates two responsibilities:

1. The dictionary file decides which words are Scrabble-valid.
2. This program decides which dictionary words can be built from the rack.

Expected dictionary format: one word per line.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Iterable


DEFAULT_RACK = "tabind"
MIN_WORD_LENGTH = 2


def normalize_word(raw_word: str) -> str:
    """Return a lowercase alphabetic word, or an empty string if invalid."""
    word = raw_word.strip().lower()
    return word if word.isalpha() else ""


def can_build_from_rack(word: str, rack: str = DEFAULT_RACK) -> bool:
    """Return True when every letter in word is available in rack."""
    clean_word = normalize_word(word)
    clean_rack = normalize_word(rack)

    if not clean_word or not clean_rack:
        return False
    if len(clean_word) < MIN_WORD_LENGTH or len(clean_word) > len(clean_rack):
        return False

    word_counts = Counter(clean_word)
    rack_counts = Counter(clean_rack)
    return all(count <= rack_counts[letter] for letter, count in word_counts.items())


def find_words(dictionary_words: Iterable[str], rack: str = DEFAULT_RACK) -> list[str]:
    """Filter dictionary_words to an alphabetized, deduplicated result list."""
    matches = {
        word
        for raw_word in dictionary_words
        if (word := normalize_word(raw_word)) and can_build_from_rack(word, rack)
    }
    return sorted(matches)


def read_dictionary(path: Path) -> list[str]:
    """Load dictionary entries from a UTF-8 text file."""
    return path.read_text(encoding="utf-8").splitlines()


def write_output(words: Iterable[str], output_path: Path | None) -> None:
    """Write words to a file when requested, otherwise print to stdout."""
    text = "\n".join(words)
    if text:
        text += "\n"

    if output_path:
        output_path.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find alphabetized Scrabble words that can be made from a rack."
    )
    parser.add_argument(
        "dictionary",
        type=Path,
        help="Text dictionary file with one Scrabble word per line.",
    )
    parser.add_argument(
        "--letters",
        default=DEFAULT_RACK,
        help=f"Rack letters to use once each. Default: {DEFAULT_RACK}",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional file path for the alphabetized result.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    dictionary_words = read_dictionary(args.dictionary)
    words = find_words(dictionary_words, args.letters)
    write_output(words, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
