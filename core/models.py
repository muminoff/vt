from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=16, null=False, blank=False, unique=True)
    joined_date = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    pass


class Announcement(models.Model):

    class Meta:
        db_table = 'announcements'

    pass


class Member(models.Model):

    class Meta:
        db_table = 'members'

    pass


class Room(models.Model):

    class Meta:
        db_table = 'rooms'

    pass
