def even_ab(s):
    """
    Checks if the input string 's' has an even number of 'a' and 'b' characters.

    Args:
        s (str): Input string consisting of characters 'a' and 'b' only.

    Returns:
        str: 'accepted' if the string has an even number of 'a' and 'b' characters,
             otherwise 'rejected'.
    """
    state = 'E'
    for c in s:
        assert c in 'ab'
        state = 'O' if state == 'E' else 'E'
    return 'accepted' if state == 'E' else 'rejected'


def ends_with_b(s):
    """
    Determines if the input string 's' ends with the character 'b' using a state machine.

    Args:
        s (str): Input string consisting of characters 'a' and 'b' only.

    Returns:
        str: 'accepted' if the string ends with 'b', otherwise 'rejected'.
    """
    transitions = {
        ('q0','a'):'q0',
        ('q0','b'):'q1',
        ('q1','a'):'q0',
        ('q1','b'):'q1'
    }
    state = 'q0'
    for c in s:
        state = transitions[(state, c)]
        print(f'Reached state: {state} on char: {c}')
    return 'accepted' if state == 'q1' else 'rejected'


def contains_aba(s):
    """
    Checks if the input string 's' contains the substring 'aba' using a state machine.

    Args:
        s (str): Input string consisting of characters 'a' and 'b' only.

    Returns:
        str: 'accepted' if the string contains 'aba', otherwise 'rejected'.
    """
    transitions = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q0',
        ('q3', 'a'): 'q3',  # Once accepted, stay in q3
        ('q3', 'b'): 'q3',
    }

    state = 'q0'
    for c in s:
        state = transitions[(state, c)]
        print(f'state: {state}, current char: {c}')
        if state == 'q3':
            return 'accepted'

    return 'rejected'
