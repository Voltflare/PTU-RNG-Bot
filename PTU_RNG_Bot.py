import random

class PTU_RNG_Bot:
    def __init__(self, types, type_matrix):
        self.types = types
        self.type_matrix = type_matrix
        self.type_indices = range(0, len(type_matrix))
        self.length_of_each_type = []
        for i in self.type_indices:
            self.length_of_each_type.append(len(type_matrix[i]))
            
    #Initializate initial rarity of 2 for all Pokemon        
    def initialize_common_rarities(self):
        for i in self.type_indices:
            #initialize rarities of common Pokemon (twice as often as other Pokemon)
            row = self.type_matrix[i]
            self.type_matrix[i] = self.type_matrix[i] + row
        
        
        
        
        
    #Creates common encounter within type_matrix pool at "pokemon_type" row - both inputs must be strings
    #Rarity of encounter is 1-4 (1 being the least common and 4 being the most common)
    def create_common_encounter(self, pokemon_name, pokemon_type, rarity):
    
        #validate input
        if (not isinstance(pokemon_name, str) or not isinstance(pokemon_type, str)):
            print("Pokemon inputs must be of type 'string.' Could not add.")
            return
        if (not isinstance(rarity, int)):
            print("Rarity must be of type 'integer.' Could not add.")
            return
    
        #check to see if duplicate Pokemon
        if pokemon_name in self.type_matrix:
            print("Pokemon already exists in matrix. Could not add.")
            return
    
        #Find index for Pokemon in the matrix
        common_mon = pokemon_name.lower().capitalize() #safe for SquIrTle, squirtle, SQUIRTLE, etc
        common_mon_type = None
        for key, value in self.types.items():
            if key == pokemon_type.lower().capitalize(): #safe for type, tYpe, Type, etc
                common_mon_type = value
  
        #if invalid bounds, return (as we cannot work on the matrix)
        if (common_mon_type >= len(self.type_matrix) or common_mon_type == None):
            print("Invalid Matrix Operation. Could not add.")
            return
        else:
            #Check rarity
            if rarity > 4:
                rarity = 4
            else:
                for i in range(0, rarity):
                    #Index row and add Pokemon- rare = add only once
                    self.type_matrix[common_mon_type].append(common_mon)
            
            #Sort by alphabetical value after adding mon to make it look pretty            
            self.type_matrix[common_mon_type].sort()  
            print("Successfully added {} to matrix row {}.".format(pokemon_name, pokemon_type))
            
            
            
    #Creates rare encounter within type_matrix pool at "pokemon_type" row- both inputs must be strings
    #Rarity is locked to "1" for rare encounters
    def create_rare_encounter(self, pokemon_name, pokemon_type):
    
        #validate input
        if (not isinstance(pokemon_name, str) or not isinstance(pokemon_type, str)):
            print("Inputs must be of type 'string.' Could not add.")
            return
    
        #check to see if duplicate Pokemon
        if pokemon_name in self.type_matrix:
            print("Pokemon already exists in matrix. Could not add.")
            return
    
        #Find index for Pokemon in the matrix
        rare_mon = pokemon_name.lower().capitalize() #safe for SquIrTle, squirtle, SQUIRTLE, etc
        rare_mon_type = None
        for key, value in self.types.items():
            if key == pokemon_type.lower().capitalize(): #safe for type, tYpe, Type, etc
                rare_mon_type = value
  
        #if invalid bounds, return (as we cannot work on the matrix)
        if (rare_mon_type >= len(self.type_matrix) or rare_mon_type == None):
            print("Invalid Matrix Operation. Could not add.")
            return
        else:
            #Index row and add Pokemon- rare = add only once
            self.type_matrix[rare_mon_type].append(rare_mon)
            #Sort by alphabetical value after adding mon to make it look pretty
            self.type_matrix[rare_mon_type].sort() 
            print("Successfully added {} to matrix row {}.".format(pokemon_name, pokemon_type))
            
            
            
    #Generates random Pokemon teams of specified "num_mons" Picks from rows and columns of type_matrix
    def generate_team(self, num_mons):
        if (not isinstance(num_mons, int)):
            print("Input is not a valid number of Pokemon")
            return
        
        team = []
        for mon in range(0, num_mons):
            #generate num_mons mons
            randtype = random.choice(self.type_indices)
            randmon = random.choice(range(0, self.length_of_each_type[randtype])) #prevents array overflow
            generated_mon = self.type_matrix[randtype][randmon]
            team.append(generated_mon)
        print("Generated Team: ", team)
        
    def print_type_matrix(self):
        #pair of type_of_mon, row is like ("Dark", 0), etc
        print("---- Encounter Table: ----")
        print("--------------------------")
        for type_of_mon, row in self.types.items():
            print("--------------------------")
            print(type_of_mon,": ", self.type_matrix[row])
        print("--------------------------")
        