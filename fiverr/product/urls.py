from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.home, name='product-home'),
    url(r'^(?P<slug>[\w-]+)/$', views.product_detail, name='product-detail'),
    url(r'^category/(?P<category_name_slug>[\w-]+)/$', views.category_list, name='category-list'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()
