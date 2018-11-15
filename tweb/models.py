from django.db import models

# Create your models here.
class Company(models.Model):
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    tel = models.CharField(max_length=15,blank=True)


class StudentManager(models.Manager):
    def create_student(self, name):
        #方式二
        student = self.create(name=name)
        return student
        #方式一
        # student = Student(name = 'xjz52')
        # student.save()

class Classes(models.Model):
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    name =models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey('Classes',on_delete=models.CASCADE)


