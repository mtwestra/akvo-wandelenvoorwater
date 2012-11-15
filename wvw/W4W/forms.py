#from django import forms
from django import forms
from recaptchawidget.fields import ReCaptchaField 
from models import steunpunt, project

class InschrijfForm(forms.Form):

	NAAM_SCHOOL = forms.CharField(label='Naam school',max_length=200,error_messages={'required': 'Dit veld graag invullen'},)	
	ADRES = forms.CharField(label='Adres',max_length=100,error_messages={'required': 'Dit veld graag invullen'}) 
	POSTCODE = forms.CharField(label='Postcode',max_length=10, error_messages={'required': 'Dit veld graag invullen'}) 	
	PLAATS = forms.CharField(label='Plaats',max_length=100,error_messages={'required': 'Dit veld graag invullen'})	
	
	NAAM_CONTACT = forms.CharField(label='Naam contactpersoon',max_length=100,error_messages={'required': 'Dit veld graag invullen'})	
	EMAIL_CONTACT = forms.EmailField(label='E-mail',error_messages={'required': 'Vul een geldig email adres in'})
	NR_TELEFOON = forms.CharField(label='Telefoon',max_length=15,required=False)
	
#	EERDER_MEEGEDAAN_nee=forms.MultipleChoiceField(label='Eerder meegedaan',choices=MEEGEDAAN)
	EERDER_MEEGEDAAN_nee=forms.BooleanField(label='Nee',required=False)
	EERDER_MEEGEDAAN_VJ=forms.BooleanField(label='Vorig jaar',required=False)
	EERDER_MEEGEDAAN_TJ=forms.BooleanField(label='Twee jaar geleden',required=False)
	EERDER_MEEGEDAAN_eerder=forms.BooleanField(label='Meer dan twee jaar geleden',required=False)
	
	NUM_GROEP_GR7=forms.IntegerField(label='Aantal groepen 7',required=False)
	NUM_GROEP_GR8=forms.IntegerField(label='Aantal groepen 8',required=False)
	NUM_GROEP_GR67=forms.IntegerField(label='Aantal gemengde groepen 6/7',required=False)
	NUM_GROEP_GR678=forms.IntegerField(label='Aantal gemengde groepen 6/7/8',required=False)
	NUM_GROEP_GR78=forms.IntegerField(label='Aantal gemengde groepen 7/8',required=False)

	TOTAAL_LEERLINGEN=forms.IntegerField(label='Totaal aantal leerlingen',error_messages={'required': 'Dit veld graag invullen'})

	STEUNPUNT=forms.ModelChoiceField(label='Steunpunt',queryset=steunpunt.objects.order_by('NAAM').filter(ACTIEF=True), empty_label="----", error_messages={'required': 'Maak een keuze. Is het steunpunt nog onbekend, kies dan "nog onbekend" uit de lijst'},required=True)
	PROJECT=forms.ModelChoiceField(label='Project',queryset=project.objects.filter(ACTIEF=True), empty_label="(Nog onbekend)", error_messages={'required': 'Maak een keuze. Is het project nog onbekend, kies dan "nog onbekend" uit de lijst'},required=False)

	DATUM_WANDELING=forms.DateField(label='Datum wandeling',input_formats=('%d-%m-%Y','%d-%m-%y'),required=False)
	PLAATS_WANDELING=forms.CharField(label='Plaats wandeling',max_length=100,required=False)
	OPMERKINGEN = forms.CharField(label='Opmerkingen',max_length=1000,required=False,widget=forms.Textarea)
	
	AKKOORD_VOORW = forms.BooleanField(label='Ja, ik ga akkoord met de voorwaarden',error_messages={'required': 'Dit veld graag invullen'})
	recaptcha = ReCaptchaField()	