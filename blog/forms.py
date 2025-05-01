from django import forms
from django.core.exceptions import ValidationError
from blog.models import BlogPost, PostAuthor


class BlogPostWithAuthorForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, label="Имя автора")
    author_email = forms.EmailField(max_length=100, label="Email автора")

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview_image', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['author_name'].initial = self.instance.author.name
            self.fields['author_email'].initial = self.instance.author.email

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('author_name')
        email = cleaned_data.get('author_email')

        current_author = self.instance.author if self.instance.pk else None

        # Проверка по name
        existing_by_name = PostAuthor.objects.filter(name=name)
        if current_author:
            existing_by_name = existing_by_name.exclude(pk=current_author.pk)
        if existing_by_name.exists():
            raise ValidationError("Автор с таким именем уже существует.")

        # Проверка по email
        existing_by_email = PostAuthor.objects.filter(email=email)
        if current_author:
            existing_by_email = existing_by_email.exclude(pk=current_author.pk)
        if existing_by_email.exists():
            raise ValidationError("Автор с таким email уже существует.")

        # Сохраняем для использования в save()
        self.cleaned_author_name = name
        self.cleaned_author_email = email
        return cleaned_data

    def save(self, commit=True):
        blog_post = super().save(commit=False)

        current_author = self.instance.author if self.instance.pk else None

        if current_author:
            # Обновляем данные автора
            current_author.name = self.cleaned_author_name
            current_author.email = self.cleaned_author_email
            current_author.save()
            blog_post.author = current_author
        else:
            # Создаём нового автора
            blog_post.author = PostAuthor.objects.create(
                name=self.cleaned_author_name,
                email=self.cleaned_author_email
            )

        if commit:
            blog_post.save()
        return blog_post
