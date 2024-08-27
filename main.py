def calculateBMR(G,W,H,A):
    if G.lower() == "m":
        BMR1 = 10*W + 6.25*H - 5*A + 5
        BMR2 = 13.397*W + 4.799*H - 5.677*A + 88.362
        BMR = (BMR1+BMR2)/2
        return BMR
    elif G.lower() == "f":
        BMR1 = 10*W + 6.25*H - 5*A - 161
        BMR2 = 9.247*W + 3.098*H - 4.330*A + 447.593
        BMR = (BMR1+BMR2)/2
        return round(BMR)

def calculateCalories(BMR):
    return f"\nmaintenance calories:\n\nsedentary: {round(BMR*1.2)}\nlight exercise: {round(BMR*1.375)}\nmoderate exercise: {round(BMR*1.55)}\nheavy exercise: {round(BMR*1.725)}\nextreme exercise: {round(BMR*1.9)}"

#user input section

try:
    G = input("enter your Gender (m/f): ")
    W = float(input("enter your weight in KG: "))
    H = float(input("enter your height in CM: "))
    A = float(input("enter your age: "))
except:
    print("Error, Restart.")
    exit()

print("\n")

print(f"BMR: {(calculateBMR(G,W,H,A))} KCAL")

print(( calculateCalories(calculateBMR(G,W,H,A)))) 



