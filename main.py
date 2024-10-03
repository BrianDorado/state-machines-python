
from state_machines import regular_expressions


def test_evenab():
    print("Testing evenab function:")
    test_cases = [
        ("abba", "accepted"),
        ("abb", "rejected"),
        ("abbaabbaba", "accepted"),
        ("abbaabba", "accepted"),
        ("abbaa", "rejected")
    ]

    for s, expected in test_cases:
        result = regular_expressions.even_ab(s)
        print(f"Input: {s}, Expected: {expected}, Got: {result}")
    print("-" * 40)


def test_ends_with_b():
    print("Testing ends_with_b function:")
    test_cases = [
        ("aabab", "accepted"),
        ("aaba", "rejected")
    ]

    for s, expected in test_cases:
        result = regular_expressions.ends_with_b(s)
        print(f"Input: {s}, Expected: {expected}, Got: {result}")
    print("-" * 40)


def test_contains_aba():
    print("Testing contains_aba function:")
    test_cases = [
        ("ababa", "accepted"),
        ("aabb", "rejected"),
        ("aabba", "rejected"),
        ("ababba", "accepted"),
        ("aabbbabbaba", "accepted"),
        ("abaaabbbabb", "accepted")
    ]

    for s, expected in test_cases:
        result = regular_expressions.contains_aba(s)
        print(f"Input: {s}, Expected: {expected}, Got: {result}")
    print("-" * 40)


if __name__ == "__main__":
    test_evenab()
    test_ends_with_b()
    test_contains_aba()

