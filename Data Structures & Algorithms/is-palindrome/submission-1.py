class Solution:
    def isPalindrome(self, s: str) -> bool:
        def rec(substr):
            if substr == "":
                return True
            if substr[0] != substr[-1]:
                return False
            return rec(substr[1:-1])

        return rec(re.sub(r"[^A-Za-z0-9]", "", s).lower())