# -*- encoding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SelectField, DateField
from wtforms.validators import Email, DataRequired

# login and registration


class CreateInvoiceForm(FlaskForm):
    aircraft_tailnumber = StringField('Aircraft Tail Number',id='aircraft_tailnumber',validators=[DataRequired()])
    days_till_invoice_due = StringField('Days Till Invoice Due', id='days_till_invoice_due', validators=[DataRequired()])
    total_amount = DecimalField('Total Amount', id='total_amount', validators=[DataRequired()])
    product_name = StringField('Product Name', id='product_name', validators=[DataRequired()])

class EditInvoiceForm(FlaskForm):
    #Make Dynamic Status choices from database ======
    invoice_status = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    invoice_due_date = DateField('Invoice Due Date', id='invoice_due_date', validators=[DataRequired()])

    days_till_invoice_due = IntegerField('Days Till Invoice Due', id='days_till_invoice_due', validators=[DataRequired()])
    product_name = StringField('Product Name', id='product_name', validators=[DataRequired()])
    registered_owner = StringField('Registered Owner', id='registered_owner', validators=[DataRequired()])

    #Address Data
    address_street = StringField('Address Street', id='address_street', validators=[DataRequired()])
    address_city = StringField('Address City', id='address_city', validators=[DataRequired()])
    address_state = StringField('Address State', id='address_state', validators=[DataRequired()])
    address_zip = StringField('Address Zip', id='address_zip', validators=[DataRequired()])

    total_amount = DecimalField('Total Amount', id='total_amount', validators=[DataRequired()])

