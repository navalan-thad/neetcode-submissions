class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def circuit(i):
            dist = 0
            curr = 0
            while dist < len(gas) and curr >= 0:
                if i == len(gas):
                    i = 0
                curr = curr + gas[i] - cost[i]
                i += 1
                dist += 1
                
                print(f"current distance: {dist}")
                print(f"current cost: {curr}")
            return True if dist >= len(gas) and curr >=0 else False

        for i in range(len(gas)):
            print(f"using start = {i}")
            res = circuit(i)
            if res:
                return i

        return -1
            
    

            

        
            



        