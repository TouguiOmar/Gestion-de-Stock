from django import forms
from .models import Depot, Fournisseur, Client, Administrateur, Article, Commande, DetailCommande, Stock, Devis, DetailDevis

class DepotForm(forms.ModelForm):
	class Meta:
		model = Depot
		fields = ['ID_Depot', 'Nom', 'Description', 'Adresse']

class FournisseurForm(forms.ModelForm):
	class Meta:
		model = Fournisseur
		fields = ['ID_Fournisseur', 'Entreprise', 'Description', 'Email', 'Tel', 'Adresse']

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['ID_Client', 'Entreprise', 'Description', 'Email', 'Tel', 'Adresse']

class AdministrateurForm(forms.ModelForm):
	CHOICES = [('Homme','Homme'), ('Femme','Femme')]
	Genre = forms.ChoiceField(choices=CHOICES)
	class Meta:
		model = Administrateur
		fields = ['ID_Administrateur', 'Password', 'Nom', 'Prenom', 'Genre', 'Email', 'Tel', 'Photo', 'ID_Depot']

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['ID_Article', 'Nom', 'Description', 'Photo', 'Prix_Unitaire', 'ID_Fournisseur']

class CommandeForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = ['ID_Commande', 'ID_Client']

class DetailCommandeForm(forms.ModelForm):
	class Meta:
		model = DetailCommande
		fields = ['ID_Commande', 'ID_Article', 'Prix', 'Quantite']

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['ID_Depot', 'ID_Article', 'Quantite']

class DevisForm(forms.ModelForm):
	class Meta:
		model = Devis
		fields = ['ID_Devis', 'Transport', 'Type_Transport', 'Chauffeur', 'Matricule', 'Date_Sortie']

class DetailDevisForm(forms.ModelForm):
	class Meta:
		model = DetailDevis
		fields = ['ID_Devis', 'ID_Article', 'Quantite']

#******************************************************************************************************************

class EditDepotForm(forms.ModelForm):
	class Meta:
		model = Depot
		fields = ['ID_Depot', 'Nom', 'Description', 'Adresse']

class EditFournisseurForm(forms.ModelForm):
	class Meta:
		model = Fournisseur
		fields = ['ID_Fournisseur', 'Entreprise', 'Description', 'Email', 'Tel', 'Adresse']

class EditClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['ID_Client', 'Entreprise', 'Description', 'Email', 'Tel', 'Adresse']

class EditAdministrateurForm(forms.ModelForm):
	CHOICES = [('Homme','Homme'), ('Femme','Femme')]
	Genre = forms.ChoiceField(choices=CHOICES)
	class Meta:
		model = Administrateur
		fields = ['ID_Administrateur', 'Password', 'Nom', 'Prenom', 'Genre', 'Email', 'Tel', 'Photo', 'ID_Depot']

class EditArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['ID_Article', 'Nom', 'Description', 'Photo', 'Prix_Unitaire', 'ID_Fournisseur']

class EditCommandeForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = ['ID_Commande', 'ID_Client']

class EditDetailCommandeForm(forms.ModelForm):
	class Meta:
		model = DetailCommande
		fields = ['Quantite', 'Prix']

class EditStockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['Quantite']

class EditDevisForm(forms.ModelForm):
	class Meta:
		model = Devis
		fields = ['ID_Devis', 'Date_Devis', 'ID_Client']

class EditDetailDevisForm(forms.ModelForm):
	class Meta:
		model = DetailDevis
		fields = ['ID_Devis', 'ID_Article', 'Quantite']