from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    DateTime,
    TIMESTAMP,
    text,
    BLOB,
)
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    roles = Column(String)
    role_id = Column(Integer, ForeignKey("user_roles.id"))
    role = relationship("UserRole", back_populates="users")


class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    users = relationship("User", back_populates="role")


# abode represent rental property or home for sale or rent
# class Abode(Base):
#     __tablename__ = "abodes"
#     id = Column(Integer, primary_key=True)
#     address = Column(String)
#     city = Column(String)
#     state = Column(String)
#     zipcode = Column(String)
#     price = Column(Integer)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     photos = Column(BLOB)
#     num_beds = Column(Integer)
#     num_baths = Column(Integer)
#     square_feet = Column(Integer)
#     created_at = Column(
#         TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
#     )
#     updated_at = Column(
#         TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
#     )


# class FavoriteAbode(Base):
#     __tablename__ = "favorite_abodes"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     property_id = Column(Integer, ForeignKey("abodes.id"))
#     user = relationship("User", back_populates="favorite_abodes")
#     property = relationship("Property", back_populates="favorite_users")
