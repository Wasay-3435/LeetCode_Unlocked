class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Return True if s is a palindrome after:
        - Ignoring non-alphanumeric characters
        - Treating uppercase and lowercase letters as equal
        """

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters from the left
            if not s[left].isalnum():
                left += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters without case sensitivity
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True
