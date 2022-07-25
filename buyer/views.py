from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Buyer
from .forms import Buyerform

@csrf_exempt
def buyer_signup(request):
    buyerform = Buyerform(request.POST)
    if request.method == 'POST':
        buyerform = Buyerform(request.POST)
        if buyerform.is_valid():
            buyerform.save()
        else:
            print(buyerform.errors)
    # obj = Buyer.objects.all()
    return render(request, 'buyer-signup.html', {'buyerform':buyerform})

@csrf_exempt
def byr_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            log = Buyer.objects.get(email = email, password = password)
            request.session['buyer-id'] = log.id
            msg = 1
            return JsonResponse({'msg':msg})
        except:
            msg = 0
            return JsonResponse({'msg':msg})
    return render(request, 'buyer-login.html')


def byr_home(request):
    return render(request, 'byr-home.html')

@csrf_exempt
def buyer_verify(request):
    email = request.POST['email']
    check = Buyer.objects.filter(email = email).exists()
    if check:
        message = ''
        return JsonResponse({'msg': message})
    else:
        message = "E-mail not registered"
        return JsonResponse({"msg":message})