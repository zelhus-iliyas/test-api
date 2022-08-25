from django.contrib import admin

from new.models import NewJson

# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('_id', 'created_date')
admin.site.register(NewJson,NewAdmin)