# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import list_detail
from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from W4W.models import school, inschrijving, project, steunpunt
from W4W.excel import *
from datetime import *
from forms import InschrijfForm
from django.core.mail import send_mail

def query_school(request):
	"""
        Returns a list of schools based on the query paremeters, and displays using generic view list
    """
	naamschool= request.GET.get('naam_school', '')
	plaatsnaam= request.GET.get('plaatsnaam', '')
	gemeente= request.GET.get('gemeente', '')
	
	orderby= request.GET.get('order', 'nd')	
	pagina=request.GET.get('page','1')
	error_mesg=''
    
	if (naamschool=='' and plaatsnaam=='' and gemeente==''):
		if (orderby=='nd'): results = school.objects.all().order_by('NAAM_VOLLEDIG')
		elif (orderby=='nu'): results = school.objects.all().order_by('-NAAM_VOLLEDIG')
		elif (orderby=='pd'): results = school.objects.all().order_by('NAAM_PLAATS_VEST')
		elif (orderby=='pu'): results = school.objects.all().order_by('-NAAM_PLAATS_VEST')
		elif (orderby=='gd'): results = school.objects.all().order_by('GEMEENTENAAM')
		elif (orderby=='gu'): results = school.objects.all().order_by('-GEMEENTENAAM')

	
	elif (len(naamschool)>2) :
		if (orderby=='nd'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('NAAM_VOLLEDIG')
		elif (orderby=='nu'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('-NAAM_VOLLEDIG')
		elif (orderby=='pd'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('NAAM_PLAATS_VEST')
		elif (orderby=='pu'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('-NAAM_PLAATS_VEST')
		elif (orderby=='gd'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('GEMEENTENAAM')
		elif (orderby=='gu'): results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('-GEMEENTENAAM')
	
	elif (len(plaatsnaam)>2) :
		if (orderby=='nd'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('NAAM_VOLLEDIG')
		elif (orderby=='nu'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('-NAAM_VOLLEDIG')
		elif (orderby=='pd'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('NAAM_PLAATS_VEST')
		elif (orderby=='pu'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('-NAAM_PLAATS_VEST')
		elif (orderby=='gd'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('GEMEENTENAAM')
		elif (orderby=='gu'): results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('-GEMEENTENAAM')
		
	elif (len(gemeente)>2) :
		if (orderby=='nd'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('NAAM_VOLLEDIG')
		elif (orderby=='nu'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('-NAAM_VOLLEDIG')
		elif (orderby=='pd'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('NAAM_PLAATS_VEST')
		elif (orderby=='pu'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('-NAAM_PLAATS_VEST')
		elif (orderby=='gd'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('GEMEENTENAAM')
		elif (orderby=='gu'): results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('-GEMEENTENAAM')	
		
	else:
		results = school.objects.none()
		error_mesg='Er zijn minstens drie letters nodig voor een zoekopdracht.'
	
	return list_detail.object_list(request,queryset=results,paginate_by=20, page=pagina,template_name='W4W/school_list.html',extra_context={'naamschool':naamschool,'plaatsnaam':plaatsnaam,'gemeente':gemeente,'order_by':orderby,'error_msg':error_mesg})	 

def query_inschrijving(request):
	"""
        Returns a list of inschrijvingen, and displays using generic view list
    """
	orderby= request.GET.get('order', 'nd')	
	pagina=request.GET.get('page','1')
	export=request.GET.get('ex','0')
	error_mesg=''
  
	if (orderby=='id'): results = inschrijving.objects.filter(ACTIEF=True).order_by('-id')  
	elif (orderby=='nd'): results = inschrijving.objects.filter(ACTIEF=True).order_by('NAAM_SCHOOL')
	elif (orderby=='nu'): results = inschrijving.objects.filter(ACTIEF=True).order_by('-NAAM_SCHOOL')
	elif (orderby=='pd'): results = inschrijving.objects.filter(ACTIEF=True).order_by('PLAATS')
	elif (orderby=='pu'): results = inschrijving.objects.filter(ACTIEF=True).order_by('-PLAATS')
	elif (orderby=='sd'): results = inschrijving.objects.filter(ACTIEF=True).order_by('STEUNPUNT')
	elif (orderby=='su'): results = inschrijving.objects.filter(ACTIEF=True).order_by('-STEUNPUNT')
	
	else:
		results = inschrijving.objects.none()
		error_mesg='Geen inschrijvingen gevonden.'
	
	numschools=len(results)
	return list_detail.object_list(request,queryset=results,paginate_by=20, page=pagina,template_name='W4W/inschrijving_list.html',extra_context={'export':export,'order_by':orderby,'error_msg':error_mesg,'numschools':numschools})	 

def query_steunpunt(request):
	"""
        Returns a list of steunpunten, and displays using generic view list
    """
	orderby= request.GET.get('order', 'id')	
	pagina=request.GET.get('page','1')
	error_mesg=''
    
	results = steunpunt.objects.filter(ACTIEF=True).exclude(NAAM__contains='onbekend').order_by('id')
	
	if not(results):
		error_mesg='Geen inschrijvingen gevonden.'
	
	return list_detail.object_list(request,queryset=results,paginate_by=20, page=pagina,template_name='W4W/steunpunt_list.html',extra_context={'order_by':orderby,'error_msg':error_mesg})	 



def inschrijf(request):
	if request.method == 'POST': # If the form has been submitted...
		form = InschrijfForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			
			STEUNPUNT_c=form.cleaned_data['STEUNPUNT']
			PROJECT_c=project.objects.get(id=76) #form.cleaned_data['PROJECT']
			NUM_GROEP_GR7_c=form.cleaned_data['NUM_GROEP_GR7']
			NUM_GROEP_GR8_c=form.cleaned_data['NUM_GROEP_GR8']
			NUM_GROEP_GR67_c=form.cleaned_data['NUM_GROEP_GR67']
			NUM_GROEP_GR678_c=form.cleaned_data['NUM_GROEP_GR678']
			NUM_GROEP_GR78_c=form.cleaned_data['NUM_GROEP_GR78']
			ACTIEF_c=True
			TOTAAL_LEERLINGEN_c=form.cleaned_data['TOTAAL_LEERLINGEN']
			DATUM_WANDELING_c=form.cleaned_data['DATUM_WANDELING']
			PLAATS_WANDELING_c=form.cleaned_data['PLAATS_WANDELING']
			
			Nu=datetime.today()
			ThisYear=Nu.year
			EERDER_MEEGEDAAN_c=''

			if form.cleaned_data['EERDER_MEEGEDAAN_nee']:
				EERDER_MEEGEDAAN_c+='nee '
			else:
				if form.cleaned_data['EERDER_MEEGEDAAN_VJ']:
					EERDER_MEEGEDAAN_c+='2012 '
				if form.cleaned_data['EERDER_MEEGEDAAN_TJ']:
					EERDER_MEEGEDAAN_c+='2011 '
				if form.cleaned_data['EERDER_MEEGEDAAN_eerder']:
					EERDER_MEEGEDAAN_c+='eerder '
			
			NAAM_SCHOOL_c =form.cleaned_data['NAAM_SCHOOL']
			NAAM_CONTACT_c=form.cleaned_data['NAAM_CONTACT']
			EMAIL_CONTACT_c=form.cleaned_data['EMAIL_CONTACT']
			ADRES_c =form.cleaned_data['ADRES']
			POSTCODE_c=form.cleaned_data['POSTCODE']
			PLAATS_c=form.cleaned_data['PLAATS']
			NR_TELEFOON_c=form.cleaned_data['NR_TELEFOON']
			AKKOORD_VOORW_c= form.cleaned_data['AKKOORD_VOORW']
			OPMERKINGEN_c=form.cleaned_data['OPMERKINGEN']
			
			INVOER_DATUM_c= Nu
			LAATSTE_WIJZIGING_c=Nu
			
			inschr=inschrijving(STEUNPUNT=STEUNPUNT_c, PROJECT=PROJECT_c, NUM_GROEP_GR7=NUM_GROEP_GR7_c, NUM_GROEP_GR8=NUM_GROEP_GR8_c, NUM_GROEP_GR67=NUM_GROEP_GR67_c, NUM_GROEP_GR678=NUM_GROEP_GR678_c, NUM_GROEP_GR78=NUM_GROEP_GR78_c, ACTIEF=ACTIEF_c, TOTAAL_LEERLINGEN=TOTAAL_LEERLINGEN_c, DATUM_WANDELING=DATUM_WANDELING_c, PLAATS_WANDELING=PLAATS_WANDELING_c, EERDER_MEEGEDAAN=EERDER_MEEGEDAAN_c, NAAM_SCHOOL=NAAM_SCHOOL_c , NAAM_CONTACT=NAAM_CONTACT_c, EMAIL_CONTACT=EMAIL_CONTACT_c, ADRES=ADRES_c , POSTCODE=POSTCODE_c, PLAATS=PLAATS_c, NR_TELEFOON=NR_TELEFOON_c, AKKOORD_VOORW=AKKOORD_VOORW_c , OPMERKINGEN=OPMERKINGEN_c, INVOER_DATUM=INVOER_DATUM_c,  LAATSTE_WIJZIGING=LAATSTE_WIJZIGING_c)
			inschr.save()
			message='Dag Chris,\n\n'+'De school '+NAAM_SCHOOL_c+' heeft zich ingeschreven.\n'+'Contactpersoon: '+NAAM_CONTACT_c +'\n\nGroetjes, je WvW admin'
			
			send_mail('WvW inschrijving ' + NAAM_SCHOOL_c, message, 'no-reply@wandelenvoorwater.nl',
    ['chris@akvo.org'], fail_silently=True)
			
			return HttpResponseRedirect('/WvW_media/thanks.html') # Redirect after POST
	else:
		form = InschrijfForm() # An unbound form

	return render_to_response('W4W/school_form.html', {'form': form}, context_instance=RequestContext(request))


def export_to_excel_school(request):
	"""
	Exports current school selection to excel.
	"""
	naamschool= request.GET.get('naam_school', '')
	plaatsnaam= request.GET.get('plaatsnaam', '')
	gemeente= request.GET.get('gemeente', '')

	if (len(naamschool)>2) :
		results = school.objects.filter(NAAM_VOLLEDIG__contains=naamschool).order_by('NAAM_VOLLEDIG')
	elif (len(plaatsnaam)>2) :
		results = school.objects.filter(NAAM_PLAATS_VEST__contains=plaatsnaam).order_by('NAAM_VOLLEDIG')
	elif (len(gemeente)>2) :
		results = school.objects.filter(GEMEENTENAAM__contains=gemeente).order_by('NAAM_VOLLEDIG')
	else :
		results = school.objects.all()
	
	xls=excel_export_scholen(request, results)
	return xls
	
def export_to_excel_inschrijf(request):
	"""
	Exports inschrijvingen to excel.
	"""
	
	results = inschrijving.objects.order_by('STEUNPUNT')
	
	xls=excel_export_inschrijvingen(request, results)
	return xls

	
	