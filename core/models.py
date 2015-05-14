from django.db import models


class User(models.Model):

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
