from django.contrib import admin

from .models import Tag, Post


admin.site.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post)

