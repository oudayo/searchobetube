from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "title",
            "link",
            "snippet",
            "image",
            "level",
            "totalResults",
            "count",
            "startIndex",
        )


