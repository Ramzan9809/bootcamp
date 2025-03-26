from django.contrib import admin
from .models import (CategoryCourses, Courses, OurCourses, Blog, Comments,
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

class BlogAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 

class SocialLinksInline(admin.TabularInline):
     model = SocialLinks
     extra = 1
 
class InstructorsAdmin(admin.ModelAdmin):
     list_display = ['name', 'position']
     inlines = [SocialLinksInline,]

class CommentsAdmin(admin.ModelAdmin):
     list_display = ['name', 'blog']

class CourseAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug' :('title',)}
 
admin.site.register(CategoryBook, CategoryBookAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Comments, CommentsAdmin)

admin.site.register(CategoryCourses, CategoryCoursesAdmin)
admin.site.register(Courses,CourseAdmin)
admin.site.register(OurCourses)
admin.site.register(Blog,  BlogAdmin)

admin.site.register(Reviews)
admin.site.register(CoursePage)
admin.site.register(SocialLinks)
admin.site.register(Instructors, InstructorsAdmin)
admin.site.register(Data)
