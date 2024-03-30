import numpy as np

def TM(alphabet):
    simga = ['0', '1', 'b', '_', '0/', '1/']
    transitions = {
        'q0' : {'b' : ['q1', 'b', 1], '0' : ['q2', '0/', 1], '1' : ['q3', '1/', 1]},
        'q1' : {'0/' : ['q1', '0/', 1], '1/' : ['q1', '1/', 1], '_' : ['qa', '_', -1], '0' : ['qr', '0', -1], '1' : ['qr', '1', -1]},
        'q2' : {'_' : ['qr', '_', 1], '0' : ['q2', '0', 1], '1' : ['q2', '1', 1], 'b' : ['q4', 'b', 1]},
        'q3' : {'b' : ['q5', 'b', 1], '0' : ['q3', '0', 1], '1' : ['q3', '1', 1], '_' : ['qr', '_', 1]},
        'q4' : {'0/' : ['q4', '0/', 1], '1/' : ['q4', '1/', 1], '_' : ['qr', '_', 1], '1' : ['qr', '1', 1], '0' : ['q6', '0/', -1]},
        'q5' : {'1' : ['q6', '1/', -1], '_' : ['qr', '_', 1], '0' : ['qr', '0', 1], '0/' : ['q5', '0/', 1], '1/' : ['q5', '1/', 1]},
        'q6' : {'0/' : ['q6', '0/', -1], '1/' : ['q6', '1/', -1], 'b' : ['q7', 'b', -1]},
        'q7' : {'0' : ['q7', '0', -1], '1' : ['q7', '1', -1], '0/' : ['q0', '0/', 1], '1/' : ['q0', '1/', 1]}
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

        print(f'alphabet: {alphabet}\ncurrent char: {alphabet[head]}\ncurrent state: {current_state}\n')

    return True if current_state == 'qa' else False


print(TM(['a', 'a', 'a', '_']))

