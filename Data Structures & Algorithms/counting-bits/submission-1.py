class Solution:
    def countBits(self, n: int) -> List[int]:

        outputs = [0, 1]

        if n == 0:
            return [0][:1]
        elif n == 1:
            return outputs
        
        def ones(n):
            count = 0
            while n > 0:
                n = n & (n-1)
                count += 1
            return count
        
        for i in range(2, n+1):
            outputs.append(ones(i))

        return outputs
        