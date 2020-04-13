class Hero:
    
    ### Construtor  ##################################
    def __init__(self, name, voc, sex):
        self.name = name
        self.voc = voc
        self.sex = sex
        self.lvl = 1
        self.life = 10
        self.mana = 5
        self.p = False

        print('Character', self.name, 'created.')
        print()


    ### Sets  ##################################
    def setLvl(self, lvl):
        self.lvl = lvl

    def setName(self, name):
        self.name = name

    def setVoc(self, voc):
        self.voc = voc

    def setSex(self, sex):
        self.sex = sex

    def setLife(self, life):
        self.life = life

    def setMana(self, mana):
        self.mana = mana

    ##################################

    ### Gets  ##################################
    def getName(self):
        return self.name

    def getLvl(self):
        return self.lvl

    def getVoc(self):
        return self.voc

    def getSex(self):
        return self.sex

    def getLife(self):
        return self.life

    def getMana(self):
        return self.mana
    ##################################



    ### Metodos
    def printHero(self):
        print('Name:', self.name)
        print('Level:', self.lvl)
        print('Vocation:', self.voc)
        print('Sex:', self.sex)
        print('Life: {:.1f}'.format(self.life))
        print('Mana:{:.1f}'.format(self.mana))
        print()

    def upLvl(self):
        self.lvl += 1
        self.life += 0.5 * self.lvl
        self.mana += 0.3 * self.lvl
        print(self.name, 'went up one level')
        print('Your level is now', self.lvl )
        print('Your life is now {:.1f}'.format(self.life))
        print('Your mana is now {:.1f}'.format(self.mana))
        print()

    def downLvl(self):
        if self.lvl > 1:
            self.lvl -= 1
            self.life -= 0.5 * self.lvl
            self.mana -= 0.3 * self.lvl
            print(self.name, 'loss one level')
            print('Your level is now', self.lvl )
            print('Your life is now {:.1f}'.format(self.life))
            print('Your mana is now {:.1f}'.format(self.mana))
            print()
        else:
            print('Minimum level 1')
            print()

    def promotion(self):
            print(self.name, 'received a promotion!')
            if self.voc == 'Knight':
                self.voc ='Elite Knight'
                print(self.name, 'is now a', self.voc)
            elif self.voc == 'Druid': 
                self.voc = 'Elder Druid'
                print(self.name, 'is now a', self.voc)
            elif self.voc == 'Sorcerer': 
                self.voc = 'Master Sorcerer'               
                print(self.name, 'is now a', self.voc)
            elif self.voc == 'Paladin': 
                self.voc = 'Royal Paladin'
                print(self.name, 'is now a', self.voc)
            else:
                self.voc = 'Unknow'
                print(self.name, 'is now a', self.voc)
            print()
            self.p = True