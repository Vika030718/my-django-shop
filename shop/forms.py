from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class SearchForm(forms.Form):
    product_name = forms.CharField(max_length=100,
                                   label='',
                                   required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Product name',
                                                                'class': 'form-control'}),)
    product_price_start = forms.IntegerField(label='Price',
                                             required=False,
                                             widget=forms.NumberInput(attrs={'placeholder': 'From',
                                                                             'class': 'form-control'}),)
    product_price_end = forms.IntegerField(label='',
                                           required=False,
                                           widget=forms.NumberInput(attrs={'placeholder': 'To',
                                                                           'class': 'form-control'}),)
    product_brand = forms.CharField(max_length=100,
                                    label='',
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Brand',
                                                                  'class': 'form-control'}),)
    pub_date = forms.DateField(widget=DatePickerInput(format='YYYY-MM-DD'),
                               required=False)