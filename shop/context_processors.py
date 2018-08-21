from .models import Category
from .forms import CallMe

def menu(request):
    category_list = Category.objects.all()
    return {"category_list": category_list}

def callme(request):
    send_email_form = CallMe()
    return {"send_email_form": send_email_form}
