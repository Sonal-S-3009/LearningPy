height, weight  = list(map(int,input("Please enter your Height (cm) and Weight (kg).").split(" ")))
bmi =   weight/((height*0.01)**2)
print("BMI :", bmi)