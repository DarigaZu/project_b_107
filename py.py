class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  

    def delete_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.delete_student(self)  

    def view_courses(self):
        return [course.course_name for course in self.courses]       

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.students = []                

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def delete_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def view_students(self):
        return [student.name for student in self.students]    

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def reg_student(self, name, student_id):
        new_student = Student(name, student_id)
        self.students.append(new_student)    
        print(f'Студент {name} зарегистрирован!')

    def create_course(self, course_name, course_id):
        new_course = Course(course_name, course_id)
        self.courses.append(new_course)    
        print(f'Курс {course_name} создан!')

    def enroll_student(self, student_id, course_id):
        student_found = False 
        course_found = False  
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                for course in self.courses:
                    if course.course_id == course_id:
                        course_found = True
                        student.add_course(course)
                        print(f'{student.name} записан на курс {course.course_name}')
                        return
        
        if not student_found or not course_found: 
            print('Студент или курс не найдены.')

    def drop_student(self, student_id, course_id):
        student_found = False  
        course_found = False   
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                for course in self.courses:
                    if course.course_id == course_id:
                        course_found = True
                        student.delete_course(course)
                        print(f'{student.name} удален с курса {course.course_name}')
                        return
        
        if not student_found or not course_found: 
            print('Студент или курс не найдены.')


school = School()                   
school.reg_student('Dariga', 1)
school.reg_student('Mary', 2)
school.reg_student('Ruby', 3)

school.create_course('JavaScript', 10)
school.create_course('Python', 11)
school.create_course('Java', 12)

school.enroll_student(1, 10)  
school.enroll_student(2, 11) 
school.enroll_student(3, 12)
school.enroll_student(3, 10) 

print("Студенты на курсе JavaScript:", school.courses[0].view_students())   
print("Курсы Mary:", school.students[1].view_courses())   
print("Курсы Ruby:", school.students[2].view_courses())   
