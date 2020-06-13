from django.contrib import admin

from .models import Tipo_Model, tag, Post, Contacto

admin.site.register(Tipo_Model)
admin.site.register(tag)
admin.site.register(Post)
admin.site.register(Contacto)
