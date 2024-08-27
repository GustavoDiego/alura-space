from django.db import models
import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):

        OPCOES = [

                ("NEBULOSA", "Nebulosa"),
                ("ESTRELA", "Estrela"),
                ("GALÁXIA", "Galáxia"),
                ("PLANETA", "Planeta")

        ]


        nome = models.CharField(max_length=100, null = False, blank=False)
        legenda = models.CharField(max_length=150, null = False, blank=False)
        categoria = models.CharField(max_length=100,choices=OPCOES, default="")
        descricao = models.TextField(null = False, blank=False)
        foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) #poder cadastrar sem a necessidade de preencher o campo (blank = True)
        publicado = models.BooleanField(default=True)
        data_fotogarfia = models.DateTimeField(default=datetime.datetime.now, blank= False)
        usuario = models.ForeignKey(
                to=User,
                on_delete=models.SET_NULL,
                null=True,
                blank=False,
                related_name= "user",


        )

        def __str__(self):
            return self.nome
