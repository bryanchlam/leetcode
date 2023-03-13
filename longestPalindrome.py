s = "cbbd"

resultString = ""
resultLen = 0


for i in range(len(s)):
    # odd length
    leftIdx, rightIdx = i, i
    while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
        if (rightIdx - leftIdx + 1) > resultLen:
            resultString = s[leftIdx:rightIdx+1]
            resultLen = rightIdx - leftIdx + 1
        
        leftIdx -= 1
        rightIdx += 1
    # even length
    leftIdx, rightIdx = i, i+1
    while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
        if (rightIdx - leftIdx + 1) > resultLen:
            resultString = s[leftIdx:rightIdx+1]
            resultLen = rightIdx - leftIdx + 1
        
        leftIdx -= 1
        rightIdx += 1
    
print(resultString)