class Solution(object):
    result = []

    def bar(self, S, i_first):
        for i in range(1, len(S)):
            # if S[i] == '0' and i != len(S):
            #     continue
            if int(S[:i]) == i_first:
                self.result.append(i_first)
                if i == len(S):
                    return True
                self.bar(S[i:], self.result[len(self.result)-1]+i_first)

            elif i == len(S):
                self.result = []
                return False


    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        """
        先找第一个数
        再找第二个数
        看是否有符合条件的第三个数,用前两个数去剩下的字符串中找是否有符合条件的值
        """
        for i in range(1, len(S)):
            if S[i] == '0':
                continue
            first_num = int(S[:i])
            for j in range(1, len(S[i:])):
                if S[j + i] == '0':
                    continue
                two_num = int(S[i:j+i])
                self.result.append(first_num)
                self.result.append(two_num)
                if self.bar(S[i + j:], first_num + two_num):
                    return self.result

print(Solution().splitIntoFibonacci("123456579"))