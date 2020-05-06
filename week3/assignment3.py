def compute_min_refills(distance, tank, stops):
    # write your code here
    # stops is an array
    num = 0
    i=0
    discovered = 0
    for i in range(0,len(stops)-1):
        if stops[i] <= tank :
                discovered = stops[i]
                num += 1
                if discovered + tank > distance:
                    num += 1
                    continue
        elif stops[i+1] - stops[i] > tank:
                num=-1
        elif distance - stops[len(stops)-1] > tank:
                num=-1

    return num

if __name__ == '__main__':
    distance = int(input())
    tank = int(input())
    stops = []
    for i in input().split(""):
        stops.append(int(i))
    print(compute_min_refills(700,200,[100,200,300,400]))
    #print(compute_min_refills(950, 400, [200,375,550,750]))
    #print(compute_min_refills(700, 200, [100,200,300,400]))
