# Generated by Django 5.0.3 on 2024-08-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ethnicity",
                    models.IntegerField(
                        choices=[
                            (0, "Caucasian"),
                            (1, "African American"),
                            (2, "Asian"),
                            (3, "Other"),
                        ]
                    ),
                ),
                (
                    "parental_education",
                    models.IntegerField(
                        choices=[
                            (0, "None"),
                            (1, "High School"),
                            (2, "Some College"),
                            (3, "Bachelor's"),
                            (4, "Higher"),
                        ]
                    ),
                ),
                ("study_time_weekly", models.IntegerField()),
                ("absences", models.IntegerField()),
                ("tutoring", models.IntegerField(choices=[(0, "No"), (1, "Yes")])),
                (
                    "parental_support",
                    models.IntegerField(
                        choices=[
                            (0, "None"),
                            (1, "Low"),
                            (2, "Moderate"),
                            (3, "High"),
                            (4, "Very High"),
                        ]
                    ),
                ),
                (
                    "extracurricular",
                    models.IntegerField(choices=[(0, "No"), (1, "Yes")]),
                ),
                ("sports", models.IntegerField(choices=[(0, "No"), (1, "Yes")])),
                ("music", models.IntegerField(choices=[(0, "No"), (1, "Yes")])),
                ("volunteering", models.IntegerField(choices=[(0, "No"), (1, "Yes")])),
                ("gpa", models.FloatField()),
                (
                    "grade_class",
                    models.IntegerField(
                        choices=[(0, "A"), (1, "B"), (2, "C"), (3, "D"), (4, "F")]
                    ),
                ),
            ],
        ),
    ]