




def get_tailnumber_data(aircraft_tailnumber):
    #Check if most recent database has been downloaded
    #https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download

    #Check if aircraft tailnumber exists and pull data from FAA Database

    #DUMMY DATA
    data = {
        'invoice_status': 'Pending',
        'registered_owner': 'John Doe',
        'aircraft_tailnumber': 'N12345',
        'address_street': '123 Main St',
        'address_city': 'Anytown',
        'address_state': 'CA',
        'address_zip': '12345',
        'manufacturer_name': 'Cessna',
        'model_name': '172',
        'type_aircraft': 'Single Engine Land',
    }

    if data:
        return data
    else:
        return None

