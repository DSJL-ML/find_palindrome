# find the longest palindromic substring in a given string s
def palindrome_string(s):
    # for loop starting with the longest possible length of substring having palindrome = length/2
    substring = None
    for i in range(int(len(s)/2),2,-1):
    # iterate through all the possible length i of substring, starting with the longest length (reverse iteration)
        if substring:
            break
            
        else:
            for j in range(len(s)-i+1):
            # iterate substring with length i through string s, starting with indice j                
                if s[j:(j+i)] == s[(j+i*2):(j+i):-1]:
                    substring = s[j:(j+i*2+1)]
                    break
                elif s[j:(j+i)] == s[(j+i*2-1):(j+i-1):-1]:
                    substring = s[j:(j+i*2)]
                else:
                    continue
                
    print substring