# 给定 nums = [2, 7, 11, 15], target = 20
#
# 因为 nums[0] + nums[1] + nums[2] = 2 + 7 + 11 = 20
# 所以返回 [0, 1, 2]
def sum_list(i_list, target_int):
    i_dict = {}
    for i in range(len(i_list)):
        diff = target_int - i_list[i]
        for j in i_dict:
            if j <= diff and diff - j in i_dict:
                return [i_dict[j], i_dict[diff - j], i]
        i_dict[i_list[i]] = i


if __name__ == '__main__':
    assert sum_list([2, 7, 11, 15], 20) == [0, 1, 2]
