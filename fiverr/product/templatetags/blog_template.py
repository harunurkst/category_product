from django import template
from product.models import Category, MainProduct

register = template.Library()


@register.inclusion_tag('product/sidebar.html')
def get_sidebar():
    category = Category.objects.all()
    return {'cats': category,}
