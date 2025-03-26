from django.shortcuts import render, redirect
from .models import (CategoryCourses, Courses, OurCourses, Blog, Comments,
                      CategoryBook, Books, Instructors, Data)
from project.forms import ReviewForm

# main
# -------------------------------


def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = ReviewForm()
    return render(request, 'courses.html', {'form':form})

def index(request):
    category = CategoryCourses.objects.all()
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

# books
# -------------------------------

def books(request):
    category = CategoryBook.objects.all()
    book = Books.objects.all()
    data = Data.objects.latest('id')
    context = {
        'category': category,
        'data': data,
        'book': book,
    }
    return render(request, 'page/books.html', context)

def book_detail(request, slug):
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
    return render(request, 'page/book-detail.html', context)

# blog
# -------------------------------

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
    slug = slug
    comments = Comments.objects.all()
    context = {
         'data':data,
         'blog':blog, 
         'blogs_latest':blogs_latest, 
         'slug': slug,
         'comments': comments,
     }
    return render(request, 'page/blog-detail.html', context)

# courses
# -------------------------------

def courses(request):
    category = CategoryCourses.objects.all()
    data = Data.objects.latest('id')
    courses = Courses.objects.all()
    context = {
        'category': category,
        'data': data,
        'courses': courses,
    }
    return render(request, 'page/courses.html', context)


def course_detail(request, slug):
    category = CategoryCourses.objects.all()
    data = Data.objects.latest('id')
    courses = Courses.objects.latest('id')
    instructors = Instructors.objects.all()
    slug = slug
    context = {
        'category': category,
        'data': data,
        'courses': courses,
        'slug': slug,
        'instructors': instructors,
    }
    return render(request, 'page/course_detail.html', context)

# contact
# -------------------------------

def contact(request):
    data = Data.objects.latest('id')
    context = {
        'data': data,
    }
    return render(request, 'page/contact.html', context)