from django.contrib import admin
from .models import Post, Author, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug", "id")
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ("title", "author")
    list_display = ("title", "author")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)