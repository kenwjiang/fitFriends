from __future__ import unicode_literals
from django.db import models
# from apps.finder_app.models import Gym
from datetime import datetime, timedelta, date
import bcrypt
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class LoginManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if not email_regex.match(postData['log-email']):
            errors['email_login'] = 'Please enter a valid email.'
        if len(postData['current-password']) < 8:
            errors['password_login']= 'Please enter a valid password.'

        user = User.objects.filter(email=postData['log-email'])
        if len(user) == 0:
            errors['no_user'] = 'This account does not exist yet.'
        for user_login in user:
            if not bcrypt.checkpw(postData['current-password'].encode(), user_login.password.encode()):
                errors['no_match'] = 'The email and password combination does not match.'
        return errors

    def registration_validator(self, postData):
        errors = {}
        if not email_regex.match(postData['email']):
            errors['email_reg'] = 'Invalid Email Address! Please enter a valid email address'
        all_users = User.objects.all()
        for user in all_users:
            if user.email == postData['email']:
                errors['existing'] = 'This email already exists in our database!'


        if postData['dob'] == '':
            errors['birthday'] = 'Please enter a valid date of birth.'
        else:
            dob = datetime.strptime(postData['dob'], '%Y-%m-%d')
            today = date.today()
            if (dob.year + 13, dob.month, dob.day) > (today.year, today.month, today.day):
                errors['birthday'] = 'You must be at least 13 years old to register.'

        password = postData['reg-password']
        if postData['reg-password'] != postData['pw_confirm'] or len(postData['pw_confirm']) == 0:
            errors['pw_confirm'] = 'Passwords do not match, please check again.'
        if len(password) < 8:
            errors['pw'] = 'Your password should be at least 8 characters.'
        elif re.search('[0-9]', password) is None:
            errors['pw'] = 'Your password must contain at least 1 number.'


        if len(postData['first_name']) < 2:
            errors['first_name'] = 'Please enter a valid first name.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Please enter a valid last name.'
        return errors

    def ajax_validator(self, postData):
        errors = {}
        if not email_regex.match(postData['email']):
            errors['email_reg'] = 'Invalid Email Address! Please enter a valid email address'
        all_users = User.objects.all()
        for user in all_users:
            if user.email == postData['email']:
                errors['existing'] = 'This email already exists in our database!'
        return errors

class Gym(models.Model):
    place_id = models.CharField(max_length=100, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #default gym - user foreign key

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    def_gym = models.ForeignKey(Gym, related_name='user_gym', default=None)
    gender = models.CharField(max_length=25, choices=(('male','Male'),('female','Female')))
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

class Preference(models.Model):
    gender = models.CharField(max_length=25, choices=(('male','Male'),('female','Female')))
    categories = models.CharField(max_length=255)
    user_schedule = models.CharField(max_length=255)
    userPref = models.ForeignKey(User, related_name='preference')
    # gymPref = models.ForeignKey(Gym, related_name="gymPrefence")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
