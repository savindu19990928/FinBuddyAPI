from django.contrib import admin
from .models import SupportRequest, SupportReply

class SupportReplyInline(admin.StackedInline):
    model = SupportReply
    extra = 1

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'status', 'created_at')
    list_filter = ('status',)
    inlines = [SupportReplyInline]

admin.site.register(SupportReply)
