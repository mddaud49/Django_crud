from django import forms
from .models import StuModel

class StudentReg(forms.ModelForm):
      class Meta:
        model=StuModel
        fields=['name','email','password']
        widgets={'password':forms.PasswordInput,}