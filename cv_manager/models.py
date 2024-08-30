from django.db import models
from django.utils.text import slugify

class ColorPallete(models.Model):
    pallete_name = models.CharField(max_length=30, null=False)
    primary_color = models.CharField(max_length=30, null=False)
    secondary_color = models.CharField(max_length=30, null=False)
    contrast_color = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.pallete_name

class Person(models.Model):
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    profile_image = models.ImageField(
        upload_to='profile_images/',  
        height_field=None,  
        width_field=None,  
        max_length=255,  
        blank=True, 
        null=True  
    )
    about = models.TextField(null=False)
    slug = models.SlugField(null=False)
    pallete = models.ForeignKey(ColorPallete, related_name='color_pallete', on_delete=models.PROTECT, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name.split[0]} {self.last_name.split[0]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name}, {self.name}"

class Contact(models.Model):
    Types = [
        ('fas fa-envelope','Email'),
        ('fas fa-phone','Phone'),
        ('fas fa-map-marker-alt','Adress'),
        ('fab fa-github','Github'),
        ('fab fa-linkedin','Linkedin'),
        ('fab fa-facebook','Facebook'),
        ('fab fa-instagram','Instagram'),
        ('fab fa-twitter','Twitter'),
        ('fas fa-cogs','Other'),
    ]
    
    person = models.ForeignKey(Person, related_name='contacts', on_delete=models.CASCADE)
    value = models.CharField(max_length=30,null=False)
    contact_type = models.CharField(max_length=30, choices=Types)

    def __str__(self):
        return f"({self.get_contact_type_display()}) {self.value}"
    
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
