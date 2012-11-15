from django.http import HttpResponse
import xlwt


import xlwt
from datetime import datetime
import time

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
	num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')



def excel_export_scholen(request,scholen):
	response = HttpResponse(mimetype="application/ms-excel")
   
	naamschool= request.GET.get('naam_school', '')
	plaatsnaam= request.GET.get('plaatsnaam', '')
	gemeente= request.GET.get('gemeente', '')
    
	filenaam='Scholen_'+naamschool+plaatsnaam+gemeente+'.xls'
	response['Content-Disposition'] = 'attachment; filename='+filenaam
    
	style0 = xlwt.easyxf('font: name Arial, bold on')
	style1 = xlwt.easyxf('font: name Arial, bold off')
  
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Scholen')
    
	ws.write(0, 0, 'BRIN code',style0)
	ws.write(0, 1, 'Naam school',style0)
	ws.col(1).width = 6600
	ws.write(0, 2, 'Straat',style0)
	ws.col(2).width = 5000
	ws.write(0, 3, 'Huisummer',style0)
	ws.write(0, 4, 'Postcode',style0)
	ws.write(0, 5, 'Plaatsnaam',style0)
	ws.col(5).width = 5000
	ws.write(0, 6, 'Gemeente',style0)
	ws.col(6).width = 5000
	ws.write(0, 7, 'Provincie',style0)
	ws.col(7).width = 5000
	ws.write(0, 8, 'Straat corr.',style0)
	ws.col(8).width = 5000
	ws.write(0, 9, 'Huisnummer corr.',style0)
	ws.write(0, 10, 'Postcode corr.',style0)
	ws.write(0, 11, 'Plaatsnaam corr.',style0)
	ws.col(11).width = 3000
	ws.write(0, 12, 'Telefoon',style0)
	ws.col(12).width = 3000
	ws.write(0, 13, 'Fax',style0)
	ws.write(0, 14, 'Internet',style0)
	ws.col(14).width = 6500
	ws.write(0, 15, 'Naam bevoegd gezag',style0)
	ws.col(15).width = 5000
	ws.write(0, 16, 'Straatnaam bev. gezag',style0)
	ws.col(16).width = 5000
	ws.write(0, 17, 'Huisnummer bev. gezag',style0)
	ws.write(0, 18, 'Postcode bev. gezag',style0)
	ws.write(0, 19, 'Plaatsnaam bev. gezag',style0)
	ws.col(19).width = 5000
	
	for idx,school in  enumerate(scholen):
		ws.write(idx+1, 0,school.BRIN_NUMMER,style1)	
		ws.write(idx+1, 1,school.NAAM_VOLLEDIG,style1) 
		ws.write(idx+1, 2,school.NAAM_STRAAT_VEST,style1) 
		ws.write(idx+1, 3,school.NR_HUIS_VEST,style1) 
		ws.write(idx+1, 4,school.POSTCODE_VEST,style1) 	
		ws.write(idx+1, 5,school.NAAM_PLAATS_VEST,style1) 
		ws.write(idx+1, 6,school.GEMEENTENAAM,style1) 
		ws.write(idx+1, 7,school.PROVINCIE_VEST,style1) 
		ws.write(idx+1, 8,school.NAAM_STRAAT_CORR,style1) 	
		ws.write(idx+1, 9,school.NR_HUIS_CORR,style1) 
		ws.write(idx+1, 10,school.POSTCODE_CORR,style1) 		
		ws.write(idx+1, 11,school.NAAM_PLAATS_CORR,style1)
		ws.write(idx+1, 12,school.NR_TELEFOON,style1)	
		ws.write(idx+1, 13,school.NR_FAX,style1) 
		ws.write(idx+1, 14,school.INTERNET,style1)
		ws.write(idx+1, 15,school.NAAM_VOLLEDIG_GEZ,style1) 
		ws.write(idx+1, 16,school.NAAM_STRAAT_COR_GEZ,style1)
		ws.write(idx+1, 17,school.NR_HUIS_CORR_GEZ,style1)
		ws.write(idx+1, 18,school.POSTCODE_CORR_GEZ,style1)
		ws.write(idx+1, 19,school.NAAM_PLAATS_CORR_GEZ,style1) 

	wb.save(response)
	return response
    
    

