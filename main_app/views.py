from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bid

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bids_index(request):
    cats = Bid.objects.all()
    return render(request, 'bids/index.html', {
        'bids': bids
    })

def bids_detail(request, bid_id):
    bid = Bid.objects.get(id=bid_id)
    id_list = bid.price.all().values_list('id')
    return render(request, 'cats/detail.html', {
        'bid': bid
    })

class BidCreate(CreateView):
    model = Bid
    fields = ['name', 'price', 'description', 'date']

class BidUpdate(UpdateView):
    model = Bid
    fields = ['name', 'price', 'description', 'date']

class BidDelete(DeleteView):
    model = Bid
    success_url = '/bids'
