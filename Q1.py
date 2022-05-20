from math import sqrt


def multiplicativeCongruentialMethod(m, a, randumNumber_p):

    return (randumNumber_p * a) % m


# ----------* variable inititialization *-------------------------
inital_postion = [0, 0]
m = 16381
a = 572
random_seed = 6
random_number = multiplicativeCongruentialMethod(m, a, random_seed)

# --------------* a list to store the distance of each run *-------------------
distance_square_of_each_run = [0] * 500


# --------------* loop *---------------------------
for n in range(500):
    inital_postion = [0, 0]
    for i in range(200):
        random_number = multiplicativeCongruentialMethod(m, a, random_number)
        k = random_number

        if k % 4 == 0:
            inital_postion[0] = inital_postion[0] + 1

        if k % 4 == 1:
            inital_postion[0] = inital_postion[0] - 1

        if k % 4 == 2:
            inital_postion[1] = inital_postion[1] + 1

        if k % 4 == 3:
            inital_postion[1] = inital_postion[1] - 1

    distance_square_of_each_run[n] = inital_postion[0] ** 2 + inital_postion[1] ** 2

    # print(inital_postion)

# print(distance_square_of_each_run)
sum = 0

for distn in distance_square_of_each_run:
    sum += distn

average = sum / 500

print("Aveage: ", average)
print("Squrt of Average: ", sqrt(average))
print("squr of 200 : ", sqrt(200))

# -----------------* OUTPUT *---------------------------
# Aveage:  213.996
# Squrt of Average:  14.628602120503517
# squr of 200 :  14.142135623730951
