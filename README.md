# API: Customer and User one to one releationship:

## Suppose you have two model with name user and customer. And customer are related to user with one to one relationship. You have to create a rest api view for create a customer.

### Field of user are:-

1. first_name
2. last_name
3. email
4. mobile no.

### Field of customer are:-

- profile number

#### Note:- email and mobile number are unique.

## Steps to Execute the project

## 1. Clone repository -

Run the following command to clone the repository:

```bash
git clone git@github.com:acemourya/Store-Project.git
```

After succesfully cloning the repository, move the current directory to store-project by running the following command:

```bash
cd StoreProject
```

## 2. Set up the virtual environment -

Make sure that virtualenv package is already installed. If not, install it using the following command:

```bash
$ pip3 install virtualenv
```

Now, create the virtual environment:

```bash
$ virtualenv venv -p python3
```

Activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

## 3. Install dependencies -

Install the requirements for the project using the **requirements.txt** file:

```bash
$ pip3 install -r requirements.txt
```

## 4. Run the project -

1. Run mange.py
   - $ python3 manage.py makemigrations
   - $ python3 manage.py migrate
2. Create superuser account by
   - $ python3 manage.py createsuperuser
   - $ python3 manage.py migrate
3. Run server
   - $ python3 manage.py runserver

Open given server link on brower :

    http://127.0.0.1:8000/customer/

    Input Body:

    {
      "profile_number": 1234,
      "user": {
         "first_name": "XYZ",
         "last_name": "XYZ",
         "email": "xyz@gmail.com",
         "phone_number": "1234556789"
         }
      }

## 6. For stoping runable project

In terminal press: **ctrl + C**

Deactivate virtual environment.

```bash
$ deactivate
```
