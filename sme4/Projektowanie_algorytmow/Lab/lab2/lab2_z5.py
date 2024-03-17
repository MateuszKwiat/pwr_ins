import numpy as np
import ast

def FSM(alphabet):
    sigma = None
    transitions = None
    initial_state = None
    final_state = None

    with open('fsm_settings.txt') as f:
        lines = f.readlines()
        sigma = ast.literal_eval(lines[0])
        transitions = ast.literal_eval(lines[1])
        initial_state = ast.literal_eval(lines[2])
        final_state = ast.literal_eval(lines[3])

    current_state = initial_state[0]

    print(f'input: {alphabet}')
    print(f'Initial state: {initial_state}')
    print(f'Current state: {current_state}')

    for char in alphabet:
        current_state = transitions[current_state][char]
        print(f'char: {char}, new state: {current_state}')

    with open('fsm_output_settings.txt', 'w') as f:
        f.write(str(sigma) + '\n')
        f.write(str(transitions) + '\n')
        f.write(str(initial_state) + '\n')
        f.write(str(final_state) + '\n')

    return True if current_state in final_state else False


print(FSM('bcddd'))
print()
print(FSM('aaacbddd'))
print()
print(FSM('aabcddd'))
print()
print(FSM('aabccddd'))