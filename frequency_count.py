a = [1,2,2,3,1,4,3,3]

freq = {}

# for item,value in enumerate(a):
#     freq[value] = freq.get(value,0) + 1
#     # print(item,value)

for i in a:
    freq[i] = freq.get(i,0) + 1
freq['age']    
print(freq)
