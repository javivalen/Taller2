# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    first_name = models.CharField(max_length=30)
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


class Cursos(models.Model):
    semestres = models.ForeignKey('Semestres', models.DO_NOTHING)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING)
    anho = models.DateField(db_column='Anho')  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=32)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    codigo = models.CharField(max_length=10)
    ud = models.CharField(db_column='UD', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.nombre + " y su codigo es: "+ self.codigo

    class Meta:
        managed = False
        db_table = 'cursos'


class Departamento(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    sitioweb = models.CharField(max_length=45, blank=True, null=True)
    jefe_depto = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Jefe_depto_id')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


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


class RolUsuarioCurso(models.Model):
    tipo_usuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING)
    cursos = models.ForeignKey(Cursos, models.DO_NOTHING)
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rol_usuario_curso'


class Semestres(models.Model):
    nombre_semestre = models.CharField(db_column='Nombre_Semestre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semestres'


class TipoUsuario(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class UsuarioTipoUsuario(models.Model):
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING)
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_tipo_usuario'


class Usuarios(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=64)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=128)  # Field name made lowercase.
    rut = models.CharField(db_column='RUT', max_length=32)  # Field name made lowercase.
    puntaje_psu = models.FloatField(db_column='Puntaje_PSU')  # Field name made lowercase.
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'usuarios'
