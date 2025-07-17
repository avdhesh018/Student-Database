from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_profile',null=True,blank=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    enroll = models.CharField(max_length=14,unique=True)
    photo = models.ImageField(upload_to='student/images')
    url = models.URLField(blank=True)
    email = models.EmailField()
    desc = models.TextField()

    python = models.IntegerField(default=0)
    fsd = models.IntegerField(default=0)
    coa = models.IntegerField(default=0)

    def __str__(self):
        return self.name
