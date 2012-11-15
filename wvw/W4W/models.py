from django.db import models

class school(models.Model):
	class Meta:
		verbose_name = "School"
		verbose_name_plural="Scholen"
        
	BRIN_NUMMER = models.CharField('BRIN code',max_length=15,blank=True, null=True)
	NAAM_VOLLEDIG =	models.CharField('Naam school',max_length=100,blank=True, null=True)
	NAAM_STRAAT_VEST = models.CharField('Straat',max_length=100,blank=True, null=True)
	NR_HUIS_VEST = models.CharField('Huisnummer',max_length=15,blank=True, null=True) 
	POSTCODE_VEST = models.CharField('Postcode',max_length=10,blank=True, null=True) 	
	NAAM_PLAATS_VEST = models.CharField('Plaats',max_length=100,blank=True, null=True)	
	GEMEENTENAAM = models.CharField('Gemeente',max_length=100,blank=True, null=True)	
	
	GEOCODED=models.CharField('Geocoded',max_length=25,blank=True, null=True)
	LONGITUDE=models.CharField('Longitude',max_length=20,blank=True, null=True)
	LATITUDE=models.CharField('Latitude',max_length=20,blank=True, null=True)
	
	NAAM_STRAAT_CORR = models.CharField('Straat',max_length=100,blank=True, null=True)		
	NR_HUIS_CORR =	models.CharField('Huisnummer',max_length=15,blank=True, null=True)
	POSTCODE_CORR = models.CharField('Postcode',max_length=10,blank=True, null=True)		
	NAAM_PLAATS_CORR =	models.CharField('Plaats',max_length=100,blank=True, null=True)	
	NR_TELEFOON	=models.CharField('Telefoon',max_length=15,blank=True, null=True)
	NR_FAX = models.CharField('Fax',max_length=15,blank=True, null=True)
	
	PROVINCIE_VEST = models.CharField('Provincie',max_length=100,blank=True, null=True)		
	NAAM_VOLLEDIG_GEZ =	models.CharField('Naam',max_length=100,blank=True, null=True)	
	NR_ADMINISTRATIE_GEZ =	models.CharField('Administratienummer',max_length=100,blank=True, null=True)	
	NAAM_STRAAT_COR_GEZ	=models.CharField('Straat',max_length=100,blank=True, null=True)	
	NR_HUIS_CORR_GEZ =models.CharField('Huisnummer',max_length=15,blank=True, null=True)
	POSTCODE_CORR_GEZ =	models.CharField('Postcode',max_length=100,blank=True, null=True)	
	NAAM_PLAATS_CORR_GEZ =models.CharField('Plaats',max_length=100,blank=True, null=True)		
	INTERNET =models.CharField('Website',max_length=100,blank=True, null=True)	
	def __unicode__(self):
		return self.NAAM_VOLLEDIG


class project(models.Model):
	class Meta:
		verbose_name = "Project"
		verbose_name_plural="Projecten"
		
	ACTIEF=models.BooleanField('Actief')
	AKVO_CODE=models.IntegerField('Code Akvo project',blank=True, null=True)
	PROJECT_AANDUIDING=models.CharField('Project aanduiding',max_length=100,blank=True, null=True)
	
	PROJECT_NAAM = models.CharField('Naam contactpersoon',max_length=100,blank=True, null=True)
	PROJECT_BESCHRIJVING = models.CharField('Opmerkingen',max_length=250,blank=True, null=True)
	
	INVOER_DATUM = models.DateField('Invoerdatum',blank=True, null=True)
	LAATSTE_WIJZIGING = models.DateTimeField('Laatste wijziging',blank=True, null=True)
	def __unicode__(self):
		return u'%s' % (self.PROJECT_NAAM)
	
