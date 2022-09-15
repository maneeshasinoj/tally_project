from django.db import models
from re import T

import app1

# Create your models here.

# Ajmy

class StockGroup(models.Model):
    grp_name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.grp_name

class Stockcategory(models.Model):
    cat_name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.cat_name

class stock_item(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    rateper=models.IntegerField(null=True)
    value=models.IntegerField(null=True)    
    group = models.ForeignKey(StockGroup,on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Stockcategory,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class voucherlist(models.Model):
    item = models.ForeignKey(stock_item,on_delete=models.SET_NULL, null=True) 
    party_name=models.CharField(max_length=100,null=True)
    vouch_type=models.CharField(max_length=100,null=True)
    date=models.DateField()
    quantity=models.IntegerField()
    rateper=models.IntegerField(null=True)
    value=models.IntegerField() 
    group = models.ForeignKey(StockGroup,on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Stockcategory,on_delete=models.SET_NULL, null=True)

class company(models.Model):
    comp_name=models.CharField(max_length=100,null=True)
    start_date=models.DateField()    


# praveen , Jisha, Riya

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)

class Features(models.Model):
    maintain_accounts = models.CharField(max_length=10)
    bill_wise_entry = models.CharField(max_length=10)
    cost_centres = models.CharField(max_length=10)
    interest_calc = models.CharField(max_length=10)
    maintain_inventory = models.CharField(max_length=10)
    integrate_accounts = models.CharField(max_length=10)
    multiple_price_level = models.CharField(max_length=10)
    batches = models.CharField(max_length=10)
    expirydate_batches = models.CharField(max_length=10)
    joborder_processing = models.CharField(max_length=10)
    cost_tracking = models.CharField(max_length=10)
    job_costing= models.CharField(max_length=10)
    discount_invoices = models.CharField(max_length=10)
    Billed_Quantity = models.CharField(max_length=10)
    gst = models.CharField(max_length=10)
    tds = models.CharField(max_length=10)
    tcs = models.CharField(max_length=10)
    vat = models.CharField(max_length=10)
    excise = models.CharField(max_length=10)
    servicetax = models.CharField(max_length=10)
    payroll = models.CharField(max_length=10)
    multiple_addrss = models.CharField(max_length=10)
    vouchers = models.CharField(max_length=10)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)

class GST(models.Model):
    state = models.CharField(max_length=255,null=True)
    reg_type = models.CharField(max_length=50,null=True)
    assessee = models.CharField(max_length=50,null=True)
    gst_applicable = models.CharField(max_length=50,null=True)
    gstin = models.CharField(max_length=100,null=True)
    periodicity = models.CharField(max_length=50,null=True)
    flood_cess = models.CharField(max_length=20,null=True)
    applicable_from = models.CharField(max_length=50,null=True)
    gst_rate_details = models.CharField(max_length=20,null=True)
    advance_receipts = models.CharField(max_length=20,null=True)
    reverse_charge = models.CharField(max_length=20,null=True)
    gst_classification = models.CharField(max_length=20,null=True)
    bond_details = models.CharField(max_length=20,null=True)
    tax_rate = models.CharField(max_length=20,null=True)
    tax_calc = models.CharField(max_length=100,null=True)
    tax_purchase = models.CharField(max_length=20,null=True)
    
    eway_bill = models.CharField(max_length=20,null=True)
    applicable_form = models.CharField(max_length=50,null=True)
    threshold_includes = models.CharField(max_length=255,null=True)
    threshold_limit = models.IntegerField(null=True)
    intrastate = models.CharField(max_length=20,null=True)
    threshold_limit2 = models.IntegerField(null=True)
    print_eway = models.CharField(max_length=20,null=True)

    e_invoice = models.CharField(max_length=20,null=True)
    app_from = models.CharField(max_length=50,null=True)
    billfrom_place = models.CharField(max_length=50,null=True)
    dperiod = models.CharField(max_length=50,null=True)
    send_ewaybill = models.CharField(max_length=50,null=True)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)
    
class gst_lutbond(models.Model):
    lutbond = models.CharField(max_length=50)
    validity_from = models.DateField()
    validity_to = models.DateField()  

class gst_taxability(models.Model):
    taxability = models.CharField(max_length=50)
    applicable_dt = models.CharField(max_length=50,null=True)
    integrated_tax = models.CharField(max_length=50)
    cess = models.CharField(max_length=50)
    flood_cess = models.CharField(max_length=50)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True) 

class Tds_Details(models.Model):
    tan_regno = models.CharField(max_length=40)
    tan = models.CharField(max_length=40)
    deductor_type = models.CharField(max_length=100)
    deductor_branch = models.CharField(max_length=255)
    person_details = models.CharField(max_length=255)
    ignore_it = models.CharField(max_length=40)
    active_tds = models.CharField(max_length=40)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)

class tds_person(models.Model):
    name = models.CharField(max_length=255,null=True)
    son_daughter = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)
    flat_no = models.CharField(max_length=10,null=True)
    building = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    town = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=15,null=True)
    std = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True) 

class tally_group(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    group_name = models.CharField(max_length=255)
    group_alias = models.CharField(max_length=255)
    group_under = models.CharField(max_length=255)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255)
    debit_credit = models.CharField(max_length=255)
    calculation = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)

class currencyAlteration(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    Symbol = models.CharField(max_length=255)
    FormalName = models.CharField(max_length=255)
    ISOCurrency = models.CharField(max_length=30,null=True)
    DecimalPlace = models.IntegerField()
    showAmount = models.CharField(max_length=20)
    suffixSymbol = models.CharField(max_length=20)
    AddSpace = models.CharField(max_length=20)
    wordRep = models.CharField(max_length=255,null=True)
    DecimalWords = models.IntegerField()

class company_alt_currency(models.Model):
    c_symbol = models.CharField(max_length=255)
    formal_name = models.CharField(max_length=255)
    iso_Ccode = models.CharField(max_length=30,null=True)
    decimal_place = models.IntegerField()
    show_amtM = models.CharField(max_length=20)
    suffix_smblA = models.CharField(max_length=20)
    add_space = models.CharField(max_length=20)
    word_rep = models.CharField(max_length=255,null=True)
    no_decimal = models.IntegerField()
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class rateofexchange(models.Model):
    date_ROE = models.DateField(null=True)
    currencyName =models.CharField(max_length=100, null=True)
    std_rate = models.CharField(max_length=100, null=True)
    sell_voucher_rate = models.CharField(max_length=100, null=True)
    sell_specified_rate = models.CharField(max_length=100, null=True)
    buy_specified_rate = models.CharField(max_length=100, null=True)
    buy_voucher_rate = models.CharField(max_length=100, null=True)
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)


