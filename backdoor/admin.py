from django.contrib import admin

from backdoor.models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'enable')

admin.site.register(Url, UrlAdmin)