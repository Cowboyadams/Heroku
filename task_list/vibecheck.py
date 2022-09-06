
# Variables that you can work with:
#   User_local (local City)(string)
#   is_day (if it is day) (int, either 1 for true or 0 for false)
#   cloud_percent (the number of percentage of cloud coverage) (int)
#   rain (current rain precipitation in inch) (float)
#   user_date (current date and time of user) (str, format is as follows:  Year-mt-day hr:min)
#   uv (uv rating) (1-2 = low, 3-5 = moderate, 6-9 = high, 10+ = extreme)
#
# Input variable formating:
#   ['city', 'date and time', is_day, cloud_coverage, Rainfall, uv]
#      0             1          2            4            5      6



# Decides what the current vibe is
def vibecheck(info):
    if info[4] > 0.01:
        answer_vibe = 4
        return(answer_vibe)
    elif info[3] > 40:
        answer_vibe = 1
        return(answer_vibe)
    else:
        answer_vibe = 2
        return(answer_vibe)

