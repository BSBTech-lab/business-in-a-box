from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "application": "Business in a Box",
        "version": "2.0.0",
        "message": "Backend is running successfully."
    })