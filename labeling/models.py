from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20, null=True)
    member = models.ForeignKey(User)
    stateoption = (("Labeling","LABELING"),("Checking","CHECKING"),("Rechecking","RELABELING"),("Finish","FINISH"))
    state = models.CharField(max_length=20, choices=stateoption)
    class Meta:
        ordering = ['state']
    def __str__(self):
        return self.name
class Labeling(models.Model):
    """docstring for labeling."""
    project = models.ForeignKey(Project)
    choice = models.CharField(max_length=20,blank=True)
    image = models.ImageField(upload_to='photos/',blank=True,null=True)
    judge = models.BooleanField(default=False)
    comment = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.choice

class Group(models.Model):
    project = models.ForeignKey(Project)
    member = models.ManyToManyField(User)
    def __str__(self):
        return self.project.name
    # jason = models.CharField(max_length=20)
    # time = models.CharField(max_length=20)
    # projectname =  models.CharField(max_length=20)
    # def __str__(self):
    #     return self.name
