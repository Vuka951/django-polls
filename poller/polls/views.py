from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

# Display questions


def index(request):
    return render(request, 'polls/index.html')
