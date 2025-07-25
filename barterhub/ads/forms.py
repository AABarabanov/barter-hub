from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ad, ExchangeProposal


class AdForm(forms.ModelForm):
    """Класс, описывающий форму для создания и редактирования объявления"""

    class Meta:
        model = Ad
        fields = ["title", "description", "image_url", "category", "condition"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "image_url": forms.URLInput(
                attrs={"placeholder": "https://example.com/image.jpg"}
            ),
        }


class ProposalForm(forms.ModelForm):
    """Класс, описывающий форму для отправки предложения обмена"""

    class Meta:
        model = ExchangeProposal
        fields = ["ad_receiver", "comment"]
        widgets = {"comment": forms.Textarea(attrs={"rows": 3})}


class RegisterForm(UserCreationForm):
    """Класс, описывающий форму для регистрации"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
