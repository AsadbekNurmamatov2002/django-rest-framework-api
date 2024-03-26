from django import forms 
from .models import Orders

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields = "__all__"
        # exclude=('product','xomashyo')

