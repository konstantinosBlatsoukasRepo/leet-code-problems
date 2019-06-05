class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = [number for number in range(left, right + 1)]

        self_dividing_numbers = []
        for number in numbers:
            digits = {num for num in str(number)}
            total_digits = len(digits)
            if "0" not in digits:

                total_success = 0
                for digit in digits:
                    if number % int(digit) == 0:
                        total_success += 1

                if total_success == total_digits:
                    self_dividing_numbers.append(number)

        return self_dividing_numbers
