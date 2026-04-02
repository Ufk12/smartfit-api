from typing import Optional
from size_database import (
    EU_TO_CM, EU_TO_US_MEN, US_MEN_TO_EU, EU_TO_US_WOMEN,
    US_WOMEN_TO_EU, EU_TO_UK_MEN, UK_MEN_TO_EU,
    BRAND_OFFSETS, MODEL_OVERRIDES, BRAND_CONFIDENCE, MODEL_CONFIDENCE,
    get_brand_display_name,
)

def normalize_to_eu(size: float, system: str) -> Optional[float]:
    system = system.lower().strip()
    if system == "eu":
        return float(size)
    elif system in ("us", "us_men"):
        return US_MEN_TO_EU.get(float(size))
    elif system == "us_women":
        return US_WOMEN_TO_EU.get(float(size))
    elif system == "uk":
        return UK_MEN_TO_EU.get(float(size))
    elif system == "cm":
        cm = float(size)
        best_eu, best_diff = None, 999
        for eu, length in EU_TO_CM.items():
            diff = abs(length - cm)
            if diff < best_diff:
                best_diff = diff
                best_eu = eu
        return best_eu
    return None

def eu_to_output(eu_size: float, system: str) -> Optional[float]:
    system = system.lower().strip()
    if system == "eu": return eu_size
    elif system in ("us", "us_men"): return EU_TO_US_MEN.get(eu_size)
    elif system == "us_women": return EU_TO_US_WOMEN.get(eu_size)
    elif system == "uk": return EU_TO_UK_MEN.get(eu_size)
    elif system == "cm": return EU_TO_CM.get(eu_size)
    return None

def normalize_model_key(model: str) -> str:
    if not model: return ""
    return model.lower().strip().replace(" ", "_").replace("-", "_")

def snap_to_valid_eu(size: float) -> float:
    return round(size * 2) / 2

def convert_size(source_brand, source_size, source_system, target_brand, target_model=None, output_system=None):
    source_brand = source_brand.lower().strip()
    target_brand = target_brand.lower().strip()
    output_system = output_system or source_system

    if source_brand not in BRAND_OFFSETS:
        return {"error": f"Unknown source brand: '{source_brand}'"}
    if target_brand not in BRAND_OFFSETS:
        return {"error": f"Unknown target brand: '{target_brand}'"}

    eu_source = normalize_to_eu(source_size, source_system)
    if eu_source is None:
        return {"error": f"Could not convert size {source_size} ({source_system}) to EU"}

    neutral_eu = eu_source - BRAND_OFFSETS[source_brand]
    target_model_key = normalize_model_key(target_model) if target_model else ""
    target_model_offset = MODEL_OVERRIDES.get((target_brand, target_model_key), 0.0)
    target_eu = neutral_eu + BRAND_OFFSETS[target_brand] + target_model_offset
    target_eu_snapped = snap_to_valid_eu(target_eu)

    recommended = eu_to_output(target_eu_snapped, output_system)
    if recommended is None:
        for delta in [0.5, -0.5, 1.0, -1.0]:
            recommended = eu_to_output(snap_to_valid_eu(target_eu + delta), output_system)
            if recommended is not None:
                target_eu_snapped = snap_to_valid_eu(target_eu + delta)
                break

    conf_levels = {"high": 3, "medium": 2, "low": 1}
    base_conf = conf_levels.get(BRAND_CONFIDENCE.get(source_brand, "medium"), 2)
    tgt_conf = conf_levels.get(BRAND_CONFIDENCE.get(target_brand, "medium"), 2)
    combined = min(base_conf, tgt_conf)
    if target_model_key:
        m_conf = MODEL_CONFIDENCE.get((target_brand, target_model_key))
        if m_conf:
            combined = min(combined, conf_levels.get(m_conf, 2))
    confidence_str = ["low", "medium", "high"][combined - 1]
    if source_brand == target_brand and not target_model_key:
        confidence_str = "high"

    return {
        "recommended_size": recommended,
        "size_system": output_system,
        "confidence": confidence_str,
        "source": {"brand": get_brand_display_name(source_brand), "size": source_size, "system": source_system, "eu_equivalent": eu_source},
        "target": {"brand": get_brand_display_name(target_brand), "model": target_model or None, "eu_equivalent": target_eu_snapped},
    }
