To create a HELLO-WORLD web application container using Django, I am using a docker container inside a django application. To do that :<br>
Create a new django project : django-admin startproject DockerinDjango
Then create a new django application : python3 manage.py startapp Docker_in_Django
Then create a view in django application
Do the required changes in settings.py, urls.py and views.py
Create a new Dockerfile in the root of the project folder.
Now build the container image : docker build -t dockerindjango .
Then run the container : docker run -it -p 8000:8000 dockereindjango
Now visit http://localhost:8000 in the local browser to see the response.
