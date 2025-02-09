-- Création de la table avec les bonnes colonnes
CREATE TABLE IF NOT EXISTS test_data (
    id SERIAL PRIMARY KEY,
    name TEXT,
    fam_name TEXT,
    birth Text,
    school TEXT
);

-- init-db.sql
COPY test_data(name, fam_name, birth, school)
FROM '/docker-entrypoint-initdb.d/data.csv'
WITH (FORMAT csv, HEADER true);

