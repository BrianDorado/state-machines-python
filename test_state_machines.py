import unittest
from state_machines import regular_expressions

class TestStateMachines(unittest.TestCase):

    def test_evenab(self):
        """Test cases for the evenab function."""
        test_cases = [
            ("abba", "accepted"),
            ("abb", "rejected"),
            ("abbaabbaba", "accepted"),
            ("abbaabba", "accepted"),
            ("abbaa", "rejected")
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(regular_expressions.even_ab(s), expected)

    def test_ends_with_b(self):
        """Test cases for the ends_with_b function."""
        test_cases = [
            ("aabab", "accepted"),
            ("aaba", "rejected")
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(regular_expressions.ends_with_b(s), expected)

    def test_contains_aba(self):
        """Test cases for the contains_aba function."""
        test_cases = [
            ("ababa", "accepted"),
            ("aabb", "rejected"),
            ("aabba", "rejected"),
            ("ababba", "accepted"),
            ("aabbbabbaba", "accepted"),
            ("abaaabbbabb", "accepted")
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(regular_expressions.contains_aba(s), expected)

if __name__ == '__main__':
    unittest.main()
