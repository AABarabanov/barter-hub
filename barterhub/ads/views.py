from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import ListView

from .models import Ad
from .forms import AdForm, ProposalForm, RegisterForm


# todo: Документация!
class AdListView(ListView):
    model = Ad
    template_name = "ads/ad_list.html"
    context_object_name = "ads"

    def get_queryset(self):
        # Базовый запрос - все объявления
        return Ad.objects.all()


class MyAdsListView(AdListView):
    def get_queryset(self):
        # Объявления текущего пользователя
        return super().get_queryset().filter(user=self.request.user)


def home(request):
    return render(
        request,
        "ads/index.html",
        {"user": request.user},  # Используем существующий шаблон
    )


def ad_create(request: HttpRequest) -> HttpResponse:
    """
    Функция для обработки создания нового объявления

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        (HttpResponse): HTTP-ответ с HTML-страницей с формой или редирект на список объявлений после успешного сохранения.
    """
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect("ad_list")
    else:
        form = AdForm()
    return render(request, "ads/ad_form.html", {"form": form})


def send_proposal(request: HttpRequest, ad_id: int) -> HttpResponse:
    """
    Функция для обработки отправки предложения обмена относительно объявления с заданным идентификатором.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        ad_id (int): Идентификатор объявления получателя предложения.

    Returns:
        HttpResponse: HTTP-ответ с HTML-страницей с формой предложения или редирект на страницу объявления после успешного сохранения.

    Raises:
        Http404: Если объявление получателя не найдено.
    """
    receiver_ad = get_object_or_404(Ad, id=ad_id)
    if request.method == "POST":
        form = ProposalForm(request.POST)
    if form.is_valid():
        proposal = form.save(commit=False)
        proposal.ad_sender = Ad.objects.filter(
            user=request.user
        ).first()  # Находим объявление пользователя
        proposal.ad_receiver = receiver_ad
        proposal.save()
        return redirect("ad_detail", ad_id=ad_id)
    else:
        form = ProposalForm()
    return render(
        request, "ads/proposal_form.html", {"form": form, "receiver_ad": receiver_ad}
    )


def ad_detail(request, ad_id):
    """
    Функция для отображения страницы с подробной информацией об объявлении.

    Args:
        request (HttpRequest): Объект запроса Django.
        ad_id (int): Идентификатор объявления.

    Returns:
        HttpResponse: HTML-страница с деталями объявления

    Raises:
        Http404: Если объявление с заданным id не существует.
    """

    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, "ads/ad_detail.html", {"ad": ad})


def register(request):
    # TODO: Добавить доки
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "ads/register.html", {"form": form})
