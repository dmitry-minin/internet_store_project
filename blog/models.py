from django.db import models


class PostAuthor(models.Model):
    """
    Model representing a blog post author.
    """
    name = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name="Имя автора")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email автора")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор поста"
        verbose_name_plural = "Авторы постов"
        ordering = ["name"]


class BlogPost(models.Model):
    """
    Model representing a blog post.
    """
    author = models.ForeignKey(PostAuthor, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор поста")
    title = models.CharField(max_length=200, verbose_name="Название поста")
    content = models.TextField(verbose_name="Содержимое поста")
    preview_image = models.ImageField(upload_to='blog_previews/', blank=True, null=True,
                                      verbose_name="Изображение превью")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-updated_at"]
