# Customer Query Classification (AI + DevOps)

### Problem

Banking support teams face high volumes of repetitive queries (e.g., "Check balance", "Reset PIN").

### Solution

We used AI + DevOps to automatically classify queriesand automated deployment with GitHub Actions and Docker.

### Run Locally

1. Train model:
   python ai_model/train_model.py
2. Start API:
   python app/app.py
3. Test API (POST):
   {"query": "I lost my debit card"}

### DevOps and AI Tools

- GitHub Actions (CI/CD)
- Docker (Containerization)
- Flask (Serving model)
- Scikit-learn (Text classification)
