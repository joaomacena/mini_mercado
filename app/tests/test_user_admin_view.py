from fastapi.testclient import TestClient

def test_user_admin_create(client:TestClient ,admin_auth_header):
    response = client.post('/admin_user/',
                            headers= admin_auth_header,
                            json={
                                'display_name': 'test',
                                'email': 'tetes@',
                                'password': '123',
                                'role' : 'admin'
                            })
    assert response.status_code == 201
    assert response.json()['email'] == 'tetes@'


def test_user_admin_create_equal_email_error(client:TestClient ,admin_auth_header):
    response = client.post('/admin_user/',
                            headers= admin_auth_header,
                            json={
                                'display_name': 'test',
                                'email': 'tetes@',
                                'password': '123',
                                'role' : 'admin'
                            })
    assert response.status_code == 201
    assert response.json()['email'] == 'tetes@'

    response = client.post('/admin_user/',
                            headers= admin_auth_header,
                            json={
                                'display_name': 'test2',
                                'email': 'tetes@',
                                'password': '1235',
                                'role' : 'admin'
                            })
    assert response.status_code == 400



def test_user_admin_update(client:TestClient ,admin_auth_header):
    response = client.post('/admin_user/',
                            headers= admin_auth_header,
                            json={
                                'display_name': 'test',
                                'email': 'tetes@',
                                'password': '123',
                                'role' : 'admin'
                            })
    assert response.status_code == 201
    assert response.json()['display_name'] == 'test'
    id_atual = response.json()['id']
    

    response = client.put(f'/admin_user/{id_atual}',
                            headers= admin_auth_header,
                            json={
                                'display_name': 'test_novo',
                                'email': 'tetes@',
                                'password': '123',
                                'role' : 'admin'
                            })
    assert response.status_code == 200

    