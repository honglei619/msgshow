from django.contrib import admin
from myapp.models import Queue,QueueAdmin,Result,ResultAdmin
admin.site.register(Queue,QueueAdmin)
admin.site.register(Result,ResultAdmin)
