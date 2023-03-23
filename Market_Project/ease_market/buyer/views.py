from django.shortcuts import render
from django.views import View
#from seller.models import Seller
#from django.app import apps
# model = apps.get_model('seller', 'Seller')

from seller.models import Seller

# Create your views here.
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        # items = model.objects.all()
        items = Seller.objects.all()
        print(items)
        context = {'items': items }
        return render(request, 'buyer/all_products.html', context)

def product_detail(request, slug):
	#return HttpResponse(slug)
	item = Seller.objects.get(slug=slug)
	context = {'item': item}
	return render(request, 'buyer/product_detail.html', context)