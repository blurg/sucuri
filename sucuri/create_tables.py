import os
from sqlalchemy import create_engine
from sucuri.sucuri_app.sql_sucuri.database import Base

dsn = os.environ.get("SUCURI_DB")
engine = create_engine(dsn)
Base.metadata.create_all(engine)