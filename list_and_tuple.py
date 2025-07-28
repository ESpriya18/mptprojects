my_list=[1,2,3,4]
my_tuple=(100,300,500)
print("original list:",my_list)
print("Original tuple:",my_tuple)
my_list.append(5)
print("changed list:",my_list)
try:
    my_tuple[0]=600
except TypeError as e:
    print("Error  in modifying tuple:",e)
