from django.shortcuts import *
from django.http import HttpResponse
from django.forms import ModelForm
from combat.models import *
from django.template import RequestContext

# Create your views here.

# Default home page
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Page Accueil appli jdr</h1>
              <p>plein de liens seront présent plus tard</p>"""
    return HttpResponse(text)

# Class for generate a form from models
class PathfinderWeaponForm(ModelForm):
    class Meta:
        model = PathfinderWeapon
        fields = '__all__'

# Class for generate a form from models
class PathfinderCreatureForm(ModelForm):
    class Meta:
        model = PathfinderCreatures
        fields = '__all__'

# View for Create creature
def createCreature(request,name):
    """ Page for create creature in the database"""
    return render(request,'combat/date.html',locals())



# View for create Weapon
def createWeapon(request):
    """"Page for weapon creation"""
    if request.method == 'POST': # If the form has been submitted...
        form = PathfinderWeaponForm(request.POST) # A form bound to the POST data
        name = request.POST['name']
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/combat/create/success?type=weapon&name='+name) # Redirect after POST
    else:
        weapon_form=PathfinderWeaponForm()
        title='Formulaire pour la creation d\'arme'
        #return render_to_response('combat/create.html',{'title': title,'weapon_form': weapon_form},context_instance=RequestContext(request)))
        return render_to_response('combat/form.html',{'title': title,'weapon_form': weapon_form},context_instance=RequestContext(request))


def display(request):
    """Page for displaying weapon"""
    #object=PathfinderWeapon.objects.all()[0]
    objects=PathfinderWeapon.objects.all()
    keys=PathfinderWeapon._meta.get_fields()
    return render(request,'combat/display.html',{'object':objects,'key':keys})
    #return render(request,'combat/display.html',locals())



def success(request):
    """Page for displaying weapon"""
    type=request.GET['type']
    name=request.GET['name']
    title='Succes'
    text='The '+type+' named \"'+name+'\" has been successfully created'
    return render(request,'combat/index.html',{'title':title,'text':text})

# View for display fight
def fight(request,id):
    """"Page for weapon creation"""
    return redirect(home)