class cost_centre(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    c_name=models.CharField(max_length=255)
    cost_alias = models.CharField(max_length=255)
    under = models.CharField(max_length=255)

class Voucher(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    voucher_name = models.CharField(max_length=255,null=True)
    alias = models.CharField(max_length=255,null=True)
    voucher_type = models.CharField(max_length=255,null=True)
    abbreviation = models.CharField(max_length=255,null=True)
    voucherActivate = models.CharField(max_length=20,null=True)
    voucherNumber = models.CharField(max_length=200,null=True)
    preventDuplicate = models.CharField(max_length=20,null=True)
    advance_con = models.CharField(max_length=20,null=True)
    voucherEffective = models.CharField(max_length=20,null=True)
    transaction = models.CharField(max_length=20,null=True)
    make_optional = models.CharField(max_length=20,null=True)
    voucherNarration = models.CharField(max_length=20,null=True)
    provideNarration = models.CharField(max_length=20,null=True)
    manu_jrnl = models.CharField(max_length=20,null=True)
    track_purchase = models.CharField(max_length=20,null=True)
    enable_acc = models.CharField(max_length=20,null=True)
    prnt_VA_save = models.CharField(max_length=20,null=True)
    prnt_frml = models.CharField(max_length=20,null=True)
    jurisdiction = models.CharField(max_length=20,null=True)
    title_print = models.CharField(max_length=20,null=True)
    set_alter = models.CharField(max_length=20,null=True)
    pos_invoice = models.CharField(max_length=20,null=True)
    msg_1 = models.CharField(max_length=255,null=True)
    msg_2 = models.CharField(max_length=255,null=True)
    default_bank = models.CharField(max_length=255,null=True)
    name_class = models.CharField(max_length=255,null=True)

class tally_ledger(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True)
    under = models.CharField(max_length=255)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True)
    mname = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=6,null=True)
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_uin = models.CharField(max_length=100,null=True)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True)

    set_odl = models.CharField(max_length=255,null=True)
    ac_holder_nm = models.CharField(max_length=255,null=True)
    acc_no = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    SA_cheque_bk = models.CharField(max_length=20,null=True)
    Echeque_p = models.CharField(max_length=20,null=True)
    SA_chequeP_con = models.CharField(max_length=20,null=True)
    
    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    valuation_type = models.CharField(max_length=100,null=True)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True)
    setalter_gstdetails = models.CharField(max_length=20,null=True)
    type_of_supply = models.CharField(max_length=100,null=True)
    assessable_value = models.CharField(max_length=100,null=True)
    appropriate_to = models.CharField(max_length=100,null=True)
    method_of_calculation = models.CharField(max_length=100,null=True)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)

class ledger_cheque_demension(models.Model):
    cheque_width = models.IntegerField(null=True)
    cheque_height = models.IntegerField(null=True)
    startL_leftEdge = models.IntegerField(null=True)
    startL_topEdge = models.IntegerField(null=True)
    distancel_leftEdge = models.IntegerField(null=True)
    distancel_topEdge = models.IntegerField(null=True)
    date_style = models.CharField(max_length=100,null=True)
    date_seperator = models.CharField(max_length=10,null=True)
    separator_width = models.IntegerField(null=True)
    character_distance = models.FloatField(null=True)
    Pdistancel_leftEdge = models.IntegerField(null=True)
    Pdistancel_topEdge = models.IntegerField(null=True)
    area_width = models.IntegerField(null=True)
    secondL_DTE = models.IntegerField(null=True)
    secondfirstL_height = models.IntegerField(null=True)
    firstL_dTE = models.IntegerField(null=True)
    sl_fisrtl_LE = models.IntegerField(null=True)
    sl_secondl_LE = models.IntegerField(null=True)
    amount_widtharea = models.IntegerField(null=True)
    currencyFNM_print = models.CharField(max_length=10,null=True)
    df_TE = models.IntegerField(null=True)
    startL_LE = models.IntegerField(null=True)
    amt_widtharea = models.IntegerField(null=True)
    currencyS_print = models.CharField(max_length=10,null=True)
    company_name = models.CharField(max_length=10,null=True)
    print_CN = models.CharField(max_length=10,null=True)
    salutation_Fsign = models.CharField(max_length=100,null=True)
    salutation_Ssign = models.CharField(max_length=100,null=True)
    top_Edistance = models.IntegerField(null=True)
    startLF_leftE = models.IntegerField(null=True)
    width_sign_area = models.IntegerField(null=True)
    height_sign_area = models.IntegerField(null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class ledger_bankdetails(models.Model):
    transaction_type = models.CharField(max_length=100)
    cross_using = models.CharField(max_length=100)
    acc_no = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class bank_name(models.Model):
    bankname = models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class ledger_chequebook(models.Model):
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    no_of_cheques = models.IntegerField()
    cheque_bookname = models.CharField(max_length=100)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class ledger_gstvalues(models.Model):
    nature_of_transaction = models.CharField(max_length=255)
    taxable = models.CharField(max_length=100,null=True)
    taxability = models.CharField(max_length=100,null=True)
    appicable_from = models.DateField(null=True)
    integrated_tax = models.CharField(max_length=100,null=True)
    cess = models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class voucher_advanceconf(models.Model):
    starting_no = models.IntegerField()
    numerical_partwidth = models.IntegerField()
    prefill_zero = models.CharField(max_length=10)
    restart_applicable_dt = models.DateField()
    restart_startingno = models.IntegerField()
    restart_particular = models.CharField(max_length=100)
    prefix_applicable_dt = models.DateField()
    prefix_particular = models.CharField(max_length=100)
    suffix_applicable_dt = models.DateField()
    suffix_particular = models.CharField(max_length=100)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class ledger_taxreggst(models.Model):
    registration_type = models.CharField(max_length=255)
    assessee_teritory = models.CharField(max_length=10)
    commerce_operator = models.CharField(max_length=10)
    party_deemed = models.CharField(max_length=10)
    party_type = models.CharField(max_length=100)
    gstin_uin = models.CharField(max_length=100)
    transporter = models.CharField(max_length=10)
    transporter_id = models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Currency_alt(models.Model):
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)
    stddate=models.CharField(max_length=255,blank=True,null=True)
    stdrate=models.CharField(max_length=255,default='null')
    selldate=models.CharField(max_length=255,blank=True,null=True)
    selvorate=models.CharField(max_length=255,default='null')
    sellrate=models.CharField(max_length=255,default='null')
    buydate=models.CharField(max_length=255,blank=True,null=True)
    buyvorate=models.CharField(max_length=255,default='null')
    buyrate=models.CharField(max_length=255,default='null')
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class cost_center(models.Model):
    c_name = models.CharField(max_length=255)
    cost_alias = models.CharField(max_length=255)
    under = models.CharField(max_length=255)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    

# Rafi

class CreateStockGrp(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)

# class CreateStockGrp(models.Model):
#     name=models.CharField(max_length=100)
#     alias=models.CharField(max_length=100)
#     under_name=models.CharField(max_length=50)
#     quantities=models.CharField(max_length=50)

class CreateEmployeeGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class UnitCrt(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    type=models.CharField(max_length=100,null=True)
    symbol=models.CharField(max_length=20,null=True)
    formal_name=models.CharField(max_length=50,null=True)

# class UnitCrt(models.Model):
#     type=models.CharField(max_length=100,null=True)
#     symbol=models.CharField(max_length=20,null=True)
#     formal_name=models.CharField(max_length=50,null=True)
#     uqc=models.CharField(max_length=50,null=True)
#     decimal=models.IntegerField(null=True)
#     first_unit=models.CharField(max_length=50,null=True)
#     conversion=models.CharField(max_length=30,null=True)
#     second_unit=models.CharField(max_length=30,null=True)

class pancin(models.Model):
    pan=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)

