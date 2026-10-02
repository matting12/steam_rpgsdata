from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("steam_app_id", models.PositiveIntegerField(blank=True, null=True)),
                ("rank", models.PositiveSmallIntegerField()),
                ("title", models.CharField(max_length=200)),
                ("url", models.URLField(blank=True, max_length=500)),
                ("image", models.URLField(blank=True, max_length=500)),
                ("discount", models.CharField(blank=True, max_length=10)),
                ("price", models.CharField(default="N/A", max_length=20)),
                ("is_free", models.BooleanField(default=False)),
                ("scraped_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["rank"]},
        ),
    ]
