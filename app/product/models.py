from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
#  Xomashyolar jadvali
class Xomashyolar(models.Model):
    nome=models.CharField(max_length=250)
    image=models.ImageField(upload_to='product/%Y/%M/%D/')
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
    
#  product va Xomashyolarni birlashtirovchi qo'shimcha jadval
class Productkx(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    xomashyolar=models.ForeignKey(Xomashyolar,on_delete=models.CASCADE)
    soni=models.IntegerField()

# buyrutma uchun qo'shimcha jadval
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    xomashyo=models.ForeignKey(Xomashyolar,on_delete=models.CASCADE , null=True, blank=True)
    soni=models.PositiveIntegerField(default=1)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
   
    