def excel_export_inschrijvingen(request,inschrijvingen):
	response = HttpResponse(mimetype="application/ms-excel")
    
	filenaam='Inschrijvingen'+'.xls'
	response['Content-Disposition'] = 'attachment; filename='+filenaam
    
	style0 = xlwt.easyxf('font: name Arial, bold on')
	style1 = xlwt.easyxf('font: name Arial, bold off')
	style2 = xlwt.easyxf(num_format_str='D-MMM-YY')
  
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Inschrijvingen')
    
	ws.write(0, 0, 'BRIN code',style0)
	ws.write(0, 1, 'Naam school',style0)
	ws.col(1).width = 6600
	ws.write(0, 2, 'Adres',style0)
	ws.col(2).width = 5000
	ws.write(0, 3, 'Postcode',style0)
	ws.write(0, 4, 'Plaatsnaam',style0)
	ws.col(5).width = 5000
	ws.write(0, 5, 'Contactpersoon',style0)
	ws.col(6).width = 5000
	ws.write(0, 6, 'Email contactpersoon',style0)
	ws.col(7).width = 5000
	ws.write(0, 7, 'Telefoon',style0)
	ws.col(8).width = 5000
	ws.write(0, 8, 'Steunpunt',style0)
	ws.write(0, 9, 'Project',style0)
	ws.write(0, 10, 'Aantal leerlingen',style0)
	ws.col(11).width = 3000
	ws.write(0, 11, 'groep 7',style0)
	ws.write(0, 12, 'groep 8',style0)
	ws.write(0, 13, 'groep 6/7',style0)
	ws.write(0, 14, 'groep 6/7/8',style0)
	ws.write(0, 15, 'groep 7/8',style0)
	ws.write(0, 16, 'Datum wandeling',style0)
	ws.write(0, 17, 'Datum inschrijving',style0)
	ws.write(0, 18, 'Plaats wandeling',style0)
	ws.write(0, 19, 'Akkoord voorwaarden',style0)
	ws.write(0, 20, 'Opmerkingen',style0)
	ws.col(19).width = 5000


	for idx,inschrijving in  enumerate(inschrijvingen):
		dateWand=inschrijving.DATUM_WANDELING
		ws.write(idx+1, 0,inschrijving.BRIN_NUMMER,style1)	
		ws.write(idx+1, 1,inschrijving.NAAM_SCHOOL,style1) 
		ws.write(idx+1, 2,inschrijving.ADRES,style1) 
		ws.write(idx+1, 3,inschrijving.POSTCODE,style1) 
		ws.write(idx+1, 4,inschrijving.PLAATS,style1) 	
		ws.write(idx+1, 5,inschrijving.NAAM_CONTACT,style1) 
		ws.write(idx+1, 6,inschrijving.EMAIL_CONTACT,style1) 
		ws.write(idx+1, 7,inschrijving.NR_TELEFOON,style1) 
		ws.write(idx+1, 8,inschrijving.STEUNPUNT.NAAM,style1) 	
	#	ws.write(idx+1, 9,inschrijving.PROJECT.id,style1) 
		ws.write(idx+1, 10,inschrijving.TOTAAL_LEERLINGEN,style1) 		
		ws.write(idx+1, 11,inschrijving.NUM_GROEP_GR7,style1)
		ws.write(idx+1, 12,inschrijving.NUM_GROEP_GR8,style1)	
		ws.write(idx+1, 13,inschrijving.NUM_GROEP_GR67,style1) 
		ws.write(idx+1, 14,inschrijving.NUM_GROEP_GR678,style1)
		ws.write(idx+1, 15,inschrijving.NUM_GROEP_GR78,style1) 
		ws.write(idx+1, 16,inschrijving.DATUM_WANDELING,style2)
		ws.write(idx+1, 17,inschrijving.INVOER_DATUM,style2)
		ws.write(idx+1, 18,inschrijving.PLAATS_WANDELING,style1)
		ws.write(idx+1, 19,inschrijving.AKKOORD_VOORW,style1)
		ws.write(idx+1, 20,inschrijving.OPMERKINGEN,style1) 


	wb.save(response)
	return response