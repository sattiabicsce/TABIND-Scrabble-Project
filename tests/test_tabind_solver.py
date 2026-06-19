import unittest
from contextlib import redirect_stdout
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

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

    def test_main_reads_full_dictionary_path(self):
        with TemporaryDirectory() as tmp_dir:
            dictionary_path = Path(tmp_dir) / "scrabble_dictionary.txt"
            dictionary_path.write_text(
                "\n".join(["tin", "bandit", "tabid", "about", "banana"]),
                encoding="utf-8",
            )

            output = StringIO()
            with redirect_stdout(output):
                status_code = main([str(dictionary_path)])

        self.assertEqual(status_code, 0)
        self.assertEqual(output.getvalue().splitlines(), ["bandit", "tabid", "tin"])

    def test_main_uses_bundled_full_dictionary_by_default(self):
        output = StringIO()
        with redirect_stdout(output):
            status_code = main([])

        words = output.getvalue().splitlines()
        self.assertEqual(status_code, 0)
        self.assertEqual(len(words), 65)
        self.assertEqual(words[0], "ab")
        self.assertEqual(words[-1], "tind")

    def test_main_reports_missing_dictionary(self):
        output = StringIO()
        error_output = StringIO()
        with self.assertRaises(SystemExit) as raised, redirect_stdout(output), redirect_stderr(error_output):
            main(["missing_scrabble_dictionary.txt"])

        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
