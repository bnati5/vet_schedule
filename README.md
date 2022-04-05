# Vetster Schedule

This very simple Django app checks for availability of a vet in the calendar with 1 hour interval. The data is stored in a json file under ```\assets\data\blocks.json```


## How to run the app (django)  


1. Create a virtual environment.

If you are using python3 please replace python with python3 in the below bash command 

```shell
python -m venv env
source env/bin/activate
```

2. Install requirements.txt  

If you are using pip3 please replace pip with pip3 in the below bash command 

```shell
pip install -r requirements.txt
```

3. Runserver

```shell
python manage.py runserver
```
Alternatively you can specify the port:

```shell
python manage.py runserver <port>
```
 
## How to test the API

1. Using cURL

Please replace the <YYYY-MM-DDThh:mm:ssTZD> with a datetime sting folowing the format.
```shell
curl --location --request POST 'http://localhost:7000/vet-schedule/?datetime_start=<YYYY-MM-DDThh:mm:ssTZD>'
```
sample:
```shell
curl --location --request POST 'http://localhost:7000/vet-schedule/?datetime_start=2021-11-30T10:00:00-06:00'
```


You can use any testing method you with. However the request should only be sent through **POST**

