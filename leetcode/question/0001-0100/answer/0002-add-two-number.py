from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    # ListNode 轉換成數字清單
    def listNodeToNumList(HeadListNode: ListNode) -> List[int]:
        # 數字清單
        num_list = []
        while HeadListNode is not None:
            num_list.append(HeadListNode.val)
            HeadListNode = HeadListNode.next

        return num_list

    @staticmethod
    # 數字清單轉換成 ListNode
    def numListToListNode(nums_list: List[int]) -> ListNode:
        # 初始化鏈結節點
        HeadListNode = ListNode(None)

        # 設定目前鏈結節點
        CurrentListNode = HeadListNode
        for value in nums_list:
            # 設定鏈結節點的下一節點
            CurrentListNode.next = ListNode(value)
            # 將下一節點設為目前節點
            CurrentListNode = CurrentListNode.next

        return HeadListNode.next

    def addTwoNumbers(self, FirstNumberListNode: ListNode, SecondNumberListNode: ListNode) -> ListNode:
        # 建立答案節點，預設個位數是 0
        AnswerListNode = ListNode(0)
        CurrentAnswerListNode = AnswerListNode  # 目前答案節點
        number_1: int = 0  # 第 1 個加總數值
        number_2: int = 0  # 第 2 個加總數值
        carry_number: int = 0  # 加總後的進位數值
        number_sum: int = 0  # 加總數值

        while FirstNumberListNode is not None or SecondNumberListNode is not None or carry_number != 0:
            # === 計算第 1 個數字 ===
            if FirstNumberListNode is None:
                # 若「第 1 數字節點」為 nil，表示沒有數字可以做加總了，設定可加總數字為 0
                number_1 = 0
            else:
                # 若「第 1 數字節點」有值，將節點數值設定為此次第 1 個加總數值
                number_1 = FirstNumberListNode.val
                FirstNumberListNode = FirstNumberListNode.next

            # === 計算第 2 個數字 ===
            if SecondNumberListNode is None:
                # 若「第 2 數字節點」為 nil，表示沒有數字可以做加總了，設定可加總數字為 0
                number_2 = 0
            else:
                number_2 = SecondNumberListNode.val
                SecondNumberListNode = SecondNumberListNode.next

            # 加總數值
            number_sum = number_1 + number_2 + carry_number
            # 設定餘數為目前答案節點數值
            CurrentAnswerListNode.next = ListNode(number_sum % 10)
            # 設定答案節點的下一節點為目前節點，繼續往後做加總
            CurrentAnswerListNode = CurrentAnswerListNode.next
            # 取得加總後的進位數值，繼續往後做加總
            carry_number = int(number_sum / 10)

        return AnswerListNode.next


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.listNodeToNumList(s.addTwoNumbers(s.numListToListNode([2, 4, 3]), s.numListToListNode([5, 6, 4]))))
    print(s.listNodeToNumList(
        s.addTwoNumbers(s.numListToListNode([9, 9, 9, 9, 9, 9, 9]), s.numListToListNode([9, 9, 9, 9]))))
