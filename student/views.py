from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchEnroll')
    if searchTerm:
        students = Student.objects.filter(enroll__icontains = searchTerm)
    else:
        students = Student.objects.all().order_by('roll')
    return render(request,'home.html',{'searchTerm':searchTerm,'students':students})

@login_required
def detail(request,student_id):
    students =  get_object_or_404(Student, pk = student_id)
    if request.user.groups.filter(name='faculty').exists():
        return render(request,'detail.html',{'students':students,'is_faculty': True})
    if hasattr(request.user,'student_profile') and students.user == request.user:
        return render(request,'detail.html',{'students':students,'is_faculty': False})
    
    return render(request,'detail.html',{'error': 'You Do Not Have Permission To View This Page'})


@login_required
def delete_student(request,student_id):
    if not request.user.groups.filter(name='faculty').exists():
        return HttpResponseForbidden('You Do Not Have Delete Student 😖')
    students =  get_object_or_404(Student, pk = student_id)
    if request.method == 'POST':
        students.delete()
        return redirect('home')
    return render(request,'delete_student.html',{'students':students})


class MarksForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['python','fsd','coa']

@login_required
def edit_marks(request,student_id):
    if not request.user.groups.filter(name='faculty').exists():
        return HttpResponseForbidden('You Do Not Have Access To Edit Marks 😖')
    else:
        students =  get_object_or_404(Student, pk = student_id)
        if request.method == 'POST':
            form = MarksForm(request.POST, instance=students)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('detail',args=[student_id]))
        else:
            form = MarksForm(instance=students)
        return render(request,'edit_marks.html',{'form':form,'students':students})