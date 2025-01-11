from django.contrib import admin
from .models import Owner, Skill, Certificate, CertificateSkill, OwnerSkill

admin.site.register(Owner)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(CertificateSkill)
admin.site.register(OwnerSkill)