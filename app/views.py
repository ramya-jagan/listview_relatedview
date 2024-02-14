from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from app.models import *
from django.urls import reverse_lazy
# Create your views here.
class SchoolList(ListView):
   model=School
   context_object_name='schools'
   ordering=['sname']
  # queryset=School.objects.filter(id=1)
  # template_name=app/School_list.html


class SchoolDetail(DetailView):
   model=School
   context_object_name='sclobject' 


   
class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model = School
    context_object_name='schlobject'
    success_url=reverse_lazy('SchoolList')
  