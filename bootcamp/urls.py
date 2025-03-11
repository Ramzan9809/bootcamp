from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project.views import index, bookPage, bookDetail, contact, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='home'),
    path('books/', bookPage, name='bookPage'),
    path('books_detail/', bookDetail, name='bookDetail'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  path('product/<slug:slug>/', product_detail, name='product_detail'),