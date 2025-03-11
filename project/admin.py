from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (CategoryForCourses, Courses, OurCourses,
                     Reviews, CategoryBook, CoursePage, Books, SocialLinks, Instructors)



class BooksAdmin(admin.ModelAdmin):
     list_display = ['title', 'author', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 
admin.site.register(CategoryBook, CategoryAdmin)
admin.site.register(Books, BooksAdmin)

admin.site.register(CategoryForCourses)
admin.site.register(Courses)
admin.site.register(OurCourses)

admin.site.register(Reviews)
admin.site.register(CoursePage)
admin.site.register(SocialLinks)
admin.site.register(Instructors)
