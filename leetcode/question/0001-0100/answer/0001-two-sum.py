from typing import List


class Solution:
    def twoSum(self, nums_list: List[int], final_sum_value: int) -> List[int]:
        # 數字反向對應表
        num_reverse_mapping = {}

        # 列舉數字清單
        enumerate_nums_list = enumerate(nums_list)

        for current_num_key, current_num_value in enumerate_nums_list:
            # 其他鍵值數值
            other_value = final_sum_value - current_num_value
            # 數值是否存在反轉對應表
            is_other_value_exist = (other_value in num_reverse_mapping)

            if is_other_value_exist:
                # 若其他數值有存在反轉表，回傳 key 值
                other_num_key = num_reverse_mapping[other_value]
                return [other_num_key, current_num_key]

            # 沒有找到數值，將數值位置 key 記錄下來
            num_reverse_mapping[current_num_value] = current_num_key


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 2, 4], 7))
