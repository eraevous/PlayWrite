"""Smoke test: the package imports and declares a version.

There are no features to test yet. This test exists so CI has something real to
run, and so the first feature PR adds tests beside an already-working harness.
"""

import unittest

import prospero


class PackageTest(unittest.TestCase):
    def test_version_is_a_dotted_string(self):
        # A version string such as "0.0.0": three dot-separated integers.
        parts = prospero.__version__.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(part.isdigit() for part in parts))


if __name__ == "__main__":
    unittest.main()
