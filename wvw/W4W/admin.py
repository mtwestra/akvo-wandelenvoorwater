from W4W.models import school,steunpunt,inschrijving, project
from django.contrib import admin

class scholenAdmin(admin.ModelAdmin):
	fieldsets = [
        (None, {'fields': ['NAAM_VOLLEDIG','NAAM_STRAAT_VEST','NR_HUIS_VEST','POSTCODE_VEST','NAAM_PLAATS_VEST','GEMEENTENAAM','PROVINCIE_VEST', 'INTERNET' ,'NR_TELEFOON','NR_FAX','BRIN_NUMMER'	
]}),
        ('Correspondentieadres', {'fields': ['NAAM_STRAAT_CORR','NR_HUIS_CORR','POSTCODE_CORR','NAAM_PLAATS_CORR'
]}),
        ('Bevoegd gezag', {'fields': ['NAAM_VOLLEDIG_GEZ','NR_ADMINISTRATIE_GEZ','NAAM_STRAAT_COR_GEZ','NR_HUIS_CORR_GEZ','POSTCODE_CORR_GEZ','NAAM_PLAATS_CORR_GEZ']})
    ]
    
    
	list_display = ('id','NAAM_VOLLEDIG','NAAM_PLAATS_VEST', 'GEMEENTENAAM', 'PROVINCIE_VEST')
	search_fields = ['NAAM_VOLLEDIG','BRIN_NUMMER','NAAM_PLAATS_VEST','GEMEENTENAAM']
	
def maak_inactief(modeladmin,request, queryset):
	queryset.update(ACTIEF=False)

def maak_actief(modeladmin,request, queryset):
	queryset.update(ACTIEF=True)
		
maak_inactief.short_description="Maak geselecteerde inschrijvingen inactief"
maak_actief.short_description="Maak geselecteerde inschrijvingen actief"
	
class inschrijvingAdmin(admin.ModelAdmin):	
	fieldsets = [
		('Gegevens school',{'fields':['NAAM_SCHOOL','BRIN_NUMMER','NAAM_CONTACT','EMAIL_CONTACT','ADRES','POSTCODE','PLAATS','NR_TELEFOON']}),
		('Leerlingen',{'fields':['NUM_GROEP_GR7','NUM_GROEP_GR8','NUM_GROEP_GR67','NUM_GROEP_GR678','NUM_GROEP_GR78', 'TOTAAL_LEERLINGEN']}),
		('Wandeling',{'fields':['ACTIEF','PLAATS_WANDELING','DATUM_WANDELING','EERDER_MEEGEDAAN','STEUNPUNT','PROJECT','AKKOORD_VOORW','OPMERKINGEN','INVOER_DATUM','LAATSTE_WIJZIGING']}),
			('Geolocatie',{'fields':['GEOCODED','LATITUDE','LONGITUDE']})
	]
	
	list_display=('id','ACTIEF','NAAM_SCHOOL','PLAATS_WANDELING','DATUM_WANDELING','TOTAAL_LEERLINGEN','NAAM_CONTACT','OPMERKINGEN','GEOCODED')
	search_fields=['NAAM_SCHOOL','PLAATS_WANDELING']
	actions=[maak_inactief,maak_actief]
	list_filter=('ACTIEF',)
	ordering=['-id']
			
			
class steunpuntAdmin(admin.ModelAdmin):
	fieldsets = [('Gegevens',{'fields':['ACTIEF','NAAM','WEBSITE','ADRES','POSTCODE','PLAATS','NAAM_CONTACT','EMAIL_CONTACT','NR_TELEFOON']}),('Projecten',{'fields':['PROJECTEN']}),('Admin',{'fields':['LOGO_URL','USERNAME','PASSWD','INVOER_DATUM','LAATSTE_WIJZIGING']})
	]
	
	list_display =('id','ACTIEF','NAAM','NAAM_CONTACT','NR_TELEFOON','EMAIL_CONTACT')
	search_fields = ['NAAM','NAAM_CONTACT']
	filter_horizontal = ('PROJECTEN',)
	
class projectenAdmin(admin.ModelAdmin):
	fieldsets=[(None,{'fields':['ACTIEF','AKVO_CODE','PROJECT_AANDUIDING','PROJECT_NAAM','PROJECT_BESCHRIJVING','INVOER_DATUM','LAATSTE_WIJZIGING']})
		]
	list_display=('id','ACTIEF','PROJECT_NAAM','AKVO_CODE')
	search_fields=['PROJECT_NAAM','AKVO_CODE']
	
	
admin.site.register(school,scholenAdmin)
admin.site.register(steunpunt,steunpuntAdmin)
admin.site.register(inschrijving, inschrijvingAdmin)
admin.site.register(project,projectenAdmin)



