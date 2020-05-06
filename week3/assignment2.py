# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0000 #final weights
    result = 0 #should be full capacity
    tmp = [];
    # write your code here
    for i in range(0,len(weights)):
        #if values[i] == capacity:
        #    tmp.append(weights[i]);
        if values[i]< capacity:
            value += weights[i]
            result += values[i]
            if result >= capacity:
                    tmp.append(value)
        elif values[i] == capacity :
            tmp.append(weights[i])
            continue
        elif values[i] > capacity:
            value = capacity/values[i] * weights[i]
    #print(tmp)
    return value


if __name__ == "__main__":
    """
    data = [[60,20],[100,50],[120,30]]
    n, capacity = 3,50
    weights = [60,100,120]
    values = [20,50,30]
    """
    weights = []
    values = []
    str = input().split(" ")
    n, capacity = int(str[0]),int(str[1])
    for i in input().split(" "):
        weights.append(int(i))

    for j in input().split(" "):
        values.append(int(j))
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
