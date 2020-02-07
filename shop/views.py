from django.shortcuts import render, get_object_or_404
from .models import Catergory, Product
from cart.forms import CartAddProductForm

# Listing all products by a given category
def product_list(request, category_slug=None):
    category = None
    catergories = Catergory.objects.all()
    products = Product.objects.filter(available=True)
     
    if category_slug:
        catergory = get_object_or_404(Catergory, slug=category_slug)
        products = products.filter(category=category)
        products = products.filter(category=category)
    return render(
        request,'shop/product/list.html',{'category': category,'catergories': catergories,'products': products}
    )
# retrieve and display a single product
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,'cart_product_form': cart_product_form})






