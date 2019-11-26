from django import forms
from django.contrib import admin
from .models import JohnTest

class JohnTestAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {'fields': ["article_title"]}),
        ("Content", {"fields": ["Article_content"]})
    ]


admin.site.register(JohnTest, JohnTestAdmin)
