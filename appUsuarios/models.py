from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from appUsuarios.models import Usuario

# Create your models here.

class MyAccountManager (BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password= None):
        if not email:
            raise ValueError('El usuario debe tener un correo')
        
        if not username:
            raise ValueError('El usuario debe tener un username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin= True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    ROLES= (
        ('admin', 'admin'),
        ('cliente', 'cliente'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    rol = models.CharField(max_length=30, choices=ROLES, default='cliente')

    #Atributos de DJANGO
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    
    class Meta:
        verbose_name_plural = "Usuarios"


class Carro(models.Model):
    ESTADO_PROD = (
        ('activo', 'activo'),
        ('comprado', 'comprado'),
        ('anulado', 'anulado'),
    )
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(null=False, default= 1)
    valUnit = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_PROD, default='activo')
