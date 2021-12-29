from django.forms import forms
from .models import ProductCategory


class ProductCategoryCreateForm(forms.Form):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.field.items():
            field.wodget.attrs['class'] = 'form-control'
