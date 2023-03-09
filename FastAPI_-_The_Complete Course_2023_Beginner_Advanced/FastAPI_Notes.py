# Commands:
"""
pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install "passlib[bcrypt]"
pip install python-multipart
pip install "python-jose[cryptography]"
pip install psycopg2-binary   Used in PostgreSQL
pip install alembic
pip install aiofiles
pip install jinja2

fastapi: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
uvicorn[standard]: A fast, ASGI server implementation, using uvloop and httptools.
sqlalchemy: A SQL toolkit and Object-Relational Mapping (ORM) library.
passlib[bcrypt]: Secure password hashing and storage using the bcrypt algorithm.
python-multipart: A Python library to handle HTTP multipart requests, including file uploads.
python-jose[cryptography]: A JSON Web Token (JWT) implementation for Python using cryptography library.
psycopg2-binary: A PostgreSQL database adapter for Python.
alembic: A lightweight database migration tool for usage with SQLAlchemy.
aiofiles: An async file support for Python.
jinja2: A fast and easy to use template engine for Python.

python -m venv fastapienv   Creates an environment for FastAPI
Set-ExecutionPolicy Unrestricted   Enables PowerShell to execute scripts
fastapienv\Scripts\activate   activate   Activates the virtual environment
deactivate   Deactivates the virtual environment
pip install fastapi[all]   Installs all fastapi dependencies
uvicorn my_python_file:app --reload --port 8000  Starts FastAPI app
http://127.0.0.1:8000/   Root
http://127.0.0.1:8000/openapi.json   OpenAPI specification which describes your RESTful APIs
http://127.0.0.1:8000/docs   Swagger UI

SQLite3:
    Download SQLite3 Precompiled Binaries for Windows win32-x86: https://www.sqlite.org/download.html
      Install it in C:\ and then add it to Path System Variables like this: C:\sqlite3
         Execute it using 
    sqlite3 my_db.db   Opens a SQLite shell enabling the interacting with the database db_name.db
    .schema   Shows the schema for all the tables in the database
    .mode table   Change the display from the SELECT clause to `table`
    .quit   Exits SQLite shell
    CREATE TABLE my_table (
        id SERIAL,
        first_name varchar(45) DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (fk_name) REFERENCES another_table(another_table_pk)
    )
    INSERT INTO my_table (my_col_1, my_col_2) values (my_val_1, my_val_2);   Insert values
    SELECT * FROM my_table;   Select values
    DELETE FROM my_table WHERE my_col = an_int;
    DROP TABLE my_table;

Alembic:
    alembic init my_dir   Initializes a new, generic environment
        alembic init alembic
    alembic revision -m my_message   Create a new revision of the environment
        alembic revision -m "Create phone number for USER table"
    alembic upgrade my_revision_number   Run our upgrade migration to our database
        alembic upgrade 00265b5790f3
    alembic downgrade   my_revision_number   Run our drowngrade migration to our database
        alembic upgrade 00265b5790f3
"""


# Imports
from fastapi import FastAPI, HTTPException, Request, status, Form, Header, Depends, APIRouter
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from uuid import UUID
from sqlalchemy import create_engine, Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status as starlette_status

"""
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
HTTPException: A built-in exception in FastAPI used to handle HTTP exceptions and return appropriate responses.
Request: A class that represents an incoming HTTP request.
Enum: A built-in Python class used to create enumerated types.
Optional: A built-in Python class used to represent optional (nullable) values.
BaseModel: A base class for defining Pydantic models.
Field: A decorator used to define additional metadata for model fields.
JSONResponse: A class that represents an HTTP response containing JSON data.
UUID: A built-in Python class used to represent UUIDs.
create_engine: A function from SQLAlchemy used to create a database engine.
Boolean: A class from SQLAlchemy used to represent boolean values.
Column: A class from SQLAlchemy used to define table columns.
Integer: A class from SQLAlchemy used to represent integer values.
String: A class from SQLAlchemy used to represent string values.
Float: A class from SQLAlchemy used to represent floating-point values.
ForeignKey: A class from SQLAlchemy used to define foreign key relationships between tables.
sessionmaker: A function from SQLAlchemy used to create a session factory.
Session: A class from SQLAlchemy used to represent a database session.
relationship: A function from SQLAlchemy used to define object relationships between tables.
declarative_base: A function from SQLAlchemy used to create a base class for declarative model classes.
Base: A base class for defining SQLAlchemy models.
CryptContext: A class from passlib used to manage password hashing.
OAuth2PasswordRequestForm: A class from FastAPI used to represent a form for requesting OAuth2 access tokens.
OAuth2PasswordBearer: A class from FastAPI used to represent an OAuth2 access token bearer.
datetime: A built-in Python module used to work with dates and times.
timedelta: A class from datetime used to represent time durations.
jwt: A function from jose used to encode and decode JSON Web Tokens.
JWTError: An exception class from jose used to represent errors related to JSON Web Tokens.
HTMLResponse: A class that represents an HTTP response containing HTML data.
Jinja2Templates: A class from FastAPI used to render Jinja2 templates.
StaticFiles: A class from Starlette used to serve static files.
RedirectResponse: A class that represents an HTTP redirect response.
status: A module from Starlette used to represent HTTP status codes.
""" 


