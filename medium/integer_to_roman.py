class Solution:
    def intToRoman(self, num: int) -> str:
        roman_integers_mapping = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        result = ''

        for roman_value, integer_value in roman_integers_mapping.items():
            roman_value += roman_value * (num // integer_value)
            num = num % integer_value

        return result