from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def handler400(request, exception):
    # footerAdmins = footerAdmin.objects.all()
    # context = {
    #     'footerAdmins':footerAdmins,
    # }
    # return render(request, 'pages/404.html',context)
    return render(request, 'indexpage/404.html')
def handler403(request, exception):
    return render(request, 'indexpage/404.html')

def handler404(request, exception):
    return render(request, 'indexpage/404.html')

def handler500(request):
    return render(request, 'indexpage/404.html')


