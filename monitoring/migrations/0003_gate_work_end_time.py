from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20230504_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='gate',
            name='work_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
