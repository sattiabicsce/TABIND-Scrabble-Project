# Scrabble Dictionary Input

This folder includes a full Scrabble dictionary text file as:

```text
data/scrabble_dictionary.txt
```

The solver reads that full dictionary, then keeps only the words that can be built from `tabind` while using each character no more than once.

The bundled file is derived from the North American Word List 2023 file in the `scrabblewords/scrabblewords` repository. The source file includes definitions; this project keeps only the first token on each line as the playable dictionary word.

- https://scrabbleplayers.org/w/NWL2023
- https://github.com/scrabblewords/scrabblewords/tree/main/words/North-American
- https://raw.githubusercontent.com/scrabblewords/scrabblewords/main/words/North-American/NWL2023.txt

You can also run the solver with any other full Scrabble dictionary file you are allowed to use:

```bash
python src/tabind_solver.py data/scrabble_dictionary.txt
```

The existing `sample_scrabble_dictionary.txt` file is only a small test/demo fixture. It is not the default dictionary source for the assignment.
