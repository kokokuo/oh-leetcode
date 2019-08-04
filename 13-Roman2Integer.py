

class Solution:
    def romanToInt(self, roman: str) -> int:
        """
        1. 設定初始值 total = 0
        2. 反轉 roman 為 inverted 使尋訪由最低位尋訪到最高位
        2. 由 Loop 尋訪 inverted
        3. 對目前字串轉為數值 curr
        4. 如果為第一個位數: total = curr 做初始值
        5.若非為第一位數，讓目前位數與上一位數判斷數值大小
        如果 目前位數 curr > 前一位數 prev, 則累加
        若不是，則扣減取絕對值
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        inverted = roman[::-1]
        for idx, ch in enumerate(inverted):
            curr = table[ch]
            if idx == 0:
                total = curr
            else:
                prev = table[inverted[idx - 1]]
                total = total + curr if curr >= prev else abs(total - curr)
        return total
