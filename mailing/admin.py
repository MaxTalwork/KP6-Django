from django.contrib import admin
from mailing.models import Mailing, Client, Message, Effort


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "message",
        "send_date",
        "created_at",
        "status",
        "periodicity",
        "end_date",
        "is_active",
    )
    list_filter = (
        "client_list",
        "send_date",
        "status",
        "periodicity",
        "is_active",
    )
    search_fields = ("client_list",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "client_name")
    list_filter = ("email",)
    search_fields = ("client_name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "letter_body")
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Effort)
class EffortAdmin(admin.ModelAdmin):
    list_display = ("id", "last_try", "status", "response", "mailing")
    list_filter = (
        "status",
        "last_try",
    )
    search_fields = ("status",)
