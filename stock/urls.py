from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    url(r'^logout/$', views.logout, name='logout'),
    #*****************************************************************************************
    url(r'^depot/$', views.depot, name='depot'),
    url(r'^fournisseur/$', views.fournisseur, name='fournisseur'),
    url(r'^client/$', views.client, name='client'),
    url(r'^administrateur/$', views.administrateur, name='administrateur'),
    url(r'^article/$', views.article, name='article'),
    url(r'^commande/$', views.commande, name='commande'),
    url(r'^commandeatt/$', views.commandeatt, name='commandeatt'),
    url(r'^detailcommande/([a-zA-Z0-9_ ]+)/$', views.detailcommande, name='detailcommande'),
    url(r'^detailcommandeatt/([a-zA-Z0-9_ ]+)/$', views.detailcommandeatt, name='detailcommandeatt'),
    url(r'^stock/$', views.stock, name='stock'),
    url(r'^devis/$', views.devis, name='devis'),
    url(r'^detaildevis/([a-zA-Z0-9_ ]+)/$', views.detaildevis, name='detaildevis'),
    #*****************************************************************************************
    url(r'^adddepot/$', views.adddepot, name='adddepot'),
    url(r'^addfournisseur/$', views.addfournisseur, name='addfournisseur'),
    url(r'^addclient/$', views.addclient, name='addclient'),
    url(r'^addadministrateur/$', views.addadministrateur, name='addadministrateur'),
    url(r'^addarticle/$', views.addarticle, name='addarticle'),
    url(r'^addcommande/$', views.addcommande, name='addcommande'),
    url(r'^adddetailcommande/([a-zA-Z0-9_ ]+)/$', views.adddetailcommande, name='adddetailcommande'),
    url(r'^addstock/$', views.addstock, name='addstock'),
    url(r'^adddevis/$', views.adddevis, name='adddevis'),
    url(r'^adddetaildevis/([a-zA-Z0-9_ ]+)/$', views.adddetaildevis, name='adddetaildevis'),
    #*****************************************************************************************
    url(r'^editdepot/([a-zA-Z0-9_ ]+)/$', views.editdepot, name='editdepot'),
    url(r'^editfournisseur/([a-zA-Z0-9_ ]+)/$', views.editfournisseur, name='editfournisseur'),
    url(r'^editclient/([a-zA-Z0-9_ ]+)/$', views.editclient, name='editclient'),
    url(r'^editadministrateur/([a-zA-Z0-9_]+)/$', views.editadministrateur, name='editadministrateur'),
    url(r'^editarticle/([a-zA-Z0-9_ ]+)/$', views.editarticle, name='editarticle'),
    url(r'^editcommande/([a-zA-Z0-9_ ]+)/$', views.editcommande, name='editcommande'),
    url(r'^editdetailcommande/([a-zA-Z0-9_ ]+)/([a-zA-Z0-9_ ]+)/$', views.editdetailcommande, name='editdetailcommande'),
    url(r'^editstock/([a-zA-Z0-9_ ]+)/([a-zA-Z0-9_ ]+)/$', views.editstock, name='editstock'),
    #*****************************************************************************************
    url(r'^deldepot/([a-zA-Z0-9_ ]+)/$', views.deldepot, name='deldepot'),
    url(r'^delfournisseur/([a-zA-Z0-9_ ]+)/$', views.delfournisseur, name='delfournisseur'),
    url(r'^delclient/([a-zA-Z0-9_ ]+)/$', views.delclient, name='delclient'),
    url(r'^deladministrateur/([a-zA-Z0-9_ ]+)/$', views.deladministrateur, name='deladministrateur'),
    url(r'^delarticle/([a-zA-Z0-9_ ]+)/$', views.delarticle, name='delarticle'),
    url(r'^delcommande/([a-zA-Z0-9_ ]+)/$', views.delcommande, name='delcommande'),
    url(r'^delcommandeatt/([a-zA-Z0-9_ ]+)/$', views.delcommandeatt, name='delcommandeatt'),
    url(r'^deldetailcommande/([a-zA-Z0-9_ ]+)/([a-zA-Z0-9_ ]+)/$', views.deldetailcommande, name='deldetailcommande'),
    url(r'^delstock/([a-zA-Z0-9_ ]+)/([a-zA-Z0-9_ ]+)/$', views.delstock, name='delstock'),
    url(r'^deldevis/([a-zA-Z0-9_ ]+)/$', views.deldevis, name='deldevis'),
    url(r'^deldetaildevis/([a-zA-Z0-9_ ]+)/([a-zA-Z0-9_ ]+)/$', views.deldetaildevis, name='deldetaildevis'),
    #*****************************************************************************************
    url(r'^validercommande/([a-zA-Z0-9_ ]+)/$', views.validercommande, name='validercommande'),
    url(r'^validerdevis/([a-zA-Z0-9_ ]+)/$', views.validerdevis, name='validerdevis'),
    #*****************************************************************************************
    url(r'^quantite/$', views.quantite, name='quantite'),
    #*****************************************************************************************
    url(r'^invoice/([a-zA-Z0-9_ ]+)/$', views.invoice, name='invoice'),

    url(r'^produit/$', views.produit, name='produit'),
    url(r'^retproduit/$', views.retproduit, name='retproduit'),
]
