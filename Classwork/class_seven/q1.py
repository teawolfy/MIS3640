def crazy_about_9(a, b):
    if a == 9 or b == 9 or abs(a-b)==9:
       return True
    return False

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))