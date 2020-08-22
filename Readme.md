### sponsorship-sample-web

#### Configure database and email details in settings.py file.
#### Execute following commands to setup database with necessary tables.
`<venv>/python manage.py makemigrations`
####
`<venv>/python manage.py migrate`
#### Create admin user for your application
`<venv>/python manage.py createsuperuser`
#### create admin credentials when prompted
#### Now run the application
`<venv>/python manage.py runserver`
#### the application would be started in localhost:8000 port.