import pandas as pd
import numpy as np

# Define fish types
fish_types = [
    "Salmon", "Tuna", "Clownfish", "Shark", 
    "Goldfish", "Catfish", "Trout", "Bass", 
    "Swordfish", "Snapper"
]

# Define water types
water_types = ["Freshwater", "Saltwater"]

# Define habitats
habitats = ["Reef", "Open Ocean", "River", "Lake", "Coastal"]

# Define diets
diets = ["Herbivore", "Carnivore", "Omnivore"]

# Define coloration
colorations = ["Silver", "Red", "Yellow", "Blue", "Green", "Striped", "Spotted"]

# Function to assign fish type based on logic
def assign_fish_type(length, weight, water_type, habitat, diet):
    if water_type == "Freshwater":
        if habitat in ["River", "Lake"]:
            if length < 50:
                return "Goldfish" if diet == "Herbivore" else "Catfish"
            else:
                return "Bass" if diet == "Carnivore" else "Trout"
        else:
            return "Catfish"
    else:  # Saltwater
        if habitat == "Reef":
            if length < 30:
                return "Clownfish" if coloration in ["Red", "Yellow"] else "Snapper"
            else:
                return "Snapper"
        elif habitat == "Open Ocean":
            if length > 100:
                return "Shark" if diet == "Carnivore" else "Swordfish"
            else:
                return "Tuna" if weight > 50 else "Salmon"
        else:
            return "Tuna"

# Generate sample dataset with variability
np.random.seed(42)

lengths = np.random.randint(20, 300, size=10000)  # Length in cm
weights = np.random.randint(1, 500, size=10000)   # Weight in kg
water_types_array = np.random.choice(water_types, size=10000, p=[0.4, 0.6])
habitats_array = np.random.choice(habitats, size=10000)
diets_array = np.random.choice(diets, size=10000)
colorations_array = np.random.choice(colorations, size=10000)

data = []
for i in range(10000):
    length = lengths[i]
    weight = weights[i]
    water_type = water_types_array[i]
    habitat = habitats_array[i]
    diet = diets_array[i]
    coloration = colorations_array[i]
    fish_type = assign_fish_type(length, weight, water_type, habitat, diet)
    
    data.append([length, weight, water_type, habitat, diet, coloration, fish_type])

# Create DataFrame
df = pd.DataFrame(data, columns=["Length", "Weight", "Water Type", "Habitat", "Diet", "Coloration", "Fish Type"])

# Save to Excel
df.to_excel("fish_classification_dataset.xlsx", index=False)
