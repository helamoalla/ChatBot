# ChatBot avec Mistral et Streamlit

Ce projet implémente une application de chat en utilisant un modèle pré-entraîné **Mistral-7B** hébergé sur Hugging Face et une interface utilisateur avec **Streamlit**.

## Modèle pré-entraîné : Mistral
- **Mistral-7B-Instruct-v0.3** : Un modèle de langage de pointe basé sur des réseaux neuronaux transformateurs. Il a été conçu pour des tâches de compréhension et de génération de texte.Ce modèle est open-source, ce qui signifie qu'il est librement accessible et utilisable par la communauté. Il est hébergé sur Hugging Face et peut être utilisé pour des projets variés nécessitant des solutions d'intelligence artificielle avancées.
- **Streamlit** : Une bibliothèque Python open-source qui permet de créer facilement des applications web interactives. Elle est idéale pour prototyper et déployer rapidement des applications liées au machine learning et au traitement de texte.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez installer les dépendances avec `requirements.txt`.

### Étapes :

1. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

2. **Configurer votre clé API Hugging Face** :
    - Rendez-vous sur le [site de Hugging Face](https://huggingface.co) et connectez-vous à votre compte.
    - Cliquez sur votre profil dans le coin supérieur droit, puis allez dans **Settings -> Access Tokens** et générez une nouvelle clé API.
    
3. **Ajouter la clé API dans le code** :
   - Ouvrez votre fichier `chat.py` et ajoutez votre clé API à l'emplacement prévu :
   
    ```python
    api_key = 'INSERT_API_KEY'
    ```

4. **Exécution du projet** :
    Pour lancer l'application, exécutez la commande suivante dans votre terminal :
    
    ```bash
    python -m streamlit run chat.py
    ```

    Cela ouvrira l'application de chat dans votre navigateur où vous pourrez interagir avec le modèle Mistral via une interface conviviale.

---

N'hésitez pas à ajouter des captures d'écran pour expliquer comment ajouter la clé API dans le fichier de configuration et personnaliser votre projet en conséquence !
