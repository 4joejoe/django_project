from django import forms
from .models import ResumeModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = "__all__"
    # firstname = forms.CharField(label="first name",max_length=50)
    # lastname  = forms.CharField(label="last name", max_length=50)
    # email = forms.EmailField(label="email")
    # file = forms.FileField()