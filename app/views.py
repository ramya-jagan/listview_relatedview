from django.shortcuts import render
from django.views.generic import ListView,DetailView

from app.models import *

# Create your views here.
class SchoolList(ListView):
   model=School
   context_object_name='Schools'
   ordering=['sname']
  # queryset=School.objects.filter(id=1)
  # template_name=app/School_list.html


class SchoolDetail(DetailView):
   model=School
   context_object_name='sclobject' 


   
