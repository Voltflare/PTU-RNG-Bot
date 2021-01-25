# README

<u>PTU RNG Bot:</u>

This program has two main parameters: the "Types" to be randomly picked from (of dimension dim_type), and a Type Matrix (of dimension dim_type by number_mons_per_type). The number of Pokemon in each Type/row does not need to be the same- the classdeals with that automatically.

* <b> Types: </b> Dictionary with key of "Type" and value of zero-indexed integer (ie: type number one is "Dark": 0).*

* <b> Encounter Table: </b> List of Lists whose first dimension matches the number of entries in the types dictionary. Each entry in the matrix is a Pokemon name. Each Pokemon's name should be entered only <b> once </b> in the array for an equal chance to encounter each Pokemon. ~~Duplicate checking will only be done by the called methods (and not on the initial matrix)~~ Duplicate checking has since been deprecated.*

**It is important to note that the number of rows in the Encounter Table and the number of types in the Types dictionary MUST match up.**

Examples of these two parameters:

types = {
    "Dark": 0, 
    "Fairy": 1, 
    "Grass": 2, 
    "Fire": 3, 
    "Water": 4, 
    "Electric": 5
}

encounter_table = [
["Honchkrow", "Mightyena", "Pawniard", "Shiftry", "Sneasel", "Spiritomb"], 
["Azumarill", "Clefairy", "Granbull", "Mawile", "Sylveon", "Togetic"], 
["Exeggcute", "Gloom", "Grovyle", "Maractus", "Tangela", "Tropius"],
["Charmeleon", "Fletchinder", "Ninetales", "Vulpix"], 
["Chinchou", "Poliwhirl", "Psyduck", "Staryu", "Vaporeon"],
["Elecktrike", "Emolga", "Luxio", "Manectric", "Rotom", "Stunfisk"] ]

- Encounters
    <i> Encounters are picked randomly from the bot's internal encounter table based on each Pokemon's internal <b> "rarity" value </b>, with higher rarity values being more often encountered. 
    - <b> Rarity: </b> The rarity is implicitly defined as the number of times that a Pokemon's name appears within a given row of the encounter table. *Note that Pokemon can have multiple rarities corresponding to two different rows of the table if they have multiple types* (for instance, an Emolga (Electric/Flying) could have Rarity 3 in a Flying row of ["Emolga", "Emolga", "Emolga", "Pidgey", "Spearow"] but only a Rarity 1 in an Electric row of ["Pikachu", "Pichu", "Raichu", "Emolga].</i>

**********************************************************************************************

