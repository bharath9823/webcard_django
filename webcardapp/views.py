from django.shortcuts import render
from webcardapp import forms

# Create your views here.
def index(request):
    return render(request,'index.html')
def form_view(request):
    form=stdform()

    if request.method=='POST':
        form=stdform(request.POST)

        if form.is_valid():
            print("validation Success")
            print(request.POST['first_name'])
            print(request.POST['second_name'])
            print(request.POST['age'])
            print(request.POST['DOB'])
    return render(request,'index.html',{'form':form})

