sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::-2])

cubes = [i**3 for i in range(13)]

print(cubes)

evens = [i * 2 for i in range(5)]

# print(evens)

evens = [i * 2 for i in range(5) if i**2 % 2 == 0]

# print(evens)

a = [i for i in range(20) if i% 3 ==0]

print(a)



