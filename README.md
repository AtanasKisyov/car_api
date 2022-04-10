Car API

Authentication Endpoints:

POST /account/register/


data = {

    'username',
    'first_name',
    'last_name',
    'password'

}

POST /account/login/

data = {

    'username',
    'password',

}

App Endpoints:

GET, POST /car/car-brand/

data = {

    ['car_brand', 'car_brand', 'car_brand']

}

GET, POST, DELETE /car/brand/{id}

data = {

    'car_brand_name'

}

GET, POST /car/car-model/

data = {

    ['car_model', 'car_model', 'car_model']

}

GET, POST, DELETE /car/car-model/{id}

data = {

    'car-model'

}

GET, POST /car/user-car/

data = {

    ['user_car', 'user_car', 'user_car']

}

GET, POST, DELETE /car/user-car/{id}

data = {

    'user_car'

}