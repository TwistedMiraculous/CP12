def main():
    print("--- Python Logic Tasks ---")
    print("1. Mood Checker")
    print("2. Subject's impact")
    print("3. What do you feel like doing")
    
    choice = input("\nSelect a task (1-3): ")

    # Task 1: Mood checker 
    if choice == '1':
        # .capitalize() makes "bad" become "Bad" automatically
        mood = input("How was your school day? ").capitalize()
        if mood == "Great":
            print("That is nice to hear.")
        elif mood == "Bad":
            print("Don't worry it will get better.")
        elif mood == "Very bad":
            print("Try doing some meditation.")
        
    # Task 2: Subject impact (Changed from '1' to '2')
    elif choice == '2':
        subject = input("What subject is impacting you? ").capitalize()
        if subject == "Math":
            print("It's good to take breaks from time to time.")
        elif subject == "History":
            print("It is ok, some information probably wasn't meant to be.")

    # Task 3: Activity
    elif choice == '3':
        activity = input("What do you feel like doing? ").capitalize()
        if activity == "Nothing":
            print("Do something.")
        elif activity == "Sleeping":
            print("Wake up!")
        elif activity == "Working":
            print("Good Job!")
        elif activity == "Studying":
            print("Einstein? I see...")
            
    # Error Handling
    else:
        print("Invalid selection. Please run the code again.")

if __name__ == "__main__":
    main()