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
    urls=(('creature',"creature"), ('weapon',"weapon"), ('armor',"armor"))
    return render(request,'combat/index.html',{'urls':urls,'active':"home"})

# Class for generate a form for creature , weapon and armor models
class PathfinderWeaponForm(ModelForm):
    class Meta:
        model = PathfinderWeapon
        fields = '__all__'

class PathfinderCreatureForm(ModelForm):
    class Meta:
        model = PathfinderCreatures
        fields = '__all__'

class PathfinderArmorForm(ModelForm):
    class Meta:
        model = PathfinderArmor
        fields = '__all__'

# class for generate a display Form for creature , weapon and armor
class displayCreatureForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=PathfinderCreatures.objects.all())

class displayWeaponForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=PathfinderWeapon.objects.all())

class displayArmorForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=PathfinderArmor.objects.all())

# View for Create creature
def createCreature(request,name):
    """ Page for create creature in the database"""
    return render(request,'combat/date.html',locals())


# View for create Weapon,armor and creature
def create(request,type=None):
    """"Page for weapon creation"""
    if request.method == 'POST': # If the form has been submitted...
        form = PathfinderWeaponForm(request.POST) # A form bound to the POST data
        name = request.POST['name']
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/combat/create/success?type=weapon&name='+name) # Redirect after POST
    else:
        title='Formulaire de creation'
        if type == 'weapon':
            form=PathfinderWeaponForm()
        elif type == 'creature':
            form=PathfinderCreatureForm()
        elif type == 'armor':
            form=PathfinderArmorForm()
        return render_to_response('combat/form.html',{'title': title,'form': form,'type':type,'active':"create"},context_instance=RequestContext(request))


def display(request):
    """Page for displaying weapon or creature"""
    if request.method == 'POST':
        type=request.GET.get('type','false')
        name=request.POST.get('name','false')
        object=PathfinderWeapon.objects.filter(name=name)[0]
        return render(request,'combat/display.html',{'object':object.display()})
    else:
        WeaponForm=displayWeaponForm()
        CreatureForm=displayCreatureForm()
        ArmorForm=displayArmorForm()
        active="display"
        # locals() contains all variables
        return render(request,'combat/display0.html',locals())



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
