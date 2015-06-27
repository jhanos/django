from django.db import models

# Create your models here.



class PathfinderWeapon(models.Model):
    """(models for Weapon in pathfinder )"""
    name = models.CharField(blank=True, max_length=100,primary_key=True)
    lightWeapon = models.BooleanField(default=True)
    damage = models.CharField(blank=True, max_length=100)
    crit = models.IntegerField(blank=True, null=True)
    critMulti = models.IntegerField(blank=True, null=True)
    weaponRange = models.IntegerField(blank=True, null=True)
    magic = models.IntegerField(blank=True, null=True)
    master = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def display(self):
        all_item=(('name',self.name),('lightWeapon',self.lightWeapon),('damage',self.damage),('crit',self.crit),('critMulti',self.critMulti),('weaponRange',self.weaponRange),('magic',self.magic),('master',self.master))
        return all_item

class PathfinderArmor(models.Model):
    """(models for Armor in pathfinder )"""
    name = models.CharField(blank=True, max_length=100,primary_key=True)
    AC = models.IntegerField(blank=True, null=True)
    dexLimit = models.IntegerField(blank=True, null=True)
    magic = models.IntegerField(blank=True, null=True)
    master = models.BooleanField(default=True)
    compMalus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def display(self):
        all_item=(('name',self.name),('AC',self.AC),('dexLimit',self.dexLimit),('magic',self.magic),('master',self.master),('compMalus',self.compMalus))
        return all_item

class PathfinderCreatures(models.Model):
    """(models for Pathfinder Creatures without weapon)"""
    name = models.CharField(blank=True, max_length=100,primary_key=True)
    AC = models.IntegerField(blank=True, null=True)
    ACtouch = models.IntegerField(blank=True, null=True)
    ACflat = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    init = models.IntegerField(blank=True, null=True)
    fort = models.IntegerField(blank=True, null=True)
    ref = models.IntegerField(blank=True, null=True)
    will = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    str = models.IntegerField(blank=True, null=True)
    dex = models.IntegerField(blank=True, null=True)
    con = models.IntegerField(blank=True, null=True)
    int = models.IntegerField(blank=True, null=True)
    wis = models.IntegerField(blank=True, null=True)
    cha = models.IntegerField(blank=True, null=True)
    baseAtk = models.IntegerField(blank=True, null=True)
    CMB = models.IntegerField(blank=True, null=True)
    CMD = models.IntegerField(blank=True, null=True)
    defaultWeapon1 = models.IntegerField(blank=True, null=True)
    defaultWeapon2 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def display(self):
        all_item=(('name',self.name),('AC',self.AC),('ACtouch',self.ACtouch),('ACflat',self.ACflat),('hp',self.hp),('init',self.init),('fort',self.fort),('ref',self.ref),('will',self.will),('speed',self.speed),('str',self.str),('dex',self.dex),('con',self.con),('int',self.int),('wis',self.wis),('cha',self.cha),('baseAtk',self.baseAtk),('CMB',self.CMB),('CMD',self.CMD),('defaultWeapon1',self.defaultWeapon1),('defaultWeapon2',self.defaultWeapon2))
