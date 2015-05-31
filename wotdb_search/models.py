from django.db import models

class Book(models.Model):
    title  = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def chapters(self):
        return Chapter.objects.filter(book_id=self.id).extra(order_by = ['number'])

class ChannelerType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Chapter(models.Model):
    number  = models.IntegerField(default=0)
    title   = models.CharField(max_length=100, default="")
    book    = models.ForeignKey(Book)

    def characters(self):
        povs = PointOfView.objects.all().filter(chapter_id=self.id)
        return povs

class Clan(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Interview(models.Model):
    author   = models.CharField(max_length=100, default="Robert Jordan")
    question = models.TextField(default="")
    answer   = models.TextField(default="")
    name     = models.TextField(default="")
    date     = models.CharField(max_length=32, default="")

class Job(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    COUNTRY = "Country"
    CITY    = "City"
    PLACE_TYPES = (
        (COUNTRY, "Country"),
        (CITY, "City")
    )
    name        = models.CharField(max_length=100)
    place_type  = models.CharField(max_length=32,
                                  choices=PLACE_TYPES,
                                  null=True)
    ruler       = models.CharField(max_length=100, default="")
    allegiance  = models.CharField(max_length=100, default="None")
    description = models.TextField(default="")

    def __unicode__(self):
        return self.name

    def characters(self):
        return Character.objects.filter(country_id=self.id) | Character.objects.filter(city_id=self.id)

class Sept(models.Model):
    name = models.CharField(max_length=100)
    clan = models.OneToOneField(Clan)

    def __unicode__(self):
        return self.name

class Society(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Character(models.Model):
    # Genders
    MALE   = "Male"
    FEMALE = "Female"
    OTHER  = "Other"

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )

    # Alignments
    LIGHT  = "Light"
    DARK   = "Dark"
    NEUTRAL = "Neutral"

    ALIGNMENTS = (
        (LIGHT, "Light"),
        (DARK,  "Dark"),
        (NEUTRAL, "Neutral")
    )

    # Statuses
    ALIVE   = "Alive"
    DEAD    = "Dead"
    UNKNOWN = "Unknown"

    STATUSES = (
        (ALIVE, "Alive"),
        (DEAD, "Dead"),
        (UNKNOWN, "Unknown")
    )

    # Fields
    name        = models.CharField(max_length=100)
    description = models.TextField(default="")
    gender      = models.CharField(max_length=16, default="")
    title       = models.CharField(max_length=64, default="")
    allegiance  = models.CharField(max_length=32, default="")
    age         = models.IntegerField(default=0)
    alignment   = models.CharField(max_length=32,
                                   choices=ALIGNMENTS,
                                   default=NEUTRAL)
    status      = models.CharField(max_length=32,
                                   choices=STATUSES,
                                   default=UNKNOWN)

    # Relationships
    channeler_type = models.ForeignKey(ChannelerType, null=True)
    clan           = models.ForeignKey(Clan,          null=True)
    job            = models.ForeignKey(Job,           null=True)
    sept           = models.ForeignKey(Sept,          null=True)
    society        = models.ForeignKey(Society,       null=True)
    city           = models.ForeignKey(Place,         null=True, related_name="city")
    country        = models.ForeignKey(Place,         null=True, related_name="country")

    def __unicode__(self):
        return self.name;

    def is_alive(self):
        return self.status == self.ALIVE

    def is_aiel(self):
        return self.sept or self.clan or self.society

class PointOfView(models.Model):
    character = models.ForeignKey(Character)
    book      = models.ForeignKey(Book)
    chapter   = models.ForeignKey(Chapter)
