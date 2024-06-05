# IR-Search-Engine
Search Engine with Python, NLTK, and Scikit-learn



System Architecture Diagram
Here's a visual representation of the system architecture:

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