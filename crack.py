import hashlib
import itertools
import time


with open("dictionary.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]


def generate_type_2_passwords(word):

    chars = ["@", "#", "$", "%", "&"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    passwords = set()

    # 1 place
    for char in chars:
        passwords.add(char)
    for num in nums:
        passwords.add(num)
    
    # 2 places
    for combo in itertools.product(nums + chars, repeat=2):
            passwords.add(''.join(combo))
    
    # 3 places
    comboNums = list(itertools.product(nums, repeat=2))
    comboChars = list(itertools.product(chars, repeat=2))
    
    for i in comboNums:
        passwords.add("".join(i))

    for j in comboChars:
        passwords.add("".join(j))

    for n1,n2 in comboNums:
        for char in chars:
            passwords.add(n1 + char + n2)

    for c1,c2 in comboChars:
        for num in nums:
            passwords.add(c1 + num + c2)
    
    # 4 places, reset
    comboNums = list(itertools.product(nums, repeat=2))
    comboChars = list(itertools.product(chars, repeat=2))
    
    for n1,n2 in comboNums:
        for c1,c2 in comboChars:
            passwords.add(n1 + n2 + c1 + c2)
            passwords.add(n1 + n2 + c2 + c1)
            passwords.add(n1 + c1 + n2 + c2)
            passwords.add(n1 + c1 + c2 + n2)
            passwords.add(n1 + c2 + n2 + c1)
            passwords.add(n1 + c2 + c1 + n2)

            passwords.add(n2 + n1 + c1 + c2)
            passwords.add(n2 + n1 + c2 + c1)
            passwords.add(n2 + c1 + n1 + c2)
            passwords.add(n2 + c1 + c2 + n1)
            passwords.add(n2 + c2 + n1 + c1)
            passwords.add(n2 + c2 + c1 + n1)

            passwords.add(c1 + n1 + n2 + c2)
            passwords.add(c1 + n1 + c2 + n2)
            passwords.add(c1 + n2 + n1 + c2)
            passwords.add(c1 + n2 + c2 + n1)
            passwords.add(c1 + c2 + n1 + n2)
            passwords.add(c1 + c2 + n2 + n1)

            passwords.add(c2 + n1 + n2 + c1)
            passwords.add(c2 + n1 + c1 + n2)
            passwords.add(c2 + n2 + n1 + c1)
            passwords.add(c2 + n2 + c1 + n1)
            passwords.add(c2 + c1 + n1 + n2)
            passwords.add(c2 + c1 + n2 + n1)
    
    result_list = []
    for password in passwords:
        for i in range(len(password) + 1):
            result = password[:i] + word + password[i:]
            result_list.append(result)
        
    return result_list


def crack_password(username, password_hash):
    start_time = time.time()

    found = False
    for word in words:
        word_hash = hashlib.md5(word.encode()).hexdigest()
        if word_hash == password_hash:
            found_time = time.time()
            found = True
            print(f"Password for {username}: {word}")
            print(f"Time taken: {found_time - start_time:.4f} seconds")
            return

    if not found:
         for word in words:
            type_2_passwords = generate_type_2_passwords(word)
            for type_2_password in type_2_passwords:
                type_2_password_hash = hashlib.md5(type_2_password.encode()).hexdigest()
                if type_2_password_hash == password_hash:
                    found = True
                    found_time = time.time()
                    print(f"Password for {username}: {type_2_password}")
                    print(f"Time taken: {found_time - start_time:.4f} seconds")
                    return
                
        
    unfound_time = time.time()
    print(f"Password for {username} not found.")
    print(f"Time taken 2: {unfound_time - start_time:.4f} seconds")


crack_password("Rick", "db267675397b8e9e86a74940caaa2658")
crack_password("Howard", "55824ad4959e2d9b965227bbc833c960")
crack_password("Joe", "5d17ae15a6be2d7405e4f4d5b70de212")