class steunpunt(models.Model):
	class Meta:
		verbose_name = "Steunpunt"
		verbose_name_plural="Steunpunten"
		
	ACTIEF=models.BooleanField('Actief')
	NAAM =	models.CharField('Naam steunpunt',max_length=100,blank=True, null=True)
	LOGO_URL = models.CharField('Logo URL',max_length=200,blank=True, null=True)
	WEBSITE = models.CharField('Website',max_length=100,blank=True, null=True)
	
	USERNAME = models.CharField('Username',max_length=100,blank=True, null=True)
	PASSWD = models.CharField('Password',max_length=100,blank=True, null=True)
	
	PROJECTEN = models.ManyToManyField(project,blank=True, null=True)
	
	NAAM_CONTACT = models.CharField('Naam contactpersoon',max_length=100,blank=True, null=True)	
	EMAIL_CONTACT = models.CharField('E-mail',max_length=100,blank=True, null=True)
	ADRES = models.CharField('Adres',max_length=100,blank=True, null=True) 
	POSTCODE = models.CharField('Postcode',max_length=10,blank=True, null=True) 	
	PLAATS = models.CharField('Plaats',max_length=100,blank=True, null=True)	
	NR_TELEFOON = models.CharField('Telefoon',max_length=15,blank=True, null=True)

	INVOER_DATUM = models.DateTimeField('Invoerdatum',blank=True, null=True)
	LAATSTE_WIJZIGING = models.DateTimeField('Laatste wijzing',blank=True, null=True)
	def __unicode__(self):
		return u'%s' % (self.NAAM)
		
class inschrijving(models.Model):
	class Meta:
		verbose_name = "Inschrijving"
		verbose_name_plural="Inschrijvingen"
	
	STEUNPUNT=models.ForeignKey(steunpunt, verbose_name="Steunpunt")
	PROJECT=models.ForeignKey(project, verbose_name="Project")
	
	NUM_GROEP_GR7=models.IntegerField('Aantal groepen 7', blank=True, null=True)
	NUM_GROEP_GR8=models.IntegerField('Aantal groepen 8', blank=True, null=True)
	NUM_GROEP_GR67=models.IntegerField('Aantal gemengde groepen 6/7', blank=True, null=True)
	NUM_GROEP_GR678=models.IntegerField('Aantal gemengde groepen 6/7/8',blank=True, null=True)
	NUM_GROEP_GR78=models.IntegerField('Aantal gemengde groepen 7/8', blank=True, null=True)
	
	ACTIEF=models.BooleanField('Actief')
	
	TOTAAL_LEERLINGEN=models.IntegerField('Totaal aantal leerlingen', blank=True, null=True)
	
	DATUM_WANDELING=models.DateField('Datum wandeling',blank=True, null=True)
	PLAATS_WANDELING=models.CharField('Plaats wandeling',max_length=100,blank=True,null=True)
	
	EERDER_MEEGEDAAN=models.CharField('Eerder meegedaan',max_length=100,blank=True,null=True)
	
	NAAM_SCHOOL = models.CharField('Naam school',max_length=200,blank=True,null=True)	
	BRIN_NUMMER = models.CharField('BRIN code',max_length=15,blank=True,null=True)
	NAAM_CONTACT = models.CharField('Naam contactpersoon',max_length=100,blank=True,null=True)	
	EMAIL_CONTACT = models.CharField('E-mail',max_length=100,blank=True,null=True)
	ADRES = models.CharField('Adres',max_length=100,blank=True,null=True) 
	POSTCODE = models.CharField('Postcode',max_length=10,blank=True,null=True) 	
	PLAATS = models.CharField('Plaats',max_length=100,blank=True,null=True)	
	NR_TELEFOON = models.CharField('Telefoon',max_length=15,blank=True,null=True)
	
	AKKOORD_VOORW = models.BooleanField('Akkoord met de voorwaarden?')
	OPMERKINGEN = models.CharField('Opmerkingen',max_length=1000,blank=True,null=True)
	INVOER_DATUM = models.DateTimeField('Invoerdatum',blank=True, null=True)
	LAATSTE_WIJZIGING=models.DateTimeField('Laatste wijziging',blank=True, null=True)
	GEOCODED = models.CharField('Geocode resultaat',max_length=25,blank=True,null=True,default='NONE')
	LONGITUDE = models.CharField('Longitude',max_length=20,blank=True,null=True)
	LATITUDE = models.CharField('Latitude',max_length=20,blank=True,null=True)
	
	def __unicode__(self):
		return u'%s' %(self.NAAM_SCHOOL)
		
