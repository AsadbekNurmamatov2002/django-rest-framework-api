from typing import Iterable
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
#  Xomashyolar jadvali
class Xomashyolar(models.Model):
    nome=models.CharField(max_length=250)
    soni=models.IntegerField()
    meter=models.CharField(max_length=250, null=True, blank=True)
    narxi=models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self) -> str:
        return self.nome

# Maxsulotlar jadvali
class Product(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='product/%Y/%M/%D/')
    slug=models.SlugField(max_length=260, blank=True)
    
    
    def save(self, *args, **kwargs):
        if self.slug==None:
            slug = slugify(self.name)
            has_slog=Product.objects.filter(slug=slug).exists()
            count=1
            while has_slog:
                count+=1
                slug=slugify(self.name)+'-'+str(count)
                has_slog=Product.objects.filter(slug=slug).exclude()
            self.slug=slug
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[ self.id,
                                                   self.slug])
    
    # bu function orqali biz productga bo'gluq modeldan malomot olish mumkun
    """ orders model """
    @property
    def orders(self):
        return self.orders_set.all()
    
    """ productga ketadigan Xomashyolar """
    @property
    def productkitadiganxomashyolar(self):
        return self.productkx_set.all()
    
""" 
 product va Xomashyolarni birlashtirovchi qo'shimcha 
 jadval yani Xamoshyolarga qarab omborda nima bo'lsa shu buyicha 
 producktiga kerak narsalarni tallaydi
"""
class Productkx(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    xomashyolar=models.ForeignKey(Xomashyolar,on_delete=models.CASCADE)
    soni=models.IntegerField()
    #  eslatma bu save methodni qo'llasak ham qo'llamask ham bo'ladi
    #  bu yerda Xamashyo soni productga ketadingan xomashyolar sonidan kichik bo'lsa saqlamaydii ....
    def save(self, *args, **kwargs) -> None:
        if self.soni < self.xomashyolar.soni:
            return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return str(self.soni)
    
# buyrutma uchun qo'shimcha jadval
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    xomashyo=models.ForeignKey(Xomashyolar,on_delete=models.CASCADE , null=True, blank=True)
    soni=models.PositiveIntegerField(default=1)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    """
    foydalanovchi buyretma berganda productga ketadigan
    xomashyolar soni va byruma soniga qarab biz
    byrutmani saqlashimiz va Xomshyo modelilini o'zgartirishimiz mumkun.....
    
    """
    def save(self, *args, **kwargs) -> None:
        k=Productkx.objects.filter(product=self.product)
        for i in k:
            # agar productga ketadigan xomashyo va buyrutma soni xomashyolar modelida bor xomashyolarni sonidan katta bo'lsa buyrutma bekor qilinadi
            if int(self.xomashyo.soni) > int((i.soni)*(self.soni)):
                # endi biz Xomashyolar modelidan qancha productga ketgan buyrutmani ayerib Xomashyo modelni o'zgartiramiz.....
                soni=int(self.xomashyo.soni)-int((i.soni)*(self.soni)) # ayerish
                getxomashyo=Xomashyolar.objects.filter(id=self.xomashyo.id) # id=id ga teng bulgan Xamashyo olindi
                xomashyo=getxomashyo.update(soni=soni, nome=self.xomashyo.nome, meter=self.xomashyo.meter, narxi=self.xomashyo.narxi) # o'zgartirildi soni
                return super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return str(self.soni)
    
