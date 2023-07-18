from django.shortcuts import render, redirect
from .models import Register, Purchase
from admins.models import Products
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request,'PRODUCTS.html')
def lap(request):
    return render(request,'laptops.html')
def mob(request):
    return render(request,'mobiles.html')
def tabs(request):
    return render(request,'tabs.html')
def watch(request):
    return render(request,'watches.html')

def buy(request):
    return render(request,'buy.html')





def contact(request):
    return render(request,'contact.html')

def reg(request):
    if request.method == 'POST':
        try:
            cname = request.POST.get('cname')
            cemail = request.POST.get('cemail')
            password = request.POST.get('password')
            mno = request.POST.get('mno')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')

            data = Register(
                cname=cname,
                cemail=cemail,
                paw=password,
                mno=mno,
                addr=address,
                pincode=pincode,

            )
            data.save()
            return render(request, 'login.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = Register.objects.get(cemail=email, paw=password)
            request.session['userid'] = data.cemail
            print(data)
            return render(request, 'home.html')
        except Exception as e:
            print("Exception is e:", e)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def pro(request):
    try:
        uid = request.session['userid']
        print(uid)
        data = Register.objects.get(cemail=uid)
        return render(request, 'profile.html', {'profile': [data]})
    except Exception as e:
        print("Exception is:", e)
        return render(request, 'home.html')


def uvproducts(request):
    data = Products.objects.all()
    return render(request, 'uproducts.html', {'products': data})


def buy_product(request, id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid = Register.objects.get(cemail=uid)
        id1 = cid.id
        products = Products.objects.get(id=id)
        data = Purchase(
            pname=products.pname,
            pcat=products.pcat,
            pcost=products.pcost,
            pquality=products.pquality,
            pdec=products.pdec,
            cid_id=id1,
            pid_id=id,
        )
        data.save()
        messages.success(request, '..Product Purchased Successfully')
        return render(request, 'uproducts.html')
    else:
        messages.error(request, 'not purchased.')
        return redirect('Products')

def purchase(request):
    uid=request.session['userid']
    cdata=Register.objects.get(cemail=uid)
    cid=cdata.id
    data=Purchase.objects.filter(cid_id=cid)
    return render(request,'u_purchase.html',{'data':data})

def ulogout(request):
    return render(request,'index.html')
