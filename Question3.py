# Question 3 

height = float(input("Enter the initial height: "))
bounces = 0

while height >= 0.001:
    height = height * 0.60
    bounces = bounces + 1 

print("Total bounces:", bounces)