# Phase 1 : Présentation du projet

Notre projet est un projet simple qui consiste à lier un backend et un frontend avec une petite base de données que j'ai moi-même créée. Cette base contient les noms et prénoms des créateurs du projet : **Baphisto** et **Romain**.

## Exécution de la Phase 1

Pour exécuter cette première phase, suivez les étapes suivantes :

1. **Cloner le projet** sur votre machine :

   ```bash
   git clone <URL_DU_REPO>
   cd <NOM_DU_REPO>
   ```

2. **Construire et exécuter les conteneurs avec Docker Compose** :

   ```bash
   docker-compose build
   docker-compose up -d
   ```

Votre application sera alors déployée et accessible selon la configuration définie dans le `docker-compose.yml`.

---

**Note :** Assurez-vous d'avoir Docker et Docker Compose installés sur votre machine avant d'exécuter ces commandes.

# Phase 2 : Mise en place du pipeline

Nous avons mis en place un pipeline CI/CD qui nous permet de pousser automatiquement nos images Docker sur **Docker Hub**. Cela facilite le déploiement et garantit que les versions les plus récentes de nos images sont toujours disponibles.

## Exécution de la Phase 2

1. **Configurer les accès à Docker Hub** :

   - Assurez-vous d'avoir un compte Docker Hub.
   - Connectez-vous à Docker Hub depuis votre terminal :
     ```bash
     docker login
     ```

2. **Déploiement automatique avec le pipeline** :

   - Chaque push sur la branche principale déclenche automatiquement la construction et le push des images Docker vers Docker Hub.
   - Vérifiez les logs du pipeline pour suivre l'exécution.

---

**Note :** Assurez-vous que votre fichier de configuration CI/CD est correctement paramétré pour automatiser ce processus.

# Phase 3 : Mise en place du Continuous Deployment (CD)

Nous avons mis en place un processus de **Continuous Deployment (CD)** afin d'automatiser le déploiement de notre application après chaque mise à jour. Cependant, nous avons rencontré un problème critique :

## Problème rencontré

- Une erreur de type **CrashLoopBackOff** est survenue sur le backend.
- Malgré plusieurs tentatives, nous n'avons pas encore réussi à résoudre ce problème.

## Prochaines étapes

- Analyser les logs du backend pour identifier la cause du problème :
  ```bash
  kubectl logs <nom_du_pod_backend>
  ```
- Vérifier la configuration des ressources allouées (CPU/Mémoire).
- S'assurer que la connexion à la base de données fonctionne correctement.

---

Nous continuerons à travailler sur ce problème afin d'assurer un déploiement stable de notre application.

