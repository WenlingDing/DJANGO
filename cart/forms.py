from django import forms

class AddToCartForm(forms.Form):
    qty = forms.IntegerField(min_value=1)