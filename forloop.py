student_height = input("Input a list of student heights ").split(" ")
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

count = 0
sum = 0
for height in student_height:
    count += 1
    sum += height
average =  round(sum/count)
print(average)


