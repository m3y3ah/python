if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    for student_name , student_score in sorted(students) :
        if student_score == sorted(list(set([x[1] for x in students])))[1] :
            print(student_name)