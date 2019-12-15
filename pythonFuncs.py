from itertools import chain
import Survey
#Filters a survey and prints to screen the corrected answers:
#old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):
    invalid_data = assertInvalidData(old_survey_path)
    mid_fixed = removeInvalidData(old_survey_path, invalid_data)
    lines_to_copy = countIdShow(mid_fixed)
    index_of_lines_to_copy = []
    for index, i in enumerate(lines_to_copy):
        if index % 2 == 0:
            index_of_lines_to_copy.append(i)
    with open("corrected_"+old_survey_path, "a+") as new_file, open(mid_fixed, "r") as old_file:
        lines = old_file.readlines()
        for k in index_of_lines_to_copy:
            new_file.write(lines[k])
    with open("corrected_"+old_survey_path, 'r') as final_file:
        content = final_file.read()
    print(content.rstrip('\n'))
    new_file.close()


def assertInvalidData(file_path):
    invalid_data = []
    with open(file_path,'r') as file:
        for index, line in enumerate(file):
            data = line.split(' ')
            grades = data[4:]
            if isValidData(data[0], data[2], grades) != 'GOODATA':
                invalid_data.append(index)
    file.close()
    return invalid_data


def removeInvalidData(file_path , list_of_invalid_lines):
    with open(file_path+"mid_fix", 'a+') as mid_fixed_file, open(file_path, 'r') as file:
        for index, line in enumerate(file):
            for invalid_data in list_of_invalid_lines:
                if index != invalid_data:
                    mid_fixed_file.write(line)
    mid_fixed_file.close()
    file.close()
    return file_path+"mid_fix"


def countIdShow(file_path):
    lines_to_copy = []
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            data = line.split(' ')
            if index not in lines_to_copy and data[0] not in lines_to_copy:
                lines_to_copy.append(index)
                lines_to_copy.append(data[0])
            if index not in lines_to_copy and data[0] in lines_to_copy:
                idx = lines_to_copy.index(data[0])
                lines_to_copy[idx-1] = index

    file.close()
    final_list=[*chain(*sorted(zip(lines_to_copy[::2], lines_to_copy[1::2]), key=lambda k:k[1]))]
    return final_list


def isValidData(id, age, grades):
   if len(id) != 8:
       return id
   if int(age) < 10 or int(age) > 100:
       return id
   for grade in grades:
       try:
            if int(grade) < 0 or int(grade) > 10:
                return id
       except ValueError:
            continue
   return 'GOODATA'
# ~~~~~~~~~~~~~~~~~~ Part1 DONE ~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~ Part2 ~~~~~~~~~~~~~~~~~~~~~


#Returns a new Survey item with the data of a new survey file:
#survey_path: The path to the survey
def scan_survey(survey_path):
    with open(survey_path, 'r') as file:
        new_survey = Survey.SurveyCreateSurvey()
        for line in file:
            data = line.split(' ')
            grades_array = list(filter(lambda x: x != '', data[4:]))
            grades_int = Survey.SurveyCreateIntAr(len(grades_array))
            for idx, score in enumerate(grades_array):
                Survey.SurveySetIntArIdxVal(grades_int, idx, int(score))
            if data[3] == 'Man':
                gender = True
            else:
                gender = False
            if data[1] == 'Vegan':
                habits = Survey.SURVEY_VEGAN
            elif data[1] == 'Vegaterian':
                habits = Survey.SURVEY_VEGATERIAN
            else:
                habits = Survey.SURVEY_OMNIVORE
            Survey.SurveyAddPerson(new_survey, int(data[0]), int(data[2]), gender, habits, grades_int)
    return new_survey


#Prints a python list containing the number of votes for each rating of a group according to the arguments
#s: the data of the Survey object
#choc_type: the number of the chocolate (between 0 and 4)
#gender: the gender of the group (string of "Man" or "Woman"
#min_age: the minimum age of the group (a number)
#max_age: the maximum age of the group (a number)
#eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
    if gender == 'Man':
        gender_bool = True
    else:
        gender_bool = False
    if eating_habits == 'Vegan':
        habits = Survey.SURVEY_VEGAN
    elif eating_habits == 'Vegeterian':
        habits = Survey.SURVEY_VEGATERIAN
    else:
        habits = Survey.SURVEY_OMNIVORE
    result = Survey.SurveyQuerySurvey(s, choc_type, gender_bool, min_age, max_age, habits)
    result_array=[]
    for i in range(10):
        result_array.append(Survey.SurveyGetIntArIdxVal(result, i))
    print(result_array)
    Survey.SurveyDestoryIntAr(result)


#Clears a Survey object data
#s: the data of the Survey object
def clear_survey(s):
    Survey.SurveyDestroySurvey(s)
