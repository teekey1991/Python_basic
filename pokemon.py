class pokemon:
    def __init__(self, name, type, level):

        self.name = name
        self.type = type
        self.level = level
	
    def pokemon_type(self):
        return self.type

hitokage_pokemon = pokemon(name="ヒトカゲ", type="炎", level="49")
zenigame_pokemon = pokemon(name="ゼニガメ", type="水", level="50")


print(hitokage_pokemon.pokemon_type())
