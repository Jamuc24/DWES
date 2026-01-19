from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Superviviente(models.Model):
    """
    Modelo para los supervivientes del yermo
    RELACIÓN 1:1 con User de Django para autenticación
    """
    
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='superviviente',
        verbose_name="Usuario del sistema",
        help_text="Usuario de Django asociado a este superviviente"
    )
    

    nombre = models.CharField(
        max_length=100,
        blank=True, 
        null=True,
        verbose_name="Nombre del personaje",
        help_text="Nombre en el juego (opcional - si está vacío, usa el nombre del usuario)"
    )
    
    apellido = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Apellido del personaje",
        help_text="Apellido en el juego (opcional)"
    )
    
    numero_vault = models.CharField(
        max_length=10, 
        default="101", 
        verbose_name="Número de Vault",
        help_text="Vault de origen (ej: 101, 111, 81)"
    )
    
    nivel = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Nivel del personaje",
        help_text="Nivel entre 1 y 50"
    )
    
    caps = models.IntegerField(
        default=100, 
        verbose_name="Caps (dinero)",
        help_text="Moneda del yermo"
    )
    
    salud = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Puntos de salud",
        help_text="0-100 (0 = muerto)"
    )
    
    radiacion = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Nivel de radiación",
        help_text="0-100 (100 = muerte por radiación)"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )
    
    class Meta:

        db_table = 'superviviente'
        verbose_name = 'Superviviente'
        verbose_name_plural = 'Supervivientes'
        ordering = ['apellido', 'nombre'] 

    
    def __str__(self):
        """Mostramos nombre del juego o del usuario"""
     
        if self.nombre and self.apellido:
            return f"{self.nombre} {self.apellido} (Vault {self.numero_vault})"
        
      
        nombre_completo = f"{self.usuario.first_name} {self.usuario.last_name}".strip()
        if nombre_completo:
            return f"{nombre_completo} (Vault {self.numero_vault})"

        return f"{self.usuario.username} (Vault {self.numero_vault})"
    

    @property
    def esta_sano(self):
        """Verifica si el superviviente está saludable"""
        return self.radiacion < 50 and self.salud > 20
    
    @property
    def nombre_mostrado(self):
        """Devuelve el nombre a mostrar (prioridad: juego > user > username)"""
        if self.nombre and self.apellido:
            return f"{self.nombre} {self.apellido}"
        
        nombre_completo = f"{self.usuario.first_name} {self.usuario.last_name}".strip()
        if nombre_completo:
            return nombre_completo
        
        return self.usuario.username
    
    @property
    def necesita_medicina(self):
        """¿Necesita Stimpaks o RadAway?"""
        return self.radiacion > 30 or self.salud < 50



class Perfil(models.Model):
    """Perfil extendido del superviviente (Relación 1:1)"""
    KARMA_CHOICES = [
        ('santo', 'Santo'),
        ('bueno', 'Bueno'),
        ('neutral', 'Neutral'),
        ('malo', 'Malo'),
        ('malvado', 'Malvado'),
    ]
    
    superviviente = models.OneToOneField(
        Superviviente,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='perfil'
    )
    karma = models.CharField(
        max_length=20,
        choices=KARMA_CHOICES,
        default='neutral',
        verbose_name="Karma"
    )
    reputacion = models.IntegerField(
        default=0,
        validators=[MinValueValidator(-100), MaxValueValidator(100)]
    )
    habilidades = models.TextField(
        blank=True,
        null=True,
        verbose_name="Habilidades especiales"
    )
    
    class Meta:
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return f"Perfil de {self.superviviente.nombre_mostrado}"


class Ubicacion(models.Model):
    """Ubicaciones en el yermo"""
    NIVEL_PELIGRO = [
        ('seguro', 'Seguro'),
        ('moderado', 'Riesgo Moderado'),
        ('peligroso', 'Peligroso'),
        ('mortal', 'Mortal'),
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_peligro = models.CharField(
        max_length=20,
        choices=NIVEL_PELIGRO,
        default='moderado',
        verbose_name="Nivel de peligro"
    )
    tiene_comerciantes = models.BooleanField(default=False)
    nivel_radiacion = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Nivel de radiación"
    )
    
    class Meta:
        db_table = 'ubicacion'
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        ordering = ['nivel_peligro', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_peligro_display()})"


