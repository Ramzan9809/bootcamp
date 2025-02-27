from django.shortcuts import render
from .models import CategoryForCourses, Courses, OurCourses


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