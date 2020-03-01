from django.shortcuts import render,HttpResponseRedirect
from my_portfolio_app.models import ContactForm
from django.urls import reverse
# Create your views here.
def my_first_view(request):
    return render(request,'my_portfolio_app/first_html_page.html')  
def my_home(request):
    return render(request,'my_portfolio_app/home.html')
def my_details(request):
    return render(request,'my_portfolio_app/details.html')
def my_images(request):
    return render(request,'my_portfolio_app/img.html')
def my_contact(request):
    return render(request,'my_portfolio_app/contact.html')
    
def contact_form_submit(request):
    if request.method=="POST":
        full_name=request.POST["fname"]
        email_id=request.POST["mail"]
        contact_number=request.POST["no"]
        message=request.POST["msg"]
        ContactForm.objects.create(full_name=full_name,email_id=email_id,contact_number=contact_number,message=message)
    #return HttpResponseRedirect(reverse('my_portfolio_app:contact'))
    return render(request,'my_portfolio_app/img.html')
def my_records(request):
    records=ContactForm.objects.filter(full_name="rai")
    data={'records_from_database':records}

    return render(request,'my_portfolio_app/show.html',data)
def one_data(request):
    return render(request,'my_portfolio_app/record.html')

def send_record(request):
    if request.method=="POST":
        name=request.POST["fname"]
        record=ContactForm.objects.filter(full_name=name)
        data={'record':record}
        return render(request,'my_portfolio_app/data.html',data)
