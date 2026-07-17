from django.db import models
from django.contrib.auth.models import User


# ==========================================
# Abstract Base Model
# ==========================================
class BaseInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ==========================================
# Instructor Model
# ==========================================
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ==========================================
# Course Model
# Inherits BaseInfo
# ==========================================
class Course(BaseInfo):
    CATEGORY_CHOICES = [
        ("Programming", "Programming"),
        ("Design", "Design"),
        ("Business", "Business"),
        ("Marketing", "Marketing"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.title


# ==========================================
# Student Model
# OneToOne with User
# ==========================================
class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# ==========================================
# Enrollment Model
# ==========================================
class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    enrolled_on = models.DateField(auto_now_add=True)

    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"


# ==========================================
# Review Model
# Inherits BaseInfo
# ==========================================
class Review(BaseInfo):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.IntegerField()

    comment = models.TextField()

    def __str__(self):
        return f"{self.course} - {self.rating}/5"