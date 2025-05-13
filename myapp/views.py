from django.shortcuts import render,redirect
from .forms import Employeeforms
from .models import Employee

def form(request):
    frm=Employeeforms()
    return render(request,'forms.html',{'empfrm':frm})

def addemp(request):
    if request.method=='POST':
        form=Employeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        return render(request,'forms.html')
    
def show(request):
    emp=Employee.objects.all()
    return render(request,'show.html',{'emply':emp})

def edit(request, id):
    emp1 = Employee.objects.get(id=id)
    form = Employeeforms(instance=emp1)
    if request.method == 'POST':
        form = Employeeforms(request.POST, instance=emp1)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:  
        return render(request, 'edit.html', {'form': form})
    
def delete(request,id):
    form=Employee.objects.get(id=id)
    form.delete()
    return redirect('show')

    


    

