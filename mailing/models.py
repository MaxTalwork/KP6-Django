from django.db import models
from users.models import User


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема")
    letter_body = models.TextField(
        verbose_name="Описание категории", blank=True, null=True
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"{self.title}"


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Email")
    client_name = models.TextField(verbose_name="ФИО клиента", blank=True, null=True)
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.email}"


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование рассылки")
    message = models.ForeignKey(
        Message,
        on_delete=models.SET_NULL,
        verbose_name="Сообщение",
        blank=True,
        null=True,
        related_name="Сообщение",
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания рассылки"
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )
    send_date = models.DateField(
        verbose_name="Дата начала рассылки", blank=True, null=True
    )
    next_send_date = models.DateField(
        verbose_name="Дата повтора рассылки", blank=True, null=True
    )
    is_active = models.BooleanField(default=True)

    COMPLETED = "completed"
    CREATED = "created"
    STARTED = "started"
    DAY = "once a day"
    MINUTE = "once a minute"
    WEEK = "once a week"
    MONTH = "once a month"
    STATUS = [(COMPLETED, "completed"), (CREATED, "created"), (STARTED, "started")]
    INTERVAL = [
        (DAY, "once a days"),
        (WEEK, "once a week"),
        (MONTH, "once a months"),
    ]
    status = models.CharField(
        choices=STATUS, default=CREATED, verbose_name="Статус рассылки"
    )
    periodicity = models.CharField(
        choices=INTERVAL, default=DAY, verbose_name="Периодичность"
    )
    end_date = models.DateTimeField(
        verbose_name="Дата окончания рассылки",
        blank=True,
        null=True,
    )

    client_list = models.ManyToManyField(Client, related_name="mailing_list")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["name", "created_at", "status", "periodicity"]
        permissions = [
            # ('can_view_mailing', 'Может просматривать рассылку'),
            # ('can_disable_mailing', 'Может отключать рассылку')
        ]

    def __str__(self):
        return f"{self.name}"


class Effort(models.Model):
    SUCCESS = "success"
    FAIL = "fail"
    STATUSES = [(SUCCESS, "success"), (FAIL, "fail")]
    last_try = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата попытки рассылки"
    )
    status = models.CharField(choices=STATUSES, default=SUCCESS, verbose_name="Статус")
    response = models.TextField(verbose_name="Ответ", blank=True, null=True)
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Рассылка",
    )

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
        ordering = ("status",)

    def __str__(self):
        return f"{self.status}"
