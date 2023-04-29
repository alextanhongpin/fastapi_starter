## Using enum

```python
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning ftw"}

    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the image"}

    return {"model_name": model_name, "message": "have some residual"}
```
