from django import forms
from .models import MainModel

class StuForm(forms.ModelForm):
    class Meta:
        model=MainModel
        fields=['Studentname','Email','Password']
        widgets={'Password':forms.PasswordInput}

class TeacherForm(StuForm):
    class Meta(StuForm.Meta):
        fields=['Teachername','Email','Password']
        
