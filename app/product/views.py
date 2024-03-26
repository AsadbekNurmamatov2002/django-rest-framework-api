from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Orders, Xomashyolar, Productkx
from .forms import OrderCreateForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

# bosh sahifa
def Home(request):
    product=Product.objects.all()
    order_list=Orders.objects.all()
    # o'chieish
    if request.method=="POST":
        if 'delete' in request.POST:
            pk=request.POST.get('delete')
            product=Orders.objects.get(id=pk)
            product.delete()
            messages.info(request, "Buyrutma Bekor qilindi!!!")
            return redirect('product:home')
    #  qidirish 
    elif request.method=="GET":
        q=request.GET.get('q') if request.GET.get('q') != None else ''
        product=Product.objects.filter(Q(name__icontains=q))
        order_list=Orders.objects.filter(Q(xomashyo__nome__icontains=q)|
                                                  Q(soni__icontains=q)|
                                                  Q(xomashyo__soni__icontains=q))
        
    return render(request, 'index.html',{'product':product, 'order_list':order_list})

# product detail function 
def product_detail(request, id ,slug):
    products=get_object_or_404(Product, id=id, slug=slug)
    xomashyolar=Xomashyolar.objects.all()
    if request.method=="POST":
        order_create=Orders.objects.create(
            product=products,
            soni=request.POST.get('soni'),
        )

        messages.info(request,"Buyrutma qilindi!!!")
        # kiritish Tugagach Home ga yo'naltirdim
        return redirect('product:home')
        # agr biz shu turgan page da qolishimiz kerak bo'lsa shu buyruqni ishga tushiramiz !!!
        # return redirect('product:product_detail', id=products.id, slug=products.slug)
    
    return render(request, 'product_detail.html',{'products':products, "xomashyolar":xomashyolar})
