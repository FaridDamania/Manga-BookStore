from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from django.contrib import messages

# Create your views here.

def index(request):
    top_five_products = Product.objects.all()[:8]
    categories = Category.objects.all()[:6]
    products = Product.objects.all()
    return render(request, 'bookshop/index.html', {'categories': categories, 'products': products, 'top_five_products': top_five_products})

def about(request):
    return render(request, 'bookshop/about.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'bookshop/products_list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    # Getting product id for showing all reviews related to one product
    reviewproduct = Product.objects.get(slug=slug)
    prid = reviewproduct.id

    all_reviews = Review.objects.filter(product=prid)
    
    return render(request, 'bookshop/product_detail.html', {'product': product, 'cart_product_form': cart_product_form, 'all_reviews': all_reviews})

def all_Categories(request):
    categories = Category.objects.all()
    return render(request, 'bookshop/all_category_list.html', {'categories': categories})

def contact_us(request):
    return render(request, 'bookshop/contact_us.html')

def search_Result(request):
    if request.method == 'POST':
        search_query = request.POST['search']
        query_result = Product.objects.filter(name__startswith=search_query)
        return render(request, 'bookshop/search.html', {'query_result': query_result, 'search_query': search_query})

def Comment_Review(request, product_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST['rating']
        review_comment = request.POST['review']
        product = get_object_or_404(Product, id=product_id)
        comment_review = Review.objects.create(product=product, name=name, email=email, rating=rating, review_comment=review_comment)
        messages.success(request, "Your review has been submitted")
        return render(request, 'bookshop/product_detail.html', {'product': product})

    return render(request, 'bookshop/product_detail.html')
