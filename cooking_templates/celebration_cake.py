import discord
from cooking_templates import base
import recipes

class Party(base.Party):

    def __init__(self) -> None:

        super().__init__()

        # constants
        self.STARTER = "Starter"
        self.LEAFER = "Sweet Leaf"
        self.BATTER = "Cake Batter"
        self.FROSTER = "Frosting"
        self.JAMMER = "Jammer"
        self.BAKER = "Baker"

        self.recipe = recipes.CELEBRATION_CAKE

        # roles to be fulfilled
        self.roles={
            self.STARTER : [self.OPEN],
            self.LEAFER: [self.OPEN, self.OPEN, self.OPEN, self.OPEN],
            self.BATTER: [self.OPEN, self.OPEN, self.OPEN],
            self.FROSTER: [self.OPEN], 
            self.JAMMER: [self.OPEN, self.OPEN, self.OPEN],
            self.BAKER: [self.OPEN, self.OPEN, self.OPEN]
        }
        # options to display in dropdown menu
        self.options=[
                discord.SelectOption(label = self.STARTER, description="Blueberries: Prep Station"),
                discord.SelectOption(label = self.LEAFER, description="Sweet Leaf: Mixing Station"),
                discord.SelectOption(label = self.BATTER, description="Egg, Flour, Butter: Mixing Station"),
                discord.SelectOption(label = self.FROSTER, description="Butter, Milk: Prep Station"),
                discord.SelectOption(label = self.JAMMER, description="Jam: Prep Station"),
                discord.SelectOption(label = self.BAKER, description="Oven"),
            ]
        
        self.update_post()

    def update_post(self) -> None:
        self.post_template = f"""# [Celebration Cake](https://palia.wiki.gg/wiki/Celebration_Cake)
(900Focus Base) 5m ( 258 - 314 Gold Base)
------------------------------
15 People Possible Cooking
-----------------------------
4 Prep Station
8 Mix Stations
3 Ovens
-----------------------------

**Starter** (Prep)
Blueberries (Farm only)
{self.roles[self.STARTER][0]}

**Sweet Leaf** (Mix)
(Forage only)
{self.roles[self.LEAFER][0]}
{self.roles[self.LEAFER][1]}
{self.roles[self.LEAFER][2]}
{self.roles[self.LEAFER][3]}

**Cake Batter** (Mix) 5,250g
(egg 24g each / flour 10g each / butter 80g each)
{self.roles[self.BATTER][0]}
{self.roles[self.BATTER][1]}
{self.roles[self.BATTER][2]}

**Frosting** (Prep) 7,000g
(butter 80g each / milk 60g each)
{self.roles[self.FROSTER][0]}

**Jammer** (Prep)
(Processed only)
{self.roles[self.JAMMER][0]}
{self.roles[self.JAMMER][1]}
{self.roles[self.JAMMER][2]}

**Baker** (Oven)
{self.roles[self.BAKER][0]}
{self.roles[self.BAKER][1]}
{self.roles[self.BAKER][2]}
-----------------------------"""