- Methods
    - <i> initialize_common_rarities(): </i> This method will initialize the rarity of all Pokemon in the encounter table as "common" with a rarity value of 2. If Pokemon already exist within the table, the combined rarity value will instead be doubled (ie: two entries of "Raichu" will cause Raichu to now have a rarity of 4." Rarity is discussed above.
        - <i> Note: This method is called implicitly upon construction and does not need to be called again unless desired. <i/>
        - <b> <i> Parameters: </i> </b>
            - None
    - <i> create_common_encounter(pokemon_name, pokemon_type, rarity): </i> This method will create a "common" encounter with a given rarity. The higher the "rarity" value, the more times the encounter will be entered into the encounter table (for instance, create_common_encounter("Bulbasaur", "Grass", 2) will create two entries of "Bulbasaur" in the "Grass" row of the table.
        - <b> <i> Parameters: </i> </b>
            - <b> pokemon_name: </b> the name of the Pokemon to be added to the table. The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right!
            - <b> pokemon_type: </b> the type of the Pokemon (where it will be added in the encounter table). The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right! It will generate an error if the Type that you specified does not exist.
            - <b> rarity: </b> the relative rarity of the Pokemon. The higher the rarity, the more times the Pokemon will be entered into the Encounter Table.
        - <b> <i> Sample Output: </i> </b> `Successfully added Bulbasaur (Rarity 2) to table row Grass.`
    - <i> create_rare_encounter(pokemon_name, pokemon_type): </i> This method will create a "rare" encounter with a rarity value of 1 (the most uncommon). 
        - <b> <i> Parameters: </i> </b>
            - <b> pokemon_name: </b> the name of the Pokemon to be added to the table. The program does not check if you spelled it correctly (but it does internally account for case differences), so please make sure you have spelled it right!
            - <b> pokemon_type: </b> the type of the Pokemon (where it will be added in the Encounter Table). The program does not check if you spelled it correctly (but it does check for cases), so please make sure you have spelled it right! It will return an error message if the type that you specified does not exist.
        - <b> <i> Sample Output: </i> </b> `Successfully added rare Greninja to table row Dark.`
    - <i> remove_encounter(pokemon_to_remove, num_to_remove): </i> This method will remove a specified number entries of a specific Pokemon from the table. If the number specified is more than the number of entries that exist within the table, all entries will be removed.
        - <b> <i> Parameters: </i> </b>
            - <b> pokemon_to_remove: </b> the name of the Pokemon to be removed from the table. The program does not check if you spelled it correctly (but it does internally account for case differences), so please make sure you have spelled it right (or if you <i> did </i> make a spelling mistake when adding a Pokemon, use that same spelling mistake to remove it).
            - <b> num_to_remove: </b> the number of entries of "pokemon_to_remove" to remove from the table. The program will not remove anything from the table if zero or a negative number is inputted.
        - <b> <i> Sample Output: </i> </b> `Successfully removed 2 instances of Audino from table row Normal.`
    - <i> generate_team(num_mons): </i> This method generates a random team for a Trainer based on the contained encounter table.
        - <b> <i> Parameters: </i> </b>
            - <b> num_mons: </b> the number of Pokemon to be generated. This generation method picks randomly from any type listed in the encounter table at an equal rate (ie: it is equally likely to pick an Electric or a Flying Pokemon, if they are both valid type rows).
        - <b> <i> Sample Output: </i> </b> `Generated Team:  ['Manectric', 'Clefairy', 'Ninetales', 'Vulpix']`
    - <i> generate_monotype_team(type_of_mon, num_mons): </i> This method generates a random team of Pokemon for a Trainer based on the contained encounter table. Only the specified type will be considered for generation.
        - <b> <i> Parameters: </i> </b>
            - <b> type_of_mon: </b> the type of Pokemon to be generated. If the specified type does not exist within the encounter table, the program will return an error message.
            - <b> num_mons: </b> the number of Pokemon to be generated. This generation method picks only from the specified type.
        - <b> <i> Sample Output </i> </b> `Generated Team: ['Manectric', 'Emolga', 'Pikachu']`
    - <i> print_encounter_table(): </i> This method prints out the current state of the encounter table in an easy-to-read format.
        - <b> <i> Parameters: </i> </b>
            - None
        - <b> <i> Sample Output: (One Row) </i> </b>  `Fairy: ["Azumarill", "Clefairy", "Granbull", "Mawile", "Sylveon", "Togetic"]`
    - <i> print_by_rarity(): </i> This method prints out the current state of the encounter table by rarity value, placing the highest rarities first and sorting by descending Pokemon name. Can be useful for those that want to intentionally reward certain encounters based on a dice roll.
        - <b> <i> Parameters: </i> </b>
            - None
        - <b> <i> Sample Output: (One Row) </i> </b> `Fairy :  [(2, 'Togetic'), (2, 'Sylveon'), (2, 'Granbull'), (2, 'Comfey'), (2, 'Clefairy'), (2, 'Azumarill'), (2, 'Aromatisse'), (1, 'Clefable')]`
                
***********************

<b> How to use: </b>
- `rng = PTU_RNG_Bot(types, encounter_table)` instantiates the bot with Types of "types" and Encounter Table of "encounter_table".
- `rng.initialize_common_rarities()` initializes rarities of all Pokemon currently within the encounter table as "common" (Rarity 2).
- `rng.create_common_encounter("Bulbasaur", "Grass", 2)` inserts common Pokemon "Bulbasaur" to table row "Grass" with a Rarity of 2
- `rng.create_rare_encounter("Greninja", "Dark")` inserts rare Pokemon "Greninja" to table row "Dark".
- `rng.remove_encounter("Bibarel", "Water", 2)` removes up to 2 instances of Bibarel from the Water row of the encounter table, provided Water is a Type specified within the encounter table and Bibarel exists within it.
- `rng.generate_team(4)` generates a random team of 4 Pokemon.
- `rng.generate_monotype_team("Water", 4)` generates a random team of 4 Water-Type Pokemon, if Water is a Type specified with the encounter table.
- `rng.print_encounter_table()` and `rng.print_by_rarity()` print out the current encounter table.