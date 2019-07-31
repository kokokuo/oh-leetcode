

class Solution:
    def isPalindrome(self, src: int) -> bool:
        """
        處理回文，不採用字串轉型的方式。
        如果小於正整數則返回 Fasle，否則透過取得不斷除以 10 取得商數來判斷迴圈是否到底。
        而獲得的餘數的方式放入陣列，待完成後透過陣列來做尋訪 [::-1] 判斷是否相符
        """
        slices = []
        if src < 0:
            return False
        while(src != 0):
            remainder = src % 10
            src = src // 10
            slices.append(remainder)
        if slices[::-1] == slices:
            return True
        return False