# Setting up API
app = FastAPI()


# Setting up SQLAlchemy ORM (Object Relational Mapping) with a DBMS (Database Management System)
# SQLite 
SQLALCHEMY_DATABASE_URL = "sqlite:///path_to_db/my_db_name.db" # Template
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db" # Example
# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://my_user:my_password@my_address/my_db_name" # Template
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TodoApplicationDatabase" # Example
# MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://my_user:my_password@my_address:my_port/my_db_name" # Template
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp" # Example


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args is only for SQLite
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

class MyTable(Base):
    # By default the __tablename__ converts the class name to lowercase and use underscores instead of camel case
    __tablename__ = "my_table_name"

    my_id = Column(Integer, primary_key=True, index=True)
    my_str_col = Column(String(n_characters), unique=True)
    my_int_col = Column(Integer, nullable=False)
    my_bool_col = Column(Boolean, default=False)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# SQLAlchemy models relationships
class MyUser(Base):
    __tablename__ = "my_user"
    my_id = Column(Integer, primary_key=True, index=True)
    my_first_name = Column(String[40], nullable=False)

    my_order_relation = relationship("MyOrder", back_populates="my_user_relation")

class MyOrder(Base):
    __tablename__ = "my_order"
    my_id = Column(Integer, primary_key=True, index=True)
    my_value = Column(Float, nullable=False)

    my_user_id = Column(Integer, ForeignKey("my_user.my_id"))
    my_user_relation = relationship("Myuser", back_populates="my_order_relation")


# ORM commands
"""
db.query(MyTable).all()   Fetchs all rows of MyTable
db.query(MyTable).filter(MyTable.id == an_int).first()   Fetch the first row of MyTable where id matches an_int
db.add(my_new_obj)   Adds my_new_obj to the session.
db.flush()   Saves the changes made in the session to the database, but does not end the transaction. Useful to get the table's id before commiting
db.commit()   Saves the changes and ends the transaction.
"""


# Simple get
@app.get("/")
async def my_func():
    return my_dict


# Get with parameter
# my_resource in decorator and in function definition doesn't have match
@app.get("/{my_resource}")
async def my_func(my_resource: my_type):
    return my_dict[my_resource]



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


# Get with custom list of possible values
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


# Get with header
# Header class can be a useful way to define endpoints that require custom HTTP headers to be included in the request.
@app.get("/my_path")
async def my_func(my_var: Optional[str] = Header(None)):
    return {"my_var": my_var}


# Get with database
@app.get("/")
async def my_func(db: Session = Depends(get_db)):
    return db.query(MyTable).all()


# Get with user authentication
@app.get("/{my_resource_id}")
async def my_func(
    my_resource_id: a_type,
    user: dict = Depends(my_get_curr_user_func),
    db: Session = Depends(my_get_db_func),
):
    if user is None:
        raise my_get_user_exception_func()

    my_obj = (
        db.query(MyTable)
        .filter(MyTable.id == my_resource_id)
        .filter(MyTable.user_id == user.get("id"))
        .first()
    )

    if my_model is not None:
        return my_model

    raise my_http_exception_func()


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


# Post with custom status code response
@app.post("/", status_code=status.HTTP_201_CREATED)
async def my_func(my_var_1, my_var_2):
    my_dict[my_var_1] = my_var_2
    return my_dict


