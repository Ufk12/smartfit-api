"""
SmartFit Size Database
"""

EU_SIZES = [36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5, 40, 40.5,
            41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5, 45, 45.5,
            46, 46.5, 47, 47.5, 48, 48.5, 49, 49.5, 50]

EU_TO_CM = {
    36: 22.5, 36.5: 23.0, 37: 23.5, 37.5: 23.8,
    38: 24.0, 38.5: 24.5, 39: 25.0, 39.5: 25.2,
    40: 25.5, 40.5: 26.0, 41: 26.5, 41.5: 26.8,
    42: 27.0, 42.5: 27.3, 43: 27.5, 43.5: 27.8,
    44: 28.0, 44.5: 28.3, 45: 28.5, 45.5: 28.8,
    46: 29.0, 46.5: 29.3, 47: 29.5, 47.5: 29.8,
    48: 30.0, 48.5: 30.3, 49: 30.5, 49.5: 30.8,
    50: 31.0,
}

EU_TO_US_MEN = {
    36: 4, 36.5: 4.5, 37: 5, 37.5: 5.5,
    38: 5.5, 38.5: 6, 39: 6, 39.5: 6.5,
    40: 7, 40.5: 7.5, 41: 8, 41.5: 8.5,
    42: 9, 42.5: 9.5, 43: 10, 43.5: 10.5,
    44: 11, 44.5: 11.5, 45: 12, 45.5: 12.5,
    46: 13, 46.5: 13.5, 47: 14, 47.5: 14.5,
    48: 15, 48.5: 15.5, 49: 16, 49.5: 16.5,
    50: 17,
}

US_MEN_TO_EU = {v: k for k, v in EU_TO_US_MEN.items()}
EU_TO_US_WOMEN = {k: v + 1.5 for k, v in EU_TO_US_MEN.items()}
US_WOMEN_TO_EU = {v: k for k, v in EU_TO_US_WOMEN.items()}
EU_TO_UK_MEN = {k: v - 1 for k, v in EU_TO_US_MEN.items()}
UK_MEN_TO_EU = {v: k for k, v in EU_TO_UK_MEN.items()}

BRAND_OFFSETS = {
    "nike": 0.0, "jordan": 0.0, "adidas": 0.0, "new_balance": 0.0,
    "hoka": 0.0, "brooks": 0.0, "asics": 0.0, "saucony": 0.0,
    "mizuno": 0.0, "on_running": 0.0,
    "puma": +0.5, "reebok": +0.5, "under_armour": +0.5, "fila": +0.5,
    "vans": 0.0, "converse": 0.0,
    "timberland": -0.5, "ugg": -0.5,
    "gucci": +0.5, "balenciaga": +0.5, "golden_goose": 0.0, "common_projects": 0.0,
    "salomon": 0.0, "merrell": 0.0, "keen": -0.5, "columbia": 0.0,
    "la_sportiva": +0.5, "scarpa": +0.5,
}

MODEL_OVERRIDES = {
    ("nike", "air_force_1"): +0.5,
    ("nike", "dunk"): +0.5,
    ("nike", "air_max_90"): 0.0,
    ("nike", "air_max_95"): 0.0,
    ("nike", "air_max_97"): 0.0,
    ("nike", "air_max_1"): 0.0,
    ("nike", "react"): 0.0,
    ("nike", "pegasus"): 0.0,
    ("nike", "free"): +0.5,
    ("jordan", "air_jordan_1"): +0.5,
    ("jordan", "air_jordan_3"): 0.0,
    ("jordan", "air_jordan_4"): 0.0,
    ("jordan", "air_jordan_11"): +0.5,
    ("adidas", "ultraboost"): 0.0,
    ("adidas", "yeezy_350"): +1.0,
    ("adidas", "yeezy_700"): 0.0,
    ("adidas", "stan_smith"): 0.0,
    ("adidas", "superstar"): 0.0,
    ("adidas", "nmd"): +0.5,
    ("adidas", "forum"): 0.0,
    ("adidas", "samba"): +0.5,
    ("adidas", "gazelle"): +0.5,
    ("converse", "chuck_taylor"): -1.0,
    ("converse", "chuck_70"): -1.0,
    ("converse", "run_star"): 0.0,
    ("vans", "old_skool"): +0.5,
    ("vans", "sk8_hi"): +0.5,
    ("vans", "slip_on"): +0.5,
    ("vans", "authentic"): 0.0,
    ("new_balance", "990"): 0.0,
    ("new_balance", "574"): 0.0,
    ("new_balance", "530"): 0.0,
    ("new_balance", "2002r"): 0.0,
    ("puma", "suede"): +0.5,
    ("puma", "rs_x"): +0.5,
    ("reebok", "classic"): +0.5,
    ("reebok", "club_c"): +0.5,
    ("under_armour", "hovr"): +0.5,
    ("under_armour", "curry"): +0.5,
    ("salomon", "speedcross"): 0.0,
    ("salomon", "xt_6"): 0.0,
}

BRAND_CONFIDENCE = {
    "nike": "high", "jordan": "high", "adidas": "high", "new_balance": "high",
    "converse": "high", "vans": "high", "puma": "medium", "reebok": "medium",
    "asics": "high", "hoka": "high", "brooks": "high", "saucony": "medium",
    "under_armour": "medium", "timberland": "medium", "salomon": "medium",
    "merrell": "medium", "fila": "low", "gucci": "low", "balenciaga": "low",
    "golden_goose": "low", "ugg": "medium", "keen": "medium",
}

MODEL_CONFIDENCE = {
    ("nike", "air_force_1"): "high",
    ("nike", "dunk"): "high",
    ("jordan", "air_jordan_1"): "high",
    ("jordan", "air_jordan_11"): "high",
    ("adidas", "yeezy_350"): "high",
    ("adidas", "samba"): "high",
    ("converse", "chuck_taylor"): "high",
    ("converse", "chuck_70"): "high",
}

def get_all_brands():
    return sorted(BRAND_OFFSETS.keys())

def get_brand_display_name(brand_key: str) -> str:
    display = {
        "nike": "Nike", "jordan": "Air Jordan", "adidas": "Adidas",
        "new_balance": "New Balance", "hoka": "HOKA", "brooks": "Brooks",
        "asics": "ASICS", "saucony": "Saucony", "mizuno": "Mizuno",
        "on_running": "On Running", "puma": "Puma", "reebok": "Reebok",
        "under_armour": "Under Armour", "fila": "Fila", "vans": "Vans",
        "converse": "Converse", "timberland": "Timberland", "ugg": "UGG",
        "gucci": "Gucci", "balenciaga": "Balenciaga", "golden_goose": "Golden Goose",
        "common_projects": "Common Projects", "salomon": "Salomon",
        "merrell": "Merrell", "keen": "Keen", "columbia": "Columbia",
        "la_sportiva": "La Sportiva", "scarpa": "Scarpa",
    }
    return display.get(brand_key, brand_key.replace("_", " ").title())
