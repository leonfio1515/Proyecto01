# Generated by Django 4.0.3 on 2022-07-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CajasApp', '0002_alter_manuales_nombre_manual'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetiraCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('ci_cliente', models.IntegerField()),
                ('articulo_cliente', models.CharField(max_length=17)),
                ('sucursal_retiro', models.IntegerField(choices=[('1', '1- Shopping Paysandu'), ('2', '2- Pando'), ('3', '3'), ('4', '4- San Jose'), ('5', '5- Portones Sopping'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9- Pta Carretas Shopping'), ('10', '10- Tacuarembo'), ('11', '11'), ('12', '12- Tres Cruces Shopping'), ('14', '14'), ('15', '15- Montevideo Shopping'), ('16', '16- Punta Shopping'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20- Salto Shopping'), ('21', '21'), ('22', '22- Costa Urbana Shopping'), ('23', '23'), ('24', '24- Nuevo Centro Shopping'), ('25', '25- Mercedes'), ('26', '26- Cerro'), ('27', '27'), ('28', '28- Las Piedras Shopping'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('51', '51'), ('52', '52')])),
                ('transaccion_visual', models.IntegerField()),
                ('fecha_generado', models.DateField()),
            ],
        ),
    ]
