from django.db import models
from django.utils.text import slugify

class Person(models.Model):
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    about = models.TextField(null=False)
    slug = models.SlugField(null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name.split[0]} {self.last_name.split[0]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name}, {self.name}"

class Contact(models.Model):
    Types = [
        ('email','Email'),
        ('phone','Phone'),
        ('adress','Adress'),
        ('github','Github'),
        ('linkedin','Linkedin'),
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
        ('other','Other'),
    ]
    
    person = models.ForeignKey(Person, related_name='contacts', on_delete=models.CASCADE)
    value = models.CharField(max_length=30,null=False)
    contact_type = models.CharField(max_length=30, choices=Types)

    def __str__(self):
        return f"({self.contact_type}) {self.person}"
    
class Language(models.Model):
    person = models.ForeignKey(Person, related_name='languages', on_delete=models.CASCADE)
    value = models.CharField(max_length=30,null=False)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.value

class Aptitude(models.Model):
    person = models.ForeignKey(Person, related_name='aptitudes', on_delete=models.CASCADE)
    value = models.CharField(max_length=30,null=False)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.value
    
class Skill(models.Model):
    person = models.ForeignKey(Person, related_name='skills', on_delete=models.CASCADE)
    value = models.CharField(max_length=30,null=False)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.value
    
class Education(models.Model):
    person = models.ForeignKey(Person, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=100,null=False)
    description = models.TextField(null=True, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.institution

class LaboralExp(models.Model):
    person = models.ForeignKey(Person, related_name='laboral_experience', on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.position

# Create your models here.
