from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import app, get_db, Base, TestData
import pytest

# Configuration de la base de données de test
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création d'une nouvelle session de test
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Remplacement de la dépendance de la base de données
app.dependency_overrides[get_db] = override_get_db

# Création de la base de données de test
Base.metadata.create_all(bind=engine)

# Client de test
client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    """ Réinitialise la base de données avant chaque test. """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_search_data_empty():
    """ Teste la recherche avec une base vide. """
    response = client.get("/search/?query=test")
    assert response.status_code == 200
    assert response.json() == []


def test_insert_and_search_data():
    """ Teste l'insertion et la recherche de données. """
    db = TestingSessionLocal()
    test_entry = TestData(name="John", fam_name="Doe", birth="2000-01-01", school="Test School")
    db.add(test_entry)
    db.commit()
    db.close()
    
    response = client.get("/search/?query=John")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "John"
    assert data[0]["fam_name"] == "Doe"
    assert data[0]["school"] == "Test School"
