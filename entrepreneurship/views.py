from entrepreneurship.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

def entrepreneurship(request):
    return render_to_response('entrepreneur/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all().order_by("-posted")[:5]
    })

def entrepreneurship_post(request, slug):
    return render_to_response('entrepreneur/veiw_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def entrepreneurship_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('entrepreneur/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category).order_by("-posted")[:5]
    })