class cost(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class employee_crt(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    doj=models.CharField(max_length=30)
    salary=models.CharField(max_length=50)
    empno=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    function_name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    bld_grp=models.CharField(max_length=20)
    father_mother=models.CharField(max_length=20)
    spouse=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phn=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    bank=models.CharField(max_length=50)
    incometax=models.CharField(max_length=20)
    adhar=models.CharField(max_length=20)
    uan=models.CharField(max_length=20)
    pf=models.CharField(max_length=20)
    pr=models.CharField(max_length=20)
    esi=models.CharField(max_length=20)

class bank(models.Model):
    accno=models.CharField(max_length=50)
    ifsc_Code=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)

class bank_crt(models.Model):
    accno=models.CharField(max_length=50)
    ifsc_Code=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)

class attendance_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=50,null=True)
    attendance=models.CharField(max_length=50,null=True)
    period=models.CharField(max_length=50,null=True)
    units=models.CharField(max_length=50,null=True)

class payhead_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    attendance_type=models.CharField(max_length=100,null=True)
    production_type=models.CharField(max_length=100,null=True)

class salary_crt(models.Model):
    name=models.CharField(max_length=50,null=True)
    alias=models.CharField(max_length=50,null=True)
    date=models.CharField(max_length=100,null=True)
    pay_head_name=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    pay_head_type=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)

class payroll_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    allias=models.CharField(max_length=100,null=True)
    voucher_type=models.CharField(max_length=100,null=True)
    abbreviation=models.CharField(max_length=100,null=True)
    activate_voucher=models.CharField(max_length=100,null=True)
    voucher_numbering_method=models.CharField(max_length=100,null=True)
    effective_dates=models.CharField(max_length=100,null=True)
    narration_voucher=models.CharField(max_length=100,null=True)
    print_voucher=models.CharField(max_length=100,null=True)
    classs=models.CharField(max_length=100,null=True)
    
