from django.urls import path, include

from .views import AuthorListApi, AuthorDetailApi


author_patterns = [
    path("", AuthorListApi.as_view(), name="author-list"),
    path("<int:pk>", AuthorDetailApi.as_view(), name="author-detail"),
]

urlpatterns = [
    path("authors/", include((author_patterns, "authors"))),
]
