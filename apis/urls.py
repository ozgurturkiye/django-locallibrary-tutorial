from django.urls import path, include

from .views import AuthorListApi


author_patterns = [
    path("", AuthorListApi.as_view(), name="author-list"),
    # path("<int:pk>", AuthorListApi.as_view(), name="author-detail"),
]

urlpatterns = [
    path("authors/", include((author_patterns, "authors"))),
]
