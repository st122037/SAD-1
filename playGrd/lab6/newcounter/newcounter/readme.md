1. Create a folder and add the necessary docker-compose.yml, dockerfile and requirements.txt
2. Then create python django app using :
    sudo docker-compose run web django-adminstartproject newcounter
3. Then chann=ge the DATABASES from settings.py
4. Then create a django app using:
    sudo docker-compose run web pytohn3 manage.py startapp newcounter1
5. Then do sudo docker-compose up
6. Open another terminal and check sudo docker ps
7.  Then run sudo docker exec -it newcounter_web_1 bash
8. Then inside, type python3 manage.py makemigrations newcounter1 to create a migration folder
9. Then migrate it using pytohn3 manage.py migrate
10. Then check your http://localhost:8000 to check the counter and value.    