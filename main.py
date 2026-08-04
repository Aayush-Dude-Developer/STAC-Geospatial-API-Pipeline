from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="STAC Geospatial API", version="1.0")

class STACItem(BaseModel):
    id: str
    geometry: dict
    properties: dict

@app.get("/")
async def root():
    return {"message": "STAC API Pipeline Operational. Awaiting queries."}

@app.get("/collections/{collection_id}/items/{item_id}")
async def get_stac_item(collection_id: str, item_id: str):
    # Mock endpoint representing S3 data retrieval for QGIS integration
    if collection_id != "uav-imagery-2026":
        raise HTTPException(status_code=404, detail="Collection not found")
    
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": item_id,
        "collection": collection_id,
        "assets": {
            "visual": {"href": f"s3://stac-data/{collection_id}/{item_id}.tif"}
        }
    }
