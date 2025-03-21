from django.shortcuts import render
from .models import (CategoryForCourses, Courses, OurCourses, Blog,
                     Reviews, CategoryBook, CoursePage, Books, SocialLinks, Instructors, Data)


def index(request):
    category = CategoryForCourses.objects.all()
    course = Courses.objects.all()
    ourcourse = OurCourses.objects.latest("id")
    data = Data.objects.latest('id')
    context = {
        'category': category,
        'data': data,
        'course': course,
        'ourcourse': ourcourse,
    }
    return render(request, 'index.html', context)

def bookPage(request):
    category = CategoryBook.objects.all()
    book = Books.objects.all()
    data = Data.objects.latest('id')
    context = {
        'category': category,
        'data': data,
        'book': book,
    }
    return render(request, 'page/books.html', context)

def bookDetail(request, slug):
    category = CategoryBook.objects.latest('id')
    data = Data.objects.latest('id')
    book = Books.objects.latest('id')
    slug = slug
    context = {
        'category': category,
        'book': book,
        'data': data,
        'slug': slug,
    }
    return render(request, 'page/books-detail.html', context)

def contact(request):
    data = Data.objects.latest('id')
    context = {
        'data': data,
    }
    return render(request, 'page/contact.html', context)

def blog(request):
    data = Data.objects.latest('id')
    blogs = Blog.objects.all()
    context ={
        'data': data,
        'blogs': blogs,
    }
    return render(request, 'page/blog.html', context)

def blog_detail(request, slug):
    data = Data.objects.latest('id')
    blogs_latest = Blog.objects.all()[:3]
    blog = Blog.objects.get(slug=slug) 
    context = {
         'data':data,
         'blog':blog, 
         'blogs_latest':blogs_latest, 
     }
    return render(request, 'pages/blog-detail.html', context)

def courses(request):
    category = CategoryForCourses.objects.all()
    data = Data.objects.latest('id')
    courses = Courses.objects.all()
    context = {
        'category': category,
        'data': data,
        'courses': courses,
    }
    return render(request, 'page/courses.html', context)

def courseDetail(request, slug):
    category = CategoryForCourses.objects.all()
    data = Data.objects.latest('id')
    courses = Courses.objects.all()
    slug = slug
    context = {
        'category': category,
        'data': data,
        'courses': courses,
        'slug': slug,
    }
    return render(request, 'page/course_detail.html', context)