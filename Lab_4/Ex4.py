# Try to append a tuple. It won't work.
# Kaili Takara
# Date: Sept 16, 2026

survey_respondents = (1012, 1035, 1021, 1053)
#survey_respondents.append(1054) # This will raise an AttributeError because tuples are immutable

survery_respondents = survey_respondents + (1054,) # This creates a new tuple with the additional value
print("Updated survey respondents:", survey_respondents)