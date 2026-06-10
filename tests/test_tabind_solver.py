import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.tabind_solver import can_build_from_rack, find_words, main


class TabindSolverTest(unittest.TestCase):
    def test_can_build_uses_each_letter_once(self):
        self.assertTrue(can_build_from_rack("bandit"))
        self.assertTrue(can_build_from_rack("tabid"))
        self.assertFalse(can_build_from_rack("tabbing"))
        self.assertFalse(can_build_from_rack("banana"))

    def test_find_words_deduplicates_and_sorts(self):
        dictionary = ["tin", "bandit", "tin", "bad", "about", "tabid"]
        self.assertEqual(find_words(dictionary), ["bad", "bandit", "tabid", "tin"])

    def test_find_words_ignores_non_alpha_entries(self):
        dictionary = ["ta", "t-a", "123", "", "ti"]
        self.assertEqual(find_words(dictionary), ["ta", "ti"])

    def test_single_letter_words_are_excluded(self):
        self.assertEqual(find_words(["a", "i", "an"]), ["an"])

    def test_main_uses_bundled_dictionary_by_default(self):
        output = StringIO()
        with redirect_stdout(output):
            status_code = main([])

        self.assertEqual(status_code, 0)
        words = output.getvalue().splitlines()
        self.assertEqual(len(words), 51)
        self.assertEqual(words[0], "ab")
        self.assertEqual(words[-1], "tin")


if __name__ == "__main__":
    unittest.main()
