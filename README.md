# IR-Search-Engine is Information Retrieval Search Engine

This repository contains the code for a simple search engine built using [Backend Framework, Flask] for the backend and Flutter for the frontend. The search engine is designed to work with two datasets: TREC Total Recall Track (TREC-TOT) and Webis-Touche-2020.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Datasets Used](#datasets-used)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Evaluation](#evaluation)
- [Team Members and Contributions](#team-members-and-contributions)
- [References](#references)

## Project Overview

This project implements a simple search engine designed to retrieve information from two distinct datasets: TREC Total Recall Track (TREC-TOT) and Webis-Touche-2020. The engine leverages fundamental Information Retrieval (IR) techniques, including text preprocessing, TF-IDF weighting, and cosine similarity, to facilitate effective document retrieval.

The backend of the search engine is powered by Flask, a Python web framework, while the frontend is developed using Flutter, providing a cross-platform user interface. The system is architected using a Service-Oriented Architecture (SOA) to ensure modularity and maintainability.

## Features

- Search functionality for two different datasets.
- Preprocessing of text data (tokenization, stemming, stop word removal).
- Spell correction for user queries.
- TF-IDF model for document indexing and retrieval.
- User-friendly interface built with Flutter.

## Datasets Used

1. **TREC Total Recall Track (TREC-TOT):** [Provide a link to the dataset]
    - Description: This dataset comprises a large collection of Wikipedia documents, focusing on retrieving all relevant documents for a given topic. Each document includes attributes like title, Wikidata classes, text content, sections, and infoboxes.

    - Example Document:
        ```
        TipOfTheTongueDoc(doc_id='330', page_title='Actrius', wikidata_id='Q2823770', 
        wikidata_classes=[['Q11424', 'film']], text='Actresses (Catalan: Actrius) is a 1997 ...')
        ```





2. **Webis-Touche-2020:** [Provide a link to the dataset]
    - Description: This dataset consists of posts from the Debate.org platform, an online debating forum. Each document includes the post's text, the debate topic's title, and the author's stance (pro or con) on the topic.

    - Example Document:
        ```
        BeirToucheDoc(doc_id='c67482ba-2019-04-18T13:32:05Z-00000-000', 
        text='My opponent forfeited every round. None of my arguments were answered. ...', 
        title='Contraceptive Forms for High School Students', stance='CON', 
        url='https://www.debate.org/debates/Contraceptive-Forms-for-High-School-Students/1/')
        ```

## System Architecture

This project follows a Service-Oriented Architecture (SOA) approach. The system is divided into independent and reusable services:

- **Preprocessor Service:** Cleans and preprocesses text data.
- **Spell Corrector Service:** Corrects spelling errors in user queries.
- **Document Service:** Manages the storage and retrieval of documents from the database.
- **Model Service:** Handles the saving and loading of TF-IDF models.
- **Search Engine:** Orchestrates the other services to perform the search operation.

**Communication between Services:**

- Services communicate through well-defined APIs.
- The system uses the Flask framework to create RESTful APIs.

**System Architecture Diagram:**

``` mermaid
graph LR
    subgraph Frontend using Flutter
        A[User Interface]
    end
    subgraph Backend in Python
        B[API Endpoints using Flask]
        C[Search Engine]
        D[Preprocessor Service]
        E[Spell Corrector Service]
        F[Document Service]
        G[Model Service]
        H[Database using MySQL] 
    end
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    F --> H
    G --> H
```


## Getting Started

### Prerequisites

**For the Backend:**

- **Python 3.7+:**  [https://www.python.org/downloads/](https://www.python.org/downloads/) 
- **pip:** (Usually installed with Python) - Used to install Python packages.
- **virtualenv (Recommended):**  [https://virtualenv.pypa.io/en/latest/](https://virtualenv.pypa.io/en/latest/) - To create a virtual environment and manage dependencies separately for this project.
- **MySQL Server:** [https://www.mysql.com/](https://www.mysql.com/) - You'll need a running MySQL server to store your document data.
- **MySQL Client:** You'll need a way to connect to and interact with your MySQL server (often included with MySQL Server installation, or you can use tools like MySQL Workbench).

**For the Frontend:**

- **Flutter SDK:** [https://flutter.dev/docs/get-started/install](https://flutter.dev/docs/get-started/install) - Follow the instructions for your operating system.
- **Android Studio or VS Code:** (Or any other Flutter-supported IDE) - For developing and running the Flutter app.
- **Android Emulator or Device / iOS Simulator or Device:** To run and test your Flutter app.

**Other (Potentially Needed):**

- **Git:** [https://git-scm.com/](https://git-scm.com/) - For cloning the repository (if you're using one).
- **Text Editor:** (Like VS Code, Sublime Text, Atom) - For working with the code.

**Python Libraries (Installed via pip):**
```bash
pip install Flask Flask-SQLAlchemy nltk scikit-learn spellchecker mwparserfromhell joblib pandas matplotlib wordcloud ir_datasets ir_measures
```

- **Flask:** Web framework for the backend.
- **Flask-SQLAlchemy:** Easier database interactions with Flask.
- **NLTK:** Natural Language Toolkit for text processing (tokenization, stemming, stop words).
    - **Download NLTK Data:** After installing `nltk`, run these commands in a Python environment:
        ```python
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet') 
        ```
- **scikit-learn:** Machine learning library (used for TF-IDF and cosine similarity).
- **spellchecker:** For spell correction.
- **mwparserfromhell:** Parses MediaWiki markup (likely for cleaning Wikipedia data).
- **joblib:** Saves and loads Python objects (like machine learning models).
- **pandas:** Data manipulation and analysis using DataFrames.
- **matplotlib:** Creates visualizations (plots, graphs).
- **wordcloud:** Generates word clouds.
- **ir_datasets:** Loads information retrieval datasets (like TREC-TOT).
- **ir_measures:** Evaluates information retrieval systems.


**Flutter Packages (Installed via pubspec.yaml):**

- **http:** `dependencies: http: ^1.2.1` (or latest version) - For making API requests to the backend.

### Installation

1. Clone the repository: `git clone https://github.com/YasserBar/IR-Search-Engine.git`
2. Navigate to the project directory: `cd IR-Search-Engine`
3. Install backend dependencies: `pip install -r requirements.txt`
4. Install Flutter dependencies: `flutter pub get`
5. **Set up the database:**
   - **Make sure you have MySQL Server running.** If not, download and install it from [https://www.mysql.com/](https://www.mysql.com/) and follow the setup instructions.
   - **Create the Database:**
     - Open a MySQL client (e.g., MySQL Workbench, command line).
     - Run the following command to create the database:
       ```sql
       CREATE DATABASE ir_search_engine;
       ```
   - **Configuration:** The database connection is already configured in the `config.py` file. 

6. **[Continue with other installation steps, like running migrations if needed]**.

### Running the Application

1. Start the backend server: `python app.py` (or your equivalent command)
2. Run the Flutter app: `flutter run`

## Project Structure
```markdown
IR-Search-Engine/
├── backend_simple_search_engine/ # Backend code (Flask)
│ ├── app.py # Main Flask application file
│ ├── __init__.py # initial Flask application file
│ ├── requirements.txt # Python dependencies
│ ├── services # Folder services
│ └── models # Folder where store tf-idf matrixes and vectorizers files
│
├── frontend/ # Flutter frontend code
│ ├── lib/ # Main Flutter code
│ │ ├──api_service.dart  # Connect with backend 
│ │ ├──search_screen.dart # UI
│ │ └──main.dart # Root frontend app
│ └── pubspec.yaml # Flutter dependencies
│
├── notebooks/ # Jupyter notebooks (optional)
│ └── jubyter_notebook.ipynb
└── README.md # This file
```
## Evaluation

The performance of the search engine was evaluated using the following metrics:

- Mean Average Precision (MAP)
- Recall@10
- Precision@10
- Mean Reciprocal Rank (MRR)


## Team Members and Contributions

- Yasser Barghouth `me`

## References

- TREC Total Recall Track Dataset

- Webis-Touche-2020 Dataset

- Flask framework

- NLTK library

- Scikit-learn library
