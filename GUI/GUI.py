from functions import calculateBMR, calculateCalories
from tkinter import * 
from tkinter import StringVar
import tkinter as tk

root = tk.Tk()
root.title("BMR + calorie calculator")
root.geometry("500x600")
root.resizable(False, False)


def calculate():
    if dropdownGender.cget("text") == "male":
        gender = "m"
    else:
        genderq = "f"
    try:
        weight = float(weightEntry.get())
        height = float(heightEntry.get())
        age = int(ageEntry.get())
        
        BMR = calculateBMR(gender, weight, height, age)
        calories = calculateCalories(BMR)
        resultLabel.config(text=f"your BMR is {BMR}\n {calories}")
    except:
        resultLabel.config(text="please enter valid values")


titleLabel = Label(root, text="BMR + calorie calculator", font=("Helvetica", 30))
titleLabel.pack()


genderLabel = Label(root, text="please select your gender", font=("Helvetica", 18))
genderLabel.pack(pady=10)
genderOptions = ["male",'female']
dropdownGender = tk.OptionMenu(root, StringVar(), *genderOptions)
dropdownGender.pack()
dropdownGender.config(width=5, font=("Helvetica", 18), fg="black", bg="white")

weightLabel = Label(root, text="please enter your weight (kg)", font=("Helvetica", 18))
weightLabel.pack(pady=10)
weightEntry = Entry(root, font=("Helvetica", 18))
weightEntry.pack()

heightLabel = Label(root, text="please enter your height (cm)", font=("Helvetica", 18))
heightLabel.pack(pady=10)
heightEntry = Entry(root, font=("Helvetica", 18))
heightEntry.pack()

ageLabel = Label(root, text="please enter your age", font=("Helvetica", 18))
ageLabel.pack(pady=10)
ageEntry = Entry(root, font=("Helvetica", 18))
ageEntry.pack()

calculateButton = Button(root, text="calculate", font=("Helvetica", 18), command=calculate)
calculateButton.pack(pady=10)

resultLabel = Label(root, text="", font=("Helvetica", 18))
resultLabel.pack(pady=10)


root.mainloop()