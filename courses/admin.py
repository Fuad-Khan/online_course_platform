from django.contrib import admin
from .models import (
    Instructor,
    Course,
    Student,
    Enrollment,
    Review
)


# ==========================
# Instructor Admin
# ==========================
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "expertise")
    search_fields = ("name", "expertise")


# ==========================
# Course Admin
# ==========================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "instructor",
        "price",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "instructor__name",
    )

    list_filter = (
        "category",
        "instructor",
    )


# ==========================
# Student Admin
# ==========================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "enrolled_date",
    )

    search_fields = (
        "user__username",
        "user__email",
    )


# ==========================
# Enrollment Admin
# ==========================
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
        "completed",
        "enrolled_on",
    )

    list_filter = (
        "completed",
        "course",
    )

    search_fields = (
        "student__user__username",
        "course__title",
    )


# ==========================
# Review Admin
# ==========================
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course",
        "student",
        "rating",
        "created_at",
    )

    list_filter = (
        "rating",
        "course",
    )

    search_fields = (
        "course__title",
        "student__user__username",
    )