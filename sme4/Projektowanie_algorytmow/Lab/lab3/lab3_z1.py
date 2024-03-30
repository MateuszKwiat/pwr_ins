import numpy as np

def TM(alphabet):
    simga = ['a', '_', 'a.', 'a/']
    transitions = {
        'q0' : {'a' : ['q1', 'a.', 1], '_' : ['qr', '_', -1]},
        'q1' : {'a/' : ['q1', 'a/', 1], '_' : ['qa', '_', -1], 'a' : ['q2', 'a', -1]},
        'q2' : {'a/' : ['q2', 'a/', -1], 'a.' : ['q3', 'a.', -1]},
        'q3' : {'a/' : ['q3', 'a/', 1], 'a' : ['q4', 'a', 1], 'a.' : ['q4', 'a.', 1], '_' : ['q6', '_', -1]},
        'q4' : {'_' : ['qr', '_', -1], 'a/' : ['q4', 'a/', 1], 'a' : ['q5', 'a/', 1]},
        'q5' : {'a/' : ['q5', 'a/', 1], '_' : ['qr', '_', -1], 'a' : ['q3', 'a/', 1]},
        'q6' : {'a' : ['q6', 'a', -1], 'a/' : ['q6', 'a/', -1], 'a.' : ['q1', 'a.', 1]}
    }

    initial_state = 'q0'
    current_state = initial_state
    head = 0

    print(f'input: {alphabet}')
    print(f'Initial state: {initial_state}')
    print(f'Current state: {current_state}\n')

    while current_state != 'qr' and current_state != 'qa':
        operations = transitions[current_state][alphabet[head]]
        current_state = operations[0]
        alphabet[head] = operations[1]
        head += operations[2]

        if head < 0:
            head = 0
        
        if head >= len(alphabet):
            alphabet.append('_')

        print(f'alphabet: {alphabet}\ncurrent char: {alphabet[head]}\ncurrent state: {current_state}\n')

    return True if current_state == 'qa' else False


print(TM(['a', 'a', 'a', '_']))
alphabet = [*input()]
print(TM(alphabet))

