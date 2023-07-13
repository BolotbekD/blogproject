from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural= 'Авторы'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Названия ктегории')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date_publication = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    