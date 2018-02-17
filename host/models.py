from django.db import models
from django.utils import timezone

class registration(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, default='')
    birthday = models.DateField()
    study = models.CharField(max_length = 3, choices = (('HS', 'Highscool'), ('MBO', 'MBO')))
    created_date = models.DateTimeField(default=timezone.now)
    registration_date = models.DateTimeField(blank=True, null=True)
                                        
    def registration(self):
        self.registration_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

#def study(self):
#self.study = (('HS', 'Highscool'), ('MBO', 'MBO'), ('HBO', 'HBO'), ('WO', 'WO'))
