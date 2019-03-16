from django.shortcuts import render
import os,sys
# sys.path()
# Create your views here.
# from score import get_answer
from score import main



def index(request):
    main()

    return render(request,"index.html")