from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def checkEmailAgainstDatabase(postData):

    user = User.objects.filter(email=postData['email'])
    if not user:
        return True
    else:
        return False


class UserManager(models.Manager):
    #function to check if email is already in database

    def data_validator_registration(self, postData):
        errors={}
        if len(postData['f_name']) < 1:
            errors['f_name'] = "Name cannot be blank!"
        elif len(postData['f_name']) < 2:
            errors['f_name'] = "Name cannot be less than 2 characters!"
        elif not postData['f_name'].replace(" ","").isalpha():
            errors['f_name'] = "Name cannot contain non alphabets!"

        if len(postData['l_name']) < 1:
            errors['l_name'] = "Last name name cannot be blank!"
        elif len(postData['l_name']) < 2:
            errors['l_name'] = "Last name Name cannot be less than 2 characters!"
        elif not postData['l_name'].replace(" ","").isalpha():
            errors['l_name'] = "Last name cannot contain non alphabets!"

        #email validation
        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be blank!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email format should be like abc@gmail.com..!"
        #check if email already in database
        elif not checkEmailAgainstDatabase(postData):
            errors['email'] = "Email already exists in database..!"
            print "checked in database!!cleared"

        if len(postData['password']) < 1:
            errors['password'] = "Password cannot be blank!"
        elif len(postData['password']) < 8:
            errors['password'] = "Password cannot be less than 8 characters!"

        if len(postData['pw_confirm']) < 1:
            errors['pw_confirm'] = "Enter Password again to confirm!"
        elif postData['password']!=postData['pw_confirm']:
            errors['pw_confirm'] = "Passwords do not match!"

        return errors

    def data_validator_login(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be blank!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email format should be like abc@gmail.com..!"
        elif checkEmailAgainstDatabase(postData):
            errors['email'] = "Email does not exist in database..!"

        if len(postData['password']) < 1:
            errors['password'] = "Password cannot be blank!"
        if not errors:
            # query db to check password
                user = User.objects.filter(email=postData['email'])
            # check input against hashed password
                hashed = user[0].password
                password = postData['password']
                if not bcrypt.checkpw(password.encode(), hashed.encode()):
                    errors['mismatch'] = "Incorrect password!!"
        return errors

class Level(models.Model):
    level = models.CharField(max_length=255)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    level = models.ForeignKey(Level, related_name="users",default=2)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()

#stores messages
