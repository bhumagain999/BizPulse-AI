# BizPulse AI - Business Analytics Assistant

An AI-powered business analytics assistant for Clover merchants, built with FastAPI backend and React frontend.

## Features

- 🤖 **AI-Powered Analytics**: Ask natural language questions about your business
- 📊 **CSV Data Analysis**: Query structured data using LangChain and Pandas
- 💬 **Clean Chat Interface**: Modern React UI with real-time responses
- 🔄 **Dual Modes**: Business Summary Q&A and CSV Data Analysis
- 🚀 **Production Ready**: Deployable to Render (backend) and Vercel (frontend)

## Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Start the server
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend-react
npm install
npm run dev
```

Visit `http://localhost:5173` to use the app!

## API Endpoints

- `POST /ask` - Business summary Q&A
- `POST /ask-data` - CSV data analysis with LangChain
- `GET /health` - Health check
- `GET /` - API info

## Project Structure

```
BizP/
├── backend/
│   ├── main.py              # FastAPI app with CORS
│   ├── helpers.py           # LLM functions and data helpers
│   ├── requirements.txt     # Python dependencies
│   ├── sample_sales.csv    # Demo data
│   └── .env.example        # Environment template
├── frontend-react/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   └── App.css         # Styling
│   └── package.json        # Node dependencies
└── README.md
```

## Deployment

### Backend (Render)
1. Push code to GitHub
2. Create Web Service on Render
3. Set root directory to `backend/`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Add `OPENAI_API_KEY` environment variable

### Frontend (Vercel)
1. Import repo to Vercel
2. Set root directory to `frontend-react/`
3. Vercel auto-detects Vite/React
4. Update API URLs for production

## Environment Variables

Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Technologies Used

- **Backend**: FastAPI, OpenAI GPT-4, LangChain, Pandas
- **Frontend**: React, Vite, CSS3
- **Deployment**: Render, Vercel

