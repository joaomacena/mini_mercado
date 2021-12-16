from fastapi.testclient import TestClient

def test_product_discount_create(client:TestClient ,admin_auth_header,
            product_factory, payment_method_factory):
    
    product=product_factory()
    payment_method= payment_method_factory()

    response = client.post('/product_discount/', headers= admin_auth_header,
                            json={
                                'mode': 'value',
                                'value': 12 ,
                                'product_id': product.id ,
                                'payment_method_id' : payment_method.id
                            })
    assert response.status_code == 201
    assert response.json()['value'] == 12


def test_product_discount_create_for_equal_produto(client:TestClient ,admin_auth_header,
            product_factory, payment_method_factory):
    
    product = product_factory()
    payment_method = payment_method_factory()

    response = client.post('/product_discount/', headers= admin_auth_header,
                            json={
                                'mode': 'value',
                                'value': 12 ,
                                'product_id': product.id ,
                                'payment_method_id' : payment_method.id
                            })
    assert response.status_code == 201
    assert response.json()['value'] == 12

    response = client.post('/product_discount/', headers= admin_auth_header,
                            json={
                                'mode': 'value',
                                'value': 15 ,
                                'product_id': product.id ,
                                'payment_method_id' : payment_method.id
                            })

    assert response.status_code == 400
    assert response.json()['detail'] == "Already exists a discount with this payment method"


def test_product_discount_create_for_enabled_payment_method(client:TestClient ,admin_auth_header,
            product_factory, payment_method_factory):
    
    product = product_factory()
    payment_method = payment_method_factory(enabled = False)

    response = client.post('/product_discount/', headers= admin_auth_header,
                            json={
                                'mode': 'value',
                                'value': 12 ,
                                'product_id': product.id ,
                                'payment_method_id' : payment_method.id
                            })

    assert response.status_code == 400
    assert response.json()['detail'] == "This payment method is not available"


def test_product_discount_update(client:TestClient ,admin_auth_header,
            product_factory, payment_method_factory,product_discount_factory):
    product = product_factory()
    payment_method = payment_method_factory()
    
    product_discount = product_discount_factory()

    response = client.put(f'/product_discount/{product_discount.id}', headers= admin_auth_header,
                            json={
                                'mode': 'value',
                                'value': 1100 ,
                                'product_id': product.id ,
                                'payment_method_id' : payment_method.id
                            })
    assert response.status_code == 200
    assert response.json()['value'] == 1100