from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dic = {}
        apper = 0
        tmp = 0
        for i in range(1, N+1):
            dic[i] = []

        for m,n in trust:
            dic.setdefault(m,[]).append(n)
        print(dic)

        for k, v in dic.items():
            if not v:
                tmp = k

        if tmp ==0 :
            return -1
        else:
            for j in dic.values():
                if tmp in j:
                    apper += 1

            if apper == N - 1:
                return tmp
            else:
                return -1


if __name__ == "__main__":
        test = [[1,2],[2,3],[3,1]]
        print(Solution.findJudge(Solution, 3, test))