def gradingStudents(grades):
    
    for i in grades:
        if i >= 38:
            temp = i % 5
            if temp >= 3:
                print(i + (5-temp))
            else:
                print(i)
        
        else:
            print(i)
            

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

gradingStudents(grades)
