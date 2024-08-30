from django.contrib import admin
from .models import *

# Inline classes for each related model
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1  # Number of extra forms to display
    fields = ['contact_type', 'value']
    # If you want to limit the fields in the inline forms

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['value', 'proficiency']

class AptitudeInline(admin.TabularInline):
    model = Aptitude
    extra = 1
    fields = ['value', 'proficiency']

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1
    fields = ['value', 'proficiency']

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ['institution', 'description', 'start_year', 'end_year', 'location', 'website']

class LaboralExpInline(admin.TabularInline):
    model = LaboralExp
    extra = 1
    fields = ['company', 'position', 'start_year', 'end_year', 'website']

# Main PersonAdmin class
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'slug', 'pallete']
    inlines = [ContactInline, SkillInline, AptitudeInline, LanguageInline, EducationInline, LaboralExpInline]
    prepopulated_fields = {"slug": ("name", "last_name")}

admin.site.register(ColorPallete)