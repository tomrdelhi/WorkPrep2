from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import Metrics

def index(request):
	return HttpResponse("Hello, World!")

def get_by_ID(request, transaction_id):
	transaction = get_object_or_404(Metrics, pk=transaction_id)
	return render(request, 'SimpleGetters/TransactionOverview.html', {'transaction' : transaction})
	#return JsonResponse({'transaction':transaction})

def show_attribute(request, transaction_id, attribute_name):
	transaction = get_object_or_404(Metrics, pk=transaction_id)
	attribute_value = getattr(transaction, attribute_name, False)
	if not attribute_value:
		attribute_list = transaction.__dict__.keys()
		return render(request, 'SimpleGetters/AttributeFailToFindError.html', {'attribute_name':attribute_name, 
			'transaction_id':transaction_id, 'attribute_list':attribute_list})
	else:
		return render(request, 'SimpleGetters/TransactionDetail.html', {'transaction' : transaction, 
			'attribute_name':attribute_name, 'attribute_value':attribute_value})
# Create your views here.
