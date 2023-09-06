from models.address import Address
from utils.database import db

def get_address(address_id):
    address = Address.query.get(address_id)
    return address

def get_all_addresses():
    addresses = Address.query.all()
    return addresses

def get_addresses_by_business(business_id):
    addresses = Address.query.filter_by(business_id=business_id).all()
    return addresses

def create_address(address):
    db.session.add(address)
    db.session.commit()
    return address

def delete_address(address):
    db.session.delete(address)
    db.session.commit()