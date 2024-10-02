from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, validators=[RegexValidator(regex=r'^#[0-9a-fA-F]{6}$',  # regex to color hexadecimal
                message='El formato de color debe ser #RRGGBB (hexadecimal).',
            )], help_text="Color debe ser hexadecimal (ejemplo: #FF5733)."
    )
    def __str__(self): return f"Categoría {self.name}"
    class Meta:
        verbose_name="Categoría"; verbose_name_plural="Categorías"

class Uni(models.Model):
    TIPO_CHOICES = [("publica", "Pública"), ("privada", "Privada")] # val en DB, txt shown

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50)
    location = models.CharField(max_length=50); desc = models.TextField()
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, default="publica", help_text="Selecciona si la universidad es pública o privada.")

    def __str__(self): return f"{self.name} : {self.tipo}"
    class Meta:
        verbose_name="Universidad"; verbose_name_plural="Universidades"

class Carrera(models.Model):
    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50)
    desc = models.TextField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(10)], help_text="Duración de la carrera en años (max 10)")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
        help_text="Costo mensual de la carrera (solo para universidades privadas)."
    )

    def __str__(self): return f"{self.name} : {self.uni.name} : {self.cat.name}"
    class Meta:
        verbose_name = "Carrera"; verbose_name_plural = "Carreras"
    def clean(self): # Al tratar de registrar...
        if self.uni.tipo == "privada" and not self.precio:
            raise ValidationError("El campo 'precio' es obligatorio para carreras en universidades privadas.")
        elif self.uni.tipo == "publica" and self.precio:
            raise ValidationError("Las carreras en universidades públicas no deben tener un precio.")
