# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from datetime import datetime, timedelta

class Invoices(db.Model):
        __tablename__ = 'invoices'

        invoice_id=db.Column(db.Integer, primary_key=True)

        invoice_status=db.Column('invoice_status', db.String(32))
        invoice_created_date=db.Column("create_date", db.DateTime, default=datetime.now())
        invoice_due_date=db.Column("due_date", db.DateTime)

        total_amount=db.Column('total_amount', db.Numeric)

        #Product Data
        product_name=db.Column('product_name', db.String(32))
        airport_name=db.Column('airport_name', db.String(32))


        #Data from FAA
        registered_owner=db.Column('registered_owner', db.String(32))
        aircraft_tailnumber=db.Column('aircraft_tailnumber', db.String(32))

        #Address Data
        address_street=db.Column('address_street', db.String(32))
        address_city=db.Column('address_city', db.String(32))
        address_state=db.Column('address_state', db.String(32))
        address_zip=db.Column('address_zip', db.String(32))

        #Aircraft Data
        manufacturer_name=db.Column('manufacturer_name', db.String(32))
        model_name=db.Column('model_name', db.String(32))
        type_aircraft=db.Column('type_aircraft', db.String(32))
        
        def __init__(self, invoice_status, days_till_invoice_due, total_amount, product_name, airport_name,registered_owner, aircraft_tailnumber, address_street, address_city, address_state, address_zip, manufacturer_name, model_name, type_aircraft):

            self.invoice_status = invoice_status
            self.invoice_due_date = datetime.now() + timedelta(days=int(days_till_invoice_due))
            self.total_amount = total_amount

            self.product_name = product_name
            self.airport_name = airport_name

            self.registered_owner = registered_owner
            self.aircraft_tailnumber = aircraft_tailnumber
            self.address_street = address_street
            self.address_city = address_city
            self.address_state = address_state
            self.address_zip = address_zip
            self.manufacturer_name = manufacturer_name
            self.model_name = model_name
            self.type_aircraft = type_aircraft

        def get_days_till_due(self):
            return (self.invoice_due_date - datetime.now()).days

        def get_created_date_formatted(self):
            return self.format_date(self.invoice_created_date)
        
        def get_due_date_formatted(self):
            return self.format_date(self.invoice_due_date)

        def format_date(self, date):
            return date.strftime("%b %d, %Y")

        def __repr__(self):
            return f"({self.invoice_due_date}, {self.registered_owner}, {self.aircraft_tailnumber})"


