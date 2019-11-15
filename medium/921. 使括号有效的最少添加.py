class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

    def minAddToMakeValid1(self, S):
        """
        需要左括号数量left，需要右括号数量right
        Args:
            S:

        Returns:

        """
        left = right = 0
        for i in S:
            if i == '(':
                right += 1
            else:
                left -= 1
        return left + right


if __name__ == '__main__':
    assert Solution().minAddToMakeValid("()))((") == 4
