# Generated by Django 2.2.7 on 2019-11-25 06:52

from django.db import migrations, models
import django.db.models.deletion
import selia_visualizers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('irekua_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizerComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javascript_file', models.FileField(db_column='javascript_file', help_text='Javascript file containing visualizer component', upload_to=selia_visualizers.models.visualizer_path, verbose_name='javascript file')),
            ],
            options={
                'verbose_name': 'Visualizer Component',
                'verbose_name_plural': 'Visualizers Components',
            },
        ),
        migrations.CreateModel(
            name='VisualizerComponentItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='Is visualizer app active?', verbose_name='is active')),
                ('item_type', models.ForeignKey(db_column='item_type_id', help_text='Item type', on_delete=django.db.models.deletion.CASCADE, to='irekua_database.ItemType', verbose_name='item type')),
                ('visualizer_component', models.ForeignKey(db_column='visualizer_component_id', help_text='Visualizer component', on_delete=django.db.models.deletion.CASCADE, to='selia_visualizers.VisualizerComponent', verbose_name='visualizer component')),
            ],
            options={
                'verbose_name': 'Visualizer Component Item Type',
                'verbose_name_plural': 'Visualizer Component Item Types',
                'unique_together': {('item_type', 'visualizer_component')},
            },
        ),
        migrations.AddField(
            model_name='visualizercomponent',
            name='item_types',
            field=models.ManyToManyField(through='selia_visualizers.VisualizerComponentItemType', to='irekua_database.ItemType'),
        ),
        migrations.AddField(
            model_name='visualizercomponent',
            name='visualizer',
            field=models.OneToOneField(db_column='visualizer_id', help_text='Visualizer', on_delete=django.db.models.deletion.CASCADE, to='irekua_database.Visualizer', verbose_name='visualizer'),
        ),
    ]
