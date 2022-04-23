from django.shortcuts import render, get_object_or_404, redirect
from indexpage.models import footerdb  
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def store(request):
    homepageshow = 1
    footerdbs = footerdb.objects.all()
   
    context = {
        'homepageshow' :homepageshow ,
        'footerdbs' :footerdbs ,
        
    }
    return render(request, 'pages/store.html',context)