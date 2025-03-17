from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (CategoryForCourses, Courses, OurCourses,
                     Reviews, CategoryBook, CoursePage, Books, SocialLinks, Instructors, Data)


class BooksAdmin(admin.ModelAdmin):
     list_display = ['title', 'author', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 
class CategoryBookAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}

class CategoryCoursesAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}

class SocialLinksInline(admin.TabularInline):
     model = SocialLinks
     extra = 1
 
class InstructorsAdmin(admin.ModelAdmin):
     list_display = ['name', 'position']
     inlines = [SocialLinksInline,]

class CourseAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 
admin.site.register(CategoryBook, CategoryBookAdmin)
admin.site.register(Books, BooksAdmin)

admin.site.register(CategoryForCourses, CategoryCoursesAdmin)
admin.site.register(Courses,CourseAdmin)
admin.site.register(OurCourses)

admin.site.register(Reviews)
admin.site.register(CoursePage)
admin.site.register(SocialLinks)
admin.site.register(Instructors, InstructorsAdmin)
admin.site.register(Data)
