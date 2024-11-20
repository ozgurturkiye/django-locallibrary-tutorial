from django.urls import path, include

from .views import AuthorListApi, AuthorDetailApi, GenreListApi, GenreDetailApi


author_patterns = [
    path("", AuthorListApi.as_view(), name="author-list"),
    path("<int:pk>", AuthorDetailApi.as_view(), name="author-detail"),
]

genre_patterns = [
    path("", GenreListApi.as_view(), name="genre-list"),
    path("<int:pk>", GenreDetailApi.as_view(), name="genre-detail"),
]

urlpatterns = [
    path("authors/", include((author_patterns, "authors"))),
    path("genres/", include((genre_patterns, "genres"))),
]
