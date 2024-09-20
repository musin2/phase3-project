from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for declarative models
Base = declarative_base()

# Database connection to 'recipe_manager.db'
engine = create_engine('sqlite:///recipe_manager.db', echo=True)

# Recipe model/table
class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    
    # One-to-many relationship(a recipe can have multiple ingredients)
    ingredients = relationship('Ingredient', back_populates='recipe', cascade="all, delete, delete-orphan")

# Ingredient model/table
class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True)
    ingredient_name = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))  # Foreign key linking to Recipe table
    
    # Many-to-one relationship with Recipe
    recipe = relationship('Recipe', back_populates='ingredients')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables in the database
Base.metadata.create_all(engine)
