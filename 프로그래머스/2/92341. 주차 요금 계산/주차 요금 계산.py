import math
def solution(fees, records):   
    # 차량: [입차 시간, 출차 시간]
    cars = {record[6:10] : [] for record in records}
    result = {record[6:10] : 0 for record in records}
    
    # IN이 나온 후 OUT이 나오면 배열 비우기
    # IN만 있고 OUT안나오면 배열 안 비움
    for record in records:
        time, car, inOut = record.split(' ')
        
        cars[car].append(time)
        if inOut == 'OUT':
            # print(car, cars[car])
            result[car] += calcParkingTime(cars[car])
            cars[car] = []

    for car, times in cars.items():
        result[car] += calcParkingTime(times)
    
    for car, parkingTime in result.items():
        result[car] = calcFee(parkingTime, fees)
        
    return [v for k, v in sorted(result.items())]

def calcParkingTime(times):
    # times: [inTime, outTime] | [inTime] | []
    
    # IN, OUT
    if len(times) == 2:
        inTime, outTime = times
        return (int(outTime[:2])*60+int(outTime[3:])) - (int(inTime[:2])*60+int(inTime[3:]))
    # only IN
    elif len(times) == 1:
        inTime = times[0]
        return (23*60+59) - (int(inTime[:2])*60+int(inTime[3:]))
    else:
        return 0    
    
def calcFee(parkingTime, fees):
    defaultTime, defaultFee, unitTime, unitFee = fees

    if parkingTime > defaultTime:
        return defaultFee + math.ceil((parkingTime-defaultTime)/unitTime) * unitFee
    else:
        return defaultFee