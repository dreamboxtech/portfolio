# Generated by Django 4.1.4 on 2022-12-22 16:42

import autoslug.fields
import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import embed_video.fields
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "staff_id",
                    models.CharField(blank=True, max_length=8, verbose_name="Staff ID"),
                ),
                (
                    "first_name",
                    models.CharField(max_length=20, verbose_name="First Name"),
                ),
                (
                    "middle_name",
                    models.CharField(max_length=20, verbose_name="Middle Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=20, verbose_name="Last Name"),
                ),
                (
                    "dob",
                    models.DateField(
                        blank=True,
                        default=datetime.date.today,
                        verbose_name="Date of Birth",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=50, verbose_name="Job Title")),
                (
                    "organization",
                    models.CharField(max_length=200, verbose_name="Oranization"),
                ),
                (
                    "specific_duties",
                    ckeditor.fields.RichTextField(verbose_name="Specific Duties"),
                ),
                (
                    "work_started",
                    models.DateField(blank=True, verbose_name="Dated Started"),
                ),
                ("work_ended", models.DateField(blank=True, verbose_name="Date Ended")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "M"), ("F", "F")],
                        max_length=1,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        upload_to="profile_pictures/",
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True,
                        upload_to="profile_pictures/",
                        verbose_name="Profile Picture",
                    ),
                ),
                ("country", django_countries.fields.CountryField(max_length=2)),
                (
                    "about",
                    ckeditor.fields.RichTextField(
                        max_length=500, verbose_name="About Me"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        default="None",
                        max_length=150,
                        verbose_name="Address",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                (
                    "job_title",
                    models.CharField(
                        help_text="Data Engineer",
                        max_length=100,
                        verbose_name="Job title",
                    ),
                ),
                (
                    "experience_years",
                    models.IntegerField(
                        max_length=2, verbose_name="Years of Experience"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Social",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "facebook",
                    models.URLField(
                        blank=True,
                        default="None",
                        max_length=150,
                        verbose_name="Facebook",
                    ),
                ),
                (
                    "twiiter",
                    models.URLField(
                        blank=True,
                        default="None",
                        max_length=150,
                        verbose_name="Twitter",
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        blank=True,
                        default="None",
                        max_length=150,
                        verbose_name="LinkedIn",
                    ),
                ),
                (
                    "stackoverflow",
                    models.URLField(
                        blank=True,
                        default="None",
                        max_length=150,
                        verbose_name="Stackoverflow",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publications",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Publication Title"
                    ),
                ),
                ("date", models.DateField(blank=True, verbose_name="Publication Date")),
                ("link", models.URLField(blank=True, verbose_name="Publication Link")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        max_length=200,
                        populate_from="title",
                        unique_with=("id",),
                    ),
                ),
                (
                    "keywords",
                    models.CharField(
                        max_length=100, verbose_name="Tech Stack (Comma Separated)"
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(verbose_name="Project Description"),
                ),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("STD", "STARTED"),
                            ("CMPT", "COMPLETED"),
                            ("ONG", "ONGOING"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date_started", models.DateField()),
                ("date_ended", models.DateField()),
                (
                    "category",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("MACHINE LEARNING", "MACHINE LEARNING"),
                            ("DATA SCIENCE", "DATA SCIENCE"),
                            ("DATA ANALYTICS/ANALYSIS", "DATA ANALYTICS/ANALYSIS"),
                            ("BACKEND", "BACKEND"),
                            ("FRONTEND", "FRONTEND"),
                            ("MOBILE", "MOBILE"),
                            ("DATA BASE", "DATA BASE"),
                            ("BLOCKCHAIN", "BLOCKCHAIN"),
                            ("CLOUD COMPUTING", "CLOUD COMPUTING"),
                            ("COMPUTER NETWORKING", "COMPUTER NETWORKING"),
                            ("SCRIPTING", "SCRIPTING"),
                            ("DESKTOP", "DESKTOP"),
                            ("SOFTWARE DEVELOPMENT", "SOFTWARE DEVELOPMENT"),
                            ("GAME DEVELOPMENT", "GAME DEVELOPMENT"),
                        ],
                        max_length=100,
                        verbose_name="Project Category",
                    ),
                ),
                ("technology", models.CharField(max_length=30, null=True)),
                (
                    "video",
                    embed_video.fields.EmbedVideoField(
                        blank=True, verbose_name="Video Link"
                    ),
                ),
                (
                    "contributors",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        verbose_name="Contributors (Comma separated)",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "images",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Project Images",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("High School", "High School"),
                            ("Diploma", "Diploma"),
                            ("Associate", "Associate"),
                            ("Bachelors", "Bachelors"),
                            ("Masters", "Masters"),
                            ("PhD", "PhD"),
                            ("Others", "Others"),
                            ("None", "None"),
                        ],
                        max_length=50,
                        verbose_name="Degree",
                    ),
                ),
                (
                    "course",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Course Studied"
                    ),
                ),
                (
                    "school",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Institution"
                    ),
                ),
                (
                    "grade",
                    models.CharField(blank=True, max_length=15, verbose_name="Grade"),
                ),
                (
                    "year",
                    models.DateField(blank=True, verbose_name="Year of Graduation"),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.userprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
