import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.compare_coverage import compare


class CoverageTests(unittest.TestCase):
    def test_distinguishes_filtered_and_absent(self):
        result = compare(["study-A", "study-B", "study-C"], ["study-A"], ["study-A", "study-B"])
        self.assertEqual(result["present_but_not_retrieved"], ["study-B"])
        self.assertEqual(result["absent_from_inventory"], ["study-C"])
        self.assertAlmostEqual(result["query_coverage"], 1 / 3)

    def test_missing_inventory_is_unknown(self):
        result = compare(["study-A"], [])
        self.assertIsNone(result["absent_from_inventory"])
        self.assertIsNone(result["present_but_not_retrieved"])

    def test_duplicate_rows_do_not_inflate_count(self):
        self.assertEqual(compare(["A", "A"], ["A", "A"])["target_count"], 1)

    def test_inconsistent_inventory_rejected(self):
        with self.assertRaises(ValueError):
            compare(["A"], ["A"], [])

    def test_empty_target_rejected(self):
        with self.assertRaises(ValueError):
            compare([], [])

    def test_cli_files_and_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            target, retrieved = Path(tmp) / "target.txt", Path(tmp) / "retrieved.txt"
            target.write_text("\ufeffA\nA\nB\n\n", encoding="utf-8")
            retrieved.write_text("A\n", encoding="utf-8")
            proc = subprocess.run([sys.executable, "scripts/compare_coverage.py", "--target", str(target), "--retrieved", str(retrieved)], capture_output=True, text=True, check=True)
            result = json.loads(proc.stdout)
            self.assertEqual(result["query_coverage"], 0.5)
            self.assertEqual(len(result["input_sha256"]["target"]), 64)


if __name__ == "__main__":
    unittest.main()
