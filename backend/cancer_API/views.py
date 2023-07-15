from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse('The server is running!')

def predict(request):
    return JsonResponse({'prediction': 'Not implemented yet'})