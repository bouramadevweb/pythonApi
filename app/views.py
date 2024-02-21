""" import django """
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from app.models import CLUB_ODS


# from scripts.etl_ods import ODS
# Create your views here.
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render
# from app.models import CLUB_ODS

def index(request):
    ods_club = CLUB_ODS.objects.all()
    paginator = Paginator(ods_club, 20)
    page = request.GET.get('page', 1)

    try:
        ods_club = paginator.page(page)
    except PageNotAnInteger:
        ods_club = paginator.page(1)
    except EmptyPage:
        ods_club = paginator.page(paginator.num_pages)

    context = {'title': 'ods club', 'ods_club': ods_club}
    return render(request, 'index.html', context)

def prix(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    context = {'prix': 'prix'}
    return render(request, 'prix.html', context)

def vente(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    context = {'vente': 'hello world' }
    return render(request,'ventes.html',context)

def etlindex(request):
    """_summary_

    Args:
        request (_type_): _description_
    """
    club = CLUB_ODS.objects.all()
    context = {'club': club}
    render(request, 'data_reader.html', context)
