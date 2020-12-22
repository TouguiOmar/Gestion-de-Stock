from django.contrib import admin
from .models import Depot, Fournisseur, Client, Administrateur, Article, Commande, DetailCommande, Stock, Devis, DetailDevis

admin.site.register(Depot)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Administrateur)
admin.site.register(Article)
admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(Stock)
admin.site.register(Devis)
admin.site.register(DetailDevis)