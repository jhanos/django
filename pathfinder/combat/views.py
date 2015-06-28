from django.shortcuts import *
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from combat.models import *
from django.template import RequestContext
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
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

class displayForm(forms.Form):
    name = models.ManyToManyField(PathfinderWeapon)

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
    """Page for displaying weapon or creature"""
    type=request.GET.get('type','false')
    name=request.GET.get('name','false')
    form=displayForm()
    object=PathfinderWeapon.objects.all()[0]
    #return render(request,'combat/display.html',{'object':object.display()})
    return render(request,'combat/display0.html',{'form':form})



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
