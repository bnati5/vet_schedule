# Vetster Schedule

This very simple Django app checks for availability of a vet in the calendar with 1 hour interval. The data is stored in a json file under ```\assets\data\blocks.json```


## How to run the app (django)  

1. Clone repo
```shell
git clone https://github.com/bnati5/vet_schedule.git
cd vet_schedule/
```


2. Create a virtual environment

If you are using python3 please replace **python** with **python3** in the below bash command

** For Windows **
```shell
python -m venv env
source env/scripts/activate
```
** For MAC **
```shell
python -m venv env
source env/bin/activate
```

3. Install requirements.txt  

If you are using **pip3** please replace **pip** with **pip3** in the below bash command 

```shell
pip install -r requirements.txt
```

4. Runserver

```shell
python manage.py runserver 7000
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

