class Solution:
    def lengthOfLongestSubstring(self, check_text: str) -> int:
        # 被檢查的文字長度
        check_text_length = len(check_text)

        # 驗證字串長度為 0 不檢查
        if check_text_length == 0:
            return 0

        # 建立長度 256 的整數字典
        text_ascii_int_flag = {}

        # 左方字元索引
        left_character_index: int = 0
        # 右方字元索引
        right_character_index: int = 0
        # 檢查文字最大不重複字串長度
        check_text_longest_string_length: int = 0
        # 右方指標字元 ASCII Code
        right_character_ascii_code: int = 0
        # 左方指標字元 ASCII Code
        left_character_ascii_code: int = 0
        # 目前字串長度
        current_text_string_length: int = 0

        while left_character_index <= check_text_length:
            # 若左側指標小於字串長度，繼續檢查
            if right_character_index >= check_text_length:
                # 若右側指標大於字串長度，表示已經檢查到最後的字串了，不需要再檢查
                break

            # 右方指標字元 ASCII Code
            right_character_ascii_code = ord(check_text[right_character_index])

            if right_character_ascii_code not in text_ascii_int_flag:
                # 「右側指標 + 1 小於字串長度，表示字串還沒全部檢查完」且「此文字未出現過」
                # 標記右方文字出現過
                text_ascii_int_flag[right_character_ascii_code] = 1
                # 繼續往右檢查
                right_character_index += 1
            else:
                # 左方指標字元 ASCII Code
                left_character_ascii_code = ord(check_text[left_character_index])
                # 刪除標記左方文字沒出現過
                del text_ascii_int_flag[left_character_ascii_code]
                # 將左方指標往前移動
                left_character_index += 1

            # 設定目前字串長度
            current_text_string_length = right_character_index - left_character_index
            if check_text_longest_string_length < current_text_string_length:
                # 若右方指標在左方指標前面，且長度大於目前檢查文字的最大長度，將目前長度設定為最大長度
                check_text_longest_string_length = current_text_string_length

            if left_character_index + check_text_longest_string_length >= check_text_length or right_character_index >= check_text_length:
                # 1. 左方字元索引 + 目前檢查文字的最大長度 > 文字最大長度：再往右找也找不到更長的文字了
                # 2. 右方字元索引 >= 被檢查的文字長度: 已經檢查到最後一個字元了
                # 跳出檢查
                break

        return check_text_longest_string_length


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
