class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        size = len(position)
        cars = [(position[i], speed[i]) for i in range(size)]
        cars.sort(reverse = True)

        for i in range(size):
            if len(time) == 0:
                time.append((target - cars[i][0])/cars[i][1])
            else:
                curr_time = (target - cars[i][0])/cars[i][1]
                if curr_time > time[-1]:
                    # diff fleet
                    time.append((target - cars[i][0])/cars[i][1])

        return len(time)