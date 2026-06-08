import unittest

from src.tabind_solver import can_build_from_rack, find_words


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


if __name__ == "__main__":
    unittest.main()
