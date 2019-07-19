# from django.db import models
# from apps.login_and_registration.models import User
# from django.core.validators import MaxValueValidator
# from datetime import datetime, timedelta, date, time
#
# class PreferenceCalculator(models.Manager):
#     def pref_calc(self, postData):
#         pref_strength = {
#         }
#         # assign +1 value to each of the check boxes
#         if postData['weightLoss']:
#             pref_strength['weightLoss'] = 1
#         if postData['cardio']:
#             pref_strength['cardio'] = 1
#         if postData['endurance']:
#             pref_strength['endurance'] = 1
#         if postData['flexibility']:
#             pref_strength['flexibility'] = 1
#         if postData['strength']:
#             pref_strength['strength'] = 1
#         if postData['muscle']:
#             pref_strength['muscle'] = 1
#         if postData['genFit']:
#             pref_strength['genFit'] = 1
#
#
# # class Gym(models.Model):
# #     id = models.CharField(max_length=100)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)
# #     #default gym - user foreign key
# class Preference(models.Model):
#     gender = models.CharField(max_length=25, choices=(('male','Male'),('female','Female')))
#     categories = models.CharField(max_length=255)
#     user_schedule = models.CharField(max_length=255)
#     userPref = models.ForeignKey(User, related_name='preference')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
