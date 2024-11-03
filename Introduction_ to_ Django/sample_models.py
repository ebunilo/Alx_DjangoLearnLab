from django.db import models


class College(models.Model):
    """One-to-One Relationship"""
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website=models.URLField()


class Principal(models.Model):
    """Secondary key in a One-to-One relationship"""
    CollegeID = models.OneToOneField(
                College,
                on_delete=models.CASCADE
                )
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


# One-to-Many relationship
class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()


class Teacher(models.Model):
    """One-to-Many relationship. More than one teacher can teach the same subject"""
    teacher_id = models.IntegerField(primary_key=True)
    subject_code = models.ForeignKey(
         Subject,
         on_delete=models.CASCADE
    )
    qualification = models.CharField(max_length=50)


# Many-to-Many relationship
class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_lenghh=50)


class Subject(models.Model):
    """Many-to-Many relationship"""
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)