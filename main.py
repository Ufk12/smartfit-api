from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from converter import convert_size
from size_database import BRAND_OFFSETS, MODEL_OVERRIDES, get_all_brands, get_brand_display_name

app = FastAPI(title="SmartFit API", description="Shoe size conversion between brands and models", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class ConvertRequest(BaseModel):
    source_brand: str = Field(..., example="adidas")
    source_size: float = Field(..., example=43)
    source_system: str = Field(default="eu", example="eu")
    target_brand: str = Field(..., example="nike")
    target_model: Optional[str] = Field(default=None, example="air_max_90")
    output_system: Optional[str] = Field(default=None)

    @validator("source_system", "output_system", pre=True, always=True)
    def lowercase_system(cls, v):
        return v.lower().strip() if v else v

    @validator("source_brand", "target_brand", pre=True)
    def lowercase_brand(cls, v):
        return v.lower().strip().replace(" ", "_").replace("-", "_") if v else v

@app.get("/health")
def health():
    return {"status": "ok", "service": "SmartFit API", "version": "1.0.0"}

@app.get("/brands")
def list_brands():
    return [{"key": b, "display_name": get_brand_display_name(b), "offset": BRAND_OFFSETS[b]} for b in get_all_brands()]

@app.get("/models")
def list_models(brand: Optional[str] = None):
    result = []
    for (b, m), offset in MODEL_OVERRIDES.items():
        if brand and b != brand.lower().replace(" ", "_"):
            continue
        result.append({"brand": get_brand_display_name(b), "brand_key": b, "model": m, "additional_offset_eu": offset})
    return sorted(result, key=lambda x: (x["brand_key"], x["model"]))

@app.post("/convert")
def convert(req: ConvertRequest):
    result = convert_size(req.source_brand, req.source_size, req.source_system, req.target_brand, req.target_model, req.output_system)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return result

@app.post("/convert/batch")
def convert_batch(requests: List[ConvertRequest]):
    if len(requests) > 20:
        raise HTTPException(status_code=400, detail="Max 20 items per batch")
    results = [convert_size(r.source_brand, r.source_size, r.source_system, r.target_brand, r.target_model, r.output_system) for r in requests]
    return {"results": results, "count": len(results)}
