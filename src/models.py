from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///tareas.db')
Session = sessionmaker(bind=engine)

class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    completada = Column(Boolean)

Base.metadata.create_all(engine)


