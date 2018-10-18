#how to remove the duplicates elmts from a list and print in the same sequence order.
l1 =[66,68,65,68,66,90,76,69,70,75]
l2=list(set(l1))
print(l2)
l2.sort(key=l1.index)
print(l2)

