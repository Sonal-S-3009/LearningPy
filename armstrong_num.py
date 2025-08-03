
'''def armstrong(k):
    for i in range(k+1):
        digits = [int(x) for x in str(i)]
        n = len(digits)
        sum_squared_digits =0
        for digit in digits:
            sum_squared_digits += (digit**n)
        if sum_squared_digits == i:
            print(i)
print(armstrong(500))'''

'''def longest_subarray(a):
    print(a)
    n = len(a)
    subarray = []
    longest = []
    for start in range(n):
        for end in range(start+1,n+1):
            if sum(a[start:end])==0:
                subarray.append(a[start:end])
                for array in subarray:
                    if len(array)>len(longest):
                        longest = array.copy()
    return longest

arr = []
while True:
    try:
        element = int(input("Enter the number"))
        arr.append(element)
    except ValueError:
        break
print(longest_subarray(arr))'''



def min_operation(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i  # Deleting
    for j in range(n + 1):
        dp[0][j] = j  # Inserting
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[m][n]

print(min_operation("hors", "ros"))








