from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Cat(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7,
        help_text="Color debe ser hexadecimal (ejemplo: #FF5733).",
        validators=[RegexValidator(regex=r'^#[0-9a-fA-F]{6}$',
            message="El formato de color debe ser #RRGGBB (hexadecimal, incluyendo el '#').")]
    )

    def __str__(self): return f"{self.name}"
    class Meta: verbose_name="Categoría"; verbose_name_plural="Categorías"


class Uni(models.Model):

    TIPO_CHOICES = [("publica", "Pública"), ("privada", "Privada")]

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    location = models.CharField(max_length=50)
    tipo = models.CharField(max_length=7, help_text="Selecciona si la universidad es pública o privada.",
        choices=TIPO_CHOICES,
        default="publica")
    @property
    def imgs(self): return self.uniimg_set.all()

    def is_public(self): return self.tipo=='publica'
    def __str__(self): return f"{self.name} : {self.tipo}"
    class Meta: verbose_name="Universidad"; verbose_name_plural="Universidades"


class Carrera(models.Model):

    MOD_CHOICES = [("presencial", "Presencial"), ("mixta", "Mixta"), ("virtual", "Virtual")]

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=50, choices=MOD_CHOICES, default="presencial")
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(10)], help_text="Duración de la carrera en años (max 10)")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
        help_text="Costo mensual de la carrera (solo para universidades privadas).",
        validators=[MinValueValidator(0)]
    ) # precio: DECIMAL (MAY LEFT BLANK, CHECKED LATER...)

    def __str__(self): return f"{self.name} : {self.uni.name} : {self.cat.name}"
    class Meta: verbose_name = "Carrera"; verbose_name_plural = "Carreras"
    def is_public(self): return self.uni.tipo=='publica'

    def clean(self): # ...WHEN TRYING TO REGISTER Carrera
        if self.uni.tipo == "privada" and not self.precio: # RAISE ERROR IF Uni IS privada & precio BLANK
            raise ValidationError("El campo 'precio' es obligatorio para carreras en universidades privadas.")
        elif self.uni.tipo == "publica" and self.precio: # RAISE ERROR IF Uni IS publica & precio NOT BLANK
            raise ValidationError("Las carreras en universidades públicas no deben tener un precio.")


class Curso(models.Model):

    MOD_CHOICES = [("presencial", "Presencial"), ("mixta", "Mixta"), ("virtual", "Virtual")]

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # FOREIGN KEY, LINKS AN ITEM FROM Cat
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE) # SAME ↑
    modalidad = models.CharField(max_length=50, choices=MOD_CHOICES, default="presencial")
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(24)], help_text="Duración del curso en meses (max 24)")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    enroll = models.URLField(max_length=200)
    @property
    def imgs(self): return self.cursoimg_set.all()

    def __str__(self): return f"{self.name} : {self.uni.name} : {self.cat.name}"
    class Meta: verbose_name = "Curso"; verbose_name_plural = "Cursos"
    

class Beca(models.Model):

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    enroll = models.URLField(max_length=200)

    def __str__(self): return f"{self.name} : {self.uni.name}"
    class Meta: verbose_name = "Beca"; verbose_name_plural = "Becas"


class UniImg(models.Model):
    ID = models.AutoField(primary_key=True)
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE)
    img = models.ImageField(default='Uni/default.jgp', upload_to='Uni')
class CursoImg(models.Model):
    ID = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    img = models.ImageField(default='Curso/default.jgp', upload_to='Curso')