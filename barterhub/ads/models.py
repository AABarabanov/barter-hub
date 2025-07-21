from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ad(models.Model):
    """
    Класс, описывающий модель для хранения объявлений о товарах.
    Хранит информацию о товарах, которые пользователи хотят обменять.
    Все объявления автоматически привязываются к автору (User).

    Attributes:
        user (ForeignKey): Связь с автором объявления
        title (CharField): Заголовок объявления
        description (TextField): Подробное описание товара
        image_url (URLField): Ссылка на изображение (необязательно)
        category (CharField): Категория товара
        condition (CharField): Состояние товара
        created_at (DateTimeField): Дата создания (автоматически)
    """

    CONDITION_CHOICES = [("new", "новый"), ("used", "б/у")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField()
    condition = models.CharField(choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ExchangeProposal(models.Model):
    """
    Класс, описывающий модель для предложений обмена

    Attributes:
        id (AutoField): Автоинкрементный идентификатор
        ad_sender (ForeignKey): Ссылка на объявление-инициатор
        ad_receiver (ForeignKey): Ссылка на целевое объявление
        comment (TextField): Комментарий
        status (CharField): Текущий статус предложения
        created_at (DatatimeField): Дата создания
    """

    STATUS_CHOICES = [
        ("pending", "ожидает"),
        ("accepted", "принята"),
        ("rejected", "отклонена"),
    ]

    id = models.AutoField(primary_key=True)
    ad_sender = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name="sent_proposals"
    )

    ad_receiver = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name="received_proposals"
    )

    comment = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Предложение #{self.id} ({self.status})"
