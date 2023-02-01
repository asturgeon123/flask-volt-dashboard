# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField
from wtforms.validators import Email, DataRequired

# login and registration


class CreateInvoiceForm(FlaskForm):
    aircraft_tailnumber = StringField('Aircraft Tail Number',id='aircraft_tailnumber',validators=[DataRequired()])
    days_till_invoice_due = StringField('Days Till Invoice Due', id='days_till_invoice_due', validators=[DataRequired()])
    total_amount = DecimalField('Total Amount', id='total_amount', validators=[DataRequired()])
    product_name = StringField('Product Name', id='product_name', validators=[DataRequired()])

