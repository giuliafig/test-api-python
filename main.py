from fastapi import FastAPI
from typing import List, Dict
from pydantic import BaseModel
from fastapi import HTTPException

class Product(BaseModel):
    sku: str
    name: str
    price: float
    description: str = None

app = FastAPI()

# Sample product data
products: Dict[str, Product] = {
    "BOOK001": Product(
        sku="BOOK001",
        name="Python Programming Guide",
        price=29.99,
        description="Comprehensive guide to Python programming"
    ),
    "TECH002": Product(
        sku="TECH002",
        name="Wireless Mouse",
        price=19.99,
        description="Ergonomic wireless mouse with long battery life"
    ),
    "GEAR003": Product(
        sku="GEAR003",
        name="Gaming Headset",
        price=89.99,
        description="Premium gaming headset with surround sound"
    )
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "pong"}

@app.get("/products", response_model=List[Product])
async def list_products():
    return list(products.values())

@app.get("/products/{sku}", response_model=Product)
async def get_product(sku: str):
    if sku not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return products[sku]
