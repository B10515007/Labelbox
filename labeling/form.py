from django import forms

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=20, required=False)

class addmemberForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
