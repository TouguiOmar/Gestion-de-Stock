from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Depot, Fournisseur, Client, Administrateur, Article, Commande, DetailCommande, Stock, Devis, DetailDevis
from .forms import DepotForm, FournisseurForm, ClientForm, AdministrateurForm, ArticleForm, CommandeForm, DetailCommandeForm, StockForm, DevisForm, DetailDevisForm
from .forms import EditDepotForm, EditFournisseurForm, EditClientForm, EditAdministrateurForm, EditArticleForm, EditCommandeForm, EditDetailCommandeForm, EditStockForm, EditDevisForm, EditDetailDevisForm

def index(request):
	erreur = 0
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			administrateur = Administrateur.objects.get(ID_Administrateur=username, Password=password)
			request.session['ID_Administrateur'] = administrateur.ID_Administrateur
			request.session['Nom'] = administrateur.Nom
			request.session['Prenom'] = administrateur.Prenom
			request.session['Photo'] = str(administrateur.Photo)
			request.session['ID_Depot'] = administrateur.ID_Depot.ID_Depot
			request.session['Type'] = administrateur.Type
			return redirect('accueil/')
		except Exception as e:
			erreur = 1
	return render(request, 'index.html', {'erreur':erreur})

def accueil(request):
	return render(request, 'accueil.html')

def logout(request):
	del request.session['ID_Administrateur']
	del request.session['Nom']
	del request.session['Prenom']
	del request.session['Photo']
	del request.session['ID_Depot']
	del request.session['Type']
	return redirect('/')

#*****************************************************************************************
def depot(request):
	depots = Depot.objects.all()
	return render(request, 'list/A_depot.html', {'depots':depots})

def fournisseur(request):
	fournisseurs = Fournisseur.objects.all()
	return render(request, 'list/B_fournisseur.html', {'fournisseurs':fournisseurs})

def client(request):
	clients = Client.objects.all()
	return render(request, 'list/C_client.html', {'clients':clients})

def administrateur(request):
	administrateurs = Administrateur.objects.all()
	return render(request, 'list/D_administrateur.html', {'administrateurs':administrateurs})

def article(request):
	articles = Article.objects.all()
	return render(request, 'list/E_article.html', {'articles':articles})

def commande(request):
	commandes = Commande.objects.filter(Valid=1)
	return render(request, 'list/F_commande.html', {'commandes':commandes})

def commandeatt(request):
	commandes = Commande.objects.filter(Valid=0)
	return render(request, 'list/F_commandeatt.html', {'commandes':commandes})

def detailcommande(request, ID_Commande):
	detailcommandes = DetailCommande.objects.filter(ID_Commande=ID_Commande)
	return render(request, 'list/G_detailcommande.html', {'detailcommandes':detailcommandes, 'ID_Commande':ID_Commande})

def detailcommandeatt(request, ID_Commande):
	detailcommandes = DetailCommande.objects.filter(ID_Commande=ID_Commande)
	return render(request, 'list/G_detailcommandeatt.html', {'detailcommandes':detailcommandes, 'ID_Commande':ID_Commande})

def stock(request):
	stocks = Stock.objects.filter(ID_Depot=request.session['ID_Depot'])
	return render(request, 'list/H_stock.html', {'stocks':stocks})

def devis(request):
	devis = Devis.objects.all()
	return render(request, 'list/I_devis.html', {'devis':devis})

class DevisOP:
	def __init__(self, detaildevi):
		self.detaildevi = detaildevi
		self.Montant = detaildevi.Quantite * detaildevi.Prix

def detaildevis(request, ID_Devis):
	devis       = Devis.objects.get(ID_Devis=ID_Devis)
	detaildevis = DetailDevis.objects.filter(ID_Devis=ID_Devis)
	Montant = 0
	vs = []
	for detaildevi in detaildevis:
		Montant += detaildevi.Quantite * detaildevi.Prix
		vs.append(DevisOP(detaildevi))
	return render(request, 'list/j_detaildevis.html', {'ID_Devis':ID_Devis, 'devis':devis, 'vs':vs, 'Montant':Montant})

#*****************************************************************************************
def adddepot(request):
	erreur = 0
	form = DepotForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		erreur = 1
		form = DepotForm()
	return render(request, 'add/A_depot.html', {'form':form, 'erreur':erreur})

