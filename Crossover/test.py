import random
rand = random.Random()
rand.seed(None)

a = [5,6,7,8]
b = [9,10,11,12]
c = [13,14,15,16]
d = [17,18,19,20]

e = [a,b,c,d]

ar = 0
br = 1
i = 0

print (len(e))

while i < len(e):

    randompoint = rand.randint(0, (len(e[i])))
    print(randompoint)

    zw = e[ar][0:randompoint]
    e[ar][0:randompoint] = e[br][0:randompoint]
    e[br][0:randompoint] = zw

    ar = ar + 2
    br = br + 2
    i = i + 2

print(e[0])
print(e[1])
print(e[2])
print(e[3])