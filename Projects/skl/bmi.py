'''def test2(gr):
    if gr >= 90:
        return "A"
    elif gr >= 70:
        return "B"
    elif gr >= 50:
        return "C"
    else:
        return "F"
grade  = input("Please enter your grade to receive your lettered score: ")
print (test2(grade))'''


def class_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "Obesity class 1"
    elif bmi < 39.09:
        return "Obesity class 2"
    else:
        return "Extreme Obesity Class 3"
    
weight = float(input("Let me know your weight and I will tell you your Weight Class: "))
print(f"Your weight class is ", (class_bmi(weight)))

