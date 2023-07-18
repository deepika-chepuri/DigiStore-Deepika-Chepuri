from django.shortcuts import render
from admins.models import Products
from user.models import Register,Purchase
from PIL import Image
def alogin(request):
    if request.method=='POST':
        try:
            email=request.POST.get('email')
            password=request.POST.get('password')
            if email=='n2m2@gmail.com' and password=='n2m2':
                return render(request,'ahome.html')
            else:
                return render(request,'alogin.html')
        except Exception as e:
            print("Exception is:",e)
            return render(request,'alogin.html')
    else:
        return render(request,'alogin.html')

def aproducts(request):
    if request.method=='POST':
        try:
            pname=request.POST.get('pname')
            pcat= request.POST.get('pcat')
            pcost = request.POST.get('pcost')
            pquality = request.POST.get('pquality')
            pdec= request.POST.get('pdec')
            pimage= request.FILES['pimage']

            data=Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,
                )
            data.save()
            return render(request,'ahome.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request,'a_addproducts.html')
    else:
       return render(request,'a_addproducts.html')

def avproducts(request):
    data = Products.objects.all()
    return render(request,'a_viewproducts.html',{'profile':data})

def apurchase(request):
    uid=request.session['userid']
    cdata=Register.objects.get(cemail=uid)
    cid=cdata.id
    data=Purchase.objects.all()
    return render(request,'a_purchase.html',{'data':data})

def alogout(request):
    return render(request,'alogin.html')









