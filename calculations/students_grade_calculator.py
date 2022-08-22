'''
Given different scored marks of students, we need to find grades.
The test score is an average of the respective marks scored in assignments, tests and lab-works.
The final test score is assigned using below formula.
    10 % of marks scored from submission of Assignments
    70 % of marks scored from Test
    20 % of marks scored in Lab-Works
Grade will be calculated according to :
    1. score >= 90 : "A"
    2. score >= 80 : "B"
    3. score >= 70 : "C"
    4. score >= 60 : "D"
    5. Score < 60: "E"
Also, calculate the total class average and letter grade of class.
'''


class Score:
    '''
        Score Class for calculations
    '''
    assignment_weight = 0.10 # 10%
    test_weight = 0.70 # 70%
    lab_weight = 0.20 # 20%
    class_scores = []
    def __init__(self, student):
        self.student = student

    @staticmethod
    def grade(score):
        '''
            Calculate Grade of a Student
        '''
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "E"

    @staticmethod
    def average(marks):
        '''
            Calculate Average
        '''
        return sum(marks) / len(marks)

    def score(self):
        '''
            Calculate Score of a Student
        '''
        assignment_avg = Score.average(self.student.assignment)
        test_avg = Score.average(self.student.test)
        lab_avg = Score.average(self.student.lab)
        self.student.score = round(sum(
            [
                assignment_avg * self.assignment_weight,
                test_avg * self.test_weight,
                lab_avg * self.lab_weight
            ]
        ), 2)
        self.class_scores.append(self.student.score)

    def calculate_student_result(self):
        '''
            Calculate Result of a Student
        '''
        self.score()
        self.student.grade = Score.grade(self.student.score)

    @classmethod
    def calculate_class_result(cls):
        '''
            Calculate Average Score and Grade of Class
        '''
        cls.class_average = round(Score.average(cls.class_scores), 2)
        cls.class_grade = Score.grade(cls.class_average)


class Student(Score):
    '''
        Student class
    '''
    def __init__(self, name, assignment, test, lab):
        self.name = name
        self.assignment = assignment
        self.test = test
        self.lab = lab
        Score.__init__(self, self)
        self.calculate_student_result()

    def __str__(self):
        return f"""
            Student(
                "name" = {self.name},
                "assignment" = {self.assignment},
                "test" = {self.test},
                "lab" = {self.lab},
                "score" = {self.score},
                "grade" = {self.grade},
            )
        """


if __name__ == '__main__':
    students = [
        ["Jack Frost", [80, 50, 40, 20], [75, 75], [78.20, 77.20]],
        ['James Potter', [82, 56, 44, 30], [80, 80], [67.9, 78.72]],
        ['Dylan Rhodes', [77, 82, 23, 39], [78, 77], [80, 80]],
        ['Jessica Stone', [67, 55, 77, 21], [40, 50], [69, 44.56]],
        ['Tom Hanks', [29, 89, 60, 56], [65, 56], [50, 40.6]]
    ]

    for student1 in students:
        student1 = Student(*student1)
        print(f"{'':=<80}\nAverage marks of {student1.name} is : {student1.score}")
        print(f"Grade of {student1.name} is : {student1.grade}")

    Score.calculate_class_result()
    print(f"{'':=<80}\n\nAverage marks of class is : {student1.class_average}")
    print(f"Grade of class is : {student1.class_grade}\n\n{'':=<80}")
