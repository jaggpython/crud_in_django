from django.contrib import admin
from .models import Members

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname"

admin.site.register(Members,MemberAdmin)
