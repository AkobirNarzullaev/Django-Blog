from django.contrib import admin
from .models import Post, Creator

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = []
admin.site.register(Creator)