# Pour lancer loush
 
*** Installation de l'environnement virtuel**
-python -m venv venv (window) 
-python3 -m venv venv (ubuntu/macos)

**Activation de l'environnement virtuel***
 # Window
 - source venv/Scripts/activate (git Bash/ Bash)
 - ./venv/Scripts/activate (Powershell)

 # Ubuntu/MacOs
 - source venv/Scripts/activate

*** Installation des différents package ***
Il faut la commande suivante:
 - pip install -r requirements.txt (tous les systèmes)


 `Pour les tâches en arrières plan`
  Il faut installer celery et Redis, voici le lien pour passer à l'installation sur les différents systèmes
 # https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/

  *** lancer celery sur le terminal ***
  - celery -A core worker -l INFO
  
  *** verifier que redis est en cours ***
  - redis-cli
    si redis est lancer, vous aurez une reponse : 127.0.0.1:6379>


  *** lancer maintenant le projet ***
 - python manage.py runserver (window)
 - python3 manage.py runserver (ubuntu/macos)