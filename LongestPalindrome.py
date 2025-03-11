def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    def palindrome(s: str, l: int, r:int):
        if l > 0 and r < len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l + 1
    
    start = end = 0

    for i in range(len(s)):
        odd = palindrome(s, i, i)
        even = palindrome(s, i, i + 1)
        maxlen = max(odd, even)

        if maxlen > (end - start) + 1:
            start = i - (maxlen - 1) // 2
            end = i + (maxlen - 1) // 2
        
    return s[start : end]

longestPalindrome(s = "babad")