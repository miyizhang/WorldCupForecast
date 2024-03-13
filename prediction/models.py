from django.db import models

class MatchInfo(models.Model):
    match_date = models.CharField(max_length=50)
    match_time = models.CharField(max_length=50)  # Change TimeField to CharField
    team_a = models.CharField(max_length=50)
    team_b = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

    # def save(self, *args, **kwargs):
    #     if isinstance(self.match_time, str):
    #         # Assuming the time is already in 'HH:MM:SS' format, no need to format
    #         pass
    #     else:
    #         # Format the time to 'HH:MM:SS' before saving
    #         self.match_time = self.match_time.strftime('%H:%M:%S')
    #     super(MatchInfo, self).save(*args, **kwargs)
