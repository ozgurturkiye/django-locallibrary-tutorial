from rest_framework.views import APIView
from rest_framework import serializers
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
