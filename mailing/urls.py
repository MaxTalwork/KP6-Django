from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (
    home,
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    ClientCreateView,
    MailingListView,
    MailingDetailView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
)

app_name = MailingConfig.name
urlpatterns = [
    path("", home, name="home"),

    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing_create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing_edit/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path(
        "mailing_delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"
    ),

    path("message_list/", MessageListView.as_view(), name="message_list"),
    path(
        "message/<int:pk>/", cache_page(60)(MessageDetailView.as_view()), name="message"
    ),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "message_edit/<int:pk>/", MessageUpdateView.as_view(), name="message_update"
    ),
    path(
        "message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"
    ),

    path("client_list/", ClientListView.as_view(), name="client_list"),
    path("client/<int:pk>/", cache_page(60)(ClientDetailView.as_view()), name="client"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path("client_edit/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
    path("client_delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
]
