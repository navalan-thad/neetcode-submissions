class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = {
            5: 0,
            10: 0,
        }

        for i in bills:
            if i == 5:
                change[5] += 1
            else:
                if i == 10:
                    if change[5] < 1:
                        print(change)
                        return False
                    change[10] += 1
                    change[5] -= 1
                else:
                    if change[10] >= 1 and change[5] >= 1:
                        change[10] -= 1
                        change[5] -= 1
                    elif change[5] >= 3:
                        change[5] -= 3
                    else:
                        print(change)
                        return False
        return True


        