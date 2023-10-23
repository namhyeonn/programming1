from collections import deque

def solution(prices):
    n = len(prices)
    result = [0] * n  

    stack = deque()  
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  
            result[j] = i - j

        stack.append(i)

    for i in stack:
        result[i] = n - 1 - i

    return result

if __name__ == "__main__":
    prices = [1000, 2000, 3000, 2000, 3000]
    result = solution(prices)
    print(f"prices: {prices}, result: {result}")
