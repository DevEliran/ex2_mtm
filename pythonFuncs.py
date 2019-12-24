import Survey

ID_VALID_LEN = 8
MIN_AGE = 10
MAX_AGE = 100
MIN_SCORE = 1
MAX_SCORE = 10
NUM_OF_RATINGS = 10


#Filters a survey and prints to screen the corrected answers:
#old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):
    lines_to_copy = get_correct_lines(old_survey_path)
    with open("corrected_"+old_survey_path, "w") as new_file, open(old_survey_path, 'r') as old_file:
        old_file_lines = old_file.readlines()
        for k in lines_to_copy:
            index = k[1]
            new_file.write(old_file_lines[index])
    with open("corrected_"+old_survey_path, 'r') as final_file:
        content = final_file.read()
    final_file.close()
    print(content.rstrip('\n'))


def get_correct_lines(file_path):
    lines_to_copy = {}
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            data = line.split()
            if isValidData(data[0], data[2], data[4:]):
                lines_to_copy[data[0]] = index

    file.close()
    final_list = sorted(lines_to_copy.items(), key=lambda k: k[0])
    return final_list


def isValidData(id, age, grades):
   if len(id) != ID_VALID_LEN:
       return False
   if int(age) < MIN_AGE or int(age) > MAX_AGE:
       return False
   for i in grades:
        if int(i) < MIN_SCORE or int(i) > MAX_SCORE:
            return False
   return True

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
            elif data[1] == 'Vegetarian':
                habits = Survey.SURVEY_VEGATERIAN
            else:
                habits = Survey.SURVEY_OMNIVORE
            Survey.SurveyAddPerson(new_survey, int(data[0]), int(data[2]),
                                   gender, habits, grades_int)
            Survey.SurveyDestoryIntAr(grades_int)
    return new_survey


#Prints a python list containing the number of votes for each rating of
# a group according to the arguments
#s: the data of the Survey object
#choc_type: the number of the chocolate (between 0 and 4)
#gender: the gender of the group (string of "Man" or "Woman"
#min_age: the minimum age of the group (a number)
#max_age: the maximum age of the group (a number)
#eating_habits: the eating habits of the group (string of "Omnivore",
# "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
    if gender == 'Man':
        gender_bool = True
    else:
        gender_bool = False
    if eating_habits == 'Vegan':
        habits = Survey.SURVEY_VEGAN
    elif eating_habits == 'Vegetarian':
        habits = Survey.SURVEY_VEGATERIAN
    else:
        habits = Survey.SURVEY_OMNIVORE
    result = Survey.SurveyQuerySurvey(s, choc_type, gender_bool, min_age,
                                      max_age, habits)
    result_array=[]
    for i in range(NUM_OF_RATINGS):
        result_array.append(Survey.SurveyGetIntArIdxVal(result, i))
    print(result_array)
    Survey.SurveyDestoryIntAr(result)


#Clears a Survey object data
#s: the data of the Survey object
def clear_survey(s):
    Survey.SurveyDestroySurvey(s)
