student_score = input("Input a list of student score ").split(" ")
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
k = 0
for i in student_score:
       if i > k:
           k =i


print(k)