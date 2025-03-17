from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project.views import index, bookPage, bookDetail, contact, blog, courses, courseDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='home'),
    path('books/', bookPage, name='books'),
    path('books_detail/<slug:slug>/', bookDetail, name='book_detail'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('courses/', courses, name='courses'),
    path('course_detail/<slug:slug>/', courseDetail, name='course_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  path('product/<slug:slug>/', product_detail, name='product_detail'),