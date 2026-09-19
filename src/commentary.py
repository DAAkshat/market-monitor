import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_market_commentary(sector_ranking, regime_today, corr_matrix):
    best_sector = sector_ranking.iloc[0]
    worst_sector = sector_ranking.iloc[-1]

    prompt = f"""
    You are a financial analyst writing a short daily market brief.
    Data:
    - Best performing sector (20-day return): {best_sector.name}, sector: {best_sector['sector']}, return: {best_sector['returns_n']:.2%}
    - Worst performing sector (20-day return): {worst_sector.name}, sector: {worst_sector['sector']}, return: {worst_sector['returns_n']:.2%}
    - Current market regime (VIX-based): {regime_today}
    Write a concise, 3-sentence market commentary in a professional analyst tone.
    Do not repeat the raw numbers mechanically — synthesize them into an insight.
"""
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text