from django.db import models

# Create your models here.

COURSES = (('BTech', 'BTech'),
           ('MTech', 'MTech'),
           ('BCA', 'BCA'),
           ('MCA', 'MCA'),
           )

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class Student(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(
        default='Male', choices=GENDER_CHOICES, max_length=10)
    course = models.CharField(default='BTech', choices=COURSES, max_length=10)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name + "-" + self.city


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name + "-" + self.email
