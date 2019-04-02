from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    # Mapping: int day to string
    # ToDo: Language Support
    int_day_to_str_mapping = {
        1: "Montag",
        2: "Dienstag",
        3: "Mittwoch",
        4: "Donnerstag",
        5: "Freitag",
        6: "Samstag",
        7: "Sonntag"
    }

    # get str day from int day and day mapping
    # ToDo: Language Support (might be better as a django model)
    def int_day_to_str(day, int_day_to_str_mapping):
        if day in int_day_to_str_mapping:
            return int_day_to_str_mapping[day]
        else:
            return "Unknown Day"

    # days as int in range(1,7)
    day_choices = [(str(i), i) for i in range(1,7)]
    day = models.IntegerField(default=0, choices=day_choices)
    # start_hour as int in range(0,23)
    hour_choices = [(str(i), i) for i in range(0,23)]
    start_hour = models.IntegerField(default=0, choices=hour_choices)
    # start_minute as int in range(0, 59)
    minute_choices = [(str(i), i) for i in range(0,59)]
    start_minute = models.IntegerField(default=0, choices=minute_choices)
    # link time slot to week
    # in case no week is linked, this is a virtual
    # time slot and repeated every week
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    # link to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # get string representation
    def __str__(self):
        day_str = self.int_day_to_str(self.day,self.int_day_to_str_mapping)
        return "%s - %s:%s" % (day_str, self.start_hour, self.start_minute)

    # is this a virtual time slot?
    def is_virtual():
        if week is None:
            return True
        else:
            return False

# Describes one week of a specific year
# Time Slots are linked to weeks
# ToDo:
# Logic for weeks spread over two years.
class Week(models.Model):
    # Years as int in range(2019, 2100):
    # - 2019 is the start year of the development
    # - 2100 is somewhere in the future (might be every other value)
    # I might be dead by 2100... or a cyborg!
    # In both cases i do no longer need sports.
    year_choices = [(str(i), i) for i in range(2019,2100)]
    year = models.IntegerField(default=0, choices=year_choices)
    # week of a year as int in range(1, 53)
    # (365 days / year) / (7 days / week )= 52.142... weeks / year
    week_choices = [(str(i), i) for i in range(1,53)]
    week_of_year = models.IntegerField(default=0, choices=week_choices)
    pass
    def __str__(self):
        return "%s - KW %s" % (year, week_of_year)
