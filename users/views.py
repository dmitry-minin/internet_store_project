from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.models import User
from users.forms import CustomUserCreationForm
from django.core.mail import send_mail


class UserRegisterView(CreateView):
    """
    View for user registration.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """
        If the form is valid, send a confirmation of the registration to the user.
        """
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, email):
        """
        Send a welcome email to the user method.
        """
        subject = "Welcome to our Internet store!"
        message = f"Hello {email},\n\nThank you for registering on our site."
        from_email = "project.autoemail@gmail.com"
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
