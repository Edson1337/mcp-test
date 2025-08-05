from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ToolInput(BaseModel):
    tool: str
    a: float
    b: float


def sum_func(a, b):
    return a + b

def divide_func(a, b):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return a / b

@app.post("/tool")
def use_tool(input: ToolInput):
    tools = {
        "sum": sum_func,
        "divide": divide_func
    }
    if input.tool not in tools:
        raise HTTPException(status_code=400, detail="Tool not found")
    result = tools[input.tool](input.a, input.b)
    return {"result": result}
