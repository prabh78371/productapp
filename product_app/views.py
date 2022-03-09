from django.shortcuts import redirect, render
from django.http import HttpResponse
from product_app.forms import ProductForm
from product_app.models import Products

# Create your views here.
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = ProductForm()
    return render(request,"index.html",{"form":form})

def view(request):
    # query select * from table
    prod = Products.objects.all()
    return render(request,"show.html",{"prod":prod})

def edit(request,id):
    productapp = Products.objects.get(id=id)
    return render(request,"edit.html",{"prod": productapp})

def update(request,id):
    productapp = Products.objects.get(id=id)
    form = ProductForm(request.POST,instance= productapp)
    if form.is_valid():
        form.save()
        return redirect("/view")
    return render(request,"edit.html",{"prod": productapp})

def delete(request,id):
    productapp = Products.objects.get(id=id)
    productapp.delete()
    return redirect("/view")



