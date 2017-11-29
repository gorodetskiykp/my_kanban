from django.contrib import admin

from .models import Panel, TaskChannel, TaskOwner, Task, TaskNote


admin.site.register(Panel)
admin.site.register(TaskChannel)
admin.site.register(TaskOwner)
admin.site.register(Task)
admin.site.register(TaskNote)
