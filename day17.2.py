import zombiedice 
class myZombie:
    def __init__(self,name):
        self.name=name
    def turn(self,gameState):
        diceRollResults= zombiedice.roll
        brains=0
        while diceRollResults is not None:
            brains+=diceRollResults['brains']
            if brains<2:
                diceRollResults=zombiedice.roll()
            else:
                break
zombies=(
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun',minShotguns=1),
    myZombie(name='My Zombie Bot')

)
zombiedice.runWebGui(zombies=zombies, numGames=1000)