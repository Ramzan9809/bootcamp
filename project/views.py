from django.shortcuts import render
from .models import (CategoryForCourses, Courses, OurCourses,
                     Reviews, CategoryBook, CoursePage, Books, SocialLinks, Instructors)


def index(request):
    category = CategoryForCourses.objects.all()
    course = Courses.objects.all()
    ourcourse = OurCourses.objects.latest("id")
    context = {
        'category': category,
        'course': course,
        'ourcourse': ourcourse,
    }
    return render(request, 'index.html', context)

def bookPage(request):
    category = CategoryBook.objects.all()
    book = Books.objects.all()
    context = {
        'category': category,
        'book': book,
    }
    return render(request, 'page/books.html', context)

def bookDetail(request):
    category = CategoryBook.objects.latest('id')
    book = Books.objects.latest('id')
    context = {
        'category': category,
        'book': book,
    }
    return render(request, 'page/books-detail.html', context)

def contact(request):
    return render(request, 'page/contact.html')

def blog(request):
    return render(request, 'page/blog.html')

def courses(request):
    category = CategoryForCourses.objects.all()
    courses = Courses.objects.all()
    context = {
        'category': category,
        'courses': courses,
    }
    return render(request, 'page/courses.html', context)