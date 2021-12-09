# Server Manager
This is a Server management software based on django .To store passwords and private keys the project uses keepass password manager( a famous open source password manager) so the all the details are encrypted.The web app also has a monitoring app with cpu and memory usage indicators

The projects aim is to reduce the hassle of managing passwords and keys all in one place.

## Usage

#### Using python
+ `pip install -r requirements.txt`
+ ` wssh --port=8888 --xheaders=False --origin='127.0.0.1:8000' `
On another terminal
+ `python manage.py runserver`


#### Using Docker
+ `docker -t server_manager build .`
+ `docker run  -p 8000:8000 -p 8888:8888 server_manager`

you can also add your password database to /code/DB using volume
#### Using Docker-Compose
    version: "3"
    services:
    server-manager:
        image: harsh18262/server_manager
        volumes:
        - ./password_db.kdbx:/code/DB/password_db.kdbx
        ports:
        - "8000:8000"
        - "8888:8888"


## Screenshots
![Create Keyring Screenshot](https://raw.githubusercontent.com/harsh18262/server_manager_django/main/Screenshots/create_login.png)

![Unlock Keyring Screenshot](https://raw.githubusercontent.com/harsh18262/server_manager_django/main/Screenshots/login.png)

![SSH Screenshot](https://raw.githubusercontent.com/harsh18262/server_manager_django/main/Screenshots/ssh.png)

![Monitoring Screenshot](https://raw.githubusercontent.com/harsh18262/server_manager_django/main/Screenshots/monitoring.png)

![Keyring Screenshot](https://raw.githubusercontent.com/harsh18262/server_manager_django/main/Screenshots/keyring.png)





