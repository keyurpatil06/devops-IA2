# Customer Query Classification (AI + DevOps)

### Problem

In the banking sector, customer support teams face a large number of repetitive queries like "Check balance" or "Reset PIN", leading to increased workload and slower responses.
This project automates the classification of customer queries using a simple AI model and integrates CI/CD pipelines for smooth deployment and updates.

### Solution

We used AI + DevOps to automatically classify queries and automated deployment with GitHub Actions.

### Run Locally

1. Install Dependencies
   pip install -r app/requirements.txt
2. Train model:
   python ai_model/train_model.py
3. Start API:
   python app/app.py
3. Test API (POST):
   {"query": "I lost my debit card"}

### Live Links

- Frontend (Netlify): https://devops-ia2.netlify.app/
- Backend API (Render): https://devops-ia2.onrender.com

### DevOps and AI Tools

- Flask + Scikit-learn - AI model serving for text classification
- GitHub Actions - Automated testing, building, and deployment
- Netlify - Hosting the frontend React app
- Render - Hosting and deploying the backend