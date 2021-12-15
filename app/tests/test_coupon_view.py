from fastapi.testclient import TestClient


def test_coupon_create(client:TestClient,admin_auth_header):
    response = client.post('/coupon/',
                            headers= admin_auth_header,
                            json={
                                'code': '12348',
                                'expire_at': "2021-12-16T15:57:01.902Z",
                                'limit': 10,
                                'type': 'value',
                                'value': 10.0
                            })
    assert response.status_code == 201
    assert response.json()['code'] == '12348'
    assert response.json()['limit'] == 10


def test_coupon_create_two_code_error(client:TestClient, admin_auth_header):
    response = client.post('/coupon/',
                            headers= admin_auth_header,
                            json={
                                'code': '12348',
                                'expire_at': "2021-12-16T15:57:01.902Z",
                                'limit': 10,
                                'type': 'value',
                                'value': 10.0
                            })
    assert response.status_code == 201
    response = client.post('/coupon/',
                            headers= admin_auth_header,
                            json={
                                'code': '12348',
                                'expire_at': "2021-12-19T15:57:01.902Z",
                                'limit': 5,
                                'type': 'value',
                                'value': 15.0
                            })
    print(response)
    assert response.status_code == 400


def test_coupon_update(client:TestClient, admin_auth_header):
    response = client.post('/coupon/',
                            headers= admin_auth_header,
                            json={
                                'code': '12345',
                                'expire_at': "2021-12-14T15:57:01.902Z",
                                'limit': 10,
                                'type': 'value',
                                'value': 10.0
                            })
    assert response.status_code == 201
    
    response = client.put('/coupon/1',
                            headers= admin_auth_header,
                            json={                               
                                'limit': 100,
                                'expire_at': "2021-12-19T15:57:01.902Z",
                            })

    assert response.status_code == 200
    assert response.json()['limit'] == 100
    assert response.json()['expire_at'] == '2021-12-19T15:57:01.902000'


