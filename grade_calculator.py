student_name = input("Enter student name: ")

math_marks = int(input("Enter Math marks: "))
english_marks = int(input("Enter English marks: "))
python_marks = int(input("Enter Python marks: "))
avg_marks = (math_marks + english_marks + python_marks) / 3

if((math_marks<0 or math_marks > 100) or  (english_marks<0 or english_marks > 100) or (python_marks<0 or python_marks > 100)):
    print("Invalid Marks")