# Post with Form field
# Form field is a convenient way to accept data from HTML forms in your API endpoints. But FastAPI also provides
# for other types of request data, including JSON-encoded data, query parameters, and path parameters.
@app.post("/books/login")
async def my_func(my_var_1: str = Form(), my_var_2: str = Form()):
    return {"my_var_1": my_var_1, "my_var_2": my_var_2}


# Post with database
class MyClass(BaseModel):
    my_UUID: UUID
    my_str_attribute: str
    my_int_attribute: int

@app.post("/")
async def my_func(my_obj: MyClass, db: Session = Depends(get_db)):
    my_new_obj = MyTable()
    my_new_obj.my_int_attribute = my_obj.my_int_attribute
    my_new_obj.my_str_attribute = my_obj.my_str_attribute

    db.add(my_new_obj)
    db.commit()

    return {
        "status": 201,
        "transaction": "Successful"
    }


# Post with user authentication
@app.post("/")
async def my_func(
    my_obj: MyClass,
    user: dict = Depends(my_get_curr_user_func),
    db: Session = Depends(get_db)
):
    if user is None:
        raise my_get_user_exception_func()

    my_new_obj = MyTable()
    my_new_obj.my_int_attribute = my_obj.my_int_attribute
    my_new_obj.my_str_attribute = my_obj.my_str_attribute
    my_new_obj.my_user_id = user.get("id")

    db.add(my_new_obj)
    db.commit()

    return my_successful_response_func


# Simple put 
@app.put("/{my_resource_id}")
async def my_func(my_resource_id: a_type, my_obj: MyClass):
    my_dict[my_resource_id] = my_obj
    return my_dict 


# Put with database
@app.put("/{my_resource_id}")
async def my_func(my_resource_id: a_type, my_obj: MyClass, db: Session = Depends(get_db)):
    my_updated_obj = (
        db
        .query(MyTable)
        .filter(MyTable.id == my_resource_id)
        .first()
    )
    
    my_updated_obj.my_int_attribute = my_obj.my_int_attribute
    my_updated_obj.my_str_attribute = my_obj.my_str_attribute

    db.add(my_updated_obj)
    db.commit()

    return {
        "status": 200,
        "transact": "Successful"
    }


# Put with user authentication
@app.put("/{my_resource_id}")
async def update_todo(
    my_resource_id: a_type,
    my_obj: MyClass,
    user: dict = Depends(my_get_curr_user_func),
    db: Session = Depends(get_db)
):
    if user is None:
        raise my_get_user_exception_func()

    my_updated_obj = (
        db
        .query(MyTable)
        .filter(MyTable.id == my_resource_id)
        .filter(MyTable.user_id == user.get("id"))
        .first()
    )

    if my_updated_obj is None:
        raise my_http_exception_func()
    
    my_updated_obj.my_int_attribute = my_obj.my_int_attribute
    my_updated_obj.my_str_attribute = my_obj.my_str_attribute

    db.add(my_updated_obj)
    db.commit()

    return my_successful_response_func(200)


# Simple delete
@app.delete("/{my_resource_id}")
async def my_func(my_resource_id):
    del my_dict[my_resource_id]
    return f"My resource {my_resource_id} was deleted."


# Delete with database
@app.delete("/{my_resource_id}")
async def my_func(my_resource_id: a_type, db: Session = Depends(get_db)):
    db.query(MyTable).filter(MyTable.id == my_resource_id).delete()
    db.commit()

    return {
        "status": 200,
        "transact": "Successful"
    }


# Delete with user authentication
@app.delete("/{my_resource_id}")
async def my_func(
    my_resource_id: a_type,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user is None:
        raise my_get_user_exception_func()

    my_obj = (
        db
        .query(MyTable)
        .filter(MyTable.id == my_resource_id)
        .filter(MyTable.user_id == user.get("id"))
        .first()
    )

    if my_obj is None:
        raise my_http_exception_func()
    
    db.query(MyTable).filter(MyTable.id == my_resource_id).delete()

    db.commit()

    return my_successful_response_func(200)


# Handling exceptions using HTTPException which can be used for simple exceptions
def item_cannot_be_found_exception():
    return HTTPException(
        status_code=404,
        detail="Resource not found",
        headers={"X-Header-Error": "Nothing to be seen at the UUID"}
    )

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


# Handling exceptions using exception_handler which is preferable and shoud be used for complex exceptions
# the request parameter is not mandatory but it is a standard
# part of the exception handler function signature in FastAPI
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
# response_model defines the expected JSON response format for an API endpoint.


# Routers
# Routers organizes and groups related API endpoints
router = APIRouter(
    prefix="/my_endpoint_prefix",
    tags=["my_swagger_ui_tag"],
    responses={an_error_int: {"descriptive_key": "descriptive_value"}}
) # Template
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
) # Example
app.include_router(router)
app.include_router(
    prefix="/my_endpoint_prefix",
    tags=["my_swagger_ui_tag"],
    dependencies=[Depends(your_dependency_function)],
    responses={an_error_int: {"descriptive_key": "descriptive_value"}}
)
# If you're dealing with an external API that you're not able to modify, you can still set the parameters directly in the include_router()
# Then instead of using, for example, @app.post("/token"), use @router.post("/token")



