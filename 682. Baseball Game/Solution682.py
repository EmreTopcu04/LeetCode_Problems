class Solution(object):
    def calPoints(self, operations:list):
        record = []
        while len(operations) > 0:
            s:str = operations[0]
            if s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
                record.append(int(s))
            else:
                if s == "+":
                    record.append(int(record[-1]) + int(record[-2]))
                elif s == "D":
                    record.append(int(record[-1])*2)
                else:
                    record.pop()

            operations = operations[1:]

        total = 0

        for num in record:
            total += num

        return total
        


c = Solution()

print(c.calPoints(["5","-2","4","C","D","9","+","+"]))