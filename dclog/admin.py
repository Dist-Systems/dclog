from django.contrib import admin
from nhdc.dclog import models

class LogAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Log,   LogAdmin)
admin.site.register(models.Alarm, LogAdmin)