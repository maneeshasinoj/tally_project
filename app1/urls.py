from django.urls import path
from.import views


urlpatterns = [

    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('base',views.base,name='base'),

#.........................jisha..........................
    
    path('groups',views.groups,name='groups'),
    path('create_group',views.create_group,name='create_group'),
    path('group_alt',views.group_alt,name='group_alt'),

    path('currency',views.currency,name='currency'),
    path('c_create',views.c_create,name='c_create'),

    path('create_currency',views.create_currency,name='create_currency'),

    path('c_alter',views.c_alter,name='c_alter'),
    path('alter_currency',views.alter_currency,name='alter_currency'),

    path('change_company',views.change_company,name='change_company'),
    path('company_list',views.company_list,name='company_list'),
    path('select_c',views.select_c,name='select_c'),

    path('tally_gst',views.tally_gst,name='tally_gst'),
    path('create_gst',views.create_gst,name='create_gst'),

    path('gst_tax',views.gst_tax,name='gst_tax'),
    path('create_gsttax',views.create_gsttax,name='create_gsttax'),

    path('lut_bond',views.lut_bond,name='lut_bond'),
    path('create_lutbond',views.create_lutbond,name='create_lutbond'),

    path('tds',views.tds,name='tds'),
    path('create_tds',views.create_tds,name='create_tds'),

    path('person_tds',views.person_tds,name='person_tds'),
    path('person',views.person,name='person'),

    path('shut_cmpny',views.shut_cmpny,name='shut_cmpny'),

    path('shut/<int:pk>',views.shut,name='shut'),

    path('enable/<int:pk>',views.enable,name='enable'),

    path('cost',views.cost,name='cost'),
    path('load_centre',views.load_centre,name='load_centre'),
    path('cost_alt',views.cost_alt,name='cost_alt'),

    path('c_rates',views.c_rates,name='c_rates'),
    path('rates',views.rates,name='rates'),
    path('create_ROE',views.create_ROE,name='create_ROE'),

    path('vouchers',views.vouchers,name='vouchers'),
    path('create_voucher',views.create_voucher,name='create_voucher'),

    path('vouch_advance',views.vouch_advance,name='vouch_advance'),
    path('create_voucher_advance',views.create_voucher_advance,name='create_voucher_advance'),

    path('ledgers',views.ledgers,name='ledgers'),
    path('create_ledger',views.create_ledger,name='create_ledger'),

    path('ledger_bd',views.ledger_bd,name='ledger_bd'),
    path('create_ledger_bankdetails',views.create_ledger_bankdetails,name='create_ledger_bankdetails'),

    path('b_name',views.b_name,name='b_name'),
    path('bankname',views.bankname,name='bankname'),

    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),
    path('create_ledgerdimension',views.create_ledgerdimension,name='create_ledgerdimension'),

    path('ledger_chequebk',views.ledger_chequebk,name='ledger_chequebk'),
    path('create_ledger_chequebk',views.create_ledger_chequebk,name='create_ledger_chequebk'),

    path('ledger_gst',views.ledger_gst,name='ledger_gst'),
    path('create_ledger_gst',views.create_ledger_gst,name='create_ledger_gst'),

    path('ledger_taxgst',views.ledger_taxgst,name='ledger_taxgst'),
    path('create_ledger_taxgst',views.create_ledger_taxgst,name='create_ledger_taxgst'),

    path('create_cmpny',views.create_cmpny,name='create_cmpny'),
    path('company_create',views.company_create,name='company_create'),

    path('features',views.features,name='features'),
    path('company_feature',views.company_feature,name='company_feature'),
    
#.........................Ajmy..........................

    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    # path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),

    # path('catgroupsummary',views.catgroupsummary,name='catgroupsummary'),
    path('groupsummarypage',views.groupsummarypage,name='groupsummarypage'),
    path('creategroups',views.creategroups,name='creategroups'),
    path('primarygrpsummary/<int:sk>',views.primarygrpsummary,name='primarygrpsummary'),
    path('secondarygrpsummary/<int:sk>',views.secondarygrpsummary,name='secondarygrpsummary'),
    path('productsummary/<int:sk>',views.productsummary,name='productsummary'),
    path('prdctmonthlysummary/<int:sk>',views.prdctmonthlysummary,name='prdctmonthlysummary'),
    path('vouchsummary/<int:sk>/<int:m>/<int:n>',views.vouchsummary,name='vouchsummary'),
    path('periodvouchsummary/<int:sk>/<int:m>/<int:n>',views.periodvouchsummary,name='periodvouchsummary'),
    
    path('categorysummary',views.categorysummary,name='categorysummary'),
    # path('createcategory',views.createcategory,name='createcategory'),
    path('primarycatsummary/<int:sk>',views.primarycatsummary,name='primarycatsummary'),
    path('secondarycatsummary/<int:sk>',views.secondarycatsummary,name='secondarycatsummary'),
    path('prcatsummary/<int:sk>',views.prcatsummary,name='prcatsummary'),
    path('productcatmonthlysummary/<int:sk>',views.productcatmonthlysummary,name='productcatmonthlysummary'),

    path('savestockgroup',views.savestockgroup,name='savestockgroup'),
    # path('savestockcategory',views.savestockcategory,name='savestockcategory'),


