class Solution(object):
    def fib(self, n):
        # BASE CASES
        if n == 0:
            return 0
        if n == 1:
            return 1
        # RECURSIVE CASE
        return self.fib(n - 1) + self.fib(n - 2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna