import os
from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics, status
from sharyx.settings import CONFIG, UPLOADS_PATH

class upload(generics.ListCreateAPIView):
    """
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    """
    renderer_classes = [JSONRenderer]
    parser_classes = [MultiPartParser]

    def get(self, request):
        return JsonResponse({"detail":"Method POST not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        uploaded_file = request.data['file']
        
        # checking if the uploaded_file has a supported content type
        if uploaded_file.content_type not in CONFIG['ALLOWED_CONTENT_TYPES']:
            return JsonResponse({"detail":"content type not allowed."}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        # saving the uploaded_file

        return JsonResponse({"detail":"success."})