"""digi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as v
from admins import views as v1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('lap/',v.lap,name='lap'),
    path('mob/',v.mob,name='mob'),
    path('tabs/',v.tabs,name='tabs'),
    path('watch/',v.watch,name='watch'),
    path('buy/',v.buy,name='buy'),
    path('products/',v.products,name='products'),



    path('contact/',v.contact,name='contact'),

    path('reg/', v.reg, name='reg'),
    path('login/', v.login, name='login'),
    path('pro/', v.pro, name='pro'),
    path('alogin/', v1.alogin, name='alogin'),
    path('aproducts/', v1.aproducts, name='aproducts'),
    path('avproducts/', v1.avproducts, name='avproducts'),
    path('uvproducts/<int:id>/', v.uvproducts, name='uvproducts'),
    path('uvproducts/', v.uvproducts, name='uvproducts'),
    path('buy_product/<int:id>/buy/', v.buy_product, name='buy_product'),
    path('buy_product/', v.buy_product, name='buy_product'),
    path('purchase/', v.purchase, name='purchase'),
    path('apurchase/', v1.apurchase, name='apurchase'),
    path('ulogout/', v.ulogout, name='ulogout'),
    path('alogout/', v1.alogout, name='alogout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
