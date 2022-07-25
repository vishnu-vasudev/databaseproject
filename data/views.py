
from re import X
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import imp
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registration, Department, Student, Image, Ajaxdata, Staff_registration
from .forms import Registrationform
from .decorators import login_required

# Create your views here.
@csrf_exempt
def user(request):
    registrationform = Registrationform(request.POST)
    if request.method=='POST':
    #     name = request.POST['username']
    #     password = request.POST['password']
    #     user = Registration(name = name, password = password)
    #     user.save()
    #     return redirect('user')
        registrationform = Registrationform(request.POST)

        if registrationform.is_valid():
            registrationform.save()
        else:
            print(registrationform.errors)
    ob = Registration.objects.all()
    return render(request, 'base.html', {'registrationform':registrationform, 'ob':ob})

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
            request.session['stud_id'] =log.id     
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

@login_required
def homefn(request):
    data=Student.objects.get(id=request.session['stud_id'])
    return render(request, 'home.html', {'data':data})

def password(request):
    msg=''
    if request.method == 'POST':
        oldpwd = request.POST['cr-password']
        newpwd = request.POST['n-password']
        conpwd = request.POST['cn-password']
        ob = Student.objects.get(id = request.session['stud_id'])
        
        if ob.password == oldpwd:
            if newpwd == conpwd:
                ob.password = newpwd
                ob.save()
                msg = "Password changed"
            else:
                msg = "Password does not match"
        else:
            msg = "Password invalid"
    return render(request, 'upd-password.html', {'msg':msg})

def imgdisplay(request):
    if request.method == 'POST':
        pd_name = request.POST['pd-name']
        img = request.FILES['img']
        new = Image(pd_name = pd_name, image = img)
        new.save()
    obs = Image.objects.all()

    return render(request, 'img-display.html', {'obs':obs})
    
@csrf_exempt
def ajax(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        ajaxobj = Ajaxdata(name = name, email = email, phone = phone)
        ajaxobj.save()
        return JsonResponse({"message":"data inserted"})
    return render(request, 'ajax.html')

@csrf_exempt
def mailcheck(request):
    mail = request.POST['email']
    check = Ajaxdata.objects.filter(email = mail).exists()
    if check:
        return JsonResponse({"email":"Email already exists"})
    else:
        return JsonResponse({"email":"Email available"})

def ajax_display(request):
    return render(request, 'ajax-display.html')

def tempurl(request):
    data = Ajaxdata.objects.all()
    json_data = [{"id":i.id, "name":i.name, "email":i.email, "phone":i.phone}for i in data]
    return JsonResponse({"msg":json_data})

@csrf_exempt
def tempurl2(request):
    id = request.POST['id']
    Ajaxdata.objects.get(id = id).delete()
    return JsonResponse({"msg2":"Deleted"})

@csrf_exempt
def tempurl3(request):
    id = request.POST['id']
    data5 = Ajaxdata.objects.get(id = id)
    json_udata = [{"id":data5.id, "name":data5.name, "email":data5.email, "phone":data5.phone}]
    return JsonResponse({"msg5":json_udata})

@csrf_exempt
def tableupdate(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Ajaxdata.objects.filter(id = id).update(name = name, email = email, phone = phone)
        return JsonResponse({"message":"Update Successful"})
    return render(request, 'ajax-display.html')

@api_view(['POST'])
# @csrf_exempt
def staff(request):
    # data = r.json()
    staff_data = request.data
    st_obj = Staff_registration(st_name = staff_data['name'], st_contact = staff_data['contact'], st_email = staff_data['email'])
    st_obj.save()
    return Response('Staff registered!')

@api_view(['POST'])
def staff_display(request):
    staff_display_data = Staff_registration.objects.all()
    return Response({"staff_display_data":staff_display_data})
    
@api_view(['GET'])
def index(request):
    message = 'hi'
    return Response(message)
