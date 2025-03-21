class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self,  lecturer, course, grade):
        # Выставляем оценки лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Реализует определение средней оценки, возвращает характеристики экземпляра и
        имеющиеся курсы"""
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}\n'
                  f'Курсы в процессе обучения: {courses_in_progress_string}\nЗавершенные курсы: {finished_courses_string}')
        return result

    def __lt__(self, other):
        """Реализуем сравнение студентов между собой по средней оценке"""
        if not isinstance(other, Student):
            print('Такое сравнение не корректно')
        return self.average_rating < other.average_rating



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """"Реализует определение средней оценки и возвращает характеристики экземпляра"""
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return result
    """Реализуем сравнение лекторов между собой по средней оценке"""
    def __lt__(self, other):
        if not (other,Lecturer):
            print('Такое сравнение не корректно')
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Выставляем оценки студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Возвращает характеристики экземпляра"""
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

# Создаем студентов и определяем для них изучаемые и завершенные курсы
best_student1 = Student('Dmitriy', 'Jagovdik', 'man')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Anna', 'Titova', 'woman')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

best_student3 = Student('Vladimir', 'Chervonny', 'man')
best_student3.courses_in_progress += ['Python']
best_student3.finished_courses += ['Введение в программирование']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer1 = Reviewer('Some', 'Buddy')
cool_reviewer1.courses_attached += ['Python']
cool_reviewer1.courses_attached += ['Git']

cool_reviewer2 = Reviewer('Alexandr', 'Ivanov')
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['Git']

# Создаем лекторов и закрепляем их за курсом
cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1  .courses_attached += ['Python']

cool_lecturer2 = Lecturer('Ivan', 'Popov')
cool_lecturer2.courses_attached += ['Git']

cool_lecturer3 = Lecturer('Evgeniy', 'Keller')
cool_lecturer3.courses_attached += ['Pithon']

# Выставляем оценки лекторам
best_student1.rate_hw(cool_lecturer1, 'Python', 8)
best_student1.rate_hw(cool_lecturer1, 'Python', 8)
best_student1.rate_hw(cool_lecturer1, 'Python', 9)

best_student2.rate_hw(cool_lecturer2, 'Git', 10)
best_student2.rate_hw(cool_lecturer2, 'Git', 8)
best_student2.rate_hw(cool_lecturer2, 'Git', 9)

best_student3.rate_hw(cool_lecturer3, 'Python', 9)
best_student3.rate_hw(cool_lecturer3, 'Python', 10)
best_student3.rate_hw(cool_lecturer3, 'Python', 9)

# Выставляем оценки студентам
cool_reviewer1.rate_hw(best_student1, 'Python', 7)
cool_reviewer1.rate_hw(best_student1, 'Python', 8)
cool_reviewer1.rate_hw(best_student1, 'Python', 7)

cool_reviewer2.rate_hw(best_student2, 'Git', 9)
cool_reviewer1.rate_hw(best_student2, 'Git', 10)
cool_reviewer2.rate_hw(best_student2, 'Git', 9)

cool_reviewer2.rate_hw(best_student3, 'Python', 7)
cool_reviewer2.rate_hw(best_student3, 'Python', 9)
cool_reviewer1.rate_hw(best_student3, 'Python', 10)
cool_reviewer2.rate_hw(best_student3, 'Python', 8)


# Выводим характеристики проверяющих
print(f'Перечень проверяющих:\n\n{cool_reviewer1}\n\n{cool_reviewer2}')
print()
print()

# Выводим характеристики и средней бал лекторов
print(f'Перечень лекторов:\n\n{cool_lecturer1}\n\n{cool_lecturer2}\n\n{cool_lecturer3}')
print()
print()

# Выводим характеристики, средний бал и курсы студентов
print(f'Перечень студентов:\n\n{best_student1}\n\n{best_student2}\n\n{best_student3}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам
print(f'Результат сравнения студентов: {best_student1.name} {best_student1.surname} < {best_student2.name} '
      f'{best_student2.surname} = {best_student1 < best_student2}')
print()

# Выводим результат сравнения лекторов по средним оценкам
print(f'Результат сравнения лекторов: {cool_lecturer1.name} {cool_lecturer1.surname} < {cool_lecturer2.name} '
      f'{cool_lecturer2.surname} = {cool_lecturer1 < cool_lecturer2}')
print()


# Создаем функцию для подсчета средней оценки студентов, за аргументы принимаем список студентов и название курса

student_list = [best_student1, best_student2, best_student3]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            sum_all += student.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки лекторов, за аргументы принимаем список лекторов и название курса

lecturer_list = [cool_lecturer1, cool_lecturer2, cool_lecturer3]

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lectures in lecturer_list:
        if lectures.courses_attached == [course_name]:
            sum_all += lectures.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим среднюю оценку студентов по данному курсу
print(f"Средняя оценка для всех студентов по курсу Python: {student_rating(student_list, 'Python')}")
print()

# Выводим среднюю оценку лекторов по данному курсу
print(f"Средняя оценка для всех лекторов по курсу Python: {lecturer_rating(lecturer_list, 'Python')}")
print()


