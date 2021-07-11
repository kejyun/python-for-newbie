class Solution:
    def longestPalindrome(self, check_text: str) -> str:
        # 字串長度
        check_text_length = len(check_text)
        # 文字不重複字串
        check_text_set = set(check_text)

        if check_text_length <= 1 or len(check_text_set) == 1:
            # 若字串長度小於 1，或者字串為重複字串，直接將字串回傳
            return check_text

        # manacher 檢查字串，將字串加入 # 符號，強制將字串變為奇數長度字串
        # baba  => b#a#b#a
        # babad => b#a#b#a#d
        manacher_check_text = '#'.join(check_text)
        # manacher 檢查字串長度
        manacher_check_text_length = len(manacher_check_text)
        manacher_check_text_range = range(1, manacher_check_text_length)
        # 對稱字串長度對應表
        palindrome_length_mapping_table = [0] * manacher_check_text_length

        # 最長對稱文字檢查長度
        max_check_text_length: int = int(manacher_check_text_length / 2) + 1
        for check_text_length in range(1, max_check_text_length):
            # 設定下一個檢查的文字範圍
            manacher_next_check_text_range = []
            for check_text_position in manacher_check_text_range:
                # 檢查文字位置
                # 檢查文字位置，前一個檢查文字長度位置
                check_text_previous_text_position = check_text_position - check_text_length
                # 檢查文字位置，後一個檢查文字長度位置
                check_text_next_text_position = check_text_position + check_text_length

                if check_text_previous_text_position < 0 or check_text_next_text_position >= manacher_check_text_length:
                    # 若字串索引超過字串長度，不檢查
                    continue

                if manacher_check_text[check_text_previous_text_position] != manacher_check_text[
                    check_text_next_text_position]:
                    # 若字串前後不相等，繼續檢查下一個
                    continue

                # 字串相等，將此位置紀錄，下個回合繼續做檢查
                manacher_next_check_text_range.append(check_text_position)

                if manacher_check_text[check_text_previous_text_position] == '#':
                    # 若為 manacher 字串符號，跳過不紀錄
                    continue

                # 紀錄非 # 字串，文字重複字串位置的長度
                palindrome_length_mapping_table[check_text_position] = check_text_length

            # 設定下一個字串檢查範圍，僅需檢查目前有重複出現字串位置即可
            manacher_check_text_range = manacher_next_check_text_range

        # 最長文字長度出現位置
        max_text_length_position = 0
        # 最長文字長度
        max_text_length = 0
        for text_position, text_length in enumerate(palindrome_length_mapping_table):
            if text_length > max_text_length:
                # 若文字長度大於最大文字長度，設定此位置及長度為最長長度
                max_text_length = text_length
                max_text_length_position = text_position

        # 取出最長對稱字串，並去除特殊標記「#」
        longest_palindrome_check_text = manacher_check_text[
                                        max_text_length_position - max_text_length:max_text_length_position + max_text_length + 1].replace(
            '#', '')

        return longest_palindrome_check_text


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestPalindrome('babad'))