class Objeto(models.Model):
    """Objetos disponibles en el yermo"""
    TIPOS_OBJETO = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
        ('medicina', 'Medicina'),
        ('chatarra', 'Chatarra'),
        ('municion', 'Munición'),
    ]
    
    RAREZAS = [
        ('comun', 'Común'),
        ('poco_comun', 'Poco Común'),
        ('raro', 'Raro'),
        ('legendario', 'Legendario'),
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_OBJETO,
        verbose_name="Tipo de objeto"
    )
    rareza = models.CharField(
        max_length=20,
        choices=RAREZAS,
        default='comun',
        verbose_name="Rareza"
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor en caps"
    )
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1.0,
        verbose_name="Peso (kg)"
    )
    

    danio = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Daño (para armas)"
    )
    armadura = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Valor de armadura"
    )
    curacion = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Puntos de curación"
    )
    
    class Meta:
        db_table = 'objeto'
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        ordering = ['tipo', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Inventario(models.Model):
    """Tabla intermedia para relación N:M entre Superviviente y Objeto"""
    superviviente = models.ForeignKey(
        Superviviente,
        on_delete=models.CASCADE,
        related_name='objetos_inventario'
    )
    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        related_name='en_inventarios'
    )
    cantidad = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    equipado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'inventario'
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering = ['-fecha_actualizacion']
        constraints = [
            models.UniqueConstraint(
                fields=['superviviente', 'objeto'],
                name='objeto_unico_por_superviviente'
            )
        ]
    
    def __str__(self):
        return f"{self.superviviente.nombre_mostrado} - {self.objeto.nombre} x{self.cantidad}"
    
    @property
    def peso_total(self):
        """Calcula el peso total del objeto en el inventario"""
        return float(self.objeto.peso) * self.cantidad


class Mision(models.Model):
    """Misiones disponibles en el yermo (Relación 1:N con Ubicacion)"""
    ESTADOS_MISION = [
        ('disponible', 'Disponible'),
        ('activa', 'Activa'),
        ('completada', 'Completada'),
        ('fallida', 'Fallida'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='misiones',
        verbose_name="Ubicación"
    )
    recompensa_caps = models.IntegerField(
        default=50,
        verbose_name="Recompensa en caps"
    )
    dificultad = models.CharField(
        max_length=20,
        choices=Ubicacion.NIVEL_PELIGRO,
        default='moderado',
        verbose_name="Dificultad"
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_MISION,
        default='disponible',
        verbose_name="Estado"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'mision'
        verbose_name = 'Misión'
        verbose_name_plural = 'Misiones'
        ordering = ['dificultad', 'titulo']
    
    def __str__(self):
        return f"{self.titulo} ({self.get_dificultad_display()})"


class MisionAsignada(models.Model):
    """Modelo intermedio para relación N:M entre Superviviente y Mision"""
    mision = models.ForeignKey(
        Mision,
        on_delete=models.CASCADE,
        related_name='asignaciones'
    )
    superviviente = models.ForeignKey(
        Superviviente,
        on_delete=models.CASCADE,
        related_name='misiones_asignadas'
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(blank=True, null=True)
    progreso = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Progreso (%)"
    )
    
    class Meta:
        db_table = 'mision_asignada'
        verbose_name = 'Misión Asignada'
        verbose_name_plural = 'Misiones Asignadas'
        ordering = ['-fecha_asignacion']
        constraints = [
            models.UniqueConstraint(
                fields=['mision', 'superviviente'],
                name='mision_unica_por_superviviente'
            )
        ]
    
    def __str__(self):
        return f"{self.superviviente.nombre_mostrado} - {self.mision.titulo}"
    
    
    def completar(self):
        """Marca la misión como completada"""
    
        self.progreso = 100
        self.fecha_completada = timezone.now()
        self.save()
        
        # Dar recompensa al superviviente
        self.superviviente.caps += self.mision.recompensa_caps
        self.superviviente.save()