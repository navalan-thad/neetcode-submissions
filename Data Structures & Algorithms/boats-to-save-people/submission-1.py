class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        boats = 0
        start = 0
        end = len(people)-1

        # 1,2,2,3,3
        
        while start < end:
            if people[end] + people[start] <= limit:
                boats += 1
                end -= 1
                start += 1
            else:
                boats += 1
                end -= 1
            
        if start == end:
            boats += 1

        return boats


        