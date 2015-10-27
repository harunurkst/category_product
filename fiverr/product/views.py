from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from .models import MainProduct,Category

#category list view

def home(request):
	post = MainProduct.objects.all()
	recent_post = MainProduct.objects.all()[:5]
	category_list = Category.objects.all()
	context_dict  = {'categories':category_list,'post':post,'recent_post':recent_post,}
	return render(request,'product/index.html',context_dict)
	
# Single Product detail view

def product_detail(request, slug):
    items = MainProduct.objects.filter(slug=slug)
    category_item = Category.objects.filter(slug=slug)
    return render_to_response('product/product-detail.html', {'items':items,'category-items':category_item,})

# Single Category with associated Product view
	
def category_list(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        posts = MainProduct.objects.filter(categories=category)
        context_dict['posts'] = posts
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass
    return  render(request, 'product/category-list.html',context_dict)
