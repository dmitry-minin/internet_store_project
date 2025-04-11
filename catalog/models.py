from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание продукта"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория продукта",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
