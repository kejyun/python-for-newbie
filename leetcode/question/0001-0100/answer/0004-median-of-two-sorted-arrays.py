import sys
from typing import List


class Solution(object):
    def findMedianSortedArrays(self, nums_list_1: List[int], nums_list_2: List[int]) -> float:
        # https://github.com/mission-peace/interview/blob/master/src/com/interview/binarysearch/MedianOfTwoSortedArrayOfDifferentLength.java
        # https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
        # https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
        # https://books.halfrost.com/leetcode/ChapterFour/0001~0099/0004.Median-of-Two-Sorted-Arrays/
        # 「數字清單 1」數量
        nums_list_1_length = len(nums_list_1)
        # 「數字清單 2」數量
        nums_list_2_length = len(nums_list_2)

        if nums_list_1_length > nums_list_2_length:
            # 若「數字清單 1」數量大於「數字清單 2」，將交換數字清單順序，將小的優先傳入
            return self.findMedianSortedArrays(nums_list_2, nums_list_1)

        # 「數字清單 1」左側檢查位置（從第一個開始往右檢查）
        nums_list_1_left_index = 0
        # 「數字清單 1」右側檢查位置（從最後一個開始往左檢查）
        nums_list_1_right_index = nums_list_1_length
        # 所有數字中位數可能位置，全部長度+1，bit 往右位移除 2
        all_nums_list_divide_position = (nums_list_1_length + nums_list_2_length + 1) >> 1
        # 「數字清單 1」中位數位置
        nums_list_1_median_partition_index = 0
        # 「數字清單 2」中位數位置
        nums_list_2_median_partition_index = 0

        # 找尋中位數位置
        while nums_list_1_left_index <= nums_list_1_right_index:
            # 「數字清單 1」左側檢查位置小於右側位置，繼續檢查
            # 「數字清單 1」中位數檢查拆分位置 = 目前左方最小數字位置 + 右方剩餘數字取中位數 bit 往右位移除 2
            nums_list_1_median_partition_index: int = nums_list_1_left_index + (
                    (nums_list_1_right_index - nums_list_1_left_index) >> 1)
            # 「數字清單 2」中位數檢查拆分位置 = 所有數字中位數可能位置 - 數字清單 1 中位數位置
            nums_list_2_median_partition_index: int = all_nums_list_divide_position - nums_list_1_median_partition_index

            if nums_list_1_median_partition_index > 0 and nums_list_1[nums_list_1_median_partition_index - 1] > \
                    nums_list_2[nums_list_2_median_partition_index]:
                # 「數字清單 1」中位數位置不是第一個數字，且有資料
                # 「數字清單 1」中位數左側數字比「數字清單 2」右側中位數還大（排序過的數字左側應比右側小）
                # 表示整個數字列表的中位數在「數字清單 1」目前中位數之前
                # 「數字清單 1」右方數字索引往左側移動，找「數字清單 1」中位數前面小一點的數字
                nums_list_1_right_index = nums_list_1_median_partition_index - 1
            elif nums_list_1_median_partition_index != nums_list_1_length and nums_list_1[
                nums_list_1_median_partition_index] < nums_list_2[nums_list_2_median_partition_index - 1]:
                # 「數字清單 1」中位數位置不是最後一個數字，且有資料
                # 「數字清單 1」中位數右側數字比「數字清單 2」左側中位數還小（排序過的數字右側應比左側大）
                # 「數字清單 1」中位數位置數字 比 「數字清單 2」中位數位位置的前一個數字還小
                # 「數字清單 1」左方數字索引往右側移動，找「數字清單 1」中位數後面大一點的數字
                nums_list_1_left_index = nums_list_1_median_partition_index + 1
            else:
                # 無法再劃分左右側中位數位置
                break

        # === 找出中位數 ===
        # 中位數
        median_num: float = 0.0
        # 左側中位數
        median_num_left: int = 0
        # 右側中位數
        median_num_right: int = 0

        if nums_list_1_median_partition_index == 0:
            # 「數字清單 1」中位數位置為移動到第一個數字，或是沒有數字 => 「數字清單 1」左側都沒有資料
            # 中位數左側數字 = 「數字清單 2」 左側第一個數字」
            median_num_left = nums_list_2[nums_list_2_median_partition_index - 1]
        elif nums_list_2_median_partition_index == 0:
            # 「數字清單 2」中位數位置移動到第一個數字，表示數字只有一個，或是沒有數字 => 「數字清單 2」左側都沒有資料
            # 中位數左側數字 = 「數字清單 1」 左側第一個數字」
            median_num_left = nums_list_1[nums_list_1_median_partition_index - 1]
        else:
            # 「數字清單 1」與「數字清單 2」有超過一個數字，有自己的中位數，取兩個左側中位數最大的那一個
            # 左側的數字比右側小，所以要找比較大的數字才會接近右側數字
            median_num_left = max(nums_list_1[nums_list_1_median_partition_index - 1],
                                  nums_list_2[nums_list_2_median_partition_index - 1])


        if (nums_list_1_length + nums_list_2_length) & 1 == 1:
            # 若數字總數量為奇數，直接回傳中位數數字
            median_num = float(median_num_left)
            return median_num

        # 若數字總數量為偶數，取得中位數右側最小數值
        if nums_list_1_median_partition_index == nums_list_1_length:
            # 「數字清單 1」沒有數字，或者索引超出範圍 => 「數字清單 1」右側都沒有資料，使用「數字清單 2」右側資料
            median_num_right = nums_list_2[nums_list_2_median_partition_index]
        elif nums_list_2_median_partition_index == nums_list_2_length:
            # 「數字清單 2」沒有數字，或者索引超出範圍 => 「數字清單 2」右側都沒有資料，使用「數字清單 1」右側資料
            median_num_right = nums_list_1[nums_list_1_median_partition_index]
        else:
            # 「數字清單 1」與「數字清單 2」有超過一個數字，有自己的中位數，取兩個右側中位數最小的那一個
            median_num_right = min(nums_list_1[nums_list_1_median_partition_index],
                                   nums_list_2[nums_list_2_median_partition_index])

        # 計算中位數左右平均
        median_num = float((median_num_left + median_num_right) / 2.0)

        return median_num


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1], [2, 3, 4, 5, 6]))
    print(s.findMedianSortedArrays([4], [1, 2, 3, 5, 6]))
    print(s.findMedianSortedArrays([], [1, 2, 3, 5, 6]))
