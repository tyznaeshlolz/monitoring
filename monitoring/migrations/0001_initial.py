from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gate_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OSUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pass_number', models.CharField(max_length=255, unique=True)),
                ('at_work', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.BooleanField()),
                ('pass_number', models.CharField(max_length=255)),
                ('pass_time', models.DateTimeField(auto_now_add=True)),
                ('gate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.gate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.osuser')),
            ],
        ),
    ]
