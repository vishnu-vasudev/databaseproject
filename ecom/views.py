from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from data.models import Ajaxdata, Student
from .models import Product, Seller

# Create your views here.
def f1(request):
    return render(request, 'home1.html')

def seller(request):
    if request.method == 'POST':
        name = request.POST['s_name']
        email = request.POST['s_email']
        password = request.POST['s_password']
        obj1 = Seller(s_name = name, s_email = email, s_password = password)
        obj1.save()
    return render(request, 'seller-page.html')

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['seller-email']
        password = request.POST['seller-password']
        try:
            auth = Seller.objects.get(s_email = email, s_password = password)
            request.session['seller_id'] = auth.id
            return redirect('seller-home')
        except:
            msg = 'Invalid details'
    return render(request, 'seller-login.html', {'msg':msg})

def seller_home(request):
    if request.method == 'POST':
        name = request.POST['product-name']
        price = request.POST['product-price']
        image1 = request.FILES['product-image']
        logged_ob = Seller.objects.get(id = request.session['seller_id'])
        pdctobj = Product(pd_name = name, pd_price = price, pd_image = image1, seller_id = logged_ob)
        pdctobj.save()
    data = Product.objects.filter(seller_id = request.session['seller_id'])
    return render(request, 'seller-home.html', {'data' : data})

def pd_delete(request, id):
    Product.objects.get(id = id).delete()
    return redirect('seller-home')


@csrf_exempt
def tempurl(request):
    id = request.POST['id']
    data = Product.objects.get(id = id)
    json_data = [{"id":data.id, "name":data.pd_name, "price":data.pd_price}]
    return JsonResponse({"msg":json_data})

@csrf_exempt
def tempurl2(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        Product.objects.filter(id = id).update(pd_name = name, pd_price = price)
        return JsonResponse({"message":"Update Successful"})
    return render(request, 'seller-home.html')