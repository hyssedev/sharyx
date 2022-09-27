from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, status

class upload(generics.ListCreateAPIView):
    """
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    """
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return JsonResponse({"detail":"Method POST not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        pass