def addfournisseur(request):
	erreur = 0
	form = FournisseurForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		erreur = 1
		form = FournisseurForm()
	return render(request, 'add/B_fournisseur.html', {'form':form, 'erreur':erreur})

def addclient(request):
	erreur = 0
	form = ClientForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		erreur = 1
		form = ClientForm()
	return render(request, 'add/C_client.html', {'form':form, 'erreur':erreur})

def addadministrateur(request):
	erreur = 0
	form = AdministrateurForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		erreur = 1
		form = AdministrateurForm()
	return render(request, 'add/D_administrateur.html', {'form':form, 'erreur':erreur})

def addarticle(request):
	erreur = 0
	form = ArticleForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		erreur = 1
		form = ArticleForm()
	return render(request, 'add/E_article.html', {'form':form, 'erreur':erreur})

def addcommande(request):
	erreur = 0
	form = CommandeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		ID_Commande = form.cleaned_data['ID_Commande']
		form.save()
		erreur = 1
		return HttpResponseRedirect('/detailcommande/' + ID_Commande)
	return render(request, 'add/F_commande.html', {'form':form, 'erreur':erreur})

def adddetailcommande(request, ID_Commande):
	erreur = 0
	form = DetailCommandeForm(request.POST or None, request.FILES or None, initial={'ID_Commande':ID_Commande})
	if form.is_valid():
		form.save()
		erreur = 1
		return HttpResponseRedirect('/detailcommande/' + ID_Commande)
	return render(request, 'add/G_detailcommande.html', {'form':form, 'erreur':erreur})

def addstock(request):
	erreur = 0
	ID_Depot = request.session['ID_Depot']
	form = StockForm(request.POST or None, request.FILES or None, initial={'ID_Depot':ID_Depot})
	if form.is_valid():
		form.save()
		erreur = 1
		form = StockForm(initial={'ID_Depot':ID_Depot})
	return render(request, 'add/H_stock.html', {'form':form, 'erreur':erreur})

def adddevis(request):
	erreur = 0
	form = DevisForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		ID_Commande = request.POST.get('ID_Commande')
		detailcommandes = DetailCommande.objects.filter(ID_Commande=ID_Commande)
		for detailcommande in detailcommandes:
			stock = Stock.objects.get(ID_Depot=request.session['ID_Depot'], ID_Article=detailcommande.ID_Article)
			if detailcommande.Quantite > stock.Quantite:
				erreur = 2

		if erreur != 2:
			devis = form.save(commit=False)
			ID_Devis = form.cleaned_data['ID_Devis']
			commande = Commande.objects.get(ID_Commande=ID_Commande)
			devis.ID_Client = commande.ID_Client
			form.save()

			ID_Devis1 = Devis.objects.get(ID_Devis=ID_Devis)

			for detailcommande in detailcommandes:
				detailDevis = DetailDevis()
				detailDevis.ID_Devis = ID_Devis1
				detailDevis.ID_Article = detailcommande.ID_Article
				detailDevis.Quantite = detailcommande.Quantite
				detailDevis.Prix = detailcommande.Prix
				detailDevis.save()
				stock = Stock.objects.get(ID_Depot=request.session['ID_Depot'], ID_Article=detailcommande.ID_Article)
				stock.Quantite = stock.Quantite - detailcommande.Quantite
				stock.save()

			erreur = 1
			return HttpResponseRedirect('/detaildevis/' + ID_Devis)
			
		form = DevisForm()
	commandes = Commande.objects.filter(Valid=1)
	return render(request, 'add/I_devis.html', {'form':form, 'erreur':erreur, 'commandes':commandes})

def adddetaildevis(request, ID_Devis):
	erreur = 0
	form = DetailDevisForm(request.POST or None, request.FILES or None, initial={'ID_Devis':ID_Devis})
	if form.is_valid():
		form.save()
		erreur = 1
		form = DetailDevisForm()
	return render(request, 'add/j_detaildevis.html', {'form':form, 'erreur':erreur})

#*****************************************************************************************
def editdepot(request, ID_Depot):
	erreur = 0
	depot = Depot.objects.get(ID_Depot=ID_Depot)
	form = EditDepotForm(request.POST or None, request.FILES or None, instance=depot)
	if form.is_valid():
		form.save()
		erreur = 1
		form = DepotForm(instance=depot)
	return render(request, 'edit/A_depot.html', {'form':form, 'erreur':erreur})

