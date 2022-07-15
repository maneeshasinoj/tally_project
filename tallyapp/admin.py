from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Countries,CountriesAdmin)

#admin.site.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(States,StatesAdmin)

#admin.site.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Companies,CompaniesAdmin)

#admin.site.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Group,GroupAdmin)

admin.site.register(Features)
admin.site.register(Costcentre)

#admin.site.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=('symbol',)
admin.site.register(Currency,CurrencyAdmin)

#admin.site.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display=('voucher_name',)
admin.site.register(Voucher,VoucherAdmin)


#admin.site.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Ledger,LedgerAdmin)

admin.site.register(Ledger_Mailing_Details)
admin.site.register(Ledger_Banking_Details)
admin.site.register(Ledger_Asset_Rounding)
admin.site.register(Ledger_Asset_Statutory)