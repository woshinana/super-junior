l1 = input()
l1 = eval(l1)
len1 = len(l1)
l2 = input()
l2 = eval(l2)
len2 = len(l2)
len = min(len1,len2)
sum = []
i = 1
carry = 0
while i<=len :
    a = l1[-i] +l2[-i] + carry
    if a < 10:
        sum.append(a)
        carry = 0
    else:
        carry = 1
        a = a - 10
        sum.append(a)
    i = i + 1

if len1 < len2:
    while len1 < len2:
        len1 = len1 + 1
        sum.append(l2[-len1] + carry)
        carry = 0
elif len1 > len2:
    while len1 > len2:
        len2 = len2 + 1
        sum.append(l1[-len2] + carry)
        carry = 0
else:
    if carry ==1:
        sum.append(1)
    else:
        pass
print(sum)
