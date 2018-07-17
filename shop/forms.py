from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class SearchForm(forms.Form):
    product_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'placeholder': 'Product name'}),
                                   label='',
                                   required=False)
    product_price_start = forms.IntegerField(label='', required=False)
    product_price_end = forms.IntegerField(label='', required=False)
    product_brand = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Brand'}), label='', required=False)
    pub_date = forms.DateField(widget=DatePickerInput(format='YYYY-MM-DD'), required=False)