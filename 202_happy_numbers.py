import math
import random
'''
202. Happy Number
Easy
Topics
premium lock iconCompanies

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false


'''


def _format_processed_nums_literal(dsqrs: set[int]) -> str:
    """One line you can paste into code as a set initializer."""
    inner = ", ".join(str(x) for x in sorted(dsqrs))
    return f"processed_nums = {{{inner}}}"


class Solution:

    # starting shortcuts / unhappy cycle; extend via collect_known_nums(..., random_trials=...)
    UNHAPPY_SEED = frozenset({2, 4, 5, 6, 8, 9, 11, 12, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 45, 46, 50, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 64, 65, 66, 67, 69, 72, 73, 74, 75, 76, 77, 78, 80, 81, 83, 84, 85, 89, 90, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 110, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 126, 131, 132, 134, 135, 136, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 165, 166, 168, 169, 170, 171, 172, 173, 174, 175, 177, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189, 194, 195, 196, 197, 199, 200, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 224, 225, 227, 228, 229, 231, 232, 233, 235, 237, 238, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 253, 254, 255, 256, 257, 259, 260, 261, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 290, 292, 294, 295, 296, 299, 300, 303, 304, 305, 306, 307, 308, 309, 311, 312, 314, 315, 317, 318, 321, 323, 324, 325, 328, 330, 334, 335, 336, 337, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 357, 360, 361, 369, 370, 371, 373, 375, 384, 385, 387, 393, 394, 396, 398, 400, 402, 411, 414, 417, 422, 423, 429, 433, 436, 439, 453, 467, 471, 497})

    def get_digits(self, n:int) -> list:

        digits = []

        total_digits = math.ceil(math.log10(n))

        running_num = n
        for i in range(total_digits, -1, -1):
            dnum = int(pow(10, i))
            d = running_num // dnum
            #print('running_num', running_num,  'dnum', dnum, 'd', d)
            if d > 0:
                digits.append(d)
                running_num = running_num - dnum * d

        if running_num > 0:
            digits.append(running_num)

        return digits



    def digits_square(self, digits:list) -> int:

        sumsqr = 0 
        for d in digits:
            sumsqr += d * d

        return sumsqr


    def isHappyDebug(self, n: int, debug: bool = True) -> tuple[bool, bool, set[int]]:
        """Returns (is_happy, hit_seed_early, chain_dsqrs) where chain_dsqrs is every sum-of-squares seen."""

        processed_nums = set(self.UNHAPPY_SEED)
        chain_dsqrs: set[int] = set()

        if n == 1:
            return True, False, chain_dsqrs

        if n == 0:
            return False, False, chain_dsqrs

        digits = self.get_digits(n)
        dsqr = self.digits_square(digits)
        chain_dsqrs.add(dsqr)

        if debug:
            print(digits, dsqr)

        if dsqr == 1:
            return True, False, chain_dsqrs

        if dsqr in processed_nums:
            return False, True, chain_dsqrs

        processed_nums.add(dsqr)

        while True:
            digits = self.get_digits(dsqr)
            dsqr = self.digits_square(digits)
            chain_dsqrs.add(dsqr)

            if debug:
                print(digits, dsqr)

            if dsqr == 1:
                return True, False, chain_dsqrs
            if dsqr in processed_nums:
                return False, False, chain_dsqrs
            processed_nums.add(dsqr)


    def collect_known_nums(
        self,
        n: int | None = None,
        *,
        random_trials: int | None = None,
        lo: int = 1,
        hi: int = 10**9,
    ) -> set[int]:
        """Print a sorted `processed_nums = {...}` line for copy-paste.

        Pass `n` for one walk, or `random_trials` to union dsqrs from random ints that are **not** happy.
        """

        if random_trials is not None:
            union: set[int] = set()
            unhappy_runs = 0
            for _ in range(random_trials):
                nn = random.randint(lo, hi)
                is_happy, _, chain = self.isHappyDebug(nn, debug=False)
                if not is_happy:
                    unhappy_runs += 1
                    union |= chain
            print(
                f"# dsqrs from {unhappy_runs} unhappy outcomes "
                f"({random_trials} random ints in [{lo}, {hi}])"
            )
            print(_format_processed_nums_literal(union))
            return union

        if n is None:
            raise TypeError("collect_known_nums: pass n=... or random_trials=...")

        is_happy, hit_seed, chain = self.isHappyDebug(n, debug=False)
        print("is_happy", is_happy, "hit_seed_early", hit_seed)
        if is_happy:
            print("# n is happy — no unhappy-walk dsqrs to paste")
            return set()
        print("# dsqrs seen on this unhappy walk")
        print(_format_processed_nums_literal(chain))
        return chain


    def isHappy(self, n: int) -> bool:
        is_happy, _, _ = self.isHappyDebug(n, debug=False)
        return is_happy


if __name__ == "__main__":
    s = Solution()

    if True:
        not_happy = []
        for _ in range(1000):
            n = random.randint(1, 10**9)
            if not s.isHappy(n):
                not_happy.append(n)
        print(f"not happy: {len(not_happy)} / 1000")
        #print(not_happy)

    # Set True to print dsqrs union from random **unhappy** walks only; paste into UNHAPPY_SEED
    if False:
        s.collect_known_nums(random_trials=500, lo=1, hi=10**9)

    print(s.isHappy(19))
