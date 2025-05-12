from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education, Testimonial

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'professional_title')
    fieldsets = (
        ('Basic Info', {
            'fields': ('full_name', 'professional_title', 'photo', 'resume')
        }),
        ('Professional Details', {
            'fields': ('short_bio', 'core_skills', 'career_highlights', 'mission_statement')
        }),
    )

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Testimonial)