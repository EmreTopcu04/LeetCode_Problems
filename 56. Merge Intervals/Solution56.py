class Solution(object):
    def merge(self, intervals):

        intervals.sort(key = lambda interval: interval[0])
        list = []

        for interval in intervals:
            if not list or list[-1][1] < interval[0]:
                list.append(interval) 
            else:
                list[-1] = [list[-1][0], max(list[-1][1],interval[1])]

        return list
        

c = Solution()
print(c.merge([[1,3],[2,6],[8,10],[15,18]]))        