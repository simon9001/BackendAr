from celery import shared_task
from django.utils.timezone import now
from core.models import MeetingHistory

@shared_task
def store_meeting_history(user_id, meeting_name):
    MeetingHistory.objects.create(user_id=user_id, meeting_name=meeting_name, created_at=now())
    return f"Meeting '{meeting_name}' stored for user {user_id}"
