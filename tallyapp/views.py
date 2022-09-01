from re import A
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from tallyapp.models import receiptdetails
def index(request):
    comp=Companies.objects.all()
    stock=stockgroup.objects.all()
    return render(request,'index.html',{'comp':comp,'stock':stock})

def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})

def index1(request):
    return render(request,'basepage.html')

def getStates(request):
    return States.objects.all()

def createcompany(request):
    com=States.objects.all()
    country=Countries.objects.all()
    return render(request,'createcompany.html',{'com':com,'country':country})

def companycreate(request):
    
    if request.method=='POST':
            name=request.POST['name']
            mailing_name=request.POST['mailing_name']
            address1=request.POST['address1']
            address2=request.POST['address2']
            address3=request.POST['address3']
            address4=request.POST['address4']
            state=request.POST['state']
            country=request.POST['country']
            #stateId= request.POST['statehidden']
            #print('fghj')
            
            state=States.objects.get(name=state) 
            country=Countries.objects.get(name=country) 
            pincode=request.POST['pincode']
            telephone=request.POST['telephone']
            mobile=request.POST['mobile']
            fax=request.POST['fax']
            email=request.POST['email']
            website=request.POST['website']
            fin_begin=request.POST['fin_begin']
            books_begin=request.POST['books_begin']
            currency_symbol=request.POST['currency_symbol']
            formal_name=request.POST['formal_name']
            cmp=Companies.objects.filter(name=name)
            if cmp:
                messages.info(request,'Company name already exists!!')
                return redirect('createcompany')
            else:
                ctg=Companies(name=name,mailing_name=mailing_name,address1=address1,address2=address2,address3=address3,
                    address4=address4,
                    state=state,country=country,
                    pincode=pincode,
                    telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                    books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name)
                ctg.save()
            
            
             
            
            
            demo1(request, ctg.id)
            
            # return redirect('companycreated')
            return render(request,'features.html',{'ctg':ctg})
    return render(request,'createcompany.html')

def group(request,pk):
    # feature=Features.objects.get(company_id=pk)
    cmp=Companies.objects.get(id=pk)
    return render(request,'group.html',{'cmp':cmp})
def ledger(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        #ledger
        name = request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        provide_banking_details = request.POST['provide_banking_details']
        pan_no = request.POST['pan_no']
        
        #mailing_details
        mailingname = request.POST['mailingname']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        
        #banking_details
        od_limit= request.POST['od_limit']
        holder_name = request.POST['holder_name']
        acc_no = request.POST['acc_no']
        ifsc = request.POST['ifsc']
        swift_code = request.POST['swift_code']
        bank_name = request.POST['bank_name']
        branch = request.POST['branch']
        set_cheque = request.POST['set_cheque']
        ch_printing = request.POST['ch_printing']
        ch_config = request.POST['ch_config']
        
        #Asset_rounding
        rounding_method=request.POST['rounding_method']
        round_limit=request.POST['round_limit']
        
        #Asset_statutory
        assessable_calculation=request.POST['assessable_calculation']
        appropriate_to=request.POST['appropriate_to']
        gst_applicable=request.POST['gst_applicable']
        set_alter_GST=request.POST['set_alter_GST']
        type_of_supply=request.POST['type_of_supply']
        method_of_calc=request.POST['method_of_calc']
        
        
        led=Ledger.objects.filter(name=name)
        if led:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            data = Ledger(name=name,alias=alias,under=under,provide_banking_details=provide_banking_details,
                            pan_no=pan_no,company=cmp)
            data.save()
            
            #mailing_details
            data1=Ledger_Mailing_Details(mailingname=mailingname,address=address,state=state,country=country,pincode=pincode,
                                        company=cmp,ledger=data)
            data1.save()
            
            #banking_details
            data2=Ledger_Banking_Details(od_limit=od_limit,holder_name=holder_name,acc_no=acc_no,ifsc=ifsc,swift_code=swift_code,bank_name=bank_name,
                                        branch=branch,set_cheque=set_cheque,ch_printing=ch_printing,ch_config=ch_config,
                                        company=cmp,ledger=data)
            data2.save()
            
            #Asset_rounding
            data3=Ledger_Asset_Rounding(rounding_method=rounding_method,round_limit=round_limit,
                                        company=cmp,ledger=data)
            data3.save()
            
            #Asset_statutory
            data4=Ledger_Asset_Statutory(assessable_calculation=assessable_calculation,appropriate_to=appropriate_to,
                                         gst_applicable=gst_applicable,set_alter_GST=set_alter_GST,type_of_supply=type_of_supply,
                                         method_of_calc=method_of_calc,company=cmp,ledger=data)
            data4.save()
            
            
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'ledger.html',{'cmp':cmp,'grup':grup})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=Costcentre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = Costcentre(cname=cname,alias=alia,under=under,company=cmp)
            data.save()
        # return redirect('costcentre')
    ccentre=Costcentre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    cur=Currency.objects.filter(company_id=cmp)
    return render(request,'ratesofexchange.html',{'cmp':cmp,'cur':cur})

