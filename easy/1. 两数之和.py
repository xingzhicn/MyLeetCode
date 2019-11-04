class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    For Examples:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """

    def twoSum(self, nums: list, target: int) -> list:
        """
        第一种直接双for循环暴力解法
        Args:
            nums:
            target:

        Returns:

        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums: list, target: int) -> list:
        """
        一遍哈希表
        事实证明，我们可以一次完成。在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
        如果它存在，那我们已经找到了对应解，并立即将其返回。
        Args:
            nums:
            target:

        Returns:

        """
        i_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in i_dict:
                return [i_dict[target - nums[i]], i]
            else:
                i_dict[nums[i]] = i


if __name__ == '__main__':
    # 这道题的关键在于使用hash表来存储值，因为hash表get查询性能优越
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum1([2, 7, 11, 15], 9) == [0, 1]
