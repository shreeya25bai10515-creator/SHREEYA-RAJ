# SHREEYA-RAJ
# FinGuard: Personal Finance Manager & Fraud Detection

##  Overview
FinGuard is a web application that helps users manage their finances while detecting suspicious transactions using machine learning. It combines expense tracking with real-time fraud protection.

##  Features
- ** Financial Tracking**: Add income/expenses with categories
- ** Dashboard**: View financial summary and analytics
- ** Fraud Detection**: ML-powered suspicious transaction alerts
- ** User Management**: Secure authentication and profiles

##  Technologies
- **Frontend**: React.js, Chart.js, Axios
- **Backend**: Node.js, Express.js, JWT
- **Database**: PostgreSQL
- **ML Service**: Python, Flask, Scikit-learn

### Installation
```bash
# Clone repository
git clone https://github.com/your-username/finguard.git
cd finguard

# Backend setup
cd backend
npm install
cp .env.example .env
# Configure database in .env file

# Database setup
createdb finguard_db
npm run migrate

# ML Service setup
cd ../ml-service
pip install -r requirements.txt
python train_model.py

# Frontend setup
cd ../frontend
npm install
```

### Running the Application
```bash
# Terminal 1 - Start ML Service
cd ml-service
python app.py

# Terminal 2 - Start Backend
cd backend
npm run dev

# Terminal 3 - Start Frontend
cd frontend
npm start
```

Access the app at: `http://localhost:3000`

##  Testing
```bash
# Backend tests
cd backend && npm test

# Frontend tests  
cd frontend && npm test

# ML tests
cd ml-service && python -m pytest
```
