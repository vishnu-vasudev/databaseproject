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
        obj2 = Student(stud_name = name, stud_place = place, stud_dept_id = dept_id, dob = dob)
        obj2.save()
    
    dpt_details = Department.objects.all().distinct('dpt_name')
    det = Student.objects.all()
    return render(request, 'student.html', {'dpt_details':dpt_details, 'det':det})

def st_delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect('student')

def loginfn(request):
    return render(request, 'login.html')