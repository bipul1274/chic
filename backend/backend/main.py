from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import UserProfile, OutfitRecommendation
from .stylist_engine import get_recommendation

app = FastAPI()

# --- CORS Middleware ---
# This allows our React frontend to communicate with this backend
# IMPORTANT: Add your Vercel frontend URL here after you deploy it.
origins = [
    "http://localhost:3000",
    "https://YOUR_VERCEL_URL_HERE", # <-- IMPORTANT: Change this!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chic AI Stylist API"}

@app.post("/recommend", response_model=OutfitRecommendation)
def recommend_outfit(profile: UserProfile):
    """
    Takes user profile and returns a personalized outfit recommendation.
    """
    recommendation = get_recommendation(profile)
    return recommendation
