def evaluate_password_strength(password):
    with open('dictionary.txt') as f:
        dictionary = set(line.strip() for line in f)

    if password in dictionary:
        print(f'The strength of [{password}] is weak.')

    elif any(word in password for word in dictionary):
        print(f'The strength of password [{password}] is moderate.')
    
    else:
        print(f'The strength of password [{password}] is strong.')


evaluate_password_strength('abbreviate')
evaluate_password_strength('1abbreviate#2@')
evaluate_password_strength('1Ace#2@')

