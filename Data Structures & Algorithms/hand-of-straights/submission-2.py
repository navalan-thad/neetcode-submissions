class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hand.sort()

        freq = {}
        for i in hand:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in hand:
            if freq[i] > 0:
                freq[i] -= 1
                for j in range(1, groupSize):
                    if i+j in freq and freq[i+j] > 0:
                        freq[i+j] -= 1
                    else:
                        return False
        return True

        