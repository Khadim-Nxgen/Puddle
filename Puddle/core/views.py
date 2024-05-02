from django.shortcuts import redirect, render 
from item.models import Item,Category
from .forms import SignupForm

# Create your views here.

def index(request):
  items=Item.objects.filter(is_sold=False)[0:4]
  categories=Category.objects.all()
  return render(request,"core/index.html",{
    'categories':categories,
    'items':items,
    })

def signup(request):
  form=SignupForm()
  if request.method =='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()

      return redirect('/login/')
    
  else:
    SignupForm()

  return render(request,"core/form.html",{
    'form':form
  })







def contact(request):
  return render(request,"core/contact.html")


def privacy(request):
  return render(request,"core/privacy.html")