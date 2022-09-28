import os
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics, status
from sharyx.settings import CONFIG, UPLOADS_PATH
from app.utils import rename_upload

class upload(generics.ListCreateAPIView):
    # TODO crypt it, hash it or smth
    """
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    """
    renderer_classes = [JSONRenderer]
    parser_classes = [MultiPartParser]

    def get(self, request):
        return JsonResponse({"detail":"Method GET not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        uploaded_file = request.data['file']

        # checking if the size of the uploaded_file is under 50MB
        if uploaded_file.size > CONFIG['MAX_FILE_SIZE']: return JsonResponse({"detailt":"file size too large."}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        # checking if the uploaded_file has a supported content type
        if uploaded_file.content_type not in CONFIG['ALLOWED_CONTENT_TYPES']: return JsonResponse({"detail":"content type not allowed."}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        # saving the uploaded_file, giving it a random name and checking if it already exists or not, and also saving the path
        file = rename_upload(uploaded_file)

        # returning the url for the uploaded_file
        return JsonResponse({"url":f"{request.scheme}://{request.get_host()}/uploads/{file[1]}"})