from django import forms
from . import models
class reg_form(forms.ModelForm):
    class Meta:
        model = models.reg
        fields = '__all__'
