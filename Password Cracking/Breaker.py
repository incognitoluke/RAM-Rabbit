import itertools
import time

secret = input("Please Enter Your Password: ")
k = 1
count = 0

def generate(secret, k, count):
    group = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for item in list(itertools.permutations(group, k)):
        word = ''.join(item)
        print(word)
        count += 1
        if secret == word:
            print("----------------------------")
            print("Attempts:" + str(count))
            print("Your Password is: " + word)
            return word
    generate(secret, k + 1, count)

start = time.time()
word = generate(secret, k, count)
end = time.time()
print(round(end - start,2), "Seconds")
print("----------------------------")
