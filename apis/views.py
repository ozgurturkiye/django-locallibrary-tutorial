from django.http import Http404
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from catalog.models import Author


class AuthorListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = (
                "id",
                "first_name",
                "last_name",
                "date_of_birth",
                "date_of_death",
                "is_alive",
            )

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = ("first_name", "last_name", "date_of_birth", "date_of_death")

    def get(self, request):
        authors = Author.objects.all()
        serializer = self.OutputSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class AuthorDetailApi(APIView):
    """
    Retrieve, update or delete a author instance.
    """

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = (
                "id",
                "first_name",
                "last_name",
                "date_of_birth",
                "date_of_death",
                "is_alive",
            )

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = ("first_name", "last_name", "date_of_birth", "date_of_death")

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = self.OutputSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = self.InputSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
