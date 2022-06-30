from rest_framework import serializers
from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Exam
        fields = ("id", "name")

class ExamCreateSerializer(serializers.ModelSerializer):
    min_line_length = serializers.IntegerField(default=5000, initial=5000)
    max_line_gap = serializers.IntegerField(default=1000, initial=1000)
    margin = serializers.IntegerField(default=15, initial=15)

    class Meta:
        model = Exam
        fields = ("id", "min_line_length", "max_line_gap", "margin")

class QuestionSerializer(serializers.ModelSerializer):
    type_a = serializers.CharField(required=False, max_length=100)
    type_b = serializers.CharField(required=False, max_length=100)
    level = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=True, max_length=100)
    image_url = serializers.URLField(required=True, allow_blank=False)
    class Meta:
        model = Exam
        fields = ("id",)

