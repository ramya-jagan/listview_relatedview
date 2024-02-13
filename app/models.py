from django.db import models

# Create your models here.
class School(models.Model):
  sname=models.CharField(max_length=50)
  sprincipal=models.CharField(max_length=50)
  slocation=models.CharField(max_length=50)

  def  get_absolute_url(self):
    return reverse('schooldetail',kwargs={'pk':self.pk}) 

  def __str__(self):
    return self.sname  


class Student(models.Model):
  stname=models.CharField(max_length=50)
  sage=models.CharField(max_length=50)
  sname=models.ForeignKey(School,on_delete=models.CASCADE, related_name='students')
  
