from tortoise import models, fields, Tortoise

class School(models.Model):
    """School Info"""
    name = fields.CharField(max_length=255)
    desc = fields.TextField()

    def __str__(self):
        return self.name


class Test(models.Model):
    """Test Info"""
    name = fields.CharField(max_length=255)
    school = fields.ForeignKeyField(
        model_name="models.School",
        related_name="test_school",
    )
    desc = fields.TextField()

    def __str__(self):
        return self.name

class GradeCard(models.Model):
    """Grade Card Info"""
    user = fields.ForeignKeyField(
        model_name="models.User",
        related_name="gradecard_user",
        null=True,
        on_delete=fields.CASCADE,
    )
    test = fields.ForeignKeyField(
        model_name="models.Test",
        related_name="gradecard_test",
    )

    def __str__(self):
        return self.user

class Question(models.Model):
    """Question Info"""
    image_url = fields.CharField(max_length=255) 
    type_a = fields.CharField(max_length=255)
    type_b = fields.CharField(max_length=255)
    level = fields.CharField(max_length=16)
    answer = fields.CharField(max_length=255)

    def __str__(self):
        return f"{self.type_a} {self.type_b} {self.level} {self.answer}"

class Exam(models.Model):
    """Model uid for future verification of user"""

    uid = fields.CharField(max_length=100)
    user = fields.ForeignKeyField(
        model_name="models.User",
        related_name="exam_user",
        null=True,
        on_delete=fields.CASCADE,
    )

    def __str__(self):
        return f"{self.pk}: {self.user}"
