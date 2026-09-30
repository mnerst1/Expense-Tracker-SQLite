import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import database
import main


class ExpenseValidationTests(unittest.TestCase):
    def test_amount_reprompts_for_nonfinite_and_nonpositive_values(self):
        with patch("builtins.input", side_effect=["nan", "inf", "-inf", "0", "-5", "abc", "12,50"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main.input_amount(), 12.5)

    def test_date_is_canonical_for_sorting(self):
        with patch("builtins.input", return_value="2026-9-5"):
            self.assertEqual(main.input_date(), "2026-09-05")

    def test_invalid_date_reprompts(self):
        with patch("builtins.input", side_effect=["2026-02-30", "2026-02-28"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main.input_date(), "2026-02-28")

    def test_database_rejects_invalid_amounts_without_changing_totals(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(database, "DATABASE_NAME", str(Path(folder) / "test.db")):
            database.create_database()
            database.add_expense("Lunch", "Food", 12.5, "2026-09-30")
            for amount in [float("nan"), float("inf"), float("-inf"), 0, -1]:
                with self.subTest(amount=amount), self.assertRaises(ValueError):
                    database.add_expense("Invalid", "Food", amount, "2026-09-30")
            self.assertEqual(len(database.get_all_expenses()), 1)
            self.assertEqual(database.get_total_amount(), 12.5)


if __name__ == "__main__":
    unittest.main()
