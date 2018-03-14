from django.shortcuts import render
from . import models,forms
# Create your views here.
def index(request):


    return render(request,'app/index.html',context={})

def register(request):
    form = forms.reg_form()
    if request.method == 'POST':

        form = forms.reg_form(request.POST)
        form.save()
        return index(request)


    return render(request,'app/register.html',context={'form':form})
def use(request):
      tab = models.reg.objects.all()

      return render(request,'app/users.html',context={'tab':tab})
