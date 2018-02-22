from .models import Product,Category
from django.shortcuts import render_to_response, get_object_or_404

def product(request):
    return render_to_response('product/index.html', {
        'categories': Category.objects.all(),
        'products': Product.objects.all().order_by("-addded")[:5]
    })

def view_product(request, slug):
    return render_to_response('product/veiw_post.html', {
        'product': get_object_or_404(Product, slug=slug)
    })

def product_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('product/view_category.html', {
        'category': category,
        'products': Product.objects.filter(category=category).order_by("-addded")[:5]
    })