class stock_item_crt(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    additional=models.CharField(max_length=100,null=True)
    gst=models.CharField(max_length=100,default="")
    supply=models.CharField(max_length=100,default="")
    rduty=models.CharField(max_length=100,default="")

# class stock_item_crt(models.Model):
#     name=models.CharField(max_length=100,null=True)
#     alias=models.CharField(max_length=100,null=True)
#     under=models.CharField(max_length=100,null=True)
#     category=models.CharField(max_length=100,null=True)
#     units=models.CharField(max_length=100,null=True)
#     batches=models.CharField(max_length=100,null=True)
#     manufacturing_date=models.CharField(max_length=100,null=True)
#     expiry_dates=models.CharField(max_length=100,null=True)
#     rate_of_duty=models.CharField(max_length=100,null=True)
#     quantity=models.CharField(max_length=100,null=True)
#     rate=models.CharField(max_length=100,null=True)
#     per=models.CharField(max_length=100,null=True)
#     value=models.CharField(max_length=100,null=True)
#     additional=models.CharField(max_length=100,null=True)
#     gst=models.CharField(max_length=100,default="")
#     supply=models.CharField(max_length=100,default="")
#     rduty=models.CharField(max_length=100,default="")
    
class Price_level_crt(models.Model):
    number=models.CharField(max_length=100,null=True)
    
class allocate_stock(models.Model):
    allocate=models.CharField(max_length=100,null=True)
    for_allocate=models.CharField(max_length=100,null=True)
    godown=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    amount=models.CharField(max_length=100,null=True)


# Ann

class Sales(models.Model):#ann sales table
    partyAccntname = models.CharField(max_length=225)
    currentbalancep = models.CharField(max_length=225,null=True)#current balance of party
    salesledger = models.CharField(max_length=225)
    currentbalancesl = models.IntegerField(null=True)#balance of corresponding sales ledger
    nameofitem=models.CharField(max_length=225,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(default=0)
    sales_date=models.DateField(null=True)
    total=models.IntegerField(default=0)
   # voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)

class Purchase(models.Model):#ann purchase tabel
    supplierinvoiceno= models.CharField(max_length=225,default=True)
    partyAccntname = models.CharField(max_length=225,default=True)
    currentbalancep = models.CharField(max_length=225,null=True)
    currentbalancepl = models.CharField(max_length=225,null=True)
    purchaseledger = models.CharField(max_length=225,default=True)
    nameofitem=models.CharField(max_length=225,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    purchase_date=models.DateField(null=True) 
    #voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)

class Journal(models.Model):#ann journal table
     journalledger = models.CharField(max_length=225,null=True)
     journal_date=models.DateField(null=True)  

class Particular(models.Model):#ann Particular table
    particularsby = models.CharField(max_length=225,null=True)
    particularsto = models.CharField(max_length=225,null=True)
    credit = models.IntegerField(default=0,null=True)#current balance of party
    debit = models.IntegerField(null=True,default=0)#balance of corresponding sales ledger
    journal=models.ForeignKey(Journal,on_delete=models.CASCADE,blank=True,null=True)  


# Niyas

class analysis_view(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    particular=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    iquantity=models.IntegerField(null=True)
    ieff_rate=models.IntegerField(null=True)
    ivalue=models.IntegerField(null=True)
    oquantity=models.IntegerField(null=True)
    oeff_rate=models.IntegerField(null=True)
    ovalue=models.IntegerField(null=True)

# class analysis_view(models.Model):
#     particular=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
#     iquantity=models.IntegerField(null=True)
#     ieff_rate=models.IntegerField(null=True)
#     ivalue=models.IntegerField(null=True)
#     oquantity=models.IntegerField(null=True)
#     oeff_rate=models.IntegerField(null=True)
#     ovalue=models.IntegerField(null=True)

class group_ananysis_view(models.Model):
    particular=models.ForeignKey(CreateStockGrp,on_delete=models.CASCADE)
    iquantity=models.IntegerField(null=True)
    ieff_rate=models.IntegerField(null=True)
    ivalue=models.IntegerField(null=True)
    oquantity=models.IntegerField(null=True)
    oeff_rate=models.IntegerField(null=True)
    ovalue=models.IntegerField(null=True)

class CreateGodown(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

# class CreateGodown(models.Model):
#     name=models.CharField(max_length=100)
#     alias=models.CharField(max_length=100)
#     under_name=models.CharField(max_length=50)
#     itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE,default='')

class purchase_model(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

# class purchase_model(models.Model):
#     itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
#     name=models.CharField(max_length=255)
#     date=models.DateField(auto_now_add=True)
#     qnt=models.IntegerField()
#     brate=models.IntegerField()
#     bvalue=models.IntegerField()
#     addcost=models.IntegerField()
#     totalvalue=models.IntegerField()

class sale_model(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

# class sale_model(models.Model):
#     itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
#     name=models.CharField(max_length=255)
#     date=models.DateField(auto_now_add=True)
#     qnt=models.IntegerField()
#     brate=models.IntegerField()
#     bvalue=models.IntegerField()
#     addcost=models.IntegerField()
#     totalvalue=models.IntegerField()

class CreateStockCateg(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

# class CreateStockCateg(models.Model):
#     itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE,default='')
#     name=models.CharField(max_length=100)
#     alias=models.CharField(max_length=100)
#     under_name=models.CharField(max_length=50)
#     qnt=models.IntegerField()
#     cost=models.IntegerField()
#     saleprice=models.IntegerField()


# Jerin

class items(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)

    def __str__(self):
      return self.items

class receivable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def __str__(self):
      return self.party_name


class payitems(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)

    def __str__(self):
      return self.items

class payable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(payitems,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def total(self):
      tot=sum(self.pending_amound)
      return tot

    def __str__(self):
      return self.party_name  

class grunder(models.Model):
    und=models.CharField(max_length=255)  

    def __str__(self):
      return self.und  



class GroupModel(models.Model):
    group_name  = models.CharField(max_length=225)
    group_alias  = models.CharField(max_length=225,null=True)
    group_under  = models.CharField(max_length=225)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger  = models.BooleanField(default=False)
    debit_credit  = models.BooleanField(default=False)
    calculation  = models.BooleanField(default=False)
    invoice  = models.CharField(max_length=225,null=True,blank=True)

    def _str_(self):
        return self.name      

class ledgercreation(models.Model):
    name=models.CharField(max_length=255,null=True)
    alias=models.CharField(max_length=255,null=True)
    under=models.CharField(max_length=255)
    bank_details=models.CharField(max_length=255,) 
    mname=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)
    country=models.CharField(max_length=255,null=True)
    state=models.CharField(max_length=255,null=True)
    pincode =models.IntegerField(null=True)
    pan_no =models.IntegerField(null=True)
    registration_type =models.CharField(max_length=255,null=True)
    gst_uin =models.IntegerField(null=True)
    set_alter_gstdetails =models.CharField(max_length=255,null=True)
    ac_holder_nm =models.CharField(max_length=255,null=True)
    acc_no =models.IntegerField(null=True) 
    ifsc_code =models.IntegerField(null=True)
    swift_code =models.IntegerField(null=True)
    bank_name =models.CharField(max_length=255,null=True) 
    branch =models.CharField(max_length=255,null=True)
    SA_cheque_bk =models.CharField(max_length=255,null=True)
    Echeque_p =models.CharField(max_length=255,null=True)

    occ_set_odl = models.CharField(max_length=255,null=True)
    occ_ac_holder_nm =models.CharField(max_length=255,null=True)
    occ_acc_no =models.IntegerField(null=True) 
    occ_ifsc_code =models.IntegerField(null=True)
    occ_swift_code =models.IntegerField(null=True)
    occ_bank_name =models.CharField(max_length=255,null=True) 
    occ_branch =models.CharField(max_length=255,null=True)
    occ_SA_cheque_bk =models.CharField(max_length=255,null=True)
    occ_Echeque_p =models.CharField(max_length=255,null=True)

    od_set_odl = models.CharField(max_length=255,null=True)
    od_ac_holder_nm =models.CharField(max_length=255,null=True)
    od_acc_no =models.IntegerField(null=True) 
    od_ifsc_code =models.IntegerField(null=True)
    od_swift_code =models.IntegerField(null=True)
    od_bank_name =models.CharField(max_length=255,null=True) 
    od_branch =models.CharField(max_length=255,null=True)
    od_SA_cheque_bk =models.CharField(max_length=255,null=True)
    od_Echeque_p =models.CharField(max_length=255,null=True)

    

    statutory_details=models.CharField(max_length=255,null=True)

    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)
    GST_Applicable = models.CharField(max_length=100,null=True)
    Alter_GST_Details= models.CharField(max_length=100,null=True)
    Appropriate=models.CharField(max_length=100,null=True)
    Types_of_supply=models.CharField(max_length=100,null=True)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)


class debit(models.Model):
    name=models.CharField(max_length=255) 
    credit=models.IntegerField()
    debit=models.IntegerField()

    def _str_(self):
            return self.name 

class cred(models.Model):
    name=models.CharField(max_length=255) 
    credit=models.IntegerField()
    debit=models.IntegerField()

    def _str_(self):
            return self.name 

class led(models.Model):
    date=models.DateField()
    openam=models.IntegerField()
    penam=models.IntegerField()
    due=models.DateField()
    overd=models.IntegerField() 

    # Jisha (New Work)

class revised_applicability(models.Model):
    appl_from=models.CharField(max_length=100)

class revised_applicability_composition(models.Model):
    appl_from_c=models.CharField(max_length=100)

class stockgroupcreation(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)
    quantities=models.CharField(max_length=100)
    
class stockcatagorycreation(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)

# class CreateGodown(models.Model):
#     name=models.CharField(max_length=100)
#     alias=models.CharField(max_length=100)
#     under_name=models.CharField(max_length=50)

class Price_level(models.Model):
    number=models.CharField(max_length=255,null=True)

class pancin(models.Model):
    pan=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)

class unit_simple(models.Model):
    type=models.CharField(max_length=100)
    symbol=models.CharField(max_length=100)
    formal_name=models.CharField(max_length=100)
    uqc=models.CharField(max_length=100)
    decimal=models.IntegerField()
    
class unit_compound(models.Model):
    typ=models.CharField(max_length=100)
    f_unit=models.CharField(max_length=100,null=True)
    conversion=models.IntegerField()
    s_unit=models.CharField(max_length=100,null=True)

class uqcs(models.Model):
    uqc_name=models.CharField(max_length=100)

class stock_itemcreation(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=10,null=True)
    cost_tracking=models.CharField(max_length=10,null=True)
    gst_applicable=models.CharField(max_length=100,null=True)
    typ_sply=models.CharField(max_length=100)
    set_alter=models.CharField(max_length=100)
    rate_of_duty=models.IntegerField()
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    
class gst_stockitem(models.Model):
    calc_typ=models.CharField(max_length=100)
    taxability=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    cess=models.CharField(max_length=100)

# noufal 

class countrymodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

class statemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    cname=models.ForeignKey(countrymodel,on_delete=models.CASCADE)
    sname=models.CharField(max_length=250)

class groupcreatemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    gname=models.CharField(max_length=250)
    galias=models.CharField(max_length=250)
    gunder=models.CharField(max_length=250)
    gbehaves=models.CharField(max_length=250)
    gallocate=models.CharField(max_length=250)

class groupanalysismodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    pert=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    perticular=models.CharField(max_length=250)
    pquatity=models.IntegerField()
    prate=models.IntegerField()
    pvalue=models.IntegerField()
    squatity=models.IntegerField()
    srate=models.IntegerField()
    svalue=models.IntegerField()

class purchasevouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()


class salevouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()

class ledgercreatemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lname=models.CharField(max_length=250)
    lalias=models.CharField(max_length=250)
    # lunder=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    lunder=models.CharField(max_length=250)
    lmname=models.CharField(max_length=250)
    laddress=models.CharField(max_length=250)
    lstate=models.CharField(max_length=250)
    lcountry=models.CharField(max_length=250)
    lpincode=models.CharField(max_length=250)
    lbank=models.CharField(max_length=250)
    lpan=models.CharField(max_length=250)
    lreg=models.CharField(max_length=250)

class ledgeranalysismodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lpert=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    lperticular=models.CharField(max_length=250)
    lpquatity=models.IntegerField()
    lprate=models.IntegerField()
    lpvalue=models.IntegerField()
    lsquatity=models.IntegerField()
    lsrate=models.IntegerField()
    svalue=models.IntegerField()

class purchaseledgervouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()

class salesledgervouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()



     #payroll
class emp_category(models.Model):
    cat_name= models.CharField(max_length=225)
    cat_alias= models.CharField(max_length=225)
    revenue_items=models.CharField(max_length=225)
    non_revenue_items=models.CharField(max_length=225)

class Create_employeegroup(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    define_salary=models.CharField(max_length=225) 

class Employee(models.Model):

    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    email =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)


class add_bank(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Branch_name=models.CharField(max_length=225)
    Transaction_type=models.CharField(max_length=225)


class E_found_trasfer(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Cheque=models.CharField(max_length=225)

class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225)

class compute_information(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding(models.Model):
    pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity(models.Model):
    pay_head_id=models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)





class salary(models.Model):
    name=models.CharField(max_length=225)
    under=models.CharField(max_length=225) 
    effective=models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)


class units(models.Model):
    type= models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    uqc1=models.CharField(max_length=225,default='null',blank=True)
    number_of_decimal_places=models.CharField(max_length=225)
    first_unit=models.CharField(max_length=225)
    conversion=models.CharField(max_length=225)
    second_unit=models.CharField(max_length=225)

class Create_attendence(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    type =models.CharField(max_length=225)
    period=models.CharField(max_length=225,default='null',blank=True)
    units=models.CharField(max_length=225,default='null',blank=True)   
    
class create_VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)

class unitQuantityCode(models.Model):
    new_uqc=models.CharField(max_length=225)

  
# amalkv payrollmasters &satuatory details

class empgroup(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField (max_length=50)


class empgroup2(models.Model):
    groupname = models.CharField(max_length=50)
    groupalias = models.CharField (max_length=50)
    groupunder = models.CharField (max_length=50)



class Employee1(models.Model):
    
    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    email =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)


class add_bank1(models.Model):
    employee_id= models.ForeignKey(Employee1, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Branch_name=models.CharField(max_length=225)
    Transaction_type=models.CharField(max_length=225)


class E_found_trasfer1(models.Model):
    employee_id= models.ForeignKey(Employee1, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Cheque=models.CharField(max_length=225)

class create_VoucherModels1(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)


class Create_attendence1(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    type =models.CharField(max_length=225)


class pan(models.Model):
    tax3 =models.IntegerField()
    no =models.IntegerField()


class create_payhead1(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225) 
    



class compute_information1(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead1, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding1(models.Model):
    pay_head_id = models.ForeignKey(create_payhead1, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity1(models.Model):
    pay_head_id=models.ForeignKey(create_payhead1, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)   


class units1(models.Model):
    type= models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    number_of_decimal_places=models.CharField(max_length=225)
    first_unit=models.CharField(max_length=225)
    conversion=models.CharField(max_length=225)
    second_unit=models.CharField(max_length=225)



class gst1(models.Model):
    state= models.CharField(max_length=225)
    type=models.CharField(max_length=225)
    teretory=models.CharField(max_length=225)
    uin=models.CharField(max_length=225)
    gstr1=models.CharField(max_length=225)
    kerala=models.CharField(max_length=225)
    set=models.CharField(max_length=225)
    enable= models.CharField(max_length=225)
    enable2=models.CharField(max_length=225)
    enable3=models.CharField(max_length=225)
    bond=models.CharField(max_length=225)
    taxrate=models.CharField(max_length=225)
    basistax=models.CharField(max_length=225)
    purchase=models.CharField(max_length=225)
    eway=models.CharField(max_length=225)
    applicable=models.CharField(max_length=225)
    thresholt=models.CharField(max_length=225)
    limit=models.CharField(max_length=225)
    infrastate=models.CharField(max_length=225)
    thresholt2=models.CharField(max_length=225)
    invoice=models.CharField(max_length=225)
    einvoice=models.CharField(max_length=225)



class create_salary(models.Model):
    name= models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    effective = models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    payheaad_type=models.CharField(max_length=225)
    calculation_type=models.CharField(max_length=225)


class bank3(models.Model):
    name =models.CharField(max_length=225)
    

# arif account books - group summary and group voucher

'''--------- group summary -----------'''

class Create_Group_Summary_Model(models.Model):
    Name=models.CharField(max_length=30)
    Alias=models.CharField(max_length=30)
    Under=models.CharField(max_length=40)
    Group_Subledger=models.CharField(max_length=10)
    Nett_DebitCredit_Reporting=models.CharField(max_length=10)
    Used_Calculation=models.CharField(max_length=10)
    Method_Purchase_Invoice=models.CharField(max_length=30)


class First_Group_Summary_Model(models.Model):
    Group_Name=models.ForeignKey(Create_Group_Summary_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40)
    Debit=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)

class Second_Group_Summary_Model(models.Model):
    Fgroup_Forng=models.ForeignKey(First_Group_Summary_Model,on_delete=models.CASCADE)
    CName=models.CharField(max_length=50)

class Third_Group_Summary_Model(models.Model):
    Sgroup_Forng=models.ForeignKey(Second_Group_Summary_Model,on_delete=models.CASCADE)
    PName=models.CharField(max_length=50)

class Ledger_Monthly_Summary_Model(models.Model):
    Tgroup_Forgn=models.ForeignKey(Third_Group_Summary_Model,on_delete=models.CASCADE)
    Open_Balance=models.IntegerField(default=0)
    Particular=models.CharField(max_length=30)
    Dedit=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)
    Closing_Balance=models.IntegerField(default=0)

class Ledger_Voucher_Model(models.Model):
    Particular=models.CharField(max_length=30)
    Date=models.DateField(auto_now_add=True)
    Vch_Type=models.CharField(max_length=40)
    Vch_No=models.IntegerField(default=0)
    Debit=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)
    Open_Balance=models.IntegerField(default=0)

'''-------------- group voucher -----------------'''

class Create_Group_Voucher_Model(models.Model):
    Name=models.CharField(max_length=30)
    Alias=models.CharField(max_length=30)
    Under=models.CharField(max_length=40)
    Group_Subledger=models.CharField(max_length=10)
    Nett_DebitCredit_Reporting=models.CharField(max_length=10)
    Used_Calculation=models.CharField(max_length=10)
    Method_Purchase_Invoice=models.CharField(max_length=30)

class First_Voucher_Summary_Model(models.Model):
    Voucher_Name=models.ForeignKey(Create_Group_Voucher_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40)
    Debit=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)

class Second_Voucher_Summary_Model(models.Model):
    FVoucher_Name=models.ForeignKey(First_Voucher_Summary_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40)
    Debit=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)

class Stock_Group_Summary_Model(models.Model):
    Stock_Voucher_Forgn=models.ForeignKey(Create_Group_Voucher_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40)
    Quantity=models.IntegerField(default=0)
    Rate=models.IntegerField(default=0)
    Value=models.IntegerField(default=0)

class Product_Stock_Group_Summary_Model(models.Model):
    PStock_Voucher_Forgn=models.ForeignKey(Stock_Group_Summary_Model,on_delete=models.CASCADE)
    Particular=models.CharField(max_length=40)
    Quantity=models.CharField(max_length=40)
    Rate=models.IntegerField(default=0)
    Value=models.IntegerField(default=0)

class Stock_Item_Monthly_Summary_Model(models.Model):
    Pro_Stock_Voucher_Forgn=models.ForeignKey(Product_Stock_Group_Summary_Model,on_delete=models.CASCADE)
    Open_Balance_Qty=models.IntegerField(default=0)
    Open_Balance_Value=models.IntegerField(default=0)
    Particular=models.CharField(max_length=50)
    Inwards_Qty=models.IntegerField(default=0)
    Inwards_Vlu=models.IntegerField(default=0)
    Outwards_Qty=models.IntegerField(default=0)
    Outwards_Vlu=models.IntegerField(default=0)
    Closing_Bal_Qty=models.IntegerField(default=0)
    Closing_Bal_Vlu=models.IntegerField(default=0)

class Stock_Item_Voucher_Model(models.Model):
    Pro_Stock_Forgn=models.ForeignKey(Stock_Item_Monthly_Summary_Model,on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=True)
    Particular=models.CharField(max_length=50)
    Voucher_Type=models.CharField(max_length=40,default="pay")
    Vch_No=models.IntegerField(default=0)
    Inwards_Qty=models.IntegerField(default=0)
    Inwards_Vlu=models.IntegerField(default=0)
    Outwards_Qty=models.IntegerField(default=0)
    Outwards_Vlu=models.IntegerField(default=0)

class Group_Voucher_Model(models.Model):
    Date=models.DateField(auto_now_add=True)
    Particular=models.CharField(max_length=40)
    Vch_Type=models.CharField(max_length=40)
    Vch_No=models.IntegerField(default=0)
    DEBIT=models.IntegerField(default=0)
    Credit=models.IntegerField(default=0)
    Open_Balance=models.IntegerField(default=0)

# ananthakrishnan account book - cash bank book and ledger

class Group_under(models.Model):
    group_under_Name = models.CharField(max_length=225,default="Null",blank=True)
    
    def __str__(self):
        return self.group_under_Name

class Ledger(models.Model):
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    group_under =  models.ForeignKey(Group_under,on_delete=models.CASCADE , null=True, blank=True)
    ledger_opening_bal = models.IntegerField(default="Null",blank=True)
    ledger_opening_bal_type = models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)
    provide_banking_details =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.ledger_name

class Ledger_Banking_Details(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225,default="Null",blank=True)
    holder_name =models.CharField(max_length=225,default="Null",blank=True)
    ac_number =models.CharField(max_length=225,default="Null",blank=True)
    ifsc =models.CharField(max_length=225,default="Null",blank=True)
    swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_name = models.CharField(max_length=225,default="Null",blank=True)
    branch_name = models.CharField(max_length=225,default="Null",blank=True)
    alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    chqconfg= models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Mailing_Address(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225,default="Null",blank=True)
    address = models.CharField(max_length=225,default="Null",blank=True)
    state = models.CharField(max_length=225,default="Null",blank=True)
    country =models.CharField(max_length=225,default="Null",blank=True)
    pincode =models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Tax_Register(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    register_type =models.CharField(max_length=225,default="Null",blank=True)
    pan_no = models.CharField(max_length=225,default="Null",blank=True)
    alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Satutory(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Rounding(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)

class ledger_tax(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   
class Ledger_sundry(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)
    
class Group_Under_closing_balance(models.Model):
    group_under = models.ForeignKey(Group_under,on_delete=models.CASCADE)
    total_closing_balance_debit = models.IntegerField(default="",null=True,blank=True)
    total_closing_balance_credit = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.group_under.group_under_Name

class LedgerMonths (models.Model):
    month_name=models.CharField(max_length=255)
    def __str__(self):
        return self.month_name

class Leger_Month_closing(models.Model):
    Ledger = models.ForeignKey(Ledger,on_delete=models.CASCADE, null=True, blank=True)  
    month = models.ForeignKey(LedgerMonths,on_delete=models.CASCADE, null=True, blank=True)   
    Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)
    debit = models.IntegerField(default="",null=True,blank=True)
    credit =models.IntegerField(default="",null=True,blank=True)
  
class Ledger_Voucher(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True) 
    Date = models.DateField()
    Particualrs = models.CharField(max_length=225)
    Vch_Type = models.CharField(max_length=225)
    Vch_No = models.CharField(max_length=225)
    Debit = models.IntegerField(default="",null=True,blank=True)
    Credit = models.IntegerField(default="",null=True,blank=True)
    month = models.ForeignKey(LedgerMonths,on_delete=models.CASCADE, null=True, blank=True)   

    def __str__(self):
        return self.ledger.ledger_name

class TotalClosing_balance(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Total_Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)

    def __str__(self):
        return self.ledger.ledger_name

#Maneesha..

class creditreg(models.Model):
    date=models.DateField()
    particulars=models.CharField(max_length=255)
    vouchertype=models.CharField(max_length=255)
    voucherno=models.IntegerField()
    debitamount=models.IntegerField(null=True)
    creditamount=models.IntegerField()

class debitnote(models.Model):
    date=models.DateField()
    particulars=models.CharField(max_length=255)
    vouchertype=models.CharField(max_length=255)
    voucherno=models.IntegerField()
    debitamount=models.IntegerField()
    creditamount=models.IntegerField(null=True)



'''-----Reshma------'''

class Under(models.Model):
    cat_name=models.CharField(max_length=100)
 
    def __str__(self):
        return self.cat_name

class MainGroup(models.Model):
    
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225,blank=True)
    under=models.ForeignKey(Under,null=True,on_delete=models.CASCADE)
    nature=models.CharField(max_length=255,blank=True)
    affect_gp=models.CharField(max_length=255,blank=True)
    group=models.CharField(max_length=225)
    nett_balance=models.CharField(max_length=225)
    used_for=models.CharField(max_length=225)
    method=models.CharField(max_length=225)


    def __str__(self):
        return self.name

class SubGroup(models.Model):
    maingroup=models.ForeignKey(MainGroup,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225,blank=True)
    group=models.CharField(max_length=225)
    nett_balance=models.CharField(max_length=225)
    used_for=models.CharField(max_length=225)
    method=models.CharField(max_length=225)    

    
    def __str__(self):
        return self.name

class group_count(models.Model):
    M_count=models.ForeignKey(MainGroup,null=True,on_delete=models.CASCADE)
    S_count=models.ForeignKey(SubGroup,null=True,on_delete=models.CASCADE)

class Ledger1(models.Model):
    
    subgroup=models.ForeignKey(SubGroup,null=True,on_delete=models.CASCADE)
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    ledger_opening_bal = models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)

    tax_gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    tax_register_type =models.CharField(max_length=225,default="Null",blank=True)
    tax_pan_no = models.CharField(max_length=225,default="Null",blank=True)
    tax_alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)

    sta_assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    sta_Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    sta_gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    sta_Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    sta_type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    sta_Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

    rou_Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    rou_Round_limit = models.CharField(max_length=22,default="Null",blank=True)

    ta_type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    ta_type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    ta_valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    ta_rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    ta_Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)

    sun_maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    sun_Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    sun_Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)

    bank_od_limit = models.CharField(max_length=225,default="Null",blank=True)
    bank_holder_name =models.CharField(max_length=225,default="Null",blank=True)
    bank_ac_number =models.CharField(max_length=225,default="Null",blank=True)
    bank_ifsc =models.CharField(max_length=225,default="Null",blank=True)
    bank_swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_bank_name = models.CharField(max_length=225,default="Null",blank=True)
    bank_branch_name = models.CharField(max_length=225,default="Null",blank=True)
    bank_alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    bank_enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    bank_auto_recoun= models.CharField(max_length=225,default="Null",blank=True)

    mail_name = models.CharField(max_length=225,default="Null",blank=True)
    mail_address = models.CharField(max_length=225,default="Null",blank=True)
    mail_state = models.CharField(max_length=225,default="Null",blank=True)
    mail_country =models.CharField(max_length=225,default="Null",blank=True)
    mail_pincode =models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.ledger_name
        


class lbank(models.Model):
    ledger_id=models.OneToOneField(Ledger,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=100,blank=True,default="Null")
    cross_using=models.CharField(max_length=200,blank=True,default="Null")
    acno=models.CharField(max_length=100,blank=True,default="Null")
    ifscode = models.CharField(max_length=200,blank=True,default="Null")
    bankname = models.CharField(max_length=200,blank=True,default="Null")

class lcheque(models.Model):
    ledger_id=models.ForeignKey(Ledger,on_delete=models.CASCADE)
    from_no=models.CharField(max_length=100,blank=False)
    to_no=models.CharField(max_length=100,blank=False)
    no_cheques=models.CharField(max_length=100,blank=False)
    name_cheque=models.CharField(max_length=100,blank=False)

class Print_Cheque(models.Model):
    ledger_id=models.OneToOneField(Ledger,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100,blank=False)
    payee_name=models.CharField(max_length=100,blank=False)

    cheque_number=models.CharField(max_length=100,blank=False)
    cheque_date=models.CharField(max_length=100,blank=False)

    amt_words=models.CharField(max_length=100,blank=False)
    amt_number=models.CharField(max_length=100,blank=False)

    

class Costcentr(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    emply=models.CharField(max_length=225)



class Vouchers(models.Model):
    Vouchers_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Vouchers_name

class Accounts(models.Model):
    Accounts_name =models.CharField(max_length=255)

    def __str__(self):
        return self.Accounts_name 



class Months(models.Model):
    month_name = models.CharField(max_length=255)

    def __str__(self):
        return self.month_name     


class Voucher_Register(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Date = models.DateField()
    Particulars = models.CharField(max_length=255)
    # Vch_Type = models.CharField(max_length=255)
    # Vch_No = models.IntegerField()
    Debit_Amount = models.IntegerField(default="",null=True,blank=True)
    Credit_Amount = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name

class Voucher_count(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Total_Voucher = models.IntegerField(default="",null=True,blank=True)
    # Cancelled = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name


class Total(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Total = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name


class Accounts_Total(models.Model):
    Accounts = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    Total = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Accounts.Accounts_name

class currency_default(models.Model):
    Symbol = models.CharField(max_length=255)
    FormalName = models.CharField(max_length=255)
    ISOCurrency = models.CharField(max_length=30,null=True)
    DecimalPlace = models.IntegerField()
    showAmount = models.CharField(max_length=20)
    suffixSymbol = models.CharField(max_length=20)
    AddSpace = models.CharField(max_length=20)
    wordRep = models.CharField(max_length=255,null=True)
    DecimalWords = models.IntegerField()

    def __str__(self):
        return self.Symbol




class Compound_Units(models.Model):
    type=models.CharField(max_length=50,blank=True,null=True,default='Compound')  
    first_unit=models.CharField(max_length=50,blank=True,null=True)
    conversion=models.CharField(max_length=50,blank=True,null=True)
    second_unit=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.first_unit      

class Simple_Units(models.Model):
    type=models.CharField(max_length=100,null=True,blank=True,default='Simple')
    symbol=models.CharField(max_length=20,null=True,blank=True)
    formal_name=models.CharField(max_length=50,blank=True,null=True)
    uqc=models.CharField(max_length=50,blank=True,null=True)
    decimal=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.formal_name            

class Currency(models.Model):
    Symbol = models.CharField(max_length=255,blank=True,null=True)
    FormalName = models.CharField(max_length=255,blank=True,null=True)
    ISOCurrency = models.CharField(max_length=30,blank=True,null=True)
    DecimalPlace = models.IntegerField(blank=True,null=True)
    showAmount = models.CharField(max_length=20,blank=True,null=True)
    suffixSymbol = models.CharField(max_length=20,blank=True,null=True)
    AddSpace = models.CharField(max_length=20,blank=True,null=True)
    wordRep = models.CharField(max_length=255,blank=True,null=True)
    DecimalWords = models.IntegerField(blank=True,null=True)
    stddate=models.CharField(max_length=255,blank=True,null=True)
    stdrate=models.CharField(max_length=255,blank=True,null=True)
    selldate=models.CharField(max_length=255,blank=True,null=True)
    selvorate=models.CharField(max_length=255,blank=True,null=True)
    sellrate=models.CharField(max_length=255,blank=True,null=True)
    buydate=models.CharField(max_length=255,blank=True,null=True)
    buyvorate=models.CharField(max_length=255,blank=True,null=True)
    buyrate=models.CharField(max_length=255,blank=True,null=True)       

    def __str__(self):
        return self.Symbol



class Attendance(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    attendance=models.CharField(max_length=50,null=True,blank=True)
    period=models.CharField(max_length=50,null=True,blank=True)
    units=models.CharField(max_length=50,null=True,blank=True)    

    def __str__(self):
        return self.name   

class P_cost_default(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    revenue=models.CharField(max_length=50,null=True,blank=True)
    non_revenue=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee_Group(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    salary_details=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee2(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    doj=models.CharField(max_length=30,null=True,blank=True)
    salary=models.CharField(max_length=50,null=True,blank=True)
    doresig=models.CharField(max_length=50,null=True,blank=True)
    empno=models.CharField(max_length=20,null=True,blank=True)
    designation=models.CharField(max_length=20,null=True,blank=True)
    function_name=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    dob=models.CharField(max_length=20,null=True,blank=True)
    bld_grp=models.CharField(max_length=20,null=True,blank=True)
    father_mother=models.CharField(max_length=20,null=True,blank=True)
    spouse=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    phn=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    bank=models.CharField(max_length=50,null=True,blank=True)
    incometax=models.CharField(max_length=20,null=True,blank=True)
    adhar=models.CharField(max_length=20,null=True,blank=True)
    uan=models.CharField(max_length=20,null=True,blank=True)
    pf=models.CharField(max_length=20,null=True,blank=True)
    pr=models.CharField(max_length=20,null=True,blank=True)
    esi=models.CharField(max_length=20,null=True,blank=True)        

    def __str__(self):
        return self.name


class payhead(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    round_method=models.CharField(max_length=100,null=True)
    limit=models.CharField(max_length=100,null=True)
    compute=models.CharField(max_length=100,null=True)
    effect_from=models.CharField(max_length=100,null=True)
    grt_than=models.CharField(max_length=100,null=True)
    amt_upto=models.CharField(max_length=100,null=True)
    slab=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name



class receivable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def __str__(self):
      return self.party_name


class payitems(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)

    def __str__(self):
      return self.items



class payable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(payitems,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def total(self):
      tot=sum(self.pending_amound)
      return tot

    def __str__(self):
      return self.party_name  


class grunder(models.Model):
  und=models.CharField(max_length=255)  

  def __str__(self):
      return self.und  

     



class GroupModel(models.Model):
    group_name  = models.CharField(max_length=225)
    group_alias  = models.CharField(max_length=225,null=True)
    group_under  = models.CharField(max_length=225)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger  = models.BooleanField(default=False)
    debit_credit  = models.BooleanField(default=False)
    calculation  = models.BooleanField(default=False)
    invoice  = models.CharField(max_length=225,null=True,blank=True)

    def _str_(self):
        return self.name      



class ledgercreation(models.Model):
  name=models.CharField(max_length=255,null=True)
  alias=models.CharField(max_length=255,null=True)
  under=models.CharField(max_length=255)
  bank_details=models.CharField(max_length=255,) 
  mname=models.CharField(max_length=255,null=True)
  address=models.CharField(max_length=255,null=True)
  country=models.CharField(max_length=255,null=True)
  state=models.CharField(max_length=255,null=True)
  pincode =models.IntegerField(null=True)
  pan_no =models.IntegerField(null=True)
  registration_type =models.CharField(max_length=255,null=True)
  gst_uin =models.IntegerField(null=True)
  set_alter_gstdetails =models.CharField(max_length=255,null=True)

  


  ac_holder_nm =models.CharField(max_length=255,null=True)
  acc_no =models.IntegerField(null=True) 
  ifsc_code =models.IntegerField(null=True)
  swift_code =models.IntegerField(null=True)
  bank_name =models.CharField(max_length=255,null=True) 
  branch =models.CharField(max_length=255,null=True)
  SA_cheque_bk =models.CharField(max_length=255,null=True)
  Echeque_p =models.CharField(max_length=255,null=True)

  occ_set_odl = models.CharField(max_length=255,null=True)
  occ_ac_holder_nm =models.CharField(max_length=255,null=True)
  occ_acc_no =models.IntegerField(null=True) 
  occ_ifsc_code =models.IntegerField(null=True)
  occ_swift_code =models.IntegerField(null=True)
  occ_bank_name =models.CharField(max_length=255,null=True) 
  occ_branch =models.CharField(max_length=255,null=True)
  occ_SA_cheque_bk =models.CharField(max_length=255,null=True)
  occ_Echeque_p =models.CharField(max_length=255,null=True)

  od_set_odl = models.CharField(max_length=255,null=True)
  od_ac_holder_nm =models.CharField(max_length=255,null=True)
  od_acc_no =models.IntegerField(null=True) 
  od_ifsc_code =models.IntegerField(null=True)
  od_swift_code =models.IntegerField(null=True)
  od_bank_name =models.CharField(max_length=255,null=True) 
  od_branch =models.CharField(max_length=255,null=True)
  od_SA_cheque_bk =models.CharField(max_length=255,null=True)
  od_Echeque_p =models.CharField(max_length=255,null=True)

  

  statutory_details=models.CharField(max_length=255,null=True)

  type_of_ledger = models.CharField(max_length=100,null=True)
  rounding_method = models.CharField(max_length=100,null=True)
  rounding_limit = models.IntegerField(blank=True, null=True, default=None)
  GST_Applicable = models.CharField(max_length=100,null=True)
  Alter_GST_Details= models.CharField(max_length=100,null=True)
  Appropriate=models.CharField(max_length=100,null=True)
  Types_of_supply=models.CharField(max_length=100,null=True)

  type_duty_tax = models.CharField(max_length=100,null=True)
  tax_type = models.CharField(max_length=100,null=True)
  percentage_of_calcution = models.CharField(max_length=100,null=True)
  rond_method = models.CharField(max_length=100,null=True)
  rond_limit = models.IntegerField(blank=True, null=True, default=None)

  balance_billbybill = models.CharField(max_length=100,null=True)
  credit_period = models.CharField(max_length=100,null=True)
  creditdays_voucher = models.CharField(max_length=100,null=True)

  def _str_(self):
        return self.name 





class debit(models.Model):
  name=models.CharField(max_length=255) 
  credit=models.IntegerField()
  debit=models.IntegerField()

  def _str_(self):
        return self.name 



class cred(models.Model):
  name=models.CharField(max_length=255) 
  credit=models.IntegerField()
  debit=models.IntegerField()

  def _str_(self):
        return self.name 
        

class led(models.Model):
  date=models.DateField()
  openam=models.IntegerField()
  penam=models.IntegerField()
  due=models.DateField()
  overd=models.IntegerField() 


class Stock_Group_Creation_Model(models.Model):
    Name=models.CharField(max_length=30)
    Alias=models.CharField(max_length=30)
    Under=models.CharField(max_length=40)
    Qty_Item_Added=models.CharField(max_length=10)
    Set_Alter=models.CharField(max_length=10)

'''------------ stock item -------------'''

class Stock_Item_Creation_Model(models.Model):
    Name=models.CharField(max_length=30)
    Alias=models.CharField(max_length=30)
    Under=models.CharField(max_length=40)
    Unit=models.CharField(max_length=100,null=True)
    GST_Applicable=models.CharField(max_length=100,null=True)
    Type_Of_Supply=models.CharField(max_length=100,null=True)
    Rate_Of_Duty=models.CharField(max_length=100,null=True)
    Quantity=models.CharField(max_length=100,null=True)
    Rate=models.CharField(max_length=100,null=True)
    Per=models.CharField(max_length=100,null=True)
    Value=models.CharField(max_length=100,null=True)

'''------------ voucher type ---------------'''

class Voucher_Type_Creation_Model(models.Model):
    Name=models.CharField(max_length=30)
    Alias=models.CharField(max_length=30,null=True,blank=True)
    STV=models.CharField(max_length=30,null=True,blank=True)
    Abb=models.CharField(max_length=30,null=True,blank=True)
    AVT=models.CharField(max_length=10)
    MVN=models.CharField(max_length=50)

    UEDV=models.CharField(max_length=10)
    AZVT=models.CharField(max_length=10)
    MVT=models.CharField(max_length=10)
    ANV=models.CharField(max_length=10)
    PNLV=models.CharField(max_length=10)
    EDAA=models.CharField(max_length=10)
    PVAS=models.CharField(max_length=10,null=True,blank=True)
    NC=models.CharField(max_length=40,null=True,blank=True)