# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.
#
# For example, Penny drinks the third can of cola and the queue will look like this:
#
# Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
# Write a program that will return the name of the person who will drink the n-th cola.
#
# Input
# The input data consist of an array which contains at least 1 name, and single integer n which may go as high as the biggest number your language of choice supports (if there's such limit, of course).
#
# Output / Examples
# Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.
def who_is_next(names, r):
    if len(names)>= r:
        return names[r-1]
    way= 5
    step=1
    while r:
        if (way+ (pow(2,step))* 5) >= r:
            for i in range(5):
                way+=pow(2,step)
                if  way >= r:
                    return names[i]
        else:
            step+=1
            way=way+ (pow(2,step-1))* 5

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

print(who_is_next(names, 1))#, "Sheldon")
print(who_is_next(names, 52))#, "Penny")
print(who_is_next(names, 7230702951))#, "Leonard")