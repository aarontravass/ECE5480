import hashlib

fp = open("10K_PLAINTEXT_PASSWORDS.txt", "r")

lines = [line.rstrip() for line in fp.readlines()]

fp.close()

outfile = open("RAINBOW_TEXT.txt", "a")
for password in lines:
    hashed=hashlib.md5(password.encode()).hexdigest()+'\n'
    outfile.write(hashed)

outfile.close()
