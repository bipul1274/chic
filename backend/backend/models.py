from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    height_cm: int
    weight_kg: int
    body_type: str  # e.g., 'rectangle', 'pear', 'hourglass', 'apple', 'inverted_triangle'
    style_preference: str  # e.g., 'casual', 'formal', 'streetwear'
    season: str # e.g., 'spring', 'summer', 'autumn', 'winter'

class ClothingItem(BaseModel):
    name: str
    category: str # e.g., 'Top', 'Bottom', 'Outerwear', 'Shoes'
    image_url: str 
    buy_link: Optional[str] = None # For "Buy Now" feature later

class OutfitRecommendation(BaseModel):
    outfit_name: str
    items: List[ClothingItem]
