from django.shortcuts import render, get_object_or_404, redirect
from .models import footerdb ,indexselldb ,indexdb 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def index(request):
    homepageshow = 0
    footerdbs = footerdb.objects.all()
    indexselldbs = indexselldb.objects.all()
    indexdbs = indexdb.objects.all()
    
    context = {
        'homepageshow' :homepageshow ,
        'footerdbs' :footerdbs ,
        'indexselldbs' : indexselldbs ,
        'indexdbs' : indexdbs,
    }
    return render(request, 'pages/index.html',context)