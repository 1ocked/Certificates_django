from django.db import models

class Owner(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    certificate_number = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.certificate_number


class CertificateSkill(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class OwnerSkill(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)