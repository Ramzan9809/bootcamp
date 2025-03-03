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
    return render(request, 'books.html', context)

def bookDetail(request):
    category = CategoryBook.objects.latest('id')
    book = Books.objects.latest('id')
    context = {
        'category': category,
        'book': book,
    }
    return render(request, 'books-detail.html', context)

def contact(request):
    return render(request, 'contact.html')


