from django.db import migrations


def create_gate_data(apps):
    Gate = apps.get_model('monitoring', 'Gate')
    Gate.objects.create(gate_number='1A')
    Gate.objects.create(gate_number='2Б')
    Gate.objects.create(gate_number='3D')
    Gate.objects.create(gate_number='4Ф')


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_gate_data)
    ]
