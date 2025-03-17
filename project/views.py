from django.shortcuts import render
from .models import (CategoryForCourses, Courses, OurCourses,
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

def bookDetail(request):
    category = CategoryBook.objects.latest('id')
    data = Data.objects.latest('id')
    book = Books.objects.latest('id')
    context = {
        'category': category,
        'book': book,
        'data': data,
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
    context ={
        'data': data,
    }
    return render(request, 'page/blog.html', context)

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