# Alembic, when changing something with Alembic, remember to change it also in your Python models/tables


# Alembic, create new column
# Inside alembic/versions/my_revision_number
def upgrade() -> None:
    op.add_column("my_table", sa.Column("my_new_column", sa.a_type(), nullable=a_boolean))

def downgrade() -> None:
    op.drop_column("my_table", "my_column_to_delete")


# Alembic, create new table
# Inside alembic/versions/my_revision_number
def upgrade() -> None:
    op.create_table(
        "my_table",
        sa.Column("my_id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("my_str_col", sa.String(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("my_table")


# Alembic, create new relationship
# Inside alembic/versions/my_revision_number
def upgrade() -> None:
    op.add_column(
        "my_table_1",
        sa.Column("my_fk_col", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        "my_table_2_my_table_1_fk",
        source_table="my_table_1",
        referent_table="my_table_2",
        local_cols=["my_fk_col"],
        remote_cols=["my_table_2_pk"],
        ondelete="CASCADE"
    )

def downgrade() -> None:
    op.drop_constraint(
        "my_table_2_my_table_1_fk",
        table_name="my_table_1"
    )
    op.drop_column(
        "my_table_1",
        "my_fk_col"
    )


## EXAMPLE user authentication & authorization
SECRET_KEY = "0poPIOutYZw9J5VC8Qgd" # secret key used to create a JWT token.
ALGORITHM = "HS256" # hashing algorithm used for the JWT token.
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token") # endpoint for obtaining the access token

# SQLalchemy model for users table.
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generates a hash from a password.
def get_password_hash(password):
    return bcrypt_context.hash(password)

# Verifies a plain text password against a hashed password.
def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

# Finds a user in the database and verifies its password.
def authenticate_user(username: str, password: str, db):
    user = (
        db
        .query(Users)
        .filter(Users.username == username)
        .first()
    )

    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

# Creates a JWT token for an authenticated user.
def create_access_token(
        username: str,
        user_id: int,
        expires_delta: Optional[timedelta] = None
):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    # JWT (Json Web Token):
    # Used for authorization. It securely transmits data between two parties using a JSON Object.
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_exception():
    creadentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return creadentials_exception

def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return token_exception_response

# Model for creating a new user.
class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str

# Creates a new user and stores in the database.
@app.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = Users()
    hash_password = get_password_hash(create_user.password)

    create_user_model.email = create_user.email
    create_user_model.username = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()

# Authenticates user and generates a JWT token.
@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(
        user.username,
        user.id,
        expires_delta=token_expires
    )
    return {"token": token}

# Gets the current user from the JWT token, and raises an HTTPException if the user is not found or the token is invalid
async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        raise get_user_exception()

# API route to retrieve all todos by user, requiring authentication token, and accessing the database
@app.get("/todos/user")
async def read_all_by_user(
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()
    return (
        db
        .query(models.Todos)
        .filter(models.Todos.ownder_id == user.get("id"))
        .all()
    )

# Reads a single Todo by ID for the authenticated user.
@app.get("/todo/{todo_id}")
async def read_todo(
    todo_id: int,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()
    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )
    if todo_model is not None:
        return todo_model
    raise http_exception()

# Creates a new Todo for the authenticated user.
@app.post("/")
async def create_todo(
    todo: Todo,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()

    return successful_response(201)

# Updates a new Todo for the authenticated user
@app.put("/{todo_id}")
async def update_todo(
    todo_id: int,
    todo: Todo,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    todo_model = (
        db
        .query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise http_exception
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(200)

# Deletes a new Todo for the authenticated user
@app.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    todo_model = (
        db
        .query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.onwer_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise http_exception()
    
    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Sucessful"
    }
