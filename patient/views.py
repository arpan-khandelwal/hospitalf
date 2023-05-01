from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import DetailsForm,DetailsUpdateForm,RecordForm,AccountSettingsForm
from .models import Person
# Create your views here.

def index(request):
    return render(request,'patient/index.html')


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('patient:login')


    context ={
        'form':form
    }
    return render(request,'patient/register.html',context)

@login_required
def settings(request):
    user = request.user
    form = AccountSettingsForm(instance=user)
    if request.method == "POST":
        user.username = request.post["username"]
        user.first_name = request.post["first_name"]
        user.last_name = request.post["last_name"]

        user.save()
        messages.success(request,"Account Updated Successfully")
        
        return redirect("patient:settings")

    context={
        'form' : form,
        'user' : user,
    }
    return render(request,'patient/settings.html',context)

@login_required
def update(request,id):
    person_to_update = Person.objects.get(id=id)
    form = DetailsUpdateForm(instance = person_to_update)

    if request.method == "POST":
        form = DetailsUpdateForm(request.POST)
        if form.is_valid():
            person_to_update.name = form.cleaned_data["name"]
            person_to_update.age = form.cleaned_data["age"]
            person_to_update.height = form.cleaned_data["height"]
            person_to_update.weight = form.cleaned_data["weight"]
            person_to_update.blood_pressure = form.cleaned_data["blood_pressure"]

            person_to_update.save()

            return redirect('patient:home')
                
    context ={
        'note' : person_to_update,
        'form' : form
    }
    return render(request,'patient/update.html',context)

@login_required
def home(request):
    person = Person.objects.all()
    context={
        'notes' : person,
    }
    return render(request,'patient/home.html',context)

@login_required
def delete(request,id):
    person_to_delete = Person.objects.get(id=id)
    if request.method == "POST":
        person_to_delete.delete()
        return redirect('patient:home')
    return render(request,'patient/delete.html')


@login_required
def addpatient(request):
    form = DetailsForm()
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            person_obj = form.save(commit=False)
            person_obj.user = request.user
            person_obj.save()

            return redirect('patient:home')

    context={
        'form' : form,
    }
    return render(request,'patient/addpatient.html',context)


@login_required
def addreport(request):
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            person_obj = form.save(commit=False)
            person_obj.user = request.user
            person_obj.save()

            return redirect('patient:home')

    context={
        'form' : form,
    }
    return render(request,'patient/addreport.html',context)