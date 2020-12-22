from django.db import models
import datetime

class Depot(models.Model):
	ID_Depot          = models.CharField(max_length=25, primary_key=True)
	Nom               = models.CharField(max_length=25)
	Description       = models.CharField(max_length=25)
	Adresse           = models.CharField(max_length=25)
	def __str__(self):
		return self.ID_Depot

class Fournisseur(models.Model):
	ID_Fournisseur    = models.CharField(max_length=25, primary_key=True)
	Entreprise        = models.CharField(max_length=25)
	Description       = models.CharField(max_length=25)
	Email             = models.EmailField()
	Tel               = models.CharField(max_length=25)
	Adresse           = models.CharField(max_length=25)
	def __str__(self):
		return self.ID_Fournisseur

class Client(models.Model):
	ID_Client         = models.CharField(max_length=25, primary_key=True)
	Entreprise        = models.CharField(max_length=25)
	Description       = models.CharField(max_length=25)
	Email             = models.EmailField()
	Tel               = models.CharField(max_length=25)
	Adresse           = models.CharField(max_length=25)
	def __str__(self):
		return self.ID_Client

class Administrateur(models.Model):
	ID_Administrateur = models.CharField(max_length=25, primary_key=True)
	Password          = models.CharField(max_length=25)
	Nom               = models.CharField(max_length=25)
	Prenom            = models.CharField(max_length=25)
	Genre             = models.CharField(max_length=25)
	Email             = models.EmailField()
	Tel               = models.CharField(max_length=25)
	Photo             = models.ImageField(upload_to='admins')
	ID_Depot          = models.ForeignKey(Depot, on_delete=models.CASCADE)
	Type              = models.IntegerField(default=0)

class Article(models.Model):
	ID_Article        = models.CharField(max_length=25, primary_key=True)
	Nom               = models.CharField(max_length=25)
	Description       = models.CharField(max_length=25)
	Photo             = models.ImageField(upload_to='articles')
	Prix_Unitaire     = models.FloatField()
	ID_Fournisseur    = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
	def __str__(self):
		return self.Nom

class Commande(models.Model):
	ID_Commande       = models.CharField(max_length=25, primary_key=True)
	Date_Commande     = models.DateField(default=datetime.date.today)
	ID_Client         = models.ForeignKey(Client, on_delete=models.CASCADE)
	Valid             = models.IntegerField(default=0)

class DetailCommande(models.Model):
	ID_Commande       = models.ForeignKey(Commande, on_delete=models.CASCADE)
	ID_Article        = models.ForeignKey(Article, on_delete=models.CASCADE)
	Prix              = models.FloatField()
	Quantite          = models.IntegerField()

	class Meta(object):
		unique_together = ("ID_Commande", "ID_Article")

class Stock(models.Model):
	ID_Depot          = models.ForeignKey(Depot, on_delete=models.CASCADE)
	ID_Article        = models.ForeignKey(Article, on_delete=models.CASCADE)
	Quantite          = models.IntegerField()

	class Meta(object):
		unique_together = ("ID_Depot", "ID_Article")

class Devis(models.Model):
	ID_Devis          = models.CharField(max_length=25, primary_key=True)
	Date_Devis        = models.DateField(default=datetime.date.today)
	ID_Client         = models.ForeignKey(Client, on_delete=models.CASCADE)
	Valid             = models.IntegerField(default=0)
	Transport         = models.CharField(max_length=25)
	Type_Transport    = models.CharField(max_length=25)
	Chauffeur         = models.CharField(max_length=25)
	Matricule         = models.CharField(max_length=25)
	Date_Sortie       = models.DateField(default=datetime.date.today)

class DetailDevis(models.Model):
	ID_Devis          = models.ForeignKey(Devis, on_delete=models.CASCADE)
	ID_Article        = models.ForeignKey(Article, on_delete=models.CASCADE)
	Prix              = models.FloatField()
	Quantite          = models.IntegerField()

	class Meta(object):
		unique_together = ("ID_Devis", "ID_Article")