from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])  

    while queue:
        current_doc = queue.popleft()  
        if any(current_doc[0] < doc[0] for doc in queue):
            
            queue.append(current_doc)  
        else:
            answer += 1  
            if current_doc[1] == location:
                break  

    return answer

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    result = solution(priorities, location)
    print(f"priorities: {priorities}, location: {location}, 인쇄 순서: {result}")

    priorities = [1, 1, 9, 2, 3, 4]
    location = 1
    result = solution(priorities, location)
    print(f"priorities: {priorities}, location: {location}, 인쇄 순서: {result}")

    priorities = [1, 1, 2, 1, 1, 1]
    location = 0
    result = solution(priorities, location)
    print(f"priorities: {priorities}, location: {location}, 인쇄 순서: {result}")
