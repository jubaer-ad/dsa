
count = 0
arr = []

def printPermutn(str, ans):
    
    if len(str) == 0:
        global count, arr
        count += 1
        if ans not in arr:
            arr.append(ans)
        return
    for i in range(0, len(str)):
        ch = str[i]
        ros = str[0 : i] + str[i + 1 :]
        printPermutn(ros, ans + ch)

def isPrime(num):
    flag = True
    for i in range(2, int(num / 2)):
        if num % i == 0:
            flag = False
    return flag

s = "35"
printPermutn(s, "")

print("# of Permutations:", count)
print('All Permutations:')
print(arr)
arr = list(map(int, arr))
arr2 = [int(x) for x in arr if isPrime(x)]
print('Prime List:')
print(arr2)




