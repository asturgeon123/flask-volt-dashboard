# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from flask_paginate import Pagination, get_page_args

from apps import db
#from apps.home import invoice_database_manager as invoice_db
from apps.home.models import Invoices
from apps.home.forms import CreateInvoiceForm
from apps.home import faa_utils



@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')



@blueprint.route('get_invoice/<invoice_id>')
@login_required
def get_invoice(invoice_id):

    try:
        invoice = Invoices.query.filter_by(invoice_id=invoice_id).first()
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" +"view_invoice.html", days_till_due=invoice.get_days_till_due(),due_date_formatted=invoice.get_due_date_formatted(), create_date_formatted=invoice.get_created_date_formatted() ,data=invoice)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    #except:
    #    return render_template('home/page-500.html'), 500



#FIX THIS - PAGINATION
@blueprint.route('/transactions.html')
@login_required
def load_transaction():
    template = 'transactions.html'
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        print("Current User", current_user, current_user.id, current_user.airport_code)


        #data = invoice_db.get_list_of_invoices(current_user.airport_code, page, per_page)
        #data = invoice_db.get_list_of_invoices("KJFK", page, per_page)
        #print("Data", data)

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

        #print("Page", page, "per_page", per_page, "offset", offset)


        invoices = db.session.query(Invoices).offset((page - 1) * per_page).limit(per_page).all()
        pagination = Pagination(page=page, per_page=per_page, total=len(invoices), css_framework='bootstrap5')

        #print(pagination)
        return render_template("home/" + template, invoices=invoices, page=page, per_page=per_page, pagination=pagination)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

@blueprint.route('/new_invoice.html', methods=['GET', 'POST'])
@login_required
def new_transaction():
    # Detect the current page
    segment = get_segment(request)

    form = CreateInvoiceForm(request.form)
    if 'create_invoice' in request.form:

        aircraft_tailnumber = request.form['aircraft_tailnumber']
        days_till_invoice_due = request.form['days_till_invoice_due']
        total_amount = request.form['total_amount']
        product_name = request.form['product_name']

        #Check if aircraft tailnumber exists and pull data from FAA API
        #get_tailnumber_data(aircraft_tailnumber)

        aircraft_data = faa_utils.get_tailnumber_data(aircraft_tailnumber)
        print("Aircraft Data", aircraft_data)
        if aircraft_data is None:
            print("Aircraft Tailnumber not found in FAA database")
            return render_template("home/" + 'new_invoice.html', segment=segment, form=form, success=False,msg="Aircraft Tailnumber not found in FAA database")
        else:
            print("Creating Invoice")
            #Create Invoice
            #invoice = Invoices("Processing",days_till_invoice_due,total_amount,product_name,current_user.airport_code,aircraft_data['registered_owner'],aircraft_tailnumber,aircraft_data['address_street'],aircraft_data['address_city'],aircraft_data['address_state'],aircraft_data['address_zip'],aircraft_data['model_name'],aircraft_data['type_aircraft'])
            invoice = Invoices("Processing",days_till_invoice_due,total_amount,product_name,"KCGI",aircraft_data['registered_owner'],aircraft_tailnumber,aircraft_data['address_street'],aircraft_data['address_city'],aircraft_data['address_state'],aircraft_data['address_zip'],aircraft_data['manufacturer_name'],aircraft_data['model_name'],aircraft_data['type_aircraft'])
            db.session.add(invoice)
            db.session.commit()
            return render_template("home/" + 'new_invoice.html', segment=segment, form=form, success=True, msg="Invoice created successfully")

    return render_template("home/" + 'new_invoice.html', segment=segment, form=form)
    


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
