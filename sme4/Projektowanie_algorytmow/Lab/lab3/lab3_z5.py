import numpy as np















def TM(alphabet):
    sigma = ['[', ',', ']', '0123456789', '_']
    transitions = {
        'q0' : {'[' : ['q1', 1], ',' : ['qr', -1], ']' : ['qr', -1], 'n' : ['qr', -1], '_' : ['qr', -1]},
        'q1' : {']' : ['qa', -1], 'n' : ['q2', 1], '[' : ['qr', -1], ',' : ['qr', -1], '_' : ['qr', -1]},
        'q2' : {']' : ['qa', -1], ',' : ['q3', 1], 'n' : ['q2', 1], '[' : ['qr', -1], '_' : ['qr', -1]},
        'q3' : {'n' : ['q2', 1], '[' : ['qr', -1], ',' : ['qr', -1], ']' : ['qr', -1], '_' : ['qr', -1]}
    }

    initial_state = 'q0'
    current_state = initial_state
    head = 0

    print(f'input: {alphabet}')
    print(f'Initial state: {initial_state}')
    print(f'Current state: {current_state}\n')

    while current_state != 'qr' and current_state != 'qa':
        if alphabet[head] in sigma[3]:
            operations = transitions[current_state]['n']
            
        else:
            operations = transitions[current_state][alphabet[head]]

        current_state = operations[0]
        head += operations[1]

        if head < 0:
            head = 0
        
        if head >= len(alphabet):
            alphabet += '_'

        print(f'alphabet: {alphabet}\ncurrent char: {alphabet[head]}\ncurrent state: {current_state}\n')

    return True if current_state == 'qa' else False

print(TM('[1,2,3,4,56,7]'))
alphabet = input()
print(TM(alphabet))