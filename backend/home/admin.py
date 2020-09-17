from django.contrib import admin
from .models import Cases, Conversation, Events, Message, Notes, Schedule

admin.site.register(Cases)
admin.site.register(Schedule)
admin.site.register(Conversation)
admin.site.register(Notes)
admin.site.register(Events)
admin.site.register(Message)

# Register your models here.
