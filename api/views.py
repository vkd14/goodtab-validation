from django.http import HttpResponse
from rest_framework import generics
from . import query
from . import serializers


class UploadFileView(generics.CreateAPIView):
    serializer_class = serializers.FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        resource_name = serializer.validated_data['resource_name']
        print(f"{resource_name}")
        query.upload_resource(resource_name, file)
        return HttpResponse("Upload Successful!!")
