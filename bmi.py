def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*2)
    print(bmi)
    return bmi

def  check_bmi(bmi_value):
    if(bmi_value<18.5):
        print("You are underweight")
        return -1
    elif(bmi_value > 18.5 and bmi_value < 25.0):
        print("You got Normal weight")
        return 0
    elif(bmi_value > 25.0):
        print("You are overweight")
        return 1
def main():
    bmi_value = calculate_bmi(1.75, 70)
    print("Calculated BMI:" + str(bmi_value))

if __name__ == "__main__":
    main()