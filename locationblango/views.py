from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Room
from django.db.models import Q

# Create your views here.
def frontpage(request):
    if 'search' in request.GET:
        search = request.GET.get('search')
        rooms_list = Room.objects.filter(Q(number__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search))
    else:
        
        rooms_list = Room.objects.all()


    paginator = Paginator(rooms_list, 12)
    page = request.GET.get('page',1)
    try:
        rooms = paginator.get_page(page)
    except Exception:
        rooms = paginator.page(1)

    return render(request, 'locationblango/frontpage.html', {'rooms':rooms})
