import numpy as np

def FSM(alphabet):
    sigma = ['a', 'b', 'c', 'd']
    transitions = {
        'q0' : {'a' : 'q0', 'b' : 'q1', 'c' : 'q3', 'd' : 'q3'},
        'q1' : {'a' : 'q3', 'b' : 'q3', 'c' : 'q2', 'd' : 'q3'},
        'q2' : {'a' : 'q3', 'b' : 'q3', 'c' : 'q3', 'd' : 'q2'},
        'q3' : {'a' : 'q3', 'b' : 'q3', 'c' : 'q3', 'd' : 'q3'},
    }

    initial_state = 'q0'
    final_state = 'q2'

    current_state = initial_state

    print(f'input: {alphabet}')
    print(f'Initial state: {initial_state}')
    print(f'Current state: {current_state}')

    for char in alphabet:
        current_state = transitions[current_state][char]
        print(f'char: {char}, new state: {current_state}')

    return True if current_state == final_state else False


print(FSM('bcddd'))
print()
print(FSM('aaacbddd'))
print()
print(FSM('aabcddd'))
print()
print(FSM('aabccddd'))