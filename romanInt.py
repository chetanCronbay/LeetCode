class Solution:
    def intToRoman(num: int) -> str:
        # roman = {
        #     1 : "I",
        #     5 : "V",
        #     10 : "X",
        #     50 : "L",
        #     100 : "C",
        #     500 : "D",
        #     1000 : "M",
        #     4 : "IV",
        #     9 : "IX",
        #     40 : "XL",
        #     90 : "XC",
        #     400 : "CD",
        #     900 : "CM",
        # }
        # arr = []
        # # result = []
        # n = 0
        # val = ""
        
        # while num > 0:
        #     arr.append(num % 10)
        #     num = num // 10
        
        # i = len(arr) - 1
        # print(arr)
        
        # while i >= 0:
        #     n = arr[i] * 10**i
        #     if i == 3:
        #       val = val + roman[1000] * (n // 1000)
        #       i -=1
        #     elif i == 2:
        #         while n > 0:
        #             if n == 400:
        #                 val = val + roman[400]
        #                 n = n - 400
        #             elif n == 900:
        #                 val = val + roman[900]
        #                 n = n - 900
        #             elif n >= 100 and n < 400:
        #                 val = val + roman[100] * (n // 100)
        #                 n = n - (100 * (n // 100))
        #             elif n > 400 and n >= 500:
        #                 val = val + roman[500] * (n // 500)
        #                 n = n - (500 * (n // 500))
        #         i -=1
                
        #     elif i == 1:
        #         while n > 0:
        #             if n == 40:
        #                 val = val + roman[40]
        #                 n = n - 40
        #             elif n == 90:
        #                 val = val + roman[90]
        #                 n = n - 90
        #             elif n >= 10 and n < 40:
        #                 val = val + roman[10] * (n // 10)
        #                 n = n - (10 * (n // 10))
        #             elif n > 40 and n >= 50:
        #                 val = val + roman[50] * (n // 50)
        #                 n = n - (50 * (n // 50))
        #         i -=1

        #     elif i == 0:
        #         while n > 0:
        #             if n == 4:
        #                 val = val + roman[4]
        #                 n = n - 4
        #             elif n == 9:
        #                 val = val + roman[9]
        #                 n = n - 9
        #             elif n >= 1 and n < 4:
        #                 val = val + roman[1] * (n // 1)
        #                 n = n - (1 * (n // 1))
        #             elif n > 4 and n >= 5:
        #                 val = val + roman[5] * (n // 5)
        #                 n = n - (5 * (n // 5))
        #         i -=1
        
        # return val
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)      


    intToRoman(num = 3749)