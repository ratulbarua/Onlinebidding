from django.shortcuts import render
from auctionItem.models import Lot
# Create your views here.

def live(request):
    live = Lot.objects.all()
    return render(request,'live/live.html', {'liv': live})