from fastapi.testclient import TestClient
import factory

def test_customer_create(client:TestClient, admin_auth_header):
    
    response = client.post('/customer/',
                            headers= admin_auth_header,
                            json={
                                "fist_name": "jose",
                                "last_name": "p",
                                "phone_number": "40028922",
                                "genre": "g",
                                "document_id": "string",
                                "birth_date": "2021-12-16",
                                "user_id": {
                                    "display_name": "jose25",
                                    "email": "jose@",
                                    "password": "123",
                                    "role": "customer"
                                    }
                            })

    assert response.status_code == 201
    assert response.json()['user']['display_name'] == "jose25"
    assert response.json()['user']['email'] == 'jose@'
    assert response.json()['user']['role'] == 'customer'


# def test_customer_update(client:TestClient, admin_auth_header):
#     response = client.post('/customer/',
#                             headers= admin_auth_header,
#                             json={
#                                 "fist_name": "jose",
#                                 "last_name": "p",
#                                 "phone_number": "40028922",
#                                 "genre": "g",
#                                 "document_id": "string",
#                                 "birth_date": "2021-12-16",
#                                 "user_id": {
#                                     "display_name": "jose25",
#                                     "email": "jose@",
#                                     "password": "123",
#                                     "role": "customer"
#                                     }
#                             })

#     assert response.status_code == 201
#     id_atual = response.json()['id']
    

#     response = client.put(f'/customer/{id_atual}',
#                             headers= admin_auth_header,
#                             json={
#                                 "fist_name": "jose",
#                                 "last_name": "p",
#                                 "phone_number": "40028922",
#                                 "genre": "g",
#                                 "birth_date": "2021-12-16",
#                                 "user_id": {
#                                     "display_name": "jose25",
#                                     "email": "jose@",
#                                     "password": "123",
#                                     "role": "customer"
#                                     }
#                             })

#     assert response.status_code == 200
#     assert response.json()['user']['display_name'] == "jose25"
#     assert response.json()['user']['email'] == 'jose@'
#     assert response.json()['user']['role'] == 'customer'