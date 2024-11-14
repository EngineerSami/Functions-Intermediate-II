# login_app/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
import re

class UserManager(models.Manager):
    def validate_user_data(self, first_name, last_name, email, password, confirm_password):
        errors = []
        
        if len(first_name) < 2 or not first_name.isalpha():
            errors.append("First name must be at least 2 characters and contain only letters.")
        
        if len(last_name) < 2 or not last_name.isalpha():
            errors.append("Last name must be at least 2 characters and contain only letters.")


        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            errors.append("Enter a valid email address.")


        if self.filter(email=email).exists():
            errors.append("Email is already registered.")


        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        

        if password != confirm_password:
            errors.append("Passwords do not match.")
        
        return errors

    def create_user(self, first_name, last_name, email, password, confirm_password):

        errors = self.validate_user_data(first_name, last_name, email, password, confirm_password)
        if errors:
            raise ValidationError(errors)
        

        hashed_password = make_password(password)
        

        user = self.create(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        return user

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=100)  


    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
