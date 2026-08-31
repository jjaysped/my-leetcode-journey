class Solution(object):
    def isPalindrome(self, s):
        # Step 1: clean the string — keep only letters/digits, lowercase everything
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()

        # Step 2: two-pointer check
        L = 0
        R = len(cleaned) - 1
        while L < R:
            if cleaned[L] != cleaned[R]:      # compare the two ends
                return False
            L += 1
            R -= 1
        return True
