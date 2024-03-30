def word_check(alphabet, word):
    left_iter = 0
    right_iter = len(word) - 1

    if word == 'x':
        return True
    
    if word.count('x') != 1:
        return False

    while left_iter != right_iter:
        if word[left_iter] not in alphabet or word[right_iter] not in alphabet:
            return False
        left_iter += 1
        right_iter -= 1

    return True
    
alphabet = 'egwarh'
word = ['x', 'hgxwer', 'hegxwer', 'hegxwxrer']

print(f'alphabet: {alphabet}, word: {word[0]}, output: {word_check(alphabet, word[0])}')
print(f'alphabet: {alphabet}, word: {word[1]}, output: {word_check(alphabet, word[1])}')
print(f'alphabet: {alphabet}, word: {word[2]}, output: {word_check(alphabet, word[2])}')
print(f'alphabet: {alphabet}, word: {word[3]}, output: {word_check(alphabet, word[3])}')

alphabet = input()
word = input()

print(f'alphabet: {alphabet}, word: {word}, output: {word_check(alphabet, word)}')