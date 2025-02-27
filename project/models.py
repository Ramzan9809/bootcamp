from django.db import models



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