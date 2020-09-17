from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Notes(models.Model):
    "Generated Model"
    note_id = models.UUIDField()
    case_id = models.ForeignKey(
        "home.Cases",
        on_delete=models.CASCADE,
        related_name="notes_case_id",
    )
    description = models.CharField(
        max_length=256,
    )
    date = models.DateField()
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="notes_user_id",
    )


class Events(models.Model):
    "Generated Model"
    event_id = models.UUIDField()
    case_id = models.ForeignKey(
        "home.Cases",
        on_delete=models.CASCADE,
        related_name="events_case_id",
    )
    note_id = models.ForeignKey(
        "home.Notes",
        on_delete=models.CASCADE,
        related_name="events_note_id",
    )
    schedule_id = models.ForeignKey(
        "home.Schedule",
        on_delete=models.CASCADE,
        related_name="events_schedule_id",
    )
    timestamp = models.DateTimeField()
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="events_user_id",
    )
    event_type = models.CharField(
        max_length=256,
    )


class Message(models.Model):
    "Generated Model"
    message_id = models.UUIDField()
    conversation_id = models.ForeignKey(
        "home.Conversation",
        on_delete=models.CASCADE,
        related_name="message_conversation_id",
    )
    message = models.CharField(
        max_length=2048,
    )
    sent_on = models.DateTimeField(
        auto_now=True,
    )
    sender_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="message_sender_id",
    )


class Cases(models.Model):
    "Generated Model"
    case_id = models.UUIDField()
    case_status = models.PositiveSmallIntegerField()
    patient_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cases_patient_id",
    )
    lawyer_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cases_lawyer_id",
    )
    doctor_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cases_doctor_id",
    )
    description = models.CharField(
        max_length=256,
    )
    start_date = models.DateField()
    competed_on = models.DateField()
    wmg_staff_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cases_wmg_staff_id",
    )
    broker_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cases_broker_id",
    )


class Schedule(models.Model):
    "Generated Model"
    schedule_id = models.UUIDField()
    case_id = models.ForeignKey(
        "home.Cases",
        on_delete=models.CASCADE,
        related_name="schedule_case_id",
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(
        max_length=256,
    )
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="schedule_user_id",
    )


class Conversation(models.Model):
    "Generated Model"
    sender_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="conversation_sender_id",
    )
    recipient_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="conversation_recipient_id",
    )
    conversation_id = models.UUIDField(
        null=True,
        blank=True,
    )
