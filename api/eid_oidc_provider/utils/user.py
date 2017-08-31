from django.contrib.auth.models import User

def username_exists_in_db(username):
    return User.objects.filter(username=username).exists()
