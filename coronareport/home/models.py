# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class City(models.Model):
    seq = models.IntegerField(primary_key=True)
    gubun = models.CharField(max_length=10)
    defcnt = models.IntegerField(db_column='defCnt', blank=True, null=True)  # Field name made lowercase.
    incdec = models.IntegerField(db_column='incDec', blank=True, null=True)  # Field name made lowercase.
    localocccnt = models.IntegerField(db_column='localOccCnt', blank=True, null=True)  # Field name made lowercase.
    overflowcnt = models.IntegerField(db_column='overFlowCnt', blank=True, null=True)  # Field name made lowercase.
    stdday = models.DateField(db_column='stdDay', blank=True, null=True)  # Field name made lowercase.
    createdt = models.DateTimeField(db_column='createDt', blank=True, null=True)  # Field name made lowercase.
    deathcnt = models.IntegerField(db_column='deathCnt', blank=True, null=True)  # Field name made lowercase.
    isolingcnt = models.IntegerField(db_column='isolIngCnt', blank=True, null=True)  # Field name made lowercase.
    isolclearcnt = models.IntegerField(db_column='isolClearCnt', blank=True, null=True)  # Field name made lowercase.
    qurrate = models.FloatField(db_column='qurRate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return '{}-{}'.format(self.stdday.strftime('%Y-%m-%d'), self.gubun)
        

    class Meta:
        managed = False
        db_table = 'city'

class Local(models.Model):
    seq = models.IntegerField(primary_key=True)
    accdefrate = models.FloatField(db_column='accDefRate', blank=True, null=True)  # Field name made lowercase.
    accexamcnt = models.IntegerField(db_column='accExamCnt', blank=True, null=True)  # Field name made lowercase.
    accexamcompcnt = models.IntegerField(db_column='accExamCompCnt', blank=True, null=True)  # Field name made lowercase.
    carecnt = models.IntegerField(db_column='careCnt', blank=True, null=True)  # Field name made lowercase.
    clearcnt = models.IntegerField(db_column='clearCnt', blank=True, null=True)  # Field name made lowercase.
    createdt = models.DateTimeField(db_column='createDt', blank=True, null=True)  # Field name made lowercase.
    deathcnt = models.IntegerField(db_column='deathCnt', blank=True, null=True)  # Field name made lowercase.
    decidecnt = models.IntegerField(db_column='decideCnt', blank=True, null=True)  # Field name made lowercase.
    examcnt = models.IntegerField(db_column='examCnt', blank=True, null=True)  # Field name made lowercase.
    resultnegcnt = models.IntegerField(db_column='resultNegCnt', blank=True, null=True)  # Field name made lowercase.
    statedt = models.DateField(db_column='stateDt', blank=True, null=True)  # Field name made lowercase.
    statetime = models.TimeField(db_column='stateTime', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.statedt.strftime('%Y-%m-%d')

    class Meta:
        managed = False
        db_table = 'local'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'





class Test(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
