def lang_check1(alphabet):
    if alphabet[0] != 'a':
        return False
    
    i = 1
    while i < len(alphabet) and alphabet[i] in '01':
        i += 1

    if i == len(alphabet) or (i == 1 and i != 'a'):
        return False
    
    i += 1
    if i == len(alphabet):
        return False

    while i < len(alphabet):
        if alphabet[i] not in '01':
            return False
        
        i += 1
        
    return True

def lang_check2(alphabet):
    sigma = ['0', '1', 'a']
    transitions = {
        'q0' : {'0' : 'q3', '1' : 'q3', 'a' : 'q1'},
        'q1' : {'0' : 'q1', '1' : 'q1', 'a' : 'q2'},
        'q2' : {'0' : 'q2', '1' : 'q2', 'a' : 'q3'},
        'q3' : {'0' : 'q3', '1' : 'q3', 'a' : 'q3'}

    }

    initial_state = 'q0'
    final_state = 'q2'

    current_state = initial_state

    for char in alphabet:
        current_state = transitions[current_state][char]

    return True if current_state == final_state else False


print(lang_check1('aa1'))
print(lang_check1('a011a10'))
print(lang_check1('a0110'))
print(lang_check1('10011'))
print(lang_check1('aa'))
print(lang_check1('a0101a'))
print()
print(lang_check2('aa1'))
print(lang_check2('a011a10'))
print(lang_check2('a0110'))
print(lang_check2('10011'))
print(lang_check2('aa'))
print(lang_check2('a0101a'))