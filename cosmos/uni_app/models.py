from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Cat(models.Model): # model ("table") FOR Cat (CATEGORIES)

    id = models.AutoField(primary_key=True) # id: INT PRIMARY KEY
    name = models.CharField(max_length=50) # name CHARFIELD (VARCHAR)
    color = models.CharField(max_length=7, # color CHARFIELD,
        help_text="Color debe ser hexadecimal (ejemplo: #FF5733).", # HELPTEXT
        validators=[RegexValidator(regex=r'^#[0-9a-fA-F]{6}$', # REGEX TO HEXADECIMAL COLOR INPUT
            message='El formato de color debe ser #RRGGBB (hexadecimal).')]
    )

    def __str__(self): return f"{self.name}" # SHOWS ITEM AS self.name
    
    class Meta: # DIVIDES BY "Categoría" & "Categorías" ON ADMIN PANEL
        verbose_name="Categoría"; verbose_name_plural="Categorías"


class Uni(models.Model): # model ("table") FOR Uni (UNIVERSITIES)

    # CHOICES OF Uni (value on DB, txt shown)
    TIPO_CHOICES = [("publica", "Pública"), ("privada", "Privada")]

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    location = models.CharField(max_length=50)
    tipo = models.CharField(max_length=7, help_text="Selecciona si la universidad es pública o privada.",
        choices=TIPO_CHOICES, # ALLOW TO CHOOSE BY TIPO_CHOICES
        default="publica") # publica BY DEFAULT

    def __str__(self): return f"{self.name} : {self.tipo}"
    class Meta: verbose_name="Universidad"; verbose_name_plural="Universidades"

    def is_public(self): return self.tipo=='publica'


class Carrera(models.Model): # model ("table") FOR Carrera

    id = models.AutoField(primary_key=True); name = models.CharField(max_length=50); desc = models.TextField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # FOREIGN KEY, LINKS AN ITEM FROM Cat
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE) # SAME ↑
    modalidad = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(10)], help_text="Duración de la carrera en años (max 10)")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
        help_text="Costo mensual de la carrera (solo para universidades privadas)."
    ) # precio: DECIMAL (MAY LEFT BLANK, CHECKED LATER...)

    def __str__(self): return f"{self.name} : {self.uni.name} : {self.cat.name}"
    class Meta: verbose_name = "Carrera"; verbose_name_plural = "Carreras"

    def clean(self): # ...WHEN TRYING TO REGISTER Carrera
        if self.uni.tipo == "privada" and not self.precio: # RAISE ERROR IF Uni IS privada & precio BLANK
            raise ValidationError("El campo 'precio' es obligatorio para carreras en universidades privadas.")
        elif self.uni.tipo == "publica" and self.precio: # RAISE ERROR IF Uni IS publica & precio NOT BLANK
            raise ValidationError("Las carreras en universidades públicas no deben tener un precio.")
    
    def is_public(self): return self.uni.tipo=='publica'
