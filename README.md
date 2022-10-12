# Django Learning Project
### I created this repository to follow the Django Tutorial available at https://docs.djangoproject.com/en/4.1/intro/tutorial01/

### I also used a docker structure to build this project
<br>
To build it just run:

``` 
    docker-compose build
```

To run the container execute:
```
    docker-compose run
```

To access the container bash execute:
```
    docker exec -it <containerID> bash
```

Container id can be found running `docker ps`.

To run the manage.py:
```
    docker-compose run web python manage.py
```

To run the py shell command:
```
    docker-compose run web python manage.py shell
```