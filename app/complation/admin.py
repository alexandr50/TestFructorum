from django.contrib import admin

from .models import Complation


@admin.register(Complation)
class AdminComplation(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
