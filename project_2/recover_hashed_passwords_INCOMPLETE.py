from timeit import default_timer as timer

file1 = open("RECOVERED_PASSWORD_HASHES.txt")

recovered_hashes = file1.readlines()

file1.close()

file2 = open("RAINBOW_TEXT.txt")

indexed_hashes = list(enumerate(file2))

file2.close()

file3 = open("10K_PLAINTEXT_PASSWORDS.txt")

plaintext_passwords = file3.readlines()

file3.close()


def loopMethod(input_hash, indexed_hashes, password_list):
    print("This method uses a simple for loop")
    min_time = pow(10, 10)
    max_time = 0
    not_found_time = 0
    for in_hash in input_hash:
        in_hash = in_hash.rstrip()
        found = False
        t1 = timer()
        for i, hash in indexed_hashes:
            if hash.rstrip() == in_hash:
                t2 = timer()
                print("MATCH: hash # " + in_hash + " = " + password_list[i].rstrip())
                delta = (t2 - t1) * 1000000
                print('It took ', delta, ' microseconds.\n')
                found = True
                min_time = min(min_time, delta)
                max_time = max(max_time, delta)
                break;
        if not found:
            t2 = timer()
            delta = (t2 - t1) * 1000000
            print("NO MATCH FOUND FOR ", in_hash, " = NA")
            print('It took ', delta, ' microseconds.\n')
            not_found_time = max(not_found_time, delta)
    print("Minimum time to recover the password is - ", min_time, " microseconds")
    print("Maximum time to recover the password is - ", max_time, " microseconds")
    if not_found_time > 0:
        print("Time to search the entire the Rainbow table - ", not_found_time, " microseconds")


def preCompute(indexed_hashes):
    hash_map = {}
    for i, hash in indexed_hashes:
        hash_map[hash.rstrip()] = i
    return hash_map


def mapMethod(input_hash, indexed_hashes, password_list):
    print("This method uses a hash map")
    min_time = pow(10, 10)
    max_time = 0
    not_found_time = 0
    hash_map = preCompute(indexed_hashes)
    for in_hash in input_hash:
        in_hash = in_hash.rstrip()
        found = False
        t1 = timer()
        index = hash_map.get(in_hash)
        if index is None:
            t2 = timer()
            delta = (t2 - t1) * 1000000
            print("NO MATCH FOUND FOR ", in_hash, " = NA")
            print('It took ', delta, ' microseconds.\n')
            not_found_time = max(not_found_time, delta)
        else:
            t2 = timer()
            print("MATCH: hash # " + in_hash + " = " + password_list[index].rstrip())
            delta = (t2 - t1) * 1000000
            print('It took ', delta, ' microseconds.\n')
            found = True
            min_time = min(min_time, delta)
            max_time = max(max_time, delta)
    print("Minimum time to recover the password is - ", min_time, " microseconds")
    print("Maximum time to recover the password is - ", max_time, " microseconds")
    if not_found_time > 0:
        print("Time to search the entire the Rainbow table - ", not_found_time, " microseconds")


# for each candidate hash in recovered_hashes
# you'll need some way to stop the inner for loop search
# maybe use a flag variable (True/False)
loopMethod(recovered_hashes, indexed_hashes, plaintext_passwords)
print("\n")
mapMethod(recovered_hashes, indexed_hashes, plaintext_passwords)
