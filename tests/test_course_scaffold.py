"""Sanity checks for the learning repository structure.

Run with: python -m unittest discover -s tests
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CourseScaffoldTests(unittest.TestCase):
    def test_core_course_files_exist(self):
        for relative in (
            "README.md",
            "ROADMAP.md",
            "PROGRESS.md",
            "CONTRIBUTING.md",
            "pyproject.toml",
            "templates/CHAPTER_TEMPLATE.md",
            "templates/PROJECT_TEMPLATE.md",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_all_phases_exist(self):
        for number in range(12):
            phase_dirs = list((ROOT / "phases").glob(f"phase-{number:02d}-*"))
            with self.subTest(phase=number):
                self.assertEqual(len(phase_dirs), 1, f"Expected one directory for phase {number:02d}")
                self.assertTrue((phase_dirs[0] / "README.md").is_file())

    def test_portfolio_and_learning_areas_exist(self):
        for relative in (
            "projects/README.md",
            "assessments/README.md",
            "interview-preparation/README.md",
            "resources/README.md",
            "docs/README.md",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
