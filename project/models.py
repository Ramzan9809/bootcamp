from django.db import models
from ckeditor.fields import RichTextField


class OurCourses(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    desc = models.TextField(verbose_name='Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши курсы'
        verbose_name = 'наш курс'


class CategoryForCourses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'


class Courses(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    category = models.ForeignKey(CategoryForCourses, on_delete=models.CASCADE, verbose_name="категории", blank=True, null=True)
    price = models.CharField(max_length=10, verbose_name='Стоимость')
    img = models.ImageField(blank=True, upload_to='images/')
    desc = models.TextField(verbose_name='Описание')
    but = models.CharField(max_length=50, verbose_name='Название кнопки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'курс'

class CategoryBook(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории книг'
        verbose_name_plural = 'Категории книг'


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(CategoryBook, on_delete=models.CASCADE, verbose_name="категория")
    author = models.CharField(max_length=100, verbose_name="Имя Автора")
    desc = models.TextField(verbose_name="Описание")
    Page_Count = models.CharField(max_length=100, verbose_name="Название", blank=True, null=True)
    Word_Count = models.CharField(max_length=100,    verbose_name="Название", blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'


class CoursePage(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Фото")
    count_lections = models.CharField(
        help_text="12 лекции", max_length=100, verbose_name="Количество лекции")
    hours = models.CharField(verbose_name="Сколько часов", max_length=20)
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class SocialLinks(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название соцсети")
    link = models.CharField(max_length=255, verbose_name="ссылка")
    image = models.CharField(max_length=255, verbose_name="ссылка на лого")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сеть'

class Instructors(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя фамилие")
    image = models.ImageField(upload_to='images/', verbose_name="Фото ава")
    position = models.CharField(max_length=100, verbose_name="Должность")
    description = RichTextField()

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = 'Инструкторы'
        verbose_name_plural = 'Инструкторы'


class Reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name="фио")
    desc = models.TextField(verbose_name="Описание")
    rating = models.IntegerField(default=1, verbose_name="Рейтинг")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'