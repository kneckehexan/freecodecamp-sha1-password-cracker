from hashlib import sha1

def hashPass(arr):
    newArr = []
    for a in arr:
        newArr.append(sha1(a.encode()).hexdigest())
    return newArr

def getPwd(pwdList, hashList, hash):
    try:
        index = hashList.index(hash)
        return pwdList[index]
    except ValueError:
        return "PASSWORD NOT IN DATABASE"

def crack_sha1_hash(hash, use_salts=False):

    # Load the text files
    with open("top-10000-passwords.txt", encoding='utf-8') as f:
        passwords = f.read().splitlines()

    with open("known-salts.txt", encoding='utf-8') as f:
        salts = f.read().splitlines()

    if use_salts:
        passWithSalt = []
        newPasswords = []
        for s in salts:
            for p in passwords:
                passWithSalt.append(f'{p}{s}')
                passWithSalt.append(f'{s}{p}')
                newPasswords.append(p)
                newPasswords.append(p)

        hashedPass = hashPass(passWithSalt)
        return getPwd(newPasswords, hashedPass, hash)
    else:
        hashedPass = hashPass(passwords)
        return getPwd(passwords, hashedPass, hash)