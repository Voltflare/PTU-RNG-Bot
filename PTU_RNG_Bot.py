import random

class PTU_RNG_Bot:
    def __init__(self, types, encounter_table):
        self.types = types
        for mon_type in types:
            mon_type = mon_type.lower().capitalize() #Protects against "Water" vs "water" vs "wAtEr" mismatches
        self.encounter_table = encounter_table
        self.type_indices = range(0, len(encounter_table))
        self.length_of_each_type = []
        for i in self.type_indices:
            self.length_of_each_type.append(len(encounter_table[i]))
        self.initialize_common_rarities()
            
    #Initializate initial rarity of 2 for all Pokemon        
    def initialize_common_rarities(self):
        for i in self.type_indices:
            #initialize rarities of common Pokemon (twice as often as other Pokemon)
            row = self.encounter_table[i]
            self.encounter_table[i] = self.encounter_table[i] + row
        
        
        
        
        
    #Creates common encounter within encounter_table pool at "pokemon_type" row - both inputs must be strings
    #Rarity of encounter is 1-4 (1 being the least common and 4 being the most common)
    def create_common_encounter(self, pokemon_name, pokemon_type, rarity):
    
        #validate input
        if (not isinstance(pokemon_name, str) or not isinstance(pokemon_type, str)):
            print("Pokemon inputs must be of type 'string.' Could not add.")
            return
        if (not isinstance(rarity, int)):
            print("Rarity must be of type 'integer.' Could not add.")
            return
    
        #check to see if duplicate Pokemon- no longer necessary because removal exists
        #if pokemon_name in self.encounter_table:
            #print("Pokemon already exists in table. Could not add.")
            #return
    
        #Find index for Pokemon in the table
        common_mon = pokemon_name.lower().capitalize() #safe for SquIrTle, squirtle, SQUIRTLE, etc- 
                                                       #always results in "Squirtle"
        common_mon_index = None
        common_mon_type = None
        for key, value in self.types.items():
            if key == pokemon_type.lower().capitalize(): #safe for type, tYpe, Type, etc
                common_mon_type = key
                common_mon_index = value
  
        #if invalid bounds, return (as we cannot work on the table)
        if (common_mon_index == None or common_mon_index >= len(self.encounter_table)):
            print("Invalid Table Operation. Could not add.")
            return
        else:
            #Check rarity
            if rarity > 4:
                rarity = 4
            else:
                for i in range(0, rarity):
                    #Index row and add Pokemon- rare = add only once
                    self.encounter_table[common_mon_index].append(common_mon)
            
            #Sort by alphabetical value after adding mon to make it look pretty            
            self.encounter_table[common_mon_index].sort()  
            print("Successfully added {} (Rarity {}) to table row {}.".format(common_mon, rarity, common_mon_type))
            
            
            
    #Creates rare encounter within encounter_table pool at "pokemon_type" row- both inputs must be strings
    #Rarity is locked to "1" for rare encounters
    def create_rare_encounter(self, pokemon_name, pokemon_type):
    
        #validate input
        if (not isinstance(pokemon_name, str) or not isinstance(pokemon_type, str)):
            print("Inputs must be of type 'string.' Could not add.")
            return
    
        #check to see if duplicate Pokemon- deprecated because remove functionality added
        #if pokemon_name in self.encounter_table:
            #print("Pokemon already exists in table. Could not add.")
            #return
    
        #Find index for Pokemon in the table
        rare_mon = pokemon_name.lower().capitalize() #safe for SquIrTle, squirtle, SQUIRTLE, etc
        rare_mon_index = None
        rare_mon_type = None
        for key, value in self.types.items():
            if key == pokemon_type.lower().capitalize(): #safe for type, tYpe, Type, etc
                rare_mon_index = value
                rare_mon_type = key
  
        #if invalid bounds, return (as we cannot work on the table)
        if (rare_mon_index == None or rare_mon_index >= len(self.encounter_table)):
            print("Invalid Table Operation. Could not add.")
            return
        else:
            #Index row and add Pokemon- rare = add only once
            self.encounter_table[rare_mon_index].append(rare_mon)
            #Sort by alphabetical value after adding mon to make it look pretty
            self.encounter_table[rare_mon_index].sort() 
            print("Successfully added rare {} to table row {}.".format(rare_mon, rare_mon_type))
            
    #Removes "pokemon_to_remove" num_to_remove times from the encounter table. If the table contains less occurrences of
    #pokemon_to_remove than the specified num_to_remove, all occurrences are removed.
    def remove_encounter(self, pokemon_to_remove, type_belongs_to, num_to_remove):
        #validate input
        if (not isinstance(pokemon_to_remove, str) or not isinstance(type_belongs_to, str) or not isinstance(num_to_remove, int)):
            print("Inputs must be of type 'string', 'string', 'int'. Could not remove.")
            return
        if (num_to_remove <= 0):
            print("Number of entries to remove must be a positive number greater than zero.")
            return
        
        #standardize input (ie: SQUIRTLE, Squirtle, SqUiRTlE, etc will all work properly, as long as it is spelled correctly)
        pokemon_to_remove = pokemon_to_remove.lower().capitalize()
        type_belongs_to = type_belongs_to.lower().capitalize()
        
        #check to see whether the Pokemon and type actually exists in the table
        mon_exists = False
        for row in self.encounter_table:
            if (pokemon_to_remove in row):
                mon_exists = True
        if (not mon_exists):
            print(pokemon_to_remove, "does not exist in the encounter table in any row. Could not remove.")
            return
        
        if type_belongs_to not in self.types:
            print(type_belongs_to,"is not a valid Pokemon Type within the encounter table. Could not remove.")
            return
            
                        
        #Find index for Pokemon in the table
        table_index = None
        for key, value in self.types.items():
            if key == type_belongs_to:
                table_index = value    
            
        
        #look through indexed row for Pokemon "num_to_remove" times
        num_removed = 0 #variable to track how many were actually removed, to be printed 
                        #(for the edge case of the table containing less than num_to_remove)
        for i in range(0, num_to_remove):
            removed_true = False #boolean for checking removal on each pass through the table
            #remove Pokemon from table row if it exists there
            if (pokemon_to_remove in self.encounter_table[table_index]):
                self.encounter_table[table_index].remove(pokemon_to_remove)
                num_removed = num_removed + 1
                removed_true = True
            if not removed_true: #if we didn't remove anything in this pass, there are no more entries left to remove
                                 #so we are done removing
                if num_removed == 0:
                    print(pokemon_to_remove,"does not exist within row", type_belongs_to,"of the encounter table.", 
                          "Could not remove.")
                    return
                elif num_removed == 1:
                    print("Successfully removed", num_removed, "instance of", pokemon_to_remove, ".")
                else:
                    print("Successfully removed", num_removed, "instances of", pokemon_to_remove, ".")
                print("There are no more instances of", pokemon_to_remove, "left in the table.")
                return
    
        #If we get to the end without running out of Pokemon to remove, just print the number that were removed
        if num_removed == 1:
            print("Successfully removed", num_removed, "instance of", pokemon_to_remove, "from table row",type_belongs_to,".")
        else:
            print("Successfully removed", num_removed, "instances of", pokemon_to_remove, "from row",type_belongs_to,".")
        return
                
            
            
    #Generates random Pokemon teams of specified "num_mons" Picks from rows and columns of encounter_table
    def generate_team(self, num_mons):
        if (not isinstance(num_mons, int)):
            print("Input is not a valid number of Pokemon.")
            return
        
        team = []
        for mon in range(0, num_mons):
            #generate num_mons mons
            randtype = random.choice(self.type_indices)
            randmon = random.choice(range(0, self.length_of_each_type[randtype])) #prevents array overflow
            generated_mon = self.encounter_table[randtype][randmon]
            team.append(generated_mon)
        print("Generated Team: ", team)
        
    #Generates random Monotype Pokemon teams of specified "num_mons" of a given "type_of_mon"
    def generate_monotype_team(self, type_of_mon, num_mons):
        if type_of_mon not in self.types.keys():
            print("Type is not present in table.")
            return
        elif (not isinstance(num_mons, int)):
            print("Input is not a valid number of Pokemon.")
            return
        else:
            #working match
            team = []
            for mon in range(0, num_mons):
                #generate num_mons mons
                type_of = list(self.types.keys()).index(type_of_mon)
                randmon = random.choice(range(0, self.length_of_each_type[type_of]))
                generated_mon = self.encounter_table[type_of][randmon]
                team.append(generated_mon)
            print("Generated Team: ", team)
        
    def print_encounter_table(self):
        #pair of type_of_mon, row is like ("Dark", 0), etc
        print("---- Encounter Table: ----")
        print("--------------------------")
        for type_of_mon, row in self.types.items():
            print("--------------------------")
            printable_row = sorted(self.encounter_table[row])
            print(type_of_mon,": ", printable_row)
        print("--------------------------")
        