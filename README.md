# Pet Feeder And Monitor (PFAM)

### User Guide to install and run the project

- Firstly clone the repo using:

    ```git
    git clone https://github.com/Vedant950/pfam.git
    ```

- Then navigate to the pfam folder.
- Make sure you have virual enviroment installed in your pc, if not you can download the same by using:

    ```python
    pip install virtualenv
    ```

- Then create a virtual enviroment using:

    ```python
    virtualenv env
    ```

- Activate the enviroment using:

    ```cmd
    env\Scripts\activate
    ```

- Install django using:

    ```python
    pip install django
    ```

- Then to get the database, so that the website can store the data, run:

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

- Then create a super user, so that you can access the database. Execute the commoand and do as directed:

    ```python
    python manage.py createsuperuser
    ```

- Finally, to run the server:

    ```python
    python manage.py runserver
    ```
