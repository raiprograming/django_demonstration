from django.contrib import admin
from django.urls import path
from my_portfolio_app import views

app_name="my_portfolio_app"

urlpatterns = [

path('my_first_url',views.my_first_view,name='my_first'),

path('',views.my_home,name='home'),
path('details',views.my_details,name="details"),
path('images',views.my_images,name="image"),
path('contact',views.my_contact,name="contact"),
path('contact_form_submit',views.contact_form_submit,name="contact_form_submit"),
path('records',views.my_records,name="show_data"),
path('data',views.one_data,name="one_data"),
path('data_process',views.send_record,name="one_record")
]
