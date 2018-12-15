# django-cloud
personal cloud power by django framework

## Usage

```shell
$ python -V
3.x.x
$ pip -V
...python 3.x.x
...
$ pip install django
.........

$ cd cloudsource
$ python manage.py runserver 0.0.0.0:8000
....
....
Ctrl+C to quit!
```

open browser, link to "http://your_server_ip_which_running_the_django:8000/basic/"

now, you can upload your file on it.

## Note

django-cloud server only support USER HOME diretory for now,

for example,

you running by `$ python manage.py ...`, it is on your `/home/<your logging USER>/` diretory can be select to save upload file;
