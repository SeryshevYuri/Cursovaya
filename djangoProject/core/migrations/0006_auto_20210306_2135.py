# Generated by Django 3.1.7 on 2021-03-06 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_kategoriatovara_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=255, verbose_name='Название страницы')),
                ('v_shapku', models.BooleanField(default=False, verbose_name='Выводить в шапку')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.AlterField(
            model_name='tovar',
            name='kategoria_tovara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovari_v_kategorii', to='core.kategoriatovara', verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='usluga',
            name='kategoria_uslug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uslugi_kategorii', to='core.kategoriauslug', verbose_name='Категория услуг'),
        ),
    ]