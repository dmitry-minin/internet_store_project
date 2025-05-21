from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "mobile", "country", "avatar", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Input your email"}
        )
        self.fields["mobile"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "tel",
                "placeholder": "Input your mobile number. Just digits, without spaces and symbols.",
            }
        )
        self.fields["country"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Input your country"}
        )
        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control-file d-block"}
        )
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

    def clean_mobile(self):
        """
        Checks if the mobile number contains only digits.
        """
        mobile = self.cleaned_data.get("mobile")
        if not mobile.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return mobile

