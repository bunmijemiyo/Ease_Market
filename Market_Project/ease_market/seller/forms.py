from django import forms

from .models import Seller

class CreateSeller(forms.ModelForm):

	class Meta:
		model = Seller
		fields = [
			'name', 
	        'price',
	        'quantity',
	        'description',
			'slug',
			'thumb'
	    ]
