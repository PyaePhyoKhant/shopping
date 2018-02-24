from django.shortcuts import render
from blockchain.models import Block
from django.views.generic import DetailView

def index(request):
    context = {'blocks': Block.objects.all(), 'just_test': 'Hello World!'}
    return render(request, 'blockchain/index.html', context)

def sell(request):
    return render(request, 'blockchain/sell.html')

def profile(request):
    return render(request, 'blockchain/profile.html')

class BlockDetail(DetailView):
    model = Block
    template_name = 'blockchain/detail.html'
    context_object_name = 'blk'
