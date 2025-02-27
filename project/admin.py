from django.contrib import admin
from .models import CategoryForCourses, Courses, OurCourses


admin.site.register(CategoryForCourses)
admin.site.register(Courses)
admin.site.register(OurCourses)