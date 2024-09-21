from datetime import datetime, timedelta

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, Effort, Client

import logging
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management import BaseCommand

# from mailing.task import send_mailing


def send_mailing():
    mailings = Mailing.objects.filter(is_active=True)

    for mailing in mailings:
        emails_list = mailing.client.filter(is_active=True).values_list(
            "email", flat=True
        )
        try:
            send_mail(
                subject=mailing.message.title,
                message=mailing.message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=emails_list,
            )
        except Exception as e:
            Effort.objects.create(
                mailing=mailing,
                error=e,
                status="fail",
                response="Сообщение не доставлено",
            )
        else:
            Effort.objects.create(
                mailing=mailing, status="success", response="Сообщение доставлено"
            )


# def send_mailing_plural():
#     scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
#     scheduler.add_jobstore(DjangoJobStore(), "default")
#     mailing = Mailing.objects.all()
#
#     trigger = get_mailing_period_trigger(mailing.pk)
#
#     scheduler.add_job(
#         send_mailing,
#         trigger=trigger,
#         id="send_mailing",
#         max_instances=1,
#         replace_existing=True,
#         )
#
#     try:
#         scheduler.start()
#     except KeyboardInterrupt:
#         scheduler.shutdown()


def select_mailings():
    mailing_list = Mailing.objects.filter(next_send_date__isnull=True)
    for i in mailing_list:
        i.next_send_date = i.send_date
        i.save()

    today = datetime.today()

    mailing_list = Mailing.objects.filter(next_send_date=today)

    for mailing in mailing_list:
        emails_list = mailing.client.filter(is_active=True).values_list(
            "email", flat=True
        )
        if send_mail(
            subject=mailing.message.title,
            message=mailing.message.body,
            from_email=EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        ):
            Effort.objects.create(
                mailing=mailing, status="success", response="Сообщение доставлено"
            )
        else:
            Effort.objects.create(
                mailing=mailing, status="fail", response="Сообщение не доставлено"
            )

        if mailing.interval == Mailing.DAY:
            diff = 1
        elif mailing.interval == Mailing.WEEK:
            diff = 7
        else:
            diff = 30
        mailing.next_send_date = mailing.next_send_date + timedelta(days=diff)
        mailing.save()
