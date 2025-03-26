from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project.views import (index, books, book_detail, contact, blog, courses, 
                           course_detail, blog_detail, submit_review)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='home'),
    path('books/', books, name='books'),
    path('book_detail/<slug:slug>/', book_detail, name='book_detail'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<slug:slug>/', blog_detail, name='blog_detail'),
    path('courses/', courses, name='courses'),
    path('course_detail/<slug:slug>/', course_detail, name='course_detail'),
    path('submit-review/', submit_review, name='submit_review'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  path('product/<slug:slug>/', product_detail, name='product_detail'),