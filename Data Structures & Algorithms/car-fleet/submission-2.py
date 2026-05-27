class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s, (target - p) / s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0])

        arrivals = [cars[-1][2]]

        for i in range(len(cars)-2, -1, -1):
            if cars[i][2] > arrivals[-1]:
                arrivals.append(cars[i][2])

        return len(arrivals)

        
        