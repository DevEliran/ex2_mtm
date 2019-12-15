%module Survey
%{
 #include "Survey.h"
 #define SURVEY_VEGAN 0
#define SURVEY_VEGATERIAN 1
#define SURVEY_OMNIVORE 2
Survey SurveyCreateSurvey();
SurveyReturnValue SurveyAddPerson(Survey Survey, int Id, int Age, bool Gender, int EatingHabits , int* Scores);
int* SurveyQuerySurvey(Survey survey, int ChocolateType, bool Gender, int AgeMin, int AgeMax, int EatingHabits);
void SurveyQueryDestroy(int* histogram);
void SurveyDestroySurvey(Survey survey);
int* SurveyCreateIntAr(unsigned int size);
void SurveyDestoryIntAr(int* ar);
void SurveySetIntArIdxVal (int* ar, unsigned int idx, int val);
int SurveyGetIntArIdxVal(int* ar, unsigned int idx);
%}

typedef enum { SURVEY_ALLOCATION_FAILED, SURVEY_SUCCESS} SurveyReturnValue;

typedef struct survey_t* Survey;
#define SURVEY_VEGAN 0
#define SURVEY_VEGATERIAN 1
#define SURVEY_OMNIVORE 2
Survey SurveyCreateSurvey();
SurveyReturnValue SurveyAddPerson(Survey Survey, int Id, int Age, bool Gender, int EatingHabits , int* Scores);
int* SurveyQuerySurvey(Survey survey, int ChocolateType, bool Gender, int AgeMin, int AgeMax, int EatingHabits);
void SurveyQueryDestroy(int* histogram);
void SurveyDestroySurvey(Survey survey);
int* SurveyCreateIntAr(unsigned int size);
void SurveyDestoryIntAr(int* ar);
void SurveySetIntArIdxVal (int* ar, unsigned int idx, int val);
int SurveyGetIntArIdxVal(int* ar, unsigned int idx);

