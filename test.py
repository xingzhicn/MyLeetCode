class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = str(num[0])
        result = ''
        for i in range(1, len(num)):

            # 如果是栈顶的值大于当前值，则出栈
            if stack[-1] < num[i]:
                result += stack[:-1]

                stack = stack[:-1] + str(num[i])
            else:
                result += str(num[i])
                if len(stack) == k:
                    continue
                stack = stack + str(num[i])

        if result:
            return result
        else:
            return "0"


i_list = [2.70, 3.20, 4.20, 3.90, 4.10, 2.60, 3.00, 4.10, 4.80, 1.80, 2.10, 1.90, 1.60, 1.70, 4.20, 3.70, 2.10, 4.40]
j = 0
for i in i_list:
    j += i
t = j / len(i_list)

print(Solution().removeKdigits("150200", 1))
