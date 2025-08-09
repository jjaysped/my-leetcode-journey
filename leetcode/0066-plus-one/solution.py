class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no carry, return immediately
            digits[i] = 0  # set current digit to 0 and carry 1 to next digit

        return [1] + digits  # all 9's case, add new leading 1

# Example usage:
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]

