from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=16, null=False, blank=False, unique=True)
    joined_date = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['-last_seen', 'joined_date']

    def __unicode__(self):
        return u"{username} [{phone_number}]".format(username=self.username, phone_number=self.phone_number)


class SectionCategory(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    slug = models.SlugField()

    class Meta:
        db_table = 'section_categories'
        ordering = ['name']



class Section(models.Model):
    owner = models.ForeignKey('User', null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey('SectionCategory', null=False, blank=False)
    ordering_number = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sections'
        ordering = ['ordering_number']

    def __unicode__(self):
        return u"{name} [{category}]".format(name=self.name, category=self.category)


class Member(models.Model):

    class Meta:
        db_table = 'members'

    pass


class Room(models.Model):

    class Meta:
        db_table = 'rooms'

    pass
