import random
rand = random.Random()
rand.seed(None)

a = [5,6,7,8]
b = [9,10,11,12]

c = [a,b]

randompoint = rand.randint(0, (len(c[0])))

print(c[0])
print(randompoint)
print(c[0][0:randompoint])

zw = c[0][0:randompoint]
c[0][0:randompoint]=c[1][0:randompoint]
c[1][0:randompoint]= zw

print(c[0])
print(c[1])
