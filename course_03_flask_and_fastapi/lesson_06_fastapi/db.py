import databases
import sqlalchemy
from settings import settings
import datetime

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(40)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(40)),
)

products = sqlalchemy.Table(
    'product',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                        primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(40)),
    sqlalchemy.Column("description", sqlalchemy.String(256)),
    sqlalchemy.Column("price", sqlalchemy.Integer),
)

orders = sqlalchemy.Table(
    'order',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                        primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer(), sqlalchemy.ForeignKey("user.id"), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.Integer(), sqlalchemy.ForeignKey("product.id"), nullable=False),
    sqlalchemy.Column("order_date", sqlalchemy.Date(), nullable=False, default=datetime.date.today()),
    sqlalchemy.Column("status", sqlalchemy.String(10)),
)


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


