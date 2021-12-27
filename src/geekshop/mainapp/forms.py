from django.forms import forms
from .models import ProductCategory
from mainapp.models import Product


class ProductCategoryEditForm(forms.Form):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.field.items():
            field.wodget.attrs['class'] = 'form-control'


class ProductEditForm(forms.Form):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
