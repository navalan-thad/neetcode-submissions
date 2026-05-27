class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s, (target - p) / s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0])

        fleets = 1
        lead = cars[-1][2]

        for i in range(len(cars)-2, -1, -1):
            if cars[i][2] > lead:
                lead = cars[i][2]
                fleets += 1

        return fleets

        
        