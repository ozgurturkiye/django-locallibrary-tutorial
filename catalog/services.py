from typing import Iterable
from django.shortcuts import get_object_or_404
from catalog.models import Genre


def genre_list() -> Iterable[Genre]:
    return Genre.objects.all()


def genre_get(pk: int) -> Genre:
    return get_object_or_404(Genre, pk=pk)