def editfournisseur(request, ID_Fournisseur):
	erreur = 0
	fournisseur = Fournisseur.objects.get(ID_Fournisseur=ID_Fournisseur)
	form = EditFournisseurForm(request.POST or None, request.FILES or None, instance=fournisseur)
	if form.is_valid():
		form.save()
		erreur = 1
		form = FournisseurForm(instance=fournisseur)
	return render(request, 'edit/B_fournisseur.html', {'form':form, 'erreur':erreur})

def editclient(request, ID_Client):
	erreur = 0
	client = Client.objects.get(ID_Client=ID_Client)
	form = EditClientForm(request.POST or None, request.FILES or None, instance=client)
	if form.is_valid():
		form.save()
		erreur = 1
		form = ClientForm(instance=client)
	return render(request, 'edit/C_client.html', {'form':form, 'erreur':erreur})

def editadministrateur(request, ID_Administrateur):
	erreur = 0
	administrateur = Administrateur.objects.get(ID_Administrateur=ID_Administrateur)
	form = EditAdministrateurForm(request.POST or None, request.FILES or None, instance=administrateur)
	if form.is_valid():
		form.save()
		erreur = 1
		form = AdministrateurForm(instance=administrateur)
	return render(request, 'edit/D_administrateur.html', {'form':form, 'erreur':erreur})

def editarticle(request, ID_Article):
	erreur = 0
	article = Article.objects.get(ID_Article=ID_Article)
	form = EditArticleForm(request.POST or None, request.FILES or None, instance=article)
	if form.is_valid():
		form.save()
		erreur = 1
		form = ArticleForm(instance=article)
	return render(request, 'edit/E_article.html', {'form':form, 'erreur':erreur})

def editcommande(request, ID_Commande):
	erreur = 0
	commande = Commande.objects.get(ID_Commande=ID_Commande)
	form = EditCommandeForm(request.POST or None, request.FILES or None, instance=commande)
	if form.is_valid():
		form.save()
		erreur = 1
		form = CommandeForm(instance=commande)
	return render(request, 'edit/F_commande.html', {'form':form, 'erreur':erreur})

def editdetailcommande(request, ID_Commande, ID_Article):
	erreur = 0
	detailcommande = DetailCommande.objects.get(ID_Commande=ID_Commande, ID_Article=ID_Article)
	stock = Stock.objects.get(ID_Depot=request.session['ID_Depot'], ID_Article=ID_Article)
	quantite = stock.Quantite
	form = EditDetailCommandeForm(request.POST or None, request.FILES or None, instance=detailcommande)
	if form.is_valid():
		form.save()
		erreur = 1
		return HttpResponseRedirect('/detailcommande/' + ID_Commande)
	return render(request, 'edit/G_detailcommande.html', {'form':form, 'erreur':erreur, 'quantite':quantite})

def editstock(request, ID_Depot, ID_Article):
	erreur = 0
	stock = Stock.objects.get(ID_Depot=ID_Depot, ID_Article=ID_Article)
	form = EditStockForm(request.POST or None, request.FILES or None, instance=stock)
	if form.is_valid():
		form.save()
		erreur = 1
		form = StockForm(instance=stock)
	return render(request, 'edit/H_stock.html', {'form':form, 'erreur':erreur})

#*****************************************************************************************
def deldepot(request, ID_Depot):
	depot = Depot.objects.get(ID_Depot=ID_Depot)
	depot.delete()
	return redirect('/depot')

def delfournisseur(request, ID_Fournisseur):
	fournisseur = Fournisseur.objects.get(ID_Fournisseur=ID_Fournisseur)
	fournisseur.delete()
	return redirect('/fournisseur')

def delclient(request, ID_Client):
	client = Client.objects.get(ID_Client=ID_Client)
	client.delete()
	return redirect('/client')

def deladministrateur(request, ID_Administrateur):
	administrateur = Administrateur.objects.get(ID_Administrateur=ID_Administrateur)
	administrateur.delete()
	return redirect('/administrateur')

def delarticle(request, ID_Article):
	article = Article.objects.get(ID_Article=ID_Article)
	article.delete()
	return redirect('/article')

def delcommande(request, ID_Commande):
	commande = Commande.objects.get(ID_Commande=ID_Commande)
	commande.delete()
	return redirect('/commande')

