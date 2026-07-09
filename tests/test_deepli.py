"""Tests for DEEPLI platform."""

import unittest

from deepli import hello, Platform


class TestDeepli(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from DEEPLI")

    def test_platform_status(self):
        p = Platform("Test")
        self.assertEqual(p.status(), "Test is running")


if __name__ == "__main__":
    unittest.main()
