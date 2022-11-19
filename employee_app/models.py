from django.db import models



class Language(models.Model):

    programming_lang= models.CharField(max_length=50)

    def __str__(self):
        return self.programming_lang

class Employee_database(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    employee_id= models.IntegerField()
    designation= models.CharField(max_length=50)
    lang= models.ForeignKey(Language, on_delete= models.CASCADE)

    def __str__(self):
        return self.name