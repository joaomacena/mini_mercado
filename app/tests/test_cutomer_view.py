from fastapi.testclient import TestClient
import factory

def test_customer_create(client:TestClient, admin_auth_header):
    
    response = client.post('/customer/',
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
