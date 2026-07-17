from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from django.db import connection
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .forms import StudentRegistrationForm
from .models import (
    Student,
    Course,
    Enrollment,
)


# -------------------------
# Registration
# -------------------------
def register(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            Student.objects.create(user=user)

            login(request, user)

            return redirect("my_enrollments")

    else:

        form = StudentRegistrationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )


# -------------------------
# My Enrollments
# -------------------------
class MyEnrollmentsView(LoginRequiredMixin, ListView):

    model = Enrollment

    template_name = "my_enrollments.html"

    context_object_name = "enrollments"

    login_url = "/login/"

    def get_queryset(self):
        return Enrollment.objects.filter(
            student__user=self.request.user
        ).select_related("course")


# -------------------------
# Query Results
# -------------------------
def query_results(request):

    courses = Course.objects.select_related("instructor")

    students = Student.objects.prefetch_related(
        "enrollments__course"
    )

    course_stats = Course.objects.annotate(
        average_rating=Avg("reviews__rating"),
        total_enrollments=Count("enrollments")
    )

    top_courses = (
        Course.objects.annotate(
            average_rating=Avg("reviews__rating")
        )
        .order_by("-average_rating")[:5]
    )

    with connection.cursor() as cursor:

        cursor.execute("""

        SELECT student_id,
               COUNT(course_id)

        FROM courses_enrollment

        GROUP BY student_id

        HAVING COUNT(course_id) > 3

        """)

        raw_sql = cursor.fetchall()

    return render(
        request,
        "query_results.html",
        {
            "courses": courses,
            "students": students,
            "course_stats": course_stats,
            "top_courses": top_courses,
            "raw_sql": raw_sql,
        },
    )