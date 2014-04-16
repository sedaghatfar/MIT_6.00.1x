# Write a program that counts up the number of vowels contained in the string s

count = 0
for i in s:
    if (i == "a" ) or (i == "e" ) or (i == "i" ) or (i == "o" ) or (i == "u" ):
        count += 1
print count
    
# Write a program that prints the number of times the string 'bob' occurs in s

count = 0
i = 0
while i < len(s):
    if s[i:i+3:1] == 'bob':
        count +=1
    i +=1
       
print "Number of times bob occurs is: " + str(count)

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order

from itertools import count

def long_sub(input_string):
    maxsubstr = input_string[0:0] # empty slice (to accept subclasses of str)
    for start in range(len(input_string)): # O(n)
        for end in count(start + len(maxsubstr) + 1): # O(m)
            substr = input_string[start:end] # O(m)
            if len(substr) != (end - start): # found duplicates or EOS
                break
            if sorted(substr) == list(substr):
                maxsubstr = substr
    return maxsubstr

sub = (long_sub(s))
print "Longest substring in alphabetical order is: %s" %sub
