from fastapi.testclient import TestClient
import factory

def test_address_create(client:TestClient, admin_auth_header, user_factory):
    customer = user_factory(id= factory.Faker('pyint'), role='customer')
    response = client.post('/address/',
                            headers= admin_auth_header,
                            json={
                                'Address': 'rua',
                                'city': 'sp',
                                'state': '10',
                                'number': 'value',
                                'zipcode': 'value',
                                'neighbourhood': 'value',
                                'primary': True,
                                'customer_id': customer.id
                            })
    assert response.status_code == 201
    assert response.json()['customer_id'] == customer.id
    assert response.json()['city'] == 'sp'


# def test_address_update(client:TestClient, admin_auth_header, address_factory):
#     address = address_factory()
    
    
#     response = client.put(f'/address/{address.id}',
#                             headers= admin_auth_header,
#                             json={
#                                 'Address': 'rua',
#                                 'city': 'sp',
#                                 'state': '10',
#                                 'number': 'value',
#                                 'zipcode': 'value',
#                                 'neighbourhood': 'value',
#                                 'primary': True,
                
#                             })
#     assert response.status_code == 201
#     assert response.json()['customer_id'] == address.customer_id
#     assert response.json()['city'] == 'sp'
#     assert response.json()['Address'] == 'rua'