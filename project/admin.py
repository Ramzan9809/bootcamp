from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (CategoryForCourses, Courses, OurCourses,
                     Reviews, CategoryBook, CoursePage, Books, SocialLinks, Instructors)


admin.site.register(CategoryForCourses)
admin.site.register(Courses)
admin.site.register(OurCourses)

admin.site.register(Reviews)
admin.site.register(CategoryBook)
admin.site.register(CoursePage)
admin.site.register(Books)
admin.site.register(SocialLinks)
admin.site.register(Instructors)
