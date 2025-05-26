from django import forms
from django.forms import BooleanField, ClearableFileInput
from catalog.models import Category, Product


exception_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


def validate_price(value):
    """
    Проверяет, что цена больше нуля.
    """
    if value <= 0:
        raise forms.ValidationError("Цена должна быть больше нуля.")
    return value


def validate_image(image):
    """
    Проверяет, что изображение имеет допустимый формат.
    """
    valid_formats = ['image/jpeg', 'image/png']
    if image.content_type not in valid_formats:
        raise forms.ValidationError("Формат изображения должен быть JPEG/PNG.")

    max_size = 5 * 1024 * 1024  # 5 MB
    if image.size > max_size:
        raise forms.ValidationError("Размер изображения не должен превышать 5 MB.")


class MixinProductFormStyle:
    """
    Миксин для форм, связанных с продуктами.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            elif isinstance(field.widget, ClearableFileInput):
                field.widget.attrs['class'] = "form-control-file"
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = "form-select"
            field.widget.attrs['class'] = "form-control"


class CategoryForm(MixinProductFormStyle, forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(MixinProductFormStyle, forms.ModelForm):
    """
    Форма для создания и редактирования продуктов пользователями.
    """
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name and any(word in name.lower() for word in exception_words):
            raise forms.ValidationError(
                "Название продукта содержит запрещенные слова."
            )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description and any(word in description.lower() for word in exception_words):
            raise forms.ValidationError(
                "Описание продукта содержит запрещенные слова."
            )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price:
            validate_price(price)
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            validate_image(image)
        return image


class ProductModeratorForm(MixinProductFormStyle, forms.ModelForm):
    """
    Форма для публикации продуктов модератором.
    """
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
            "published",
            "owner",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        readonly_fields = ['name', 'description', 'image', 'category', 'price', 'owner']
        for field_name in readonly_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True
