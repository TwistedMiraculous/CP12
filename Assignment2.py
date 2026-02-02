def main():
    
    #Options
    
    print("--- Python Logic Tasks ---")
    print("1. Check Positive/Negative/Zero")
    print("2. Age Categorization")
    print("3. Grade Determiner")
    
    choice = input("\nSelect a task (1-3): ")

    # Positive, Negative, or Zero 
    if choice == '1':
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is Positive.")
        elif num < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")

    # Age Categories 
    elif choice == '2':
        age = int(input("Enter age: "))
        if age >= 60:
            print("Senior Citizen")
        elif age >= 18:
            print("Adult")
        elif age >= 13:
            print("Teenager")
        else:
            print("Try again")

    # Grading System 
    elif choice == '3':
        score = float(input("Enter student score: "))
        if score >= 90:
            print("Grade: A")
        elif score >= 70:
            print("Grade: B")
        elif score >= 60:
            print("Grade: C")
        else:
            print("Result: Failed")

    else:
        print("Invalid selection. Please run the code again.")

if __name__ == "__main__":
    main()