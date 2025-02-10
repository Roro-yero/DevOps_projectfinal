# Phase 1 : Présentation du projet

Notre projet est un projet simple qui consiste à lier un backend et un frontend avec une petite base de données que j'ai moi-même créée. Cette base contient les noms et prénoms des créateurs du projet : **Baphisto** et **Romain**.

## Exécution de la Phase 1

Pour exécuter cette première phase, suivez les étapes suivantes :

1. **Cloner le projet** sur votre machine :

   ```bash
   git clonehttps://github.com/Roro-yero/DevOps_projectfinal
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

![image](https://github.com/user-attachments/assets/a86fcf19-32cd-459f-b360-25a89c9b3604)

2. **Déploiement automatique avec le pipeline** :

   - Chaque push sur la branche principale déclenche automatiquement la construction et le push des images Docker vers Docker Hub.
   - Vérifiez les logs du pipeline pour suivre l'exécution.

---

# Phase 3 : Mise en place du Continuous Deployment (CD)

Nous avons mis en place un processus de **Continuous Deployment (CD)** afin d'automatiser le déploiement de notre application après chaque mise à jour. Cependant, nous avons rencontré un problème critique :

## Problème rencontré

- Une erreur de type **CrashLoopBackOff** est survenue sur le backend. Que nous avons résolu.
- Mais nous avons tenté de déployer plusieurs fois notre application sans succès. En effet, une erreur que nous n'avons pas réussi à résoudre nous a stoppés.
- Malgré plusieurs tentatives, nous n'avons pas encore réussi à résoudre ce problème.

  ![image](https://github.com/user-attachments/assets/8af3cfac-d9f0-4d91-b637-5a23d1d18f95)



Nous continuerons à travailler sur ce problème afin d'assurer un déploiement stable de notre application.

