#
# Stand alone script
#
from django.core.management import setup_environ
from Packager import settings
setup_environ(settings)
import re

#
# Modelo de la aplicacion
#
from Packager_app import models



from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
 
@csrf_exempt
def upload_file(request):
    if request.method == "POST":
	upload = request.FILES['Filedata']
	try:
	    dest = open(upload.name, "wb+")
	    for block in upload.chunks():
		dest.write(block)
	    dest.close()
	except IOError:
	    pass # ignore failed uploads for now
 
    response = HttpResponse()
    response.write("%s\r\n" % upload.name)
    return response

def GetImageRendition(Item=None, FileName=''):
    Splited = re.match("(.+)_(PI[S|H][0-9][0-9]).([a-z][a-z][a-z])",FileName)

    if Splited:
	Sufix = '_' + Splited.group(2)
	Ext   = '.' + Splited.group(3)

    try:
	IProfile = models.ImageProfile.objects.get(sufix=Sufix, file_extension=Ext)
    
	try:
	    IRendition = models.ImageRendition.objects.get(item=Item, image_profile=IProfile)
	    return IRendition
	except:
	    return None
    except:
	return None


f = 'trolita_PIH01.png'

# Agregar una expresion Regular    

suf, ext = f.split('_')[len(f.split('_'))-1].split('.')


x = 
if x:
    print x.group(1)
    print x.group(2)
    print x.group(3)
else:
    print "File Invalido"

suf = '_' + suf
ext = '.' + ext

item = models.Item.objects.all()

irend = models.ImageProfile.objects.filter(sufix=suf, file_extension=ext)
print irend
vrend = models.ImageRendition.objects.get(item=item[0], image_profile=irend)
vrend.file_name = f
vrend.status = 'F'
vrend.save()


