# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import datetime as dt
import math

def solution(fees, records):
    # 누적 주차시간 계산
    enters = {}
    parks = defaultdict(int)
    for r in records:
        time, car, type = r.split()
        time = dt.datetime.strptime(time, "%H:%M")
        
        if type == 'IN':
            enters[car] = time
        else:
            parks[car] += (time - enters[car]).seconds // 60
            del enters[car]
    
    for car, enter in enters.items():
        leave = dt.datetime.strptime('23:59', "%H:%M")
        parks[car] += (leave - enter).seconds // 60
    
    # 주차요금 계산
    answer = []
    for car, time in sorted(parks.items()):
        over = time - fees[0]
        if over < 0:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil(over / fees[2]) * fees[3]
            answer.append(fee)
    
    return answer
    
# fees = [180, 5000, 10, 600] # 기본시간, 기본요금, 단위시간(분), 단위요금
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = 	[1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))