from genericpath import exists
 
import imp
from django.shortcuts import render,redirect
from .models import Registration, Department, Student

# Create your views here.
def user(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = Registration(name = name, password = password)
        user.save()
        return redirect('user')
    details = Registration.objects.all()
    return render(request, 'base.html', {'details':details})

def dptfn(request):
    if request.method == 'POST':
        name = request.POST['dep-name']
        obj = Department(dpt_name = name)
        obj.save()
    return render(request, 'trial.html')

def delete(request, id):
    Registration.objects.get(id=id).delete()
    return redirect('user')

def update(request, id):
    if request.method == 'POST':
        name = request.POST['upd-username']
        password = request.POST['upd-password']
        Registration.objects.filter(id = id).update(name = name, password = password)
        return redirect('user')
    get_data = Registration.objects.get(id=id)
    return render(request, 'update.html', {'get_data':get_data})

def studentfn(request):
    if request.method == 'POST':
        name = request.POST['student-name']
        place = request.POST['student-place']
        dept_id = request.POST['student-dpt']
        dob = request.POST['dob']
        username = request.POST['user-name']
        password = request.POST['pass-word']
        obj2 = Student(stud_name = name, stud_place = place, stud_dept_id = dept_id, dob = dob, username = username, password = password)
        obj2.save()
    
    dpt_details = Department.objects.all().distinct('dpt_name')
    det = Student.objects.all()
    return render(request, 'student.html', {'dpt_details':dpt_details, 'det':det})

def st_delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect('student')

def loginfn(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username1']
        password = request.POST['password1']
        try:
            log = Student.objects.get(username = username, password = password)
            return redirect('home')
        except:
            msg = 'Invalid data'

        # log = Student.objects.filter(username = username, password = password).exists()
        # print(log)
        # if log:
        #     return redirect('home')
        # else:
        #     msg = 'Invalid data'
    return render(request, 'login.html', {'msg':msg})

def homefn(request):
    return render(request, 'home.html')