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
	Prédit 0	Prédit 1
Réel 0	284	16
Réel 1	3	97