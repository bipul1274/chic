from .models import UserProfile, ClothingItem, OutfitRecommendation

# --- Mock Clothing Database ---
# In a real app, this would come from a database or a fashion API
CLOTHING_DB = {
    "tops": [
        ClothingItem(name="Classic White T-Shirt", category="Top", image_url="https://i.imgur.com/3FNr6d5.jpg"),
        ClothingItem(name="Silk Blouse", category="Top", image_url="https://i.imgur.com/sEy4a2z.jpg"),
    ],
    "bottoms": [
        ClothingItem(name="Dark Wash Straight-Leg Jeans", category="Bottom", image_url="https://i.imgur.com/S9sJ3sW.jpg"),
        ClothingItem(name="A-Line Skirt", category="Bottom", image_url="https://i.imgur.com/uUP9g7n.jpg"),
    ],
    "outerwear": [
        ClothingItem(name="Chunky Knit Sweater", category="Outerwear", image_url="https://i.imgur.com/9lqYn2d.jpg"),
        ClothingItem(name="Tailored Blazer", category="Outerwear", image_url="https://i.imgur.com/JAd2Ckt.jpg"),
    ]
}

def get_recommendation(profile: UserProfile) -> OutfitRecommendation:
    """
    A simple rule-based engine for MVP.
    This logic can be replaced by a sophisticated ML model later.
    """
    items = []
    
    # Example Rule 1: Winter, Casual for Pear body type
    if profile.season == 'winter' and profile.style_preference == 'casual' and profile.body_type == 'pear':
        items.append(CLOTHING_DB['outerwear'][0]) # Chunky Sweater
        items.append(CLOTHING_DB['bottoms'][0])   # Dark Jeans
        return OutfitRecommendation(outfit_name="Cozy Winter Casual", items=items)

    # Example Rule 2: Summer, Formal for Hourglass body type
    if profile.season == 'summer' and profile.style_preference == 'formal':
        items.append(CLOTHING_DB['tops'][1])      # Silk Blouse
        items.append(CLOTHING_DB['bottoms'][1])   # A-Line Skirt
        return OutfitRecommendation(outfit_name="Elegant Summer Evening", items=items)
        
    # Default Fallback Recommendation
    items.append(CLOTHING_DB['tops'][0])
    items.append(CLOTHING_DB['bottoms'][0])
    return OutfitRecommendation(outfit_name="Everyday Classic", items=items)
