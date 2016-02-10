#!/usr/bin/env python3.5

None

s1 = "\t\t\a\t"
s2 = "\t\n\n\t\a\s"
print(s1)
print(s2)

print(s1+s2)

s3 = 'spam'

s = 'spameggs'
s[:2] + 'U' + s[3:]
#'spUmeggs'
s[:2] + 'U' + s[2:]
#'spUameggs'

for i in range(0,len(s)):
    print(s[:i] + 'U' + s[i:])
