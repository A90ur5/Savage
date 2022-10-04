class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        #cars = [0] * len(position)
        #for i in range(len(position)):
        #    cars[i] = (position[i], speed[i])
        #cars = [(p,s) for p, s in zip(position, speed)]
        cars = list(zip(position, speed))
        cars.sort(key=lambda x : x[0],reverse=True)
        
        car_fleet_head_arrive_time = float("-inf")
        car_fleet_count = 0

        for car in cars:
            arrive_time = (target - car[0]) / car[1]
            if arrive_time > car_fleet_head_arrive_time:
                car_fleet_head_arrive_time = arrive_time
                car_fleet_count += 1

        return car_fleet_count


if __name__ == '__main__':
    ans = Solution()
    testData1 = [0,2,4]
    testData2 = [4,2,1]
    print(ans.carFleet(100, testData1, testData2))