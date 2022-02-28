class Solution:
    """
    示例 4：

    输入：s = "aab" p = "c*a*b"
    输出：true
    解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
    示例 5：

    输入：s = "mississippi" p = "mis*is*p*."
    输出：false

    """

    def isMatch(self, s: str, p: str) -> bool:
        # dp = [False]*len(s)
        i = 0
        j = 0
        while i < len(s):
            if p[i] == s[i]:
                i += 1
                j += 1
            elif p[i] == '.':
                i += 1
                j += 1
                if p[i] == '*':
                    return True
            elif p[i] == '*' and i > 0:
                tmp = p[i - 1]
                while p[i] == tmp:
                    i += 1
                i += 1
                j += 1
            elif p[i] != s[i]:
                return False
        return True


print(Solution().isMatch('mississippi', "mis*is*p*."))
