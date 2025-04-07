def num_strong_teams(num_students, str_crit, *student_skills) -> int:
    asc_skill_sort = list(student_skills)
    asc_skill_sort.sort(reverse = True)
    str_teams = 0
    team_members = 1
    temp_student = list()
    for student_skill in asc_skill_sort:
        temp_student = temp_student.append(student_skill)
        if (student_skill*team_members >= str_crit):
            team_members = 1
            str_teams += 1
            asc_skill_sort.pop(0)
    
a = num_strong_teams(6, 4, 4, 5, 3, 3, 2, 6)
print(a)