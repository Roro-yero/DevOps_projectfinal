from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import pandas as pd
import os

# Initialisation de l'application FastAPI
app = FastAPI()

#  Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

#  Configuration de la base de données PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#  Modèle SQLAlchemy mis à jour
class TestData(Base):
    __tablename__ = "test_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fam_name = Column(String, index=True)
    birth = Column(Date)
    school = Column(String)

# Création de la table si elle n'existe pas
Base.metadata.create_all(bind=engine)

#  Dépendance pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  Endpoint de recherche amélioré (recherche par nom, prénom et école)
@app.get("/search/")
def search_data(query: str, db: Session = Depends(get_db)):
    results = db.query(TestData).filter(
        (TestData.name.contains(query)) | 
        (TestData.fam_name.contains(query)) |  
        (TestData.school.contains(query))
    ).all()

    print("🔍 Résultats trouvés :", results)  # Debugging dans les logs Docker

    return results

#  Fonction pour charger les données depuis le CSV
def load_data():
    try:
        # Vérifier si le fichier data.csv est présent
        if os.path.exists("data.csv"):
            df = pd.read_csv("data.csv")
            
            db = SessionLocal()
            for _, row in df.iterrows():
                db.add(TestData(name=row["Name"], fam_name=row["fam-name"], birth=row["Birth"], school=row["School"]))
            db.commit()
            db.close()
            print("✅ Données chargées avec succès !")
        else:
            print("❌ Le fichier data.csv n'a pas été trouvé !")
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données : {e}")

# Décommenter pour charger les données au démarrage
load_data()  # Charger les données lorsque l'application démarre
