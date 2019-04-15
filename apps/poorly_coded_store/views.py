from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    
    quantity_from_form = int(request.POST["quantity"])
    item = Product.objects.get(id=request.POST["id"])
    item_price = float(item.price)
    total_charge = quantity_from_form * item_price
    print(f"Charging credit card {total_charge}")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session["charge"] = total_charge
    if "manifest" in request.session:
        request.session["manifest"] += quantity_from_form
    else:
        request.session["manifest"] = quantity_from_form
        
    if "tab" in request.session:
        request.session["tab"] += total_charge
    else:
        request.session["tab"] = total_charge
    
    return redirect("/checkout")

def checkout(request):
    
    
    return render (request, "store/checkout.html")