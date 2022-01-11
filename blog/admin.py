from django.contrib import admin

from blog.modells import Tag, Post

admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)