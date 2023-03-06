from django import forms

class stdform(forms.Form):
    fist_name=forms.CharField(max_length=100)
    second_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    DOB=forms.IntegerField()