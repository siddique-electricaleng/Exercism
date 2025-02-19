"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    int_scores = []
    for score in student_scores:
        int_scores.append(round(score))
    int_scores.sort()
    return int_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_numbers = 0
    for score in student_scores:
        if score <= 40:
            failed_numbers += 1

    return failed_numbers

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_number = []
    for score in student_scores:
        if score >= threshold:
            best_number.append(score)
    return best_number

# This was interesting, took some time to think up the algorithm with some testing

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_list =["A","B","C","D","F"]
    num_pass_grades = len(grade_list) - 1
    interval = ((highest - 40)/num_pass_grades)

    letter_grade = list()
    for grade in range(len(grade_list)-1):
        # print(grade)
        lower_bound = 41+interval*grade
        if (lower_bound) <= (highest-interval+1):
            letter_grade.append(int(lower_bound))
        else:
            break
    return letter_grade

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_List = list()
    for i in range(len(student_scores)):
        ranked_List.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranked_List 

student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']


# This was a bit interesting in the for statement
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student, score in student_info:
        if(score == 100):
            return [student,score]
        
    return []
