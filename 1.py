from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import json

app = FastAPI()

with open('recipes.json', "r") as file:
    data = json.load(file)

class RecipeModel(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl

# get all data
@app.get("/recipes")
def show_recipes():
    return data

# get special data info
@app.get("/recipes/{id}")
def show_recipe(id: int):
    res = [recipe for recipe in data if recipe["id"] == id]
    if res: 
        return res
    return 'Please try again, there is no receipt with that id number'

# generates unique id
def generate_id():
    t = len(data)+1
    for d in data:
        if(t == d["id"]):
            t+=1
    return t

# add new data
@app.post("/recipe/")
def create_recipe(new_recipe:RecipeModel):
    recipe = {
        "id": generate_id(),
        "label": new_recipe.label,
        "source": new_recipe.source,
        "url":new_recipe.url
    }
    data.append(recipe)
    with open("recipes.json", mode='w') as file:    
        file.seek(0)
        json.dump(data, file)
    
    return data

# update existing data
@app.put("/recipes/{id}")
def update_recipe(id:int, label: Optional[str] = None, source: Optional[str]=None, url: Optional[HttpUrl]=None):
    res = [recipe for recipe in data if recipe["id"] == id]
    if res:
        if label:
            res[0]["label"] = label
        if source:
            res[0]["source"] = source
        if url:
            res[0]["url"] = url
        
        with open("recipes.json", mode='w') as file:
            file.seek(0)
            json.dump(data, file)
        
        return res[0]
    return data

# remove data
@app.delete("/recipes/{id}")
def delete_recipe(id:int):
    res = [recipe for recipe in data if recipe["id"] == id]
    if res:
        data.remove(res[0])
        with open ("recipes.json", mode = 'w') as file:
            file.seek(0)
            json.dump(data, file)
        return res[0]
    return data
