class Solution(object):
    def addDigits(self, num):

        def sum_digits(n):
            if n < 10:
                return n
            return n % 10 + sum_digits(n // 10)

        if num < 10:
            return num
        return self.addDigits(sum_digits(num))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna