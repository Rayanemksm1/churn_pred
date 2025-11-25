📄 Rapport d’Analyse – Modèle de Prédiction du Churn
1. Introduction

L’objectif de ce projet est de développer un modèle permettant de prédire si un client d’un service d'abonnement va résilier (churn). Pour cela, un ensemble de données de 2000 clients a été analysé, nettoyé, puis utilisé pour entraîner un modèle de classification.

Le modèle choisi est une régression logistique, intégrée dans un pipeline comprenant un encodage OneHotEncoder pour les variables catégorielles et un passage direct pour les variables numériques.

2. Description du jeu de données

Le dataset contient 11 variables :

Variables numériques :
age, subscription_length, monthly_fee, nb_support_tickets, last_login_days, is_active

Variables catégorielles :
gender, country, contract_type

Target :
churn (0 = reste, 1 = quitte)

3. Prétraitement

Un pipeline a été conçu avec deux étapes :

🔹 a) Transformation des variables catégorielles

OneHotEncoder(drop="first")
→ Pour éviter la multicolinéarité.

🔹 b) Modèle

Régression Logistique avec max_iter = 1000.

4. Performance du modèle

Les prédictions sur les données test donnent :

📌 Accuracy : 0.9525 (95.25%)
📌 Matrice de confusion
	   Prédit 0	/  Prédit 1
Réel 0	 284	     16
Réel 1	  3	         97
📌 Rapport de classification

Classe 0 : precision 0.99 – recall 0.95

Classe 1 : precision 0.86 – recall 0.97

➡ Le modèle détecte très bien les churners (Recall = 0.97).

5. Analyse des coefficients

Les coefficients de la régression logistique permettent de comprendre l’impact de chaque variable sur la probabilité de churn.

⚠️ Un coefficient positif augmente le risque de churn.
⚠️ Un coefficient négatif diminue le risque de churn.

🔽 Tableau complet des coefficients
| feature                        | coefficient   | abs_coeff    |
| ------------------------------ | ------------- | ------------ |
| **remainder__is_active**       | **-6.179502** | **6.179502** |
| cat__country_Spain             | -0.617197     | 0.617197     |
| cat__contract_type_Monthly     | 0.464258      | 0.464258     |
| cat__country_Canada            | 0.382193      | 0.382193     |
| cat__country_France            | 0.381013      | 0.381013     |
| remainder__nb_support_tickets  | 0.378537      | 0.378537     |
| cat__gender_M                  | -0.186959     | 0.186959     |
| cat__country_Italy             | 0.115727      | 0.115727     |
| cat__country_Netherlands       | 0.113506      | 0.113506     |
| cat__country_Germany           | -0.053433     | 0.053433     |
| remainder__subscription_length | -0.005823     | 0.005823     |
| remainder__age                 | 0.003968      | 0.003968     |
| remainder__last_login_days     | 0.001961      | 0.001961     |
| remainder__monthly_fee         | -0.001102     | 0.001102     |


6. Interprétation des résultats

Voici les conclusions principales :

✅ 1. is_active (coefficient -6.18)

C’est le facteur le plus important.
→ Un client actif a très peu de risques de churn.

📉 2. Country = Spain (coefficient -0.62)

→ Les clients espagnols sont moins susceptibles de churner que les autres.

📈 3. Contract type = Monthly (coefficient +0.46)

→ Les contrats mensuels présentent un risque de churn beaucoup plus élevé.
Cela est cohérent : ils sont plus flexibles, donc plus faciles à annuler.

📈 4. Country = Canada / France (+0.38)

→ Les clients canadiens et français présentent un risque plus important de churn.

📈 5. Nombre de tickets support (+0.378)

→ Plus un client a ouvert de tickets, plus il est probablement insatisfait, donc en risque de churn.

🔸 6. Gender = Male (coefficient -0.18)

→ Les hommes churnent légèrement moins.

🔸 7. Variables avec faible influence

(age, monthly fee, last_login_days, subscription_length)
→ Elles ont un faible impact sur la probabilité de churn.

7. Conclusion générale

Le modèle est performant (95% de précision) et fournit des informations stratégiques :

🔑 Principaux facteurs de churn :

Contrat mensuel

Canada / France

Nombre élevé de tickets support

Inactivité

🔐 Principaux facteurs de rétention :

Être un client actif

Résider en Espagne

Être un client homme (impact faible)

8. Applications possibles

✔ Détection automatique des clients à risque
✔ Campagnes marketing ciblées
✔ Programme de fidélisation pour les clients mensuels
✔ Analyse du support client pour comprendre les sources d'insatisfaction
























































