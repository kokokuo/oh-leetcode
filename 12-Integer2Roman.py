

class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        roman = ""
        quotient = num
        digit = 0
        # 透過除以 10 求得商與餘數來由個位數尋訪到最高位數
        while(quotient > 0):
            remainder = quotient % 10
            quotient = quotient // 10
            # 計算目前位數的 10 次方，如 1, 10, 100, 1000...
            digit_unit = pow(10, digit)
            # 使該餘數回到正確位數的值
            remainder *= digit_unit
            # 若該餘數不為零則持續檢察署於的羅馬字
            while(remainder > 0):
                # 若直接存在表中，作轉換並串接原先的羅馬字
                if remainder in table:
                    roman = table[remainder] + roman
                    # 找到該字，扣除掉餘數
                    remainder -= remainder
                else:
                    # 若不在表中，則該位數的 10 次方數為一單位扣減，並對此次的扣減轉會成羅馬字
                    roman = table[digit_unit] + roman
                    remainder -= digit_unit
            digit += 1
        return roman
