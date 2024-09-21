from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from mailing.forms import MailingForm
from mailing.models import Message, Client, Mailing


def home(request):
    return render(request, "mailing/home.html")


def contacts(request):
    return render(request, "mailing/contacts.html")


def goods(request):
    return render(request, "mailing/goods.html")


class MessageCreateView(CreateView, LoginRequiredMixin):
    model = Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = "mailing.add_mailing"
    success_url = reverse_lazy("mailing:mailing_list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = "mailing.change_mailing"
    success_url = reverse_lazy("mailing:mailing_list")


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    # permission_required = 'mailing.view_mailing'

    # def get_context(self, request):
    #     context = super(LivreDesc, self).get_context(request)
    #     context['nb_livres'] = LivreDesc.objects.all().count()
    #     return context

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for mailing in context_data['mailing_list']:
    #         active_version = Mailing.objects.filter(is_active=True)
    #         if active_version:
    #             mailing.active_version = active_version.last().name_version
    #         else:
    #             product.active_version = 'Отсутствует'
    #     return context_data


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = "mailing.delete_mailing"
    success_url = reverse_lazy("mailing:mailing_list")
