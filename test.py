newspapers={"TOI":[3,3,3,3,3,5,6],
"Hindu":[2.5,2.5,2.5,2.5,2.5,4,4],
"ET":[4,4,4,4,4,4,10],
"BM":[1.5,1.5,1.5,1.5,1.5,1.5,1.5],
"HT":[2,2,2,2,2,4,4]}

#Budget=input(int)

new={}
l=[]
for y in newspapers.values():
    l.append(sum(y))
for x in newspapers.keys():
    for i in l:
        new={x:i}
        l.remove(i)
        break

def find(l,n,r):
        

    