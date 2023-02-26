# Commands:
"""
python -m venv fastapienv   Create an environment for FastAPI
cd fastapienv/Scripts   activate   Activate the environment
pip install fastapi[all]   Install all fastapi dependencies
uvicorn books:app --reload   Start FastAPI app
http://127.0.0.1:8000/   Root
http://127.0.0.1:8000/openapi.json   OpenAPI specification which describes your RESTful APIs
http://127.0.0.1:8000/docs   Swagger UI
"""

# Imports
from fastapi import FastAPI, HTTPException, Request
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from uuid import UUID


# Config
app = FastAPI()


# Simple get
@app.get("/")
async def my_func():
    return my_dict


# Get with parameter
@app.get("/{my_resource}")
async def my_func(my_resource: my_type):
    return my_dict[my_resource]
# my_resource in decorator and in function definition doesn't have match


# Get with parameter and optional value
@app.get("/{my_resource}")
async def my_func(my_resource: Optional[a_type]=None):
    if my_resource:
        return my_dict_1
    else:
        return my_dict_2


# Get with parameter and default/optional value
@app.get("/{my_resource}")
async def my_func(my_resource: my_type="my_default_value"):
    return my_dict[my_resource]


# Define list of possible values
class MyClass(str, Enum):
    my_possibility_1 = "My Possibility 1"
    my_possibility_2 = "My Possibility 2"

@app.get("/{my_obj}")
async def my_func(my_obj: MyClass):
    if my_obj == MyClass.my_possibility_1:
        return my_dict_1
    if my_obj == MyClass.my_possibility_2:
        return my_dict_2
    return my_dict_3


# Simple post
@app.post("/")
async def my_func(my_var_1, my_var_2):
    my_dict[my_var_1] = my_var_2
    return my_dict


# Post with data type validation
class MyClass(BaseModel):
    my_UUID: UUID
    my_str_attribute: str
    my_int_attribute: int

@app.post("/")
async def create_book(my_obj: MyClass):
    my_list.append(my_obj)
    return my_obj


# Post with data type validation and other validations
class MyClass(BaseModel):
    my_UUID: str
    my_str_attribute: Optional[str] = Field(
        title="My details about this attribute",
        max_length=100,
        min_length=1
    )
    my_int_attribute: int = Field(
        gt=-1,
        lt=101
    )

@app.post("/")
async def create_book(my_obj: MyClass):
    my_list.append(my_obj)
    return my_obj


# Post with data type validation and other validations, and pre-defined data example
class MyClass(BaseModel):
    my_UUID: str
    my_str_attribute: Optional[str] = Field(
        title="My details about this attribute",
        max_length=100,
        min_length=1
    )
    my_int_attribute: int = Field(
        gt=-1,
        lt=101
    )

    class Config:
        schema_extra = {
            "example": {
                "my_UUID": "576b164d-b05f-4bfe-ba6c-db1da286372f",
                "my_str_attribute": "A description of a book",
                "my_int_attribute": 75,
            }
        }

@app.post("/")
async def create_book(my_obj: MyClass):
    my_list.append(my_obj)
    return my_obj


# Simple put
@app.put("/{my_resource}")
async def update_book(my_resource: a_type, my_obj: MyClass):
    my_dict[my_resource] = my_obj
    return my_dict


# Simple delete
@app.delete("/{my_resource}")
async def delete_book(my_resource):
    del my_dict[my_resource]
    return f"My resource {my_resource} was deleted."


# Handling exceptions using HTTPException which can be used for simple exceptions
@app.get("/{my_resource}")
async def my_func(my_resource: my_type):
    try:
        my_dict[my_resource]
    except KeyError:
        raise item_cannot_be_found_exception()
    return my_dict[my_resource]

@app.put("/{my_resource}")
async def update_book(my_resource: a_type, my_obj: MyClass):
    try:
        my_dict[my_resource] = my_obj
    except KeyError:
        raise item_cannot_be_found_exception()
    return my_dict

@app.delete("/{my_resource}")
async def delete_book(my_resource):
    try:
        del my_dict[my_resource]
    except KeyError:
        raise item_cannot_be_found_exception()
    return f"My resource {my_resource} was deleted."

def item_cannot_be_found_exception():
    return HTTPException(
        status_code=404,
        detail="Resource not found",
        headers={"X-Header-Error": "Nothing to be seen at the UUID"}
    )


# Handling exceptions using exception_handler which is preferable and shoud be used for complex exceptions
class NegativeNumberException(Exception):
    def __init__(self, n_items_to_return):
        self.n_items_to_return = n_items_to_return

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request,
                                            exception: NegativeNumberException):
    return JSONResponse(
        status_code=400,
        content={"message": "You entered {exception.n_items_to_return} but the number must be positive"}
    )
# the request parameter is not mandatory but it is a standard
# part of the exception handler function signature in FastAPI


# Using response_model
class MyClass(BaseModel):
    my_UUID: UUID
    my_str_attribute: str
    my_int_attribute: int

class MyClassNoInt(BaseModel):
    my_UUID: UUID
    my_str_attribute: str

@app.get("/{my_resource}")
async def my_func(my_resource: my_type):
    return my_dict[my_resource]

@app.get("/no_int/{my_resource}", response_model=MyClassNoInt)
async def my_func(my_resource: my_type):
    return my_dict[my_resource]

# CONTINUE EXPLAINING THIS response_model BETTER


