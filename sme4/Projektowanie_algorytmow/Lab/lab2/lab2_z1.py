import numpy as np

def FSM(alphabet):
    sigma = ['0', '1']
    transitions = {
        'q0' : {'0' : 'q1', '1' : 'q0'},
        'q1' : {'0' : 'q3', '1' : 'q2'},
        'q2' : {'0' : 'q2', '1' : 'q0'},
        'q3' : {'0' : 'q2', '1' : 'q2'}
    }

    initial_state = 'q0'
    final_state = 'q3'

    current_state = initial_state

    print(f'input: {alphabet}')
    print(f'Initial state: {initial_state}')
    print(f'Current state: {current_state}')

    for char in alphabet:
        current_state = transitions[current_state][char]
        print(f'char: {char}, new state: {current_state}')

    return True if current_state == final_state else False


print(FSM('101100'))
print()
print(FSM(''.join([str(np.random.randint(0, 2)) for i in range(10)])))
print()
print(FSM(''.join([str(np.random.randint(0, 2)) for i in range(10)])))
print()
print(FSM(''.join([str(np.random.randint(0, 2)) for i in range(10)])))
print()
