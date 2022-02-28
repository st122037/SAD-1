To create a HELLO-WORLD web application container using Django, I am using a docker container inside a django application. To do that :<br>
Create a new django project : django-admin startproject DockerinDjango<br>
Then create a new django application : python3 manage.py startapp Docker_in_Django<br>
Then create a view in django application<br>
Do the required changes in settings.py, urls.py and views.py<br>
Create a new Dockerfile in the root of the project folder.<br>
Now build the container image : docker build -t dockerindjango .<br>
Then run the container : docker run -it -p 8000:8000 dockereindjango<br>
Now visit http://localhost:8000 in the local browser to see the response.
