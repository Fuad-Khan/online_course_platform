from django.db.models import Avg, Count
from .models import Course, Student

# select_related
courses = Course.objects.select_related("instructor")

# prefetch_related
students = Student.objects.prefetch_related(
    "enrollments__course"
)

# annotate
course_stats = Course.objects.annotate(
    average_rating=Avg("reviews__rating"),
    total_enrollments=Count("enrollments")
)

# top 5
top_courses = (
    Course.objects.annotate(
        average_rating=Avg("reviews__rating")
    )
    .order_by("-average_rating")[:5]
)