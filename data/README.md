# Scrabble Dictionary Input

This folder includes a full Scrabble dictionary text file as:

```text
data/scrabble_dictionary.txt
```

The solver reads that full dictionary, then keeps only the words that can be built from `tabind` while using each character no more than once.

The bundled file comes from Richard Ressler's Scrabble Word List dataset, described as authorized words for use in Scrabble:

- https://rressler.quarto.pub/i_data_sets/data_word_lists.html
- https://raw.githubusercontent.com/rressler/data_raw_courses/main/scrabble_words.txt

You can also run the solver with any other full Scrabble dictionary file you are allowed to use:

```bash
python src/tabind_solver.py data/scrabble_dictionary.txt
```

The existing `sample_scrabble_dictionary.txt` file is only a small test/demo fixture. It is not the default dictionary source for the assignment.
