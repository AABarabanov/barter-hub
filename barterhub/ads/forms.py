from django import forms
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
