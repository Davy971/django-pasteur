from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.forms import TextInput


class Profil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Table_correspondance(models.Model):
    libelle = models.CharField(max_length=100)
    type_analyse = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle + "/" + self.type_analyse


class Parametre_externe_analyse(models.Model):
    nom = models.CharField(max_length=60)
    valeur = models.CharField(max_length=100)
    rang = models.IntegerField(null=True)
    def __str__(self):
        return self.nom


class Parametre_interne_analyse(models.Model):
    nom = models.CharField(max_length=60)
    valeur = models.CharField(max_length=100)
    rang = models.IntegerField(null=True)
    def __str__(self):
        return self.nom


class Parametre_etalonnage(models.Model):
    nom = models.CharField(max_length=60)
    valeur = models.CharField(max_length=100)
    def __str__(self):
        return self.nom


class Codification(models.Model):
    code= models.CharField(max_length=100,verbose_name="codification",default="")
    date_rev= models.DateField(auto_now=False,verbose_name="date_revision",default="")
    revision= models.CharField(max_length=100,verbose_name="révision",default="")
    intitule= models.CharField(max_length=100,verbose_name="Intitulé",default="")
    def __str__(self):
        return self.code

class Type_analyse(models.Model):
    nom = models.CharField(max_length=100)
    parametre_interne=models.ManyToManyField(Parametre_interne_analyse,blank=True)
    parametre_externe = models.ManyToManyField(Parametre_externe_analyse,blank=True)
    parametre_etalonnage = models.ManyToManyField(Parametre_etalonnage,blank=True)
    codification = models.ForeignKey(Codification, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nom


class Etalonnage(models.Model):
    profil= models.ForeignKey(Profil,on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(Type_analyse, on_delete=models.CASCADE)
    date_etalonnage = models.DateField(auto_now=False, verbose_name="Date de l'étalonnage",default=datetime.datetime(1980, 1, 1, 1, 1, 1))
    c_lauryl = models.CharField(max_length=100, verbose_name="concentration mg/L de lauryl sulfate de sodium")
    c_mg = models.CharField(max_length=100, verbose_name="concentration mg/L")
    c_micromol_l= models.CharField(max_length=100, verbose_name="concentration µmol/L")
    c_micro_gl= models.CharField(max_length=100, verbose_name="concentration en µg/L",default="null")
    absorbance= models.CharField(max_length=100, verbose_name="absorbance")

    def __str__(self):
        return self.profil.user.username + "/"+self.type_analyse.nom


class Feuille_calcul(models.Model):
    profil= models.ForeignKey(Profil,on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(Type_analyse, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)

    date_analyse = models.DateField(auto_now=False,default=datetime.datetime(1980, 1, 1, 1, 1,1),verbose_name="Date d'analyse")
    heure_mise_sous_essai = models.TimeField(auto_now=False,default=datetime.time(00, 00),verbose_name="Heure de mise sous essai")
    date_etalonnage = models.DateField(auto_now=False, verbose_name="Date de l'étalonnage", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    longueur_onde=  models.CharField(max_length=100, verbose_name="Longueur d'onde d'analyse")
    etalonnage = models.CharField(max_length=100, verbose_name="Etalonnage",default="null")

    var1_mest = models.CharField(max_length=100, verbose_name="Numéro de lot des filtres")
    var2_mest = models.CharField(max_length=100, verbose_name="MEST de la solution de cellulose microcristalline(mg/L)")

    var3_mest = models.CharField(max_length=100, verbose_name="Rendement(%)")
    var4_mest = models.DateField(auto_now=False, verbose_name="Date de préparation de la solution de cellulose microcristalline",default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var1_ntk = models.DateField(auto_now=False, verbose_name="Date de préparation du mélange catalyseur", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var2_ntk = models.CharField(max_length=100, verbose_name="N° de lot H2SO4")
    var3_ntk = models.CharField(max_length=100, verbose_name="N° de lot acide chlorhydrique")
    var4_ntk = models.CharField(max_length=100, verbose_name="N° de lot de l’acide borique")
    var1_dbo_avec_dilution = models.DateField(auto_now=False, verbose_name="Date de préparation de l'eau de dilution", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var2_dbo_avec_dilution = models.CharField(max_length=100, verbose_name="N° échant utilisé pour l'eau de dilution ensemencée")
    var3_dbo_avec_dilution = models.CharField(max_length=100, verbose_name="DCO de cette échantillon")
    var1_dbo_sans_dilution = models.DateField(auto_now=False, verbose_name="Date de préparation de la solution de lavage",blank=True,null=True)
    var1_oxygene_dissous = models.CharField(max_length=100, verbose_name="Volume thiosulfate versé pour l'étalonnage mL")
    var2_oxygene_dissous = models.CharField(max_length=100, verbose_name="Concentration du thiosulfate de sodium mmol/L")
    var1_chlorophylle_scor_unesco = models.CharField(max_length=100, verbose_name="Lot d'acétone utilisé")
    var1_chlorophylle_lorenzen = models.CharField(max_length=100, verbose_name="Lot d'acide chlorhydrique utilisé")
    var2_chlorophylle_lorenzen = models.CharField(max_length=100, verbose_name="Lot d'acétone utilisé")
    var3_chlorophylle_lorenzen = models.DateField(auto_now=False, verbose_name="Date de préparation de l'HCI", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var1_dco = models.DateField(auto_now=False, verbose_name="Date de minéralisation", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var2_dco = models.DateField(auto_now=False, verbose_name="Date de titration", default=datetime.datetime(1980, 1, 1, 1, 1,1))
    var3_dco = models.CharField(max_length=100, verbose_name="Lot de la solution ferroïne")
    var4_dco = models.CharField(max_length=100, verbose_name="Lot du H2SO4 4 mol/l")
    var5_dco = models.CharField(max_length=100, verbose_name="Volume de sulfate versé pour la détermination de sa concentration")
    var6_dco = models.CharField(max_length=100, verbose_name="Valeur de solution de référence C")
    var7_dco = models.CharField(max_length=100, verbose_name="Essaie à blanc V1")
    var8_dco = models.CharField(max_length=100, verbose_name="Lot de sulfate de mercure")
    var9_dco = models.CharField(max_length=100, verbose_name="Lot de sulfate d'argent")
    var10_dco = models.CharField(max_length=100, verbose_name="Blanc")

    def __str__(self):
        return "Feuille N°"+ str(self.id) + " / " + self.profil.user.first_name




class Echantillon(models.Model):
    numero = models.CharField(max_length=60)
    def __str__(self):
        return self.numero

class Analyse(models.Model):
    echantillon=models.ForeignKey(Echantillon,on_delete=models.CASCADE)
    feuille_calcul = models.ForeignKey(Feuille_calcul, on_delete=models.CASCADE)
    nEchantillon= models.CharField(max_length=60, verbose_name="N° d'échantillon")
    #kmnoa4
    var1_kmno4 = models.CharField(max_length=60, verbose_name="V0 (mL)")
    var2_kmno4 = models.CharField(max_length=60, verbose_name="V1 (mL)")
    var3_kmno4 = models.CharField(max_length=60, verbose_name="V2 (mL)")
    var4_kmno4 = models.CharField(max_length=60, verbose_name="Facteur dilution")
    var5_kmno4 = models.CharField(max_length=60, verbose_name="Resultat en mg/L")
    #siccite
    var1_siccite = models.CharField(max_length=60, verbose_name="m1(g):masse de la coupelle pleine avant séchage à 105°C")
    var2_siccite = models.CharField(max_length=60, verbose_name="m2(g):masse de la coupelle après séchage à 105°C")
    var3_siccite = models.CharField(max_length=60, verbose_name="masse de matière sèche en g")
    var4_siccite = models.CharField(max_length=60, verbose_name="masse de la coupelle vide")
    var5_siccite = models.CharField(max_length=60, verbose_name="V en L")
    var6_siccite = models.CharField(max_length=60, verbose_name="[MS] en g/L")
    var7_siccite = models.CharField(max_length=60, verbose_name="MS en %")
    var8_siccite = models.CharField(max_length=60, verbose_name="taux d'eau %")
    #Matière seche et MVS
    var1_mvs= models.CharField(max_length=200, verbose_name="ma(g):masse du creuset vide")
    var2_mvs= models.CharField(max_length=200, verbose_name="mb(g):masse du creuset contenant échantillon de boue avant séchage à 105°C")
    var3_mvs= models.CharField(max_length=60, verbose_name="mc(g):masse du creuset contenant la matière sèche après séchage à 105°C")
    var4_mvs= models.CharField(max_length=60, verbose_name="m2(g):masse du creuset contenant la matière calcinée à 550°C")
    var5_mvs= models.CharField(max_length=60, verbose_name="V en L")
    var6_mvs= models.CharField(max_length=60, verbose_name="MS en % à 105°C")
    var7_mvs= models.CharField(max_length=60, verbose_name="[MS] en g/L à 105°C")
    var8_mvs= models.CharField(max_length=60, verbose_name="MVS en % à 550 °C")
    var9_mvs= models.CharField(max_length=60, verbose_name="[MVS] en g/L à 550°C")
    #MEST
    var1_mest = models.CharField(max_length=60, verbose_name="P1 (mg)")
    var2_mest = models.CharField(max_length=60, verbose_name="V (ml)")
    var3_mest = models.CharField(max_length=60, verbose_name="P2 (mg)")
    var4_mest = models.CharField(max_length=60, verbose_name="teneur de MES en mg/L")
    # #DCO
    var1_dco = models.CharField(max_length=60, verbose_name="V2 (mL)")
    var2_dco = models.CharField(max_length=60, verbose_name="Volume analysé")
    var3_dco = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var4_dco = models.CharField(max_length=60, verbose_name="DCO en mg/L")
    var5_dco = models.CharField(max_length=60, verbose_name="poste")

    # #NTK
    var1_ntk = models.CharField(max_length=60, verbose_name="C (mol/L) titre HCL")
    var2_ntk = models.CharField(max_length=60, verbose_name="V0 (ml)")
    var3_ntk = models.CharField(max_length=60, verbose_name="V1 (ml)")
    var4_ntk = models.CharField(max_length=60, verbose_name="V2 (ml)")
    var5_ntk = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var6_ntk = models.CharField(max_length=60, verbose_name="NTK mg/L")
    # #DBO avec dilution
    var1_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C3")
    var2_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C4")
    var3_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C1")
    var4_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C2")
    var5_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C1/3")
    var6_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C1-C2")
    var7_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="2C1/3")
    var8_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C3-C4")
    var9_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="Vt")
    var10_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="Ve")
    var11_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="Vt-Ve")
    var12_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="Vt/Ve")
    var13_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="(Vt-Ve)Vt")
    var14_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="DBO")
    var15_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="C1/3 <(C1-C2)")
    var16_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="(C1-C2)<2*C1/3")
    var17_dbo_avec_dilution = models.CharField(max_length=60, verbose_name="'")
    #DBO sans dilution
    var1_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="mesure1 [O2]t0")
    var2_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="mesure1 [O2]t5")
    var3_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="valeur DBO1 mg/L")
    var4_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="mesure2 [O2]t0",blank=True)
    var5_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="mesure2 [O2]t5",blank=True)
    var6_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="valeur DBO2 mg/L",blank=True)
    var7_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="r expérimentale",blank=True)
    var8_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="r théorique",blank=True)
    var9_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="limite de controle",blank=True)
    var10_dbo_sans_dilution = models.CharField(max_length=60, verbose_name="controle",blank=True)
    #sil 650
    var1_sil_650 = models.CharField(max_length=60, verbose_name="absorbance")
    var2_sil_650 = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var3_sil_650 = models.CharField(max_length=60, verbose_name="concentration en mg/L SIO2")
    #oxygene dissous
    var1_oxygene_dissous = models.CharField(max_length=60, verbose_name="v1(mL) volume échantillon titré")
    var2_oxygene_dissous = models.CharField(max_length=60, verbose_name="v2 (mL) volume thiosulfate versé")
    var3_oxygene_dissous = models.CharField(max_length=60, verbose_name="v0 (mL) volume échantillon prélevé")
    var4_oxygene_dissous = models.CharField(max_length=60, verbose_name="résultat en mg/L")
    #chlorophyle
    var1_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="volume solvant initial utilisé pour l'extraction mL")
    var2_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="volume d'eau filtrée L")
    var3_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="parcours optique en centimètre")
    var4_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 750")
    var5_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 663")
    var6_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 645")
    var7_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 630")
    var8_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 430")
    var9_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="A0 410")
    var10_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="Ca en µg/L")
    var11_chlorophylle_scor_unesco = models.CharField(max_length=60, verbose_name="Pa µg/L")
    #SABM
    var1_sabm = models.CharField(max_length=60, verbose_name="Absorbance")
    var2_sabm = models.CharField(max_length=60, verbose_name="épaisseur de la cuve(1 ou 5cm)")
    var3_sabm = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var4_sabm = models.CharField(max_length=60, verbose_name="concentration en lauryl sulfate de sodium en mg/L")
    #residu sec
    var1_residu_sec = models.CharField(max_length=60, verbose_name="mo(mg):masse de la coupelle vide")
    var2_residu_sec = models.CharField(max_length=60, verbose_name="m1(mg):masse de la coupelle pleine après séchage à 105°C")
    var3_residu_sec = models.CharField(max_length=60, verbose_name="m2(mg) masse de la coupelle après séchage à 180°C")
    var4_residu_sec = models.CharField(max_length=60, verbose_name="V volume de la prise d'essai en mL")
    var5_residu_sec = models.CharField(max_length=60, verbose_name="RS en mg/L à 105°C")
    var6_residu_sec = models.CharField(max_length=60, verbose_name="RS en mg/L à 180°C")
    #silice 815
    var1_sil_815 = models.CharField(max_length=60, verbose_name="absorbance")
    var2_sil_815 = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var3_sil_815 = models.CharField(max_length=60, verbose_name="concentration en SiO2 µg/L")
    #SIL-BC
    var1_sil_bc = models.CharField(max_length=60, verbose_name="absorbance")
    var2_sil_bc = models.CharField(max_length=60, verbose_name="facteur de dilution")
    var3_sil_bc = models.CharField(max_length=60, verbose_name="concentration en SiO2 µmol")
    #chlorophylle Lorenzen
    var1_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="volume prélevé (L)")
    var2_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="blc 665")
    var3_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="blc 750")
    var4_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A0 na 665 ")
    var5_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A0 na 750")
    var6_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A0 a 665")
    var7_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A0 a 750")
    var8_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A na 665")
    var9_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="A a 665")
    var10_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="Ca en µg/L")
    var11_chlorophylle_lorenzen = models.CharField(max_length=60, verbose_name="Pa µg/L")
    def __str__(self):
        return "Feuille N°"+ str(self.feuille_calcul.id) + " / N°"+ str(self.nEchantillon)








