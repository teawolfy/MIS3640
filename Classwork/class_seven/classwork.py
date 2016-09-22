''''
result = 0
for i in range(11):
    print ('current i:', i)
    result = result + i
print(result)
'''
'''
for i in range(2,11,2):
    print('current i: ', i)
    result += i

print(result)
'''

result = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        result = result + i
    i = i + 1

print(result)
