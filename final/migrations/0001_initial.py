# Generated by Django 2.2.6 on 2020-05-17 15:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=20, verbose_name='batch')),
                ('time1', models.TimeField(verbose_name='time1')),
                ('time2', models.TimeField(verbose_name='time2')),
                ('day', models.CharField(max_length=100, verbose_name='day')),
            ],
        ),
        migrations.CreateModel(
            name='cityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=30, verbose_name='cityname')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModelACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=30, unique=True, verbose_name='empid')),
                ('fullname', models.CharField(max_length=50, verbose_name='fullname')),
                ('password', models.CharField(max_length=30, unique=True, verbose_name='password')),
                ('bloodgroup', models.CharField(max_length=30, verbose_name='bloodgroup')),
                ('gender', models.CharField(max_length=30, verbose_name='gender')),
                ('mstatus', models.CharField(max_length=30, verbose_name='mstatus')),
                ('mobnum', models.BigIntegerField(unique=True, verbose_name='mobnum')),
                ('nativenum', models.BigIntegerField(unique=True, verbose_name='nativenum')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='email')),
                ('dob', models.CharField(max_length=30, verbose_name='dob')),
                ('paddress', models.CharField(max_length=30, verbose_name='paddress')),
                ('taddress', models.CharField(max_length=30, verbose_name='taddress')),
                ('zipcode', models.BigIntegerField(verbose_name='zipcode')),
                ('bsalary', models.BigIntegerField(verbose_name='basicsalary')),
                ('tax', models.CharField(max_length=30, verbose_name='tax')),
                ('taxpercentage', models.IntegerField(null=True, verbose_name='taxpercentage')),
                ('fsalary', models.BigIntegerField(verbose_name='finalsalary')),
                ('workdays', models.CharField(max_length=200, verbose_name='workdays')),
                ('asignleave', models.IntegerField(verbose_name='asignleave')),
                ('cutleave', models.IntegerField(verbose_name='cutleave')),
                ('cuthalfleave', models.IntegerField(verbose_name='cuthalfleave')),
                ('comingtime', models.CharField(max_length=50, verbose_name='comingtime')),
                ('leavingtime', models.CharField(max_length=50, verbose_name='leavingtime')),
                ('fathername', models.CharField(max_length=200, verbose_name='fathername')),
                ('mothername', models.CharField(max_length=200, verbose_name='mothername')),
                ('fcontact', models.BigIntegerField(unique=True, verbose_name='fcontact')),
                ('mcontact', models.BigIntegerField(unique=True, verbose_name='mcontact')),
                ('adharcard', models.CharField(max_length=200, verbose_name='adharcard')),
                ('pancard', models.CharField(max_length=200, verbose_name='pancard')),
                ('photo', models.CharField(max_length=200, verbose_name='photo')),
                ('bankname', models.CharField(max_length=30, verbose_name='bankname')),
                ('branchname', models.CharField(max_length=30, verbose_name='branchname')),
                ('accnum', models.BigIntegerField(unique=True, verbose_name='accnum')),
                ('acctype', models.CharField(max_length=30, verbose_name='acctype')),
                ('pannumber', models.BigIntegerField(unique=True, verbose_name='pannumber')),
                ('chqnumber', models.BigIntegerField(unique=True, verbose_name='chqnumber')),
                ('codeifsc', models.BigIntegerField(unique=True, verbose_name='codeifsc')),
                ('codemicr', models.BigIntegerField(unique=True, verbose_name='codemicr')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.cityModel')),
            ],
        ),
        migrations.CreateModel(
            name='feeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=25, verbose_name='lang')),
                ('langimg', models.CharField(max_length=200, verbose_name='langimg')),
                ('desc', models.TextField(max_length=200, verbose_name='desc')),
                ('dur', models.CharField(max_length=25, verbose_name='dur')),
            ],
        ),
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.CharField(max_length=200, verbose_name='photos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=30, verbose_name='pass')),
                ('fullname', models.CharField(max_length=30, verbose_name='fullname')),
            ],
        ),
        migrations.CreateModel(
            name='privilegeModelACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privname', models.CharField(max_length=30, verbose_name='privilegename')),
                ('fontcode', models.CharField(max_length=30, verbose_name='fontcode')),
            ],
        ),
        migrations.CreateModel(
            name='roleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20, unique=True, verbose_name='role')),
                ('roleimage', models.CharField(max_length=200, verbose_name='roleimage')),
            ],
        ),
        migrations.CreateModel(
            name='stateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statecode', models.CharField(max_length=30, verbose_name='statecode')),
                ('statename', models.CharField(max_length=30, verbose_name='statename')),
            ],
        ),
        migrations.CreateModel(
            name='structureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structurename', models.CharField(max_length=20, unique=True, verbose_name='structurename')),
            ],
        ),
        migrations.CreateModel(
            name='TrainigTypedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrainigTyped', models.CharField(max_length=50, verbose_name='TrainigTyped')),
            ],
        ),
        migrations.CreateModel(
            name='useradminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30, verbose_name='passowrd')),
                ('fullname', models.CharField(max_length=20, verbose_name='fullname')),
            ],
        ),
        migrations.CreateModel(
            name='registrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20, verbose_name='fullname')),
                ('pnum', models.CharField(max_length=12, verbose_name='pnum')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('reffname', models.CharField(max_length=20, verbose_name='reffname')),
                ('reffcontact', models.CharField(max_length=12, verbose_name='reffcontact')),
                ('date1', models.DateField(default=datetime.datetime(2020, 5, 17, 15, 21, 49, 284387, tzinfo=utc), null=True, verbose_name='date1')),
                ('University', models.CharField(max_length=50, verbose_name='University')),
                ('Institute', models.CharField(max_length=50, verbose_name='Institute')),
                ('Semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('Stream', models.CharField(max_length=50, verbose_name='Stream')),
                ('installment', models.IntegerField(verbose_name='installment')),
                ('remaining_installment', models.IntegerField(verbose_name='installment')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('stud_id', models.CharField(default=23, max_length=11, verbose_name='stud_id')),
                ('ass', models.CharField(max_length=500, null=True, verbose_name='ass')),
                ('TrainigTyped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.TrainigTypedModel')),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='final.batchModel')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.LanguageModel')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.feeModel')),
                ('structurename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.structureModel')),
            ],
        ),
        migrations.CreateModel(
            name='PrivToUserModelACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privId', models.TextField(verbose_name='role_user_privilage')),
                ('empId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.EmployeeModelACM')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.roleModel')),
            ],
        ),
        migrations.CreateModel(
            name='PrivToRoleModelACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privId', models.TextField(verbose_name='role_privilage')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.roleModel')),
            ],
        ),
        migrations.CreateModel(
            name='privComponentModelACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pCompName', models.CharField(max_length=100, verbose_name='privCompName')),
                ('pCompLink', models.CharField(max_length=100, verbose_name='privCompLink')),
                ('privId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.privilegeModelACM')),
            ],
        ),
        migrations.CreateModel(
            name='inquiryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentphoto', models.CharField(max_length=200, verbose_name='studentphoto')),
                ('fullname', models.CharField(max_length=25, verbose_name='fullname')),
                ('pnum', models.CharField(max_length=12, unique=True, verbose_name='pnum')),
                ('dob', models.DateField(verbose_name='dob')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('reffname', models.CharField(max_length=20, verbose_name='reffname')),
                ('reffcontact', models.CharField(max_length=12, verbose_name='reffcontact')),
                ('inqdate', models.DateField(default=datetime.datetime(2020, 5, 17, 15, 21, 49, 283451, tzinfo=utc), null=True, verbose_name='inqdate')),
                ('University', models.CharField(max_length=50, verbose_name='University')),
                ('Institute', models.CharField(max_length=50, verbose_name='Institute')),
                ('Semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('Stream', models.CharField(max_length=50, verbose_name='Stream')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('TrainigTyped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.TrainigTypedModel')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.LanguageModel')),
                ('structurename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.structureModel')),
            ],
        ),
        migrations.AddField(
            model_name='feemodel',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.LanguageModel'),
        ),
        migrations.AddField(
            model_name='feemodel',
            name='structurename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.structureModel'),
        ),
        migrations.AddField(
            model_name='employeemodelacm',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.roleModel'),
        ),
        migrations.AddField(
            model_name='employeemodelacm',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.stateModel'),
        ),
        migrations.AddField(
            model_name='citymodel',
            name='stateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.stateModel'),
        ),
        migrations.AddField(
            model_name='batchmodel',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.LanguageModel'),
        ),
        migrations.CreateModel(
            name='admin_inquiryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentphotos', models.CharField(max_length=200, verbose_name='studentphotos')),
                ('fullname', models.CharField(max_length=25, verbose_name='fullname')),
                ('pnum', models.CharField(max_length=12, verbose_name='pnum')),
                ('dob', models.DateField(verbose_name='dob')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('reffname', models.CharField(max_length=20, verbose_name='reffname')),
                ('reffcontact', models.CharField(max_length=12, verbose_name='reffcontact')),
                ('inqdate', models.DateField(default=datetime.datetime(2020, 5, 17, 15, 21, 49, 285384, tzinfo=utc), null=True, verbose_name='inqdate')),
                ('University', models.CharField(max_length=50, verbose_name='University')),
                ('Institute', models.CharField(max_length=50, verbose_name='Institute')),
                ('Semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('Stream', models.CharField(max_length=50, verbose_name='Stream')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('TrainigTyped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.TrainigTypedModel')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.LanguageModel')),
                ('structurename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.structureModel')),
            ],
        ),
    ]
