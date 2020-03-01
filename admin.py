from django.contrib import admin
from my_portfolio_app.models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]


# Register your models here.
admin.site.register(ContactForm,ContactFormAdmin)
admin.site.site_header="raiprogramming"
admin.site.site_title="Django title"
admin.site.index_title="my_port_folio"