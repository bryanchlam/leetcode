# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# string s
s = "abccba"
# index of start window
start = 0
# the length of longest substring without repeating characters
result = 0
# the lenght of string s
n = len(s)
# dictionary to store the character and its index in string s
dict = {}
# loop the string with end as the index of end window
for end in range(0,n):
    # if the character at index end exists in the dictionary
    if s[end] in dict:
        # mark down the previous occurence of the character
        duplicateIndex = dict[s[end]]
        # update the result as the maximum between current value and the size of current window
        result = max(result, end - start)
        # remove all characters before the new window in the dictionary
        for i in range(start, duplicateIndex + 1):
            del dict[s[i]]
        # update the index of start window to the next position
        start = duplicateIndex + 1
    # add the character back to the dictionary with the latest end position
    dict[s[end]] = end
    print(dict)
    print("start = ", start, "end = ", end, "result = ", result)

result = max(result, n-start)
print("result = ", result)