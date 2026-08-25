class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        boats = 0
        start = 0
        end = len(people)-1
        
        while start <= end:
            if people[end] + people[start] <= limit:
                end -= 1
                start += 1
            else:
                end -= 1
            boats += 1

        return boats


        