def voucher(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if Voucher.objects.filter(voucher_name=Vname).exists():
               pass
        
        mdl = Voucher(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,
            company=cmp

        )
        mdl.save()
    return render(request,'voucher.html',{'cmp':cmp})

def currency(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        symbol = request.POST['symbol']
        formal_name = request.POST['formal_name']
        currency_code = request.POST['currency_code']
        decimal_places = request.POST['decimal_places']
        show_in_millions = request.POST['show_in_millions']
        suffix_symbol = request.POST['suffix_symbol']
        symbol_and_amount = request.POST['symbol_and_amount']
        after_decimal = request.POST['after_decimal']
        amount_in_words = request.POST['amount_in_words']
        data = Currency(symbol=symbol,formal_name=formal_name,currency_code=currency_code,
                        decimal_places=decimal_places,show_in_millions=show_in_millions,
                        suffix_symbol=suffix_symbol,symbol_and_amount=symbol_and_amount,
                        after_decimal=after_decimal,amount_in_words=amount_in_words,company=cmp)
        data.save()
        # return redirect('costcentre')
    return render(request,'currency.html',{'cmp':cmp})



def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        grp=Group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = Group(
                name=gname,
                alias=alia,
                under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                used_purchase=meth,
                company=cmp
            )
            mdl.save()
        # return redirect('index')
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'group.html',{'cmp':cmp,'grup':grup})
    
def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html' ,{'com':com})


def altercompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address1=request.POST['address1']
        comp.address2=request.POST['address2']
        comp.address3=request.POST['address3']
        comp.address4=request.POST['address4']
            # state=request.POST['state']
            # country=request.POST['country']
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
            # currency_symbol=request.POST['currency_symbol']
            # formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview', {'comp':comp})
    return render(request,'editcompany.html',{'comp':comp})

def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        st=States.objects.filter(name=name)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')
def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        con=Countries.objects.filter(name=name)
        if con:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=Countries(name=name)
            data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')

def featurecompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        maintain_accounts=request.POST['maintain_accounts']
        ctg=features(maintain_accounts=maintain_accounts, company= comp)
        ctg.save()
    return render(request,'company.html')
def democreate(request):
    return render(request,'democreate.html')

def demo1(request, pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        #maintain_accounts=request.POST['maintain_accounts']
        ctg=Features(company= comp)
        ctg.save()
    return render(request,'company.html')

def features(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        if request.POST['bill_wise_entry'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        feature.save()
    return render(request,'features.html',{'ctg':c, 'ft':feature})


def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=False
    c.save()
    return redirect('shutcompany')


def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=True
    c.save()
    return redirect('shutcompany')


def alter(request):
    com=Companies.objects.all()
    return render(request,'altercompany.html')

def altercompany_view(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview1.html',{'com':com})

def listofgroup(request):
    com=Companies.objects.all()
    grp=Group.objects.all()
    return render(request,'listofgroup.html',{'com':com, 'grp':grp})

def listofledgers(request):
    com=Companies.objects.all()
    lgr=Ledger.objects.all()
    return render(request,'listofledgers.html',{'com':com, 'lgr':lgr})

def listofcostcentres(request):
    com=Companies.objects.all()
    return render(request,'listofcostcentres.html',{'com':com})

def listofcurrencies(request):
    com=Companies.objects.all()
    cur=Currency.objects.all()
    return render(request,'listofcurrencies.html',{'com':com, 'cur':cur})

def listofvouchertypes(request):
    com=Companies.objects.all()
    vhr=Voucher.objects.all()
    return render(request,'listofvouchertypes.html',{'com':com, 'vhr':vhr})

def alter_create_group(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        grp=Group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = Group(
                name=gname,
                alias=alia,
                under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                used_purchase=meth,
                company=cmp
            )
            mdl.save()
        # return redirect('index')
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'alter_create_group.html',{'cmp':cmp,'grup':grup})

    #######################################################################################3

def vouchers(request):
    com=Companies.objects.all()
    return render(request,"vouchers.html")


def creditnote(request):
    ledger=Ledger.objects.all()
    return render(request,'creditnote.html',{'ledger':ledger})


def receiptdetails(request):
    return render(request,'receiptdetails.html')

def partydetails(request):
    ledger=Ledger.objects.all()
    return render(request,'partydetails.html',{'ledger':ledger})

def debitnoteregister(request):
    cmp=Companies.objects.all()
    print(cmp)
    return render(request,'debitnoteregister.html',{'cmp':cmp})

def creditnoteregister(request):
    cmp=Companies.objects.all()
    print(cmp)
    return render(request,'creditnoteregister.html',{'cmp':cmp})

def date(request):
    return render(request,'voucherregister.html')

def load_receiptdetails(request):
    return render(request,'receiptdetails.html')

def add_receiptdetails(request):
    
    if request.method=='POST' :

        trackingno = request.POST['trackno']
        dispatchno = request.POST['dispatchno']
        dsptchthrough = request.POST['dsptchthrough']
        destination = request.POST['destination']
        carriername = request.POST['carriername']
        billoflading = request.POST['billoflading']
        motorvehicleno = request.POST['motorvehicleno']
        date = request.POST['date']
        invoiceno = request.POST['invoiceno']
        invoicedate = request.POST['invoicedate']
        data=receiptdetails(tracking_no=trackingno,dispatch_Doc_No=dispatchno,dispatch_through=dsptchthrough,destination=destination,
                            carrier_name=carriername,bill_of_ladding_no=billoflading,date=date,motorvehicle_no=motorvehicleno,
                            original_invoice_no=invoiceno,invoice_date=invoicedate,ledger=ledger)
        data.save()       
    return render(request,'partydetails.html')  

##############################################################################################
s=0
def stocksummary(request,pk):

    cmp=Companies.objects.get(id=pk)
    stock=stockgroup.objects.all()
    item=stockitems.objects.filter(stockgroup_id=pk)
    month=stockmonths.objects.all()
    stockmnth=stockmonthly.objects.filter()
    total=sum(item.values_list('value',flat=True))
    data={}
    data['cmp']=cmp
    data['stock']=stock
    data['item']=item
    data['total']=total
    data['month']=month
    data['stockmnth']=stockmnth
    print(total)
    return render(request,'stocksummary.html',data)    

def stockgroupsummary(request,pk):
    #cmp=Companies.objects.get(id=pk)
    month=stockmonths.objects.all()
    stock=stockgroup.objects.get(id=pk)
    print(stock)
    item=stockitems.objects.filter(stockgroup_id=stock)
    stockmnth=stockmonthly.objects.filter()
    print(stockmnth)
    total=sum(item.values_list('value',flat=True))
    s=total
    print(s)
    data={}
   # data['cmp']=cmp
    data['item']=item
    data['total']=total
    data['stock']=stock
    data['month']=month
    data['stockmnth']=stockmnth
    return render(request,'stockgroupsummary.html',data)  
    
def stockitemmonthly(request,pk,id):
    item=stockitems.objects.get(id=pk)
    stocks=stockmonthly.objects.filter(stockitem_id=item)
    for i in stocks:
        if i.month_id=='1' :
            stock=stockmonthly.objects.filter(stockitem_id=item,month_id='1')
            inqty1=sum(stock.values_list('inwards_quantity',flat=True))
            invalue1=sum(stock.values_list('inwards_value',flat=True))
            outqty1=sum(stock.values_list('outwards_quantity',flat=True))
            outvalue1=sum(stock.values_list('outwards_value',flat=True))
            closeqty1=sum(stock.values_list('closing_quantity',flat=True))
            closevalue1=sum(stock.values_list('closing_value',flat=True))
            
            
        else:

            stockss=stockmonthly.objects.filter(stockitem_id=item,month_id='2')
            inqty2=sum(stockss.values_list('inwards_quantity',flat=True))
            inqty2=sum(stockss.values_list('inwards_quantity',flat=True))
            invalue2=sum(stockss.values_list('inwards_value',flat=True))
            outqty2=sum(stockss.values_list('outwards_quantity',flat=True))
            outvalue2=sum(stockss.values_list('outwards_value',flat=True))
            closeqty2=sum(stockss.values_list('closing_quantity',flat=True))
            closevalue2=sum(stockss.values_list('closing_value',flat=True))
    
    
        sum1=0
        sum2=0
        sum3=0
        sum4=0
        sum5=0
        sum6=0
        sum7=0
        sum8=0
        for i in stocks:
            sum1+=i.openbalance_quantity
        for i in stocks:
            sum2+=i.openbalance_value
        for i in stocks:
            sum3+=i.inwards_quantity
        for i in stocks:
            sum4+=i.inwards_value
        for i in stocks:
            sum5+=i.outwards_quantity
        for i in stocks:
            sum6+=i.outwards_value
        for i in stocks:
            sum7+=i.closing_quantity
        for i in stocks:
            sum8+=i.closing_value

        
    data={"stocks":stocks,'item':item,
                        'inqty2':inqty2,'invalue2':invalue2,'outqty2':outqty2,'outvalue2':outvalue2,'closeqty2':closeqty2,'closevalue2':closevalue2,
                        'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,
                        'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8}
    return render(request,'stockitemmonthly.html',data)

def stockitemvoucher(request,pk,id):
    item=stockitems.objects.get(id=pk)
    display=stockmonthly.objects.get(particular=item.name)
    data=stockvoucher.objects.filter(stockmonth=display,date__month=id)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for i in data:
        sum1+=i.inwards_qty
    for i in data:
        sum2+=i.inwards_value
    for i in data:
        sum3+=i.outwards_qty
    for i in data:
        sum4+=i.outwards_value
    for i in data:
        sum5+=i.stockmonth.closing_quantity
    for i in data:
        sum6+=i.stockmonth.closing_value 
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'item':item}
    return render(request,'stockvoucher.html',context)







