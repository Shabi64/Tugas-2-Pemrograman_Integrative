def main():
    grades = []
    
    # Take input grades until -1 is encountered
    while True:
        grade = input("Enter grade (-1 to end): ")
        if grade == '-1':
            break
        grades.append(int(grade))
    
    # Calculate average
    average = int(sum(grades) / len(grades)) if grades else 0
    
    # Output average
    print("Average:", average)
    
    # Output grades in the order they were entered
    for grade in grades:
        print(grade)


if __name__ == "__main__":
    main()
