from itertools import product



def maximize_expression(K, M, lists):
    squared_lists = [[x**2 for x in l] for l in lists]
    
    combined = product(*squared_lists)
    
    result = 0
    for c in combined:
        temp = sum(c) % M
        result = max(result, temp)
    
    return result



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