#......................Praveen........................

    path('list_of_groups',views.list_of_groups,name='list_of_groups'),
    path('load_create_groups/<int:pk>',views.load_create_groups,name='load_create_groups'),

    path('load_alter_groups',views.load_alter_groups,name="load_alter_groups"),
    # path('branch',views.branch,name='branch'),
    # path('ledger',views.ledger,name='ledger'),
    path('list_of_ledger',views.list_of_ledger,name='list_of_ledger'),
    path('load_ledger_alter/<int:pk>',views.load_ledger_alter,name='load_ledger_alter'),

    path('ledger_gst_details',views.ledger_gst_details,name='ledger_gst_details'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('ledger_chequebook',views.ledger_chequebook,name='ledger_chequebook'),
    path('ledger_bank_details',views.ledger_bank_details,name='ledger_bank_details'),
    path('ledger_cheque_dimenssion',views.ledger_cheque_dimenssion,name='ledger_cheque_dimenssion'),

    path('load_create_ledger2',views.load_create_ledger2,name='load_create_ledger2'),
    path('list_of_currency',views.list_of_currency,name='list_of_currency'),
    path('load_currency',views.load_currency,name='load_currency'),
    path('list_of_companies',views.list_of_companies,name='list_of_companies'),
    path('create_company',views.create_company,name='create_company'),
    path('company_feature_form/<int:pk>',views.company_feature_form,name='company_feature_form'),
    path('companies_feature',views.companies_feature,name='companies_feature'),
    path('companyCreate1',views.companyCreate1,name='companyCreate1'),
    path('create_company',views.create_company,name='create_company'),
    path('select_company1',views.select_company1,name='select_company1'),
    path('shut_company1',views.shut_company1,name='shut_company1'),
    path('shut2/<int:pk>',views.shut2,name="shut2"),
    path('enable2/<int:pk>',views.enable2,name="enable2"),
    # path('shut_card',views.shut_card,name='shut_card'),

    path('load_rates_of_exchange',views.load_rates_of_exchange,name='load_rates_of_exchange'),
    path('create_currency3',views.create_currency3,name='create_currency3'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('currency_alteraion/<int:pk>',views.currency_alteraion,name='currency_alteraion'),

    path('gst_details3/<int:pk>',views.gst_details3,name='gst_details3'),
    path('gst_details_of_company',views.gst_details_of_company,name='gst_details_of_company'),
    path('lutbond/<int:pk>',views.lutbond,name='lutbond'),


    path('tds_detuctor/<int:pk>',views.tds_detuctor,name='tds_detuctor'),
    path('tds_personal/<int:pk>',views.tds_personal,name='tds_personal'),

    # path('primary',views.primary,name='primary'),
    # path('costcat',views.costcat,name='costcat'),
    # path('costcentr',views.costcentr,name='costcentr'),
    # path('voucher',views.voucher,name='voucher'),
    path('list_of_voucher_type',views.list_of_voucher_type,name='list_of_voucher_type'),
    path('load_voucher_type/<int:pk>',views.load_voucher_type,name='load_voucher_type'),
    path('voucher_type_alteration_secondary',views.voucher_type_alteration_secondary,name='voucher_type_alteration_secondary'),
    path('load_create_voucher',views.load_create_voucher,name='load_create_voucher'),
    # path('vouchpage',views.vouchpage,name='vouchpage'),

    path('list_of_cost_centers',views.list_of_cost_centers,name='list_of_cost_centers'),
    path('load_cost_centers/<int:pk>',views.load_cost_centers,name="load_cost_centers"),
    path('alter_cost_create',views.alter_cost_create,name="alter_cost_create"),


#......................Riya........................

    path('',views.index1,name='index1'),
    # path('basepage',views.basepage,name='basepage'),
    path('company',views.company,name='company'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('group1',views.group1,name='group1'),
    path('costcentre',views.costcentre,name='costcentre'),
    path('costcentre2',views.costcentre2,name='costcentre2'),
    path('group2',views.group2,name='group2'),
    path('currency1/<int:pk>',views.currency1,name='currency1'),
    path('features1/<int:pk>',views.features1,name='features1'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addstatenew',views.addstatenew,name='addstatenew'),
    path('addcountry',views.addcountry,name='addcountry'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('ratesofexchange',views.ratesofexchange,name='ratesofexchange'),
    path('featurecompany/<int:pk>',views.featurecompany,name='featurecompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),
    path('featurepage',views.featurepage,name='featurepage'),


#......................Neethu........................

    path('create',views.create,name="create"),
    path('companycreate1',views.companycreate1,name="companycreate1"),
    path('gst_details/<int:pk>',views.gst_details,name="gst_details"),
    path('add_gstdetails/<int:pk>',views.add_gstdetails,name="add_gstdetails"),
    path('tds_deductor/<int:pk>',views.tds_deductor,name="tds_deductor"),
    path('person_details/<int:pk>',views.person_details,name="person_details"),
    path('add_person/<int:pk>',views.add_person,name="add_person"),
    path('add_tds/<int:pk>',views.add_tds,name="add_tds"),
    path('features2/<int:pk>',views.features2,name="features2"),
    path('edit_features/<int:pk>',views.edit_features,name="edit_features"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('company_list1',views.company_list1,name="company_list1"),
    path('select_company',views.select_company,name="select_company"),
    path('dash_board/<int:pk>',views.dash_board,name="dash_board"),
    path('alter_company',views.alter_company,name="alter_company"),
    path('edit_page/<int:pk>',views.edit_page,name="edit_page"),
    path('edit_companydetails/<int:pk>',views.edit_companydetails,name="edit_companydetails"),
    path('change_company1',views.change_company1,name="change_company1"),
    path('shut_company',views.shut_company,name="shut_company"),
    
    path('shut1/<int:pk>',views.shut1,name="shut1"),
    path('date_change',views.date_change,name="date_change"),
    path('print_config',views.print_config,name="print_config"),
    path('add_country',views.add_country,name="add_country"),
   
    path('addstates',views.addstates,name="addstates"),
    path('state_country',views.state_country,name="state_country"),
    path('load_cities',views.load_cities,name="load_cities"),
    path('edit_gst_details/<int:pk>',views.edit_gst_details,name="edit_gst_details"),
    path('add_newgstdetails/<int:pk>',views.add_newgstdetails,name="add_newgstdetails"),
    path('edit_tds_deductor/<int:pk>',views.edit_tds_deductor,name="edit_tds_deductor"),
    path('add_newtdsdetails/<int:pk>',views.add_newtdsdetails,name="add_newtdsdetails"),
    path('edit_person_details/<int:pk>',views.edit_person_details,name="edit_person_details"),
    path('add_newpersondetails/<int:pk>',views.add_newpersondetails,name="add_newpersondetails"),


#......................Rafi........................

    path('attendance',views.attendance,name='attendance'),
    path('attendance_seconday',views.attendance_seconday,name='attendance_seconday'),
    
    # path('stock_group',views.stock_group,name='stock_group'),
    # path('stock_group_secondary',views.stock_group_secondary,name='stock_group_secondary'),
    
    path('stock_category_creation',views.stock_category_creation,name='stock_category_creation'),
    path('stock_category_secondary',views.stock_category_secondary,name='stock_category_secondary'),
    
    # path('stock_items',views.stock_items,name='stock_items'),
    path('stock_item_allocations',views.stock_item_allocations,name='stock_item_allocations'),
    
    # path('unit_creation',views.unit_creation,name='unit_creation'),
    path('uqc',views.uqc,name='uqc'),
    path('unit_creation_secondary',views.unit_creation_secondary,name='unit_creation_secondary'),
    path('uqc_secondary',views.uqc_secondary,name='uqc_secondary'),
    

    path('price_levels',views.price_levels,name='price_levels'),
    
    path('godown_alteration',views.godown_alteration,name='godown_alteration'),
    # path('godown_secondary',views.godown_secondary,name='godown_secondary'),
    
    path('employee_creation',views.employee_creation,name='employee_creation'),
    
    path('employee_group_creation',views.employee_group_creation,name='employee_group_creation'),
    path('emloyee_group_secondary',views.emloyee_group_secondary,name='emloyee_group_secondary'), 

    path('pan_cin',views.pan_cin,name='pan_cin'),
    path('pay_head',views.pay_head,name='pay_head'),
    
    path('salary_details',views.salary_details,name='salary_details'),
    
    path('payroll',views.payroll,name='payroll'),
    
    path('load/',views.load,name="load"),
    path('load_calculation/',views.load_calculation,name='load_calculation'),
    
    path('bank',views.bank,name='bank'),
    
    path('stock_item_allocations',views.stock_item_allocations,name='stock_item_allocations'),

#......................Ann........................

    path('disp_more_reports',views.disp_more_reports,name='disp_more_reports'),#ann
    path('listofpurchasevoucher/<int:pk>',views.listofpurchasevoucher,name='listofpurchasevoucher'),#ann,#listofpurchasevouchers
    path('listjournalvouchers/<int:pk>',views.listjournalvouchers,name='listjournalvouchers'),#ann,#listofjournalvouchers
    path('salesregister',views.salesregister,name='salesregister'),#ann
    path('purchaseregister',views.purchaseregister,name='purchaseregister'),#ann
    path('journalregister',views.journalregister,name='journalregister'),#ann
    path('listofsalesvoucher/<int:pk>',views.listofsalesvoucher,name='listofsalesvoucher'),#ann

#......................Niyas........................

    # path('liststockviews',views.liststockviews,name='liststockviews'),
    # path('liststockgroupviews',views.liststockgroupviews,name='liststockgroupviews'),
    # path('singlestockgroupanalysisview',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    
    # path('querystockview',views.querystockview,name='querystockview'),

    # path('salevoucheranalysisview',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    # path('purchasevoucheranalysisview',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    # path('itemmovementanalysisview',views.itemmovementanalysisview,name='itemmovementanalysisview'),
    # path('stockgroupanalysisview',views.stockgroupanalysisview,name='stockgroupanalysisview'),
    # path('stockgroupcreateview',views.stockgroupcreateview,name='stockgroupcreateview'),
    path('stockitmecreateview',views.stockitmecreateview,name='stockitmecreateview'),

#......................Jerin........................

    path('savestockgroup1',views.savestockgroup1,name='savestockgroup1'),
    path('savestockitem',views.savestockitem,name='savestockitem'),

    # path('querystockview/<int:pk>',views.querystockview,name='querystockview'),
    # path('singlestockgroupanalysisview/<int:pk>',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    # path('purchasevoucheranalysisview/<int:pk>',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    # path('salevoucheranalysisview/<int:pk>',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    # path('itemmovementanalysisview/<int:pk>',views.itemmovementanalysisview,name='itemmovementanalysisview'),


    path('receivabl',views.receivabl,name='receivabl'),
    path('payabl',views.payabl,name='payabl'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('create_group',views.create_group,name='create_group'),
    path('grcreate',views.grcreate,name='grcreate'),
    path('createledger',views.createledger,name='createledger'),
    path('credit',views.credit,name='credit'),
    path('debi',views.debi,name='debi'),
    path('ledgercreations',views.ledgercreations,name='ledgercreations'),
    path('ledgerlist',views.ledgerlist,name='ledgerlist'),
    path('nw',views.nw,name='nw'),


    #...................Jisha (New Work)......................

    path('godown_alt',views.godown_alt,name='godown_alt'),
    path('stockgroup_alt',views.stockgroup_alt,name='stockgroup_alt'),
    path('stockcate_alt',views.stockcate_alt,name='stockcate_alt'),
    path('unitcreate_alt',views.unitcreate_alt,name='unitcreate_alt'),
    path('new_uqcs',views.new_uqcs,name='new_uqcs'),

    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('stock_group',views.stock_group,name='stock_group'),
    path('load_stock_catagory',views.load_stock_catagory,name='load_stock_catagory'),
    path('stock_catagory',views.stock_catagory,name='stock_catagory'),
    path('load_unit_creation',views.load_unit_creation,name='load_unit_creation'),
    path('unit_sim',views.unit_sim,name='unit_sim'),
    path('load_unit_compound',views.load_unit_compound,name='load_unit_compound'),
    path('unit_com',views.unit_com,name='unit_com'),
    
    path('load_stock_item_creation',views.load_stock_item_creation,name='load_stock_item_creation'),
    path('stock_items_creation',views.stock_items_creation,name='stock_items_creation'),
    path('stock_accuracy',views.stock_accuracy,name='stock_accuracy'),
    path('stock_accuracy1',views.stock_accuracy1,name='stock_accuracy1'),
    path('stock_accuracy2',views.stock_accuracy2,name='stock_accuracy2'),
    path('load_company_price',views.load_company_price,name='load_company_price'),
    path('price_levels',views.price_levels,name='price_levels'),

    path('load_pan_cin',views.load_pan_cin,name='load_pan_cin'),
    path('pan_cin',views.pan_cin,name='pan_cin'),
    path('godown_creation',views.godown_creation,name='godown_creation'),
    path('godown',views.godown,name='godown'),

    path('load_rev',views.load_rev,name='load_rev'),
    path('revised',views.revised,name='revised'),
    path('load_rev_c',views.load_rev_c,name='load_rev_c'),
    path('revised_composition',views.revised_composition,name='revised_composition'),
    path('gst_stock_item',views.gst_stock_item,name='gst_stock_item'),
    path('gst_stock',views.gst_stock,name='gst_stock'),

    path('load_gst_d',views.load_gst_d,name='load_gst_d'),
    path('gst_d',views.gst_d,name='gst_d'),
    path('load_lut_bond',views.load_lut_bond,name='load_lut_bond'),
    path('lutbond',views.lutbond,name='lutbond'),
    path('load_gst_details_c',views.load_gst_details_c,name='load_gst_details_c'),
    path('gst_details_c',views.gst_details_c,name='gst_details_c'),

    path('load_tds',views.load_tds,name='load_tds'),
    path('tds_d',views.tds_d,name='tds_d'),
    path('load_person_res',views.load_person_res,name='load_person_res'),
    path('person_res',views.person_res,name='person_res'),

    path('aaa',views.aaa,name='aaa'),
    path('aa1',views.aa1,name='aa1'),

    # niyas

    path('stock_group',views.stock_group,name='stock_group'),
    path('stock_group_secondary',views.stock_group_secondary,name='stock_group_secondary'),
    path('liststockgroupviews',views.liststockgroupviews,name='liststockgroupviews'),
    path('unit_creation',views.unit_creation,name='unit_creation'),
    path('createcategory',views.createcategory,name='createcategory'),
    path('savestockcategory',views.savestockcategory,name='savestockcategory'),
    path('catgroupsummary',views.catgroupsummary,name='catgroupsummary'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('liststockviews',views.liststockviews,name='liststockviews'),
    path('godown_secondary',views.godown_secondary,name='godown_secondary'),
    path('singlestockgroupanalysisview/<int:pk>',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    path('itemmovementanalysisview',views.itemmovementanalysisview,name='itemmovementanalysisview'),
    path('purchasevoucheranalysisview/<int:pk>',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    path('salevoucheranalysisview/<int:pk>',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    path('querystockview/<int:pk>',views.querystockview,name='querystockview'),
    path('stockgroupanalysisview',views.stockgroupanalysisview,name='stockgroupanalysisview'),

    # noufal 
    path('createledgerviews',views.createledgerviews,name="createledgerviews"),
    path('ledgercreate',views.ledgercreate,name="ledgercreate"),
    path('selectledgerpage',views.selectledgerpage,name="selectledgerpage"),
    path('ledgerpage/<int:pk>',views.ledgerpage,name="ledgerpage"),
    path('ledgeritem/<int:pk>',views.ledgeritem,name="ledgeritem"),

    path('grouppage',views.grouppage,name='grouppage'),
    path('Create_Group',views.Create_Group,name="Create_Group"),
    path('creategroupviews',views.creategroupviews,name="creategroupviews"),
    path('groupanalisys/<int:pk>',views.groupanalisys,name="groupanalisys"),
    path('groupitem/<int:pk>',views.groupitem,name="groupitem"),

    # .......................Praveen(payroll masters)..........................

    #payroll masters

    path('empgroup',views.emp_grp,name='emp_grp'),
    path('addemp_grp',views.addemp_group,name='addemp_group'),
    path('employee',views.employee,name='employee'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('salary',views.salary1,name='salary1'),
    path('load',views.load,name='load'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    path('payhead2',views.payhead2,name='payhead2'),
    path('stunits',views.stunits,name='stunits'),
    path('add_units',views.add_units,name='add_units'),
    path('attendence',views.attendence,name='attendence'),
    path('emp_attendence',views.emp_attendence,name='emp_attendence'),
    path('payheads',views.payheads,name='payheads'),
    path('add_pay_head',views.add_payhead,name='add_payhead'),
    path('payvoucher',views.payvoucher,name='payvoucher'),
    path('employe_category',views.employe_category,name='employe_category'),
    path('employe_category_form',views.employe_category_form,name='employe_category_form'),
    path('add_voucher',views.add_voucher,name='add_voucher'),
#secondary
    path('empgroup2',views.emp_grp2,name='emp_grp2'),
    path('addemp_grp2',views.addemp_group2,name='addemp_group2'),
    path('attendence2',views.attendence2,name='attendence2'),
    path('employe_category_secondary',views.employe_category_secondary,name='employe_category_secondary'),
    path('uqcform',views.uqcform,name='uqcform'),
    path('stunits2',views.stunits2,name='stunits2'),



# ''''''''''''''''''''''''''''''''''''''''''''''''amal kv'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    path('emp_grp1',views.emp_grp1,name='emp_grp1'),
    path('emp_add2',views.emp_add2,name='emp_add2'),
    path('emp_add',views.emp_add,name='emp_add'),
    path('employee1',views.employee1,name='employee1'),
    path('addemployee1',views.addemployee1,name='addemployee1'),
    path('payheads1',views.payheads1,name='payheads1'),
    path('attendence3',views.attendence3,name='attendence3'),
    path('attendence1',views.attendence1,name='attendence1'),
    path('attendence4',views.attendence4,name='attendence4'),
    path('attendence_edit/<int:pk>',views.attendence_edit,name='attendence_edit'),
    path('attendence_edit2/<int:pk>',views.attendence_edit2,name='attendence_edit2'),
    path('emp_grp2_2',views.emp_grp2_2,name='emp_grp2_2'),
    path('employee2',views.employee2,name='employee2'),
    path('payheads2',views.payheads2,name='payheads2'),
    path('attendence2_2',views.attendence2_2,name='attendence2_2'),
    path('payroll1',views.payroll1,name='payroll1'),
    path('emp_gredit/<int:pk>',views.emp_gredit,name='emp_gredit'),
    path('emp_gredit2/<int:pk>',views.emp_gredit2,name='emp_gredit2'),
    path('add_voucher1',views.add_voucher1,name='add_voucher1'),
    path('add_voucher2',views.add_voucher2,name='add_voucher2'),
    path('add_voucher3',views.add_voucher3,name='add_voucher3'),
    path('add_voucher_edit/<int:pk>',views.add_voucher_edit,name='add_voucher_edit'),
    path('add_voucher_edit2/<int:pk>',views.add_voucher_edit2,name='add_voucher_edit2'),
    path('unit',views.unit,name='unit'),
    path('unit2',views.unit2,name='unit2'),
    path('unit3',views.unit3,name='unit3'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('unit_edit/<int:pk>',views.unit_edit,name='unit_edit'),
    path('unit_edit2/<int:pk>',views.unit_edit2,name='unit_edit2'),
    path('gst3',views.gst3,name='gst3'),
    path('panadd',views.panadd,name='panadd'),
    path('pan2',views.pan2,name='pan2'),
    path('gst2',views.gst2,name='gst2'),
    path('add_payheads',views.add_payheads,name='add_payheads'),
    path('payhead_edit/<int:pk>',views.payhead_edit,name='payhead_edit'),
    path('payhead_edit2/<int:pk>',views.payhead_edit2,name='payhead_edit2'),
    path('salary',views.salary,name='salary'),
    path('salary2',views.salary2,name='salary2'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    path('load',views.load,name='load'),
    path('salary3',views.salary3,name='salary3'),
    path('bank',views.bank,name='bank'),
    path('add_bank3',views.add_bank3,name='add_bank3'),

     # arif 

    # groupe-summary 

    # path('',views.Index,name='Index'),
    path('Group_Summary/<int:pk>',views.Group_Summary,name='Group_Summary'),
    path('Sec_Group_Summary/<int:pk>',views.Sec_Group_Summary,name="Sec_Group_Summary"),
    path('Thrd_Group_Summary/<int:pk>',views.Thrd_Group_Summary,name="Thrd_Group_Summary"),
    path('Ledger_Monthly_Summary/<int:pk>',views.Ledger_Monthly_Summary,name='Ledger_Monthly_Summary'),
    path('Ledger_Voucher/<int:pk>',views.Ledger_Voucher,name='Ledger_Voucher'),
    path('Select_Groups',views.Select_Groups,name='Select_Groups'),
    path('Creat_Group_Summary',views.Creat_Group_Summary,name='Creat_Group_Summary'),
    path('Group_Summary_Create',views.Group_Summary_Create,name='Group_Summary_Create'),

    # group-voucher

    path('Stock_Group_Summary/<int:pk>',views.Stock_Group_Summary,name='Stock_Group_Summary'),
    path('Stock_Item_Voucher/<int:pk>',views.Stock_Item_Voucher,name='Stock_Item_Voucher'),
    path('Stock_Item_Monthly_Summary/<int:pk>',views.Stock_Item_Monthly_Summary,name="Stock_Item_Monthly_Summary"),
    path('Group_Voucher/<int:pk>',views.Group_Voucher,name="Group_Voucher"),
    path('Voucher_Group_Summary/<int:pk>',views.Voucher_Group_Summary,name="Voucher_Group_Summary"),
    path('Creat_Group_Voucher',views.Creat_Group_Voucher,name='Creat_Group_Voucher'),
    path('Select_Group_Voucher',views.Select_Group_Voucher,name='Select_Group_Voucher'),
    path('Group_Voucher_Create',views.Group_Voucher_Create,name='Group_Voucher_Create'),
    path('Group_Voucher_Summary/<int:pk>',views.Group_Voucher_Summary,name="Group_Voucher_Summary"),
    path('Stock_Group_Summary_Product/<int:pk>',views.Stock_Group_Summary_Product,name="Stock_Group_Summary_Product"),

    # ananthakrishnan account book 

    path('cash_bank_summary',views.cash_bank_summary,name='cash_bank_summary'),
    path('group_summary',views.group_summary,name='group_summary'),
    path('ledger_cash',views.ledger_cash,name='ledger_cash'),
    #bank account
    path('cash_bank_summary2/<int:id>',views.cash_bank_summary2,name='cash_bank_summary2'),
    # path('ledger_bank/<int:id>',views.ledger_bank,name='ledger_bank'), 
    #ledger

    path('ledger_views',views.ledger_views,name='ledger_views'),
    path('create_ledger_views',views.create_ledger_views,name='create_ledger_views'),
    path('save_ledger',views.save_ledger,name='save_ledger'),
    path('ledger_show/<int:id>/<int:pk>',views.ledger_show,name='ledger_show'),
    path('ledger_show2/<int:id>',views.ledger_show2,name='ledger_show2'),
    path('ledger_monthly_summary/<int:id>',views.ledger_monthly_summary,name='ledger_monthly_summary'),

    #maneesha
    path('debitnoteregister',views.debitnoteregister,name='debitnoteregister'),
    path('creditnoteregister',views.creditnoteregister,name='creditnoteregister'),
    path('voucherregister/<int:pk>',views.voucherregister,name='voucherregister'),
    path('voucherregisterdebit/<int:pk>',views.voucherregisterdebit,name='voucherregisterdebit'),


    #...................Reshma......................

                path('Statements_accounts',views.Statements_accounts,name='Statements_accounts'),
                path('statistics',views.statistics,name='statistics'),
                path('index',views.index,name='index'),
                path('groups/',views.groups,name='groups'),
                path('m_group/<int:pk>',views.m_group,name='m_group'),
                path('s_group/<int:pk>',views.s_group,name='s_group'),
                path('ledgers_Stat/',views.ledgers_Stat,name='ledgers_Stat'),
                path('grp_alter/<int:pk>',views.grp_alter,name="grp_alter"),
                path('sub_grp_alter/<int:pk>',views.sub_grp_alter,name="sub_grp_alter"),
                path('ledger_alter/<int:pk>',views.ledger_alter,name='ledger_alter'),
                path('alter_ledger/<int:pk>',views.alter_ledger,name='alter_ledger'),
                path('ledger_bank_details/<int:pk>',views.ledger_bank_details,name='ledger_bank_details'),
                path('add_bank_details/<int:pk>',views.add_bank_details,name='add_bank_details'),
                #path('show_bdetails/',views.show_bdetails,name='show_bdetails'),
                path('ledger_cheque_details/<int:pk>',views.ledger_cheque_details,name='ledger_cheque_details'),
                path('add_cheque_details/<int:id>',views.add_cheque_details,name='add_cheque_details'),
                path('cheque_printing/<int:pk>',views.cheque_printing,name='cheque_printing'),
                path('c_printt/<int:pk>',views.c_printt,name='c_printt'), 
                path('add_cheque_dimensions/<int:id>',views.add_cheque_dimensions,name='add_cheque_dimensions'), 
                path('update_centr/<int:pk>',views.update_centr,name='update_centr'),
                path('centr/<int:pk>',views.centr,name='centr'),
                path('costcentr',views.costcentr,name='costcentr'),
                path('delete_Mgroups/<int:pk>',views.delete_Mgroups,name='delete_Mgroups'),
                path('delete_Sgroups/<int:pk>',views.delete_Sgroups,name='delete_Sgroups'),
                path('delete_ledgers/<int:pk>',views.delete_ledgers,name='delete_ledgers'),
                path('delete_centre/<int:pk>',views.delete_centre,name='delete_centre'),

                path('voucher_monthly_register/<int:id>',views.voucher_monthly_register,name='voucher_monthly_register'),
                path('voucher_register/<int:id>/<int:pk>',views.voucher_register,name='voucher_register'), 
                path('Delete/<int:id>/<int:pk>/<int:de>',views.Delete,name='Delete'),
                path('test',views.test,name='test'),

                path('units/',views.units,name='units'),
                path('currencies/',views.currencies,name='currencies'),
                path('atten_prod/',views.atten_prod,name='atten_prod'),
                path('emp_groups/',views.emp_groups,name='emp_groups'),
                path('employee/',views.employee,name='employee'),
                path('curr_alter/<int:pk>',views.curr_alter,name='curr_alter'),
                path('unit_alter/<int:pk>',views.unit_alter,name='unit_alter'),
                path('curr_alter2/<int:pk>',views.curr_alter2,name='curr_alter2'),
                path('atten_alter/<int:pk>',views.atten_alter,name='atten_alter'),
                path('empg_alter/<int:pk>',views.empg_alter,name='empg_alter'),
                path('empg_details/<int:pk>',views.empg_details,name='empg_details'),
                path('create_pay_head/',views.create_pay_head,name='create_pay_head'),
                path('p_cost/<int:pk>',views.p_cost,name='p_cost'),
                path('emp_alter/<int:pk>',views.emp_alter,name='emp_alter'),
                path('c_unit_alter/<int:pk>',views.c_unit_alter,name='c_unit_alter'),
                path('simple_unit_alter/<int:pk>',views.simple_unit_alter,name='simple_unit_alter'),
                path('compound_unit_alter/<int:pk>',views.compound_unit_alter,name='compound_unit_alter'),
                path('curr_default_alter/<int:pk>',views.curr_default_alter,name='curr_default_alter'),
                path('currency_altern/<int:pk>',views.currency_altern,name='currency_altern'),
                path('attendance_alter/<int:pk>',views.attendance_alter,name='attendance_alter'),
                path('pcost_alter/<int:pk>',views.pcost_alter,name='pcost_alter'),
                path('employee_grp_alter/<int:pk>',views.employee_grp_alter,name='employee_grp_alter'),
                path('employee_alter/<int:pk>',views.employee_alter,name='employee_alter'),
                path('attend_create/',views.attend_create,name='attend_create'),
                path('add_pay_head/',views.add_pay_head,name='add_pay_head'),



                path('Stock_Groups',views.Stock_Groups,name="Stock_Groups"),
                path('Stock_Group_Creation_Page',views.Stock_Group_Creation_Page,name="Stock_Group_Creation_Page"),
                path('Stock_Group_Creation',views.Stock_Group_Creation,name='Stock_Group_Creation'),
                path('Stock_Group_Edit_Page/<int:pk>',views.Stock_Group_Edit_Page,name='Stock_Group_Edit_Page'),
                path('Edit_Stock_Group/<int:pk>',views.Edit_Stock_Group,name='Edit_Stock_Group'),
                path('Delete_Stock_Group/<int:pk>',views.Delete_Stock_Group,name='Delete_Stock_Group'),

                path('Stock_Items',views.Stock_Items,name="Stock_Items"),
                path('Stock_Item_Creation_Page',views.Stock_Item_Creation_Page,name="Stock_Item_Creation_Page"),
                path('Stock_Item_Creation',views.Stock_Item_Creation,name='Stock_Item_Creation'),
                path('Delete_Stock_Item/<int:pk>',views.Delete_Stock_Item,name='Delete_Stock_Item'),
                path('Stock_Item_Edit_Page/<int:pk>',views.Stock_Item_Edit_Page,name='Stock_Item_Edit_Page'),
                path('Edit_Stock_Item/<int:pk>',views.Edit_Stock_Item,name='Edit_Stock_Item'),

                path('Voucher_Types',views.Voucher_Types,name="Voucher_Types"),
                path('Voucher_Type_Creation_Page',views.Voucher_Type_Creation_Page,name='Voucher_Type_Creation_Page'),
                path('Voucher_Type_Creation',views.Voucher_Type_Creation,name='Voucher_Type_Creation'),
                path('Delete_Voucher_Type/<int:pk>',views.Delete_Voucher_Type,name='Delete_Voucher_Type'),
                path('Voucher_Type_Edit_Page/<int:pk>',views.Voucher_Type_Edit_Page,name='Voucher_Type_Edit_Page'),
                path('Edit_Voucher_Types/<int:pk>',views.Edit_Voucher_Types,name='Edit_Voucher_Types'), 
                
                path('receivabl',views.receivabl,name='receivabl'),
                path('payabl',views.payabl,name='payabl'),
                path('creategroup',views.creategroup,name='creategroup'),
                path('create_group',views.create_group,name='create_group'),
                path('grcreate',views.grcreate,name='grcreate'),
                path('createledger',views.createledger,name='createledger'),
                path('credit',views.credit,name='credit'),
                path('debi',views.debi,name='debi'),
                path('ledgercreations',views.ledgercreations,name='ledgercreations'),
                path('ledgerlist',views.ledgerlist,name='ledgerlist'),
                path('nw',views.nw,name='nw'),
                path('outstanding',views.outstanding,name='outstanding'),
                        

]