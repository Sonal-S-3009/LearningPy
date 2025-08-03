'''def has_no_e(file):
    total_count =0
    count = 0
    for line in file:
        word = line.strip()
        total_count +=1
        if "e" not in word:
            print(word)
            count+=1

    percentage = (count/total_count)*100
    print(f'{percentage:.2f}')


f = open("words.txt")
has_no_e(f)'''

'''def avoids(word,forbid):
    for i in forbid:
        if i in word:
            return False
    return True

print(avoids('strange','dh'))'''

'''def uses_only(word, string):
    for i in word:
        if i not in string:
            return False

    return True
print(uses_only("car","asbasaixrsxc"))'''

'''def uses_all(word,string):
    for i in string:
        if i not in word:
            return False
    return True

print(uses_all('amigokndakv','amigo'))'''

'''def three_consecutivedouble(f):
    count = 0
    for line in f:
        word = line.strip()
        i = 0
        while i< (len(word)-5):
            if word[i]==word[i+1] and word[i+2]==word[i+3]and word[i+4]==word[i+5]:
                print(word)
                count+=1
            i+=1
    print(count)

file = open('words.txt')
three_consecitivedoubles(file)
'''
'''for i in range(100000, 999997):  # up to 999996 so that i+3 doesn't exceed 999999
    s = str(i)
    if s[2:6] == s[2:6][::-1]:  # last 4 digits palindrome
        s1 = str(i + 1)
        if s1[1:6] == s1[1:6][::-1]:  # last 5 digits palindrome
            s2 = str(i + 2)
            if s2[1:5] == s2[1:5][::-1]:  # middle 4 digits palindrome
                s3 = str(i + 3)
                if s3 == s3[::-1]:  # full 6-digit palindrome
                    print(f"Original odometer reading: {i}")
'''

def reversed_pairs():
    for age in range(1, 100):
        for diff in range(10, 70):  # mom is older
            matches = 0
            for t in range(0, 100):
                your_age = age + t
                mom_age = age + diff + t
                if your_age >= 10 and mom_age >= 10 and your_age < 100 and mom_age < 100:
                    if str(your_age).zfill(2) == str(mom_age).zfill(2)[::-1]:
                        matches += 1
            if matches == 8:
                print(f"Your age now: {age}, Mom's age now: {age + diff}, Reversible Matches: {matches}")

print(reversed_pairs())
