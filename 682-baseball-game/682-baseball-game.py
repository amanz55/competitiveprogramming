class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records=[]
        for i in range(len(ops)):
            if ops[i].isdigit() or ops[i][0]=="-":
                records.append(int(ops[i]))
            elif ops[i]=="D":
                records.append(2*int(records[-1]))
            elif ops[i]=="+":
                records.append(int(records[-1])+int(records[-2]))
            elif ops[i]=="C":
                records.pop()
        return sum(records)
        