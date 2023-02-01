
from sqlalchemy import create_engine, Column, Integer, String ,Boolean, Numeric, DateTime 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#from datetime import timedelta, date
from datetime import datetime, timedelta




Base = declarative_base()


now = datetime.now()

class Invoice(Base):
    __tablename__ = 'invoices'


    invoice_id=Column(Integer, primary_key=True)

    invoice_status=Column('invoice_status', String(32))
    invoice_created_date=Column("create_date", DateTime, default=now)
    invoice_due_date=Column("due_date", DateTime)

    total_amount=Column('total_amount', Numeric)

    #Product Data
    product_name=Column('product_name', String(32))
    airport_name=Column('airport_name', String(32))


    #Data from FAA
    registered_owner=Column('registered_owner', String(32))
    aircraft_tailnumber=Column('aircraft_tailnumber', String(32))

    #Address Data
    address_street=Column('address_street', String(32))
    address_city=Column('address_city', String(32))
    address_state=Column('address_state', String(32))
    address_zip=Column('address_zip', String(32))

    #Aircraft Data
    manufacturer_name=Column('manufacturer_name', String(32))
    model_name=Column('model_name', String(32))
    type_aircraft=Column('type_aircraft', String(32))

    def __init__(self, invoice_status, days_till_invoice_due, total_amount, product_name, airport_name,registered_owner, aircraft_tailnumber, address_street, address_city, address_state, address_zip, manufacturer_name, model_name, type_aircraft):


        self.invoice_status = invoice_status
        self.invoice_due_date = end_date = datetime.now() + timedelta(days=days_till_invoice_due)
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

    def __repr__(self):
        return f"({self.invoice_due_date}, {self.registered_owner}, {self.aircraft_tailnumber})"



engine = create_engine('sqlite:///invoices.db', echo=True)
Base.metadata.create_all(bind=engine)
 
Session = sessionmaker(bind=engine)
session = Session()


def get_list_of_invoices(airport_name, page=1, per_page=10):
    return session.query(Invoice).filter(Invoice.airport_name == airport_name).offset((page - 1) * per_page).limit(per_page).all()

#new_invoice = Invoice("Paid", 30, 10, "Landing Fee", "KJFK", "John Doe", "N12345", "123 Main St", "New York", "NY", "10001", "Boeing", "737", "Airplane")
#session.add(new_invoice)
#session.commit()


    