# How Project Works:

1) Clone the project on your system:

    
    git clone git@github.com:PsymoNiko/Task.git

2) Create Virtual environment and activate it:
    <h5>Create venv:</h5>
    
        python3 -m venv venv    

    <h66>Activate on Linux:</h6>

        source venv/bin/activate

    <h6>Activate on Windows:</h6>
        
        venv/Scripts/activate

    <h6>Activate on Mac:</h6>
        
        source venv/bin/activate

3) Install requirements:

        
    pip install -r requirements.txt


4) Set migrations on database and create your admin user:


    python manage.py migrate
    
    python manage.py createsuperuser

# Run:

    python manage.py runserver

# HAVE FUN
http://127.0.0.1:8000/