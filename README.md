# README

<u>PTU RNG Bot:</u>

This program has two main parameters: the "Types" to be randomly picked from (of dimension dim_type), and a Type Matrix (of dimension dim_type by number_mons_per_type). The number of Pokemon in each Type/row does not need to be the same- the classdeals with that automatically.

* <b> Types: </b> Dictionary with key of "Type" and value of zero-indexed integer (ie: type number one is "Dark": 0) *

* <b> Type Matrix: </b> List of Lists whose first dimension matches the number of entries in the types dictionary. Each entry in the matrix is a Pokemon name. Each Pokemon's name should be entered only <b> once </b> in the array for an equal chance to encounter each Pokemon. Duplicate checking will only be done by the called methods (and not on the initial matrix) *

Examples of these two parameters:

types = {
    "Dark": 0, 
    "Fairy": 1, 
    "Grass": 2, 
    "Fire": 3, 
    "Water": 4, 
    "Electric": 5
}

type_matrix = [
["Honchkrow", "Mightyena", "Pawniard", "Shiftry", "Sneasel", "Spiritomb"], 
["Azumarill", "Clefairy", "Granbull", "Mawile", "Sylveon", "Togetic"], 
["Exeggcute", "Gloom", "Grovyle", "Maractus", "Tangela", "Tropius"],
["Charmeleon", "Fletchinder", "Ninetales", "Vulpix"], 
["Chinchou", "Poliwhirl", "Psyduck", "Staryu", "Vaporeon"],
["Elecktrike", "Emolga", "Luxio", "Manectric", "Rotom", "Stunfisk"] ]


**********************************************************************************************

- Methods
    - <i> initialize_common_rarities(type_matrix): </i> This method will initialize the rarity of all Pokemon in the type matrix as "common" with a rarity of 2. Rarity is further discussed below.
        - <b> <i> Parameters: </i> </b>
            - <b> type_matrix: </b> the Type Matrix that was created as an encounter table. 
    - <i> create_common_encounter(pokemon_name, pokemon_type, rarity): </i> This method will create a "common" encounter with a given rarity. The higher the "rarity" value, the more times the encounter will be entered into the Type Matrix (for instance, create_common_encounter("Bulbasaur", "Grass", 2) will create two entries of "Bulbasaur" in the "Grass" row of the matrix.
        - <b> <i> Parameters: </i> </b>
            - <b> pokemon_name: </b> the name of the Pokemon to be added to the table. The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right!
            - <b> pokemon_type: </b> the type of the Pokemon (where it will be added in the Type Matrix). The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right! It will generate an error if the Type that you specified does not exist.
                - *note:* Types are singly indexed in this, so you could enter Bulbasaur into either Grass or Poison (but not both)
            - <b> rarity: </b> the relative rarity of the Pokemon. The higher the rarity, the more times the Pokemon will be entered into the Type Matrix.
        - <b> <i> Sample Output: </i> </b> `Successfully added Bulbasaur (Rarity 2) to matrix row Grass.`
    - <i> create_rare_encounter(pokemon_name, pokemon_type): </i> This method will create a "rare" encounter with a rarity of 1 (the most uncommon). 
        - <b> <i> Parameters: </i> </b>
            - <b> pokemon_name: </b> the name of the Pokemon to be added to the table. The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right!
            - <b> pokemon_type: </b> the type of the Pokemon (where it will be added in the Type Matrix). The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right! It will generate an error if the Type that you specified does not exist.
                - *note:* Types are singly indexed in this, so you could enter Bulbasaur into either Grass or Poison (but not both)
        - <b> <i> Sample Output: </i> </b> `Successfully added rare Greninja to matrix row Dark.`
    - <i> generate_team(): </i> This method generates a random team for a Trainer based on the contained type matrix.
        - <b> <i> Parameters: </i> </b>
            - None
        - <b> <i> Sample Output: </i> </b> `Generated Team:  ['Manectric', 'Clefairy', 'Ninetales', 'Vulpix']`
    - <i> print_type_matrix(): </i> This method prints out the type matrix by type for ease of viewing.
        - <b> <i> Parameters: </i> </b>
        - <b> <i> Sample Output: (One Row) </i> </b>  `Fairy: ["Azumarill", "Clefairy", "Granbull", "Mawile", "Sylveon", "Togetic"]`
            - None
                
***********************

<b> How to use: </b>
- `rng = PTU_RNG_Bot(types, type_matrix)` instantiates the bot with "types" and "type_matrix"
- `rng.initialize_common_rarities()` initializes rarities of all Pokemon as "common"
- `rng.create_common_encounter("Bulbasaur", "Grass", 2)` inserts common Pokemon "Bulbasaur" to matrix row "Grass"
- `rng.create_rare_encounter("Greninja", "Dark")` inserts rare Pokemon "Greninja" to matrix row "Dark"
- `rng.generate_team(4)` generates a random team of 4 Pokemon
- `rng.print_type_matrix()` prints out the current Type Matrix