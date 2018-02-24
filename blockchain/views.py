from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from blockchain.models import Block
from django.views.generic import DetailView


def index(request):
    if 'search_value' not in request.GET:
        context = {'blocks': Block.objects.all()}
    else:
        search_value = request.GET['search_value']
        context = {'blocks': Block.objects.filter(
            Q(title__icontains=search_value) | Q(description__icontains=search_value) | Q(
                comment__icontains=search_value))}
    return render(request, 'blockchain/index.html', context)


# def details(request):
#     return render(request, 'blockchain/details.html')

class BlockDetail(DetailView):
    model = Block
    template_name = 'blockchain/detail.html'
    context_object_name = 'block'


@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect('/')