def delcommandeatt(request, ID_Commande):
	commande = Commande.objects.get(ID_Commande=ID_Commande)
	commande.delete()
	return redirect('/commandeatt')

def deldetailcommande(request, ID_Commande, ID_Article):
	detailcommande = DetailCommande.objects.get(ID_Commande=ID_Commande, ID_Article=ID_Article)
	detailcommande.delete()
	return redirect('/detailcommande/' + ID_Commande)

def delstock(request, ID_Depot, ID_Article):
	stock = Stock.objects.get(ID_Depot=ID_Depot, ID_Article=ID_Article)
	stock.delete()
	return redirect('/stock')

def deldevis(request, ID_Devis):
	devis = Devis.objects.get(ID_Devis=ID_Devis)
	devis.delete()
	return redirect('/devis')

def deldetaildevis(request, ID_Devis, ID_Article):
	detaildevis = DetailDevis.objects.get(ID_Devis=ID_Devis, ID_Article=ID_Article)
	detaildevis.delete()
	return redirect('/detaildevis/' + ID_Devis)

#*****************************************************************************************
def validercommande(request, ID_Commande):
	commande = Commande.objects.get(ID_Commande=ID_Commande)
	commande.Valid = 1
	commande.save()
	return redirect('/commandeatt')

def validerdevis(request, ID_Devis):
	devis = Devis.objects.get(ID_Devis=ID_Devis)
	devis.Valid = 1
	devis.save()
	return redirect('/devis')

#*****************************************************************************************
def quantite(request):
	ID_Article = request.GET.get('ID_Article', None)
	try:
		stock = Stock.objects.get(ID_Depot=request.session['ID_Depot'], ID_Article=ID_Article)
		article = Article.objects.get(ID_Article=ID_Article)
		quantite = stock.Quantite
		prix = article.Prix_Unitaire
	except Exception as e:
		quantite = 0
		prix = 0
	
	return JsonResponse({'quantite':quantite, 'prix':prix})

#*****************************************************************************************
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

def invoice(request, ID_Devis):
	devis       = Devis.objects.get(ID_Devis=ID_Devis)
	detaildevis = DetailDevis.objects.filter(ID_Devis=ID_Devis)
	Montant = 0
	vs = []
	for detaildevi in detaildevis:
		Montant += detaildevi.Quantite * detaildevi.Prix
		vs.append(DevisOP(detaildevi))
	data = {
		'ID_Devis':ID_Devis,
		'devis':devis,
		'vs':vs,
		'Montant':Montant,
		}

	pdf = render_to_pdf('invoice.html', data)
	return HttpResponse(pdf, content_type='application/pdf')



def produit(request):
	articles = Article.objects.all()
	return render(request, 'produit.html', {'articles':articles})


