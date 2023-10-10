
def solution(k, d):
    def count(x):
        # x, y는 k의 배수, d를 넘지 않음
        # y <= math.sqrt(d**2 - x**2) 까지의 개수
        y = (d**2 - (x)**2)
        y = int(y ** (1/2))
        return (y // k) + 1

    return sum(count(x) for x in range(0, d+1, k))


print('ans: ', solution(1, 5))