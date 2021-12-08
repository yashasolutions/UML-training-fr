class Vehicule:
  def __init__(self, couleur, vmax, matricule, prix):
    self.couleur = couleur
    self.vmax = vmax
    self.matricule = matricule
    self.prix = prix
    self.vitesse = 0
    self.name = 'le vehicule'
  def infos(self):
    print(self.name + ' est de couleur ' + self.couleur)
    print('La vitesse max est de ' + str(self.vmax))
    print('Le matricule est ' + str(self.matricule))
    print('La vitesse actuelle est de ' + str(self.vitesse))
  def cnt(self):
    print('La vitesse actuelle est de ' + str(self.vitesse))
  def demarrer(self):
    print('On démarre !')
    self.vitesse = 10
  def accelerer(self, v):
    if self.vitesse != 0 :
        self.vitesse = self.vitesse + v
    if self.vitesse > self.vmax :
        self.vitesse = self.vmax
    print('On accélère à ' + str(self.vitesse))
  def freiner(self):
      self.vitesse = 0
      print('On freine !')

class Camion(Vehicule):
  def __init__(self, couleur, vmax, matricule, prix):
    super().__init__(couleur, vmax, matricule, prix)
    self.name = 'Le camion'


p1 = Vehicule("rouge", 400, 2837362112990, 1500)
c1 = Camion("vert", 100, 354156432, 2000)

p1.infos()
p1.demarrer()
p1.accelerer(500)
p1.freiner()

c1.infos()
c1.demarrer()
