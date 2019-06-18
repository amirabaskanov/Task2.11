#11. You are given a string.
#    In the first line, print the third character of this string.
#    In the second line, print the second to last character of this string.
#    In the third line, print the first five characters of this string.
#    n the fourth line, print all but the last two characters of this string.
#    In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first
#    In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
#    In the seventh line, print all the characters of the string in reverse order.
#    In the eighth line, print every second character of the string in reverse order, starting from the last one.
#    In the ninth line, print the length of the given string.
a = str("Python bootcamp")
print ('1) ' + a[2])
print ('2) ' + a[1:])
print ('3) ' + a[:5])
print ('4) ' + a[:-2])
print ('5) ' + a[1::2])
print ('6) ' + a[::2])
print ('7) ' + a[::-1])
print ('8) ' + a[::-2])
print ('9) ' + str(len(a)))
