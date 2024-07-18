from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.index, name="index"),
    path("book-detail/<int:book_id>", view=views.book_details, name="book-detail"),
    path("book-detail/<slug:slug>", view=views.book_details_slug, name="book-detail-slug")
]
