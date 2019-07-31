

class Solution:
    def reverse(self, x: int) -> int:
        """
        1.轉為字串，做反向尋訪取得逆向數值
        2.再除去錯誤的 "-" 並放置開頭
        3.最後轉回數字
        4.檢查其數字範圍有無在  [−2 ** 31,  2 ** 31 − 1] 之間，沒有則表示溢位
        """
        str_num = str(x)
        reverse_num = str_num[::-1]
        clean_num = reverse_num
        if "-" in reverse_num:
            clean_num = reverse_num.replace("-", "")
            clean_num = "-" + clean_num
        num = int(clean_num)
        if (-2 ** 31) < num < (2 ** 31 - 1):
            return num
        return 0