def retproduit(request):
	ID_Article = request.GET.get('ID_Article', None)
	article = Article.objects.get(ID_Article=ID_Article)
	stocks = Stock.objects.filter(ID_Article=ID_Article)
	detaildevis = DetailDevis.objects.filter(ID_Article=ID_Article)
	
	data = {
		'article':article,
		'stocks':stocks,
		'detaildevis':detaildevis,
	}

	htm  = "<div class='col-6 mt-5'>"
	htm += "<div class='card'>"
	htm += "<div class='card-body'>"
	htm += "<h4 class='header-title' style='color: white;background:#303641; padding:10px;'>Article</h4>"
	htm += "<div class='letest-news mt-5'>"

	htm += "<div class='single-post mb-xs-40 mb-sm-40'>"
	htm += "<div class='lts-thumb'>"
	htm += "<img src=" + article.Photo.url + " alt='post thumb'>"
	htm += "</div>"
	htm += "<div class='lts-content'>"
	htm += "<span>Tag RFID : " + article.ID_Article + "</span>"
	htm += "<h2><a >Nom : " + article.Nom + "</a></h2>"
	htm += "<p>Description : " + article.Description + "</p>"
	htm += "<p>Prix Unitaire : " + str(article.Prix_Unitaire) + " DH</p>"
	htm += "</div>"
	htm += "</div>"

	htm += "</div>"
	htm += "</div>"
	htm += "</div>"
	htm += "</div>"

	htm += "<div class='col-6 mt-5'>"
	htm += "<div class='card'>"
	htm += "<div class='card-body'>"
	htm += "<h4 class='header-title' style='color: white;background:#303641; padding:10px;'>fournisseur</h4>"
	htm += "<div class='letest-news mt-5'>"

	htm += "<div class='single-post mb-xs-40 mb-sm-40'>"
	htm += "<div class='lts-content'>"
	htm += "<span>Nom : " + article.ID_Fournisseur.ID_Fournisseur + "</span>"
	htm += "<h2><a >Entreprise : " + article.ID_Fournisseur.Entreprise + "</a></h2>"
	htm += "<p>Email : " + article.ID_Fournisseur.Email + "</p>"
	htm += "<p>Tel : " + article.ID_Fournisseur.Tel + "</p>"
	htm += "<p>Adresse : " + article.ID_Fournisseur.Adresse + "</p>"
	htm += "<p>Ville : " + article.ID_Fournisseur.Description + "</p>"
	htm += "</div>"
	htm += "</div>"

	htm += "</div>"
	htm += "</div>"
	htm += "</div>"
	htm += "</div>"

	if stocks:
		htm += "<div class='col-6 mt-5'>"
		htm += "<div class='card'>"
		htm += "<div class='card-body'>"
		htm += "<h4 class='header-title' style='color: white;background:#303641; padding:10px;'>Stock</h4>"
		htm += "<div class='letest-news mt-5'>"

		for stock in stocks:
			htm += "<div class='single-post mb-xs-40 mb-sm-40'>"
			htm += "<div class='lts-content'>"
			htm += "<h2><a>Depot : " + stock.ID_Depot.ID_Depot + "</a></h2>"
			htm += "<p>Description : " + stock.ID_Depot.Description + "</p>"
			htm += "<p>Adresse : " + stock.ID_Depot.Adresse + "</p>"
			htm += "<p>Ville :" + stock.ID_Depot.Nom + "</p>"
			htm += "<p>Quantite :" + str(stock.Quantite) + "</h2>"
			htm += "</div>"
			htm += "</div>"
			htm += "<hr>"

		htm += "</div>"
		htm += "</div>"
		htm += "</div>"
		htm += "</div>"


	if detaildevis:
		htm += "<div class='col-6 mt-5'>"
		htm += "<div class='card'>"
		htm += "<div class='card-body'>"
		htm += "<h4 class='header-title' style='color: white;background:#303641; padding:10px;'>Commandes</h4>"
		htm += "<div class='letest-news mt-5'>"

		for detaildevi in detaildevis:
			htm += "<div class='single-post mb-xs-40 mb-sm-40'>"
			htm += "<div class='lts-content'>"
			htm += "<span>Commande : " + detaildevi.ID_Devis.ID_Devis + "</span>"
			htm += "<h2><a >Entreprise : " + detaildevi.ID_Devis.ID_Client.Entreprise + "</a></h2>"
			htm += "<p>Date commande : " + str(detaildevi.ID_Devis.Date_Devis) + "</p>"
			
			htm += "<p>Transport : " + detaildevi.ID_Devis.Transport + "</p>"
			htm += "<p>Type Transport : " + detaildevi.ID_Devis.Type_Transport + "</p>"
			htm += "<p>Chauffeur : " + detaildevi.ID_Devis.Chauffeur + "</p>"
			htm += "<p>Matricule : " + detaildevi.ID_Devis.Matricule + "</p>"
			htm += "<p>Date Sortie : " + str(detaildevi.ID_Devis.Date_Sortie) + "</p>"
			htm += "<span>Client : " + detaildevi.ID_Devis.ID_Client.ID_Client + "</span>"
			
			htm += "<p>Email :" + detaildevi.ID_Devis.ID_Client.Email + "</p>"
			htm += "<p>Tel :" + detaildevi.ID_Devis.ID_Client.Tel + "</p>"
			htm += "<p>Adresse :" + detaildevi.ID_Devis.ID_Client.Adresse + "</p>"
			htm += "<p>Ville :" + detaildevi.ID_Devis.ID_Client.Description + "</p>"

			htm += "<p>Prix : " + str(detaildevi.Prix) + "</p>"
			htm += "<p>Quantite : " + str(detaildevi.Quantite) + "</p>"
			htm += "<hr>"


			htm += "</div>"
			htm += "</div>"

		htm += "</div>"
		htm += "</div>"
		htm += "</div>"
		htm += "</div>"


	return HttpResponse(htm)