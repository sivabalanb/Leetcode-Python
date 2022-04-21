#https://leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    '''
        * Create two pointers
        * One for start and other for the end
        * Increment the start and decrement end
        * If value at index of start != end then its not a palindrome
        * Edge case - odd palindrome
    '''
    x = str(x)
    start, end = 0, len(x) - 1
    
    #Even Palindrome
    while start <= end:
        print(f"Strt {start} end {end}")
        if x[start] == x[end]:
            start += 1
            end -= 1
        else:
            return False
    
    return True

print(isPalindrome(-121))