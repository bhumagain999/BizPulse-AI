import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from helpers import ask_llm, get_business_summary, validate_question, answer_csv_question

# Load environment variables
load_dotenv()

app = FastAPI(
    title="BizPulse AI API",
    description="AI-powered business analytics assistant for Clover merchants",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:4173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

class DataQuery(BaseModel):
    question: str
    agent_type: str = "sales"

@app.get("/")
def read_root():
    return {"message": "BizPulse AI API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "BizPulse AI"}

@app.post("/ask")
def ask_analytics(query: Query):
    try:
        # Validate input
        validate_question(query.question)
        
        # Get business summary
        summary = get_business_summary()
        
        # Get AI response
        answer = ask_llm(summary, query.question)
        
        return {
            "answer": answer,
            "question": query.question,
            "timestamp": "2024-01-01T00:00:00Z"  # In production, use actual timestamp
        }
        
    except HTTPException:
        # Re-raise HTTP exceptions as they're already properly formatted
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/ask-data")
def ask_data(query: DataQuery):
    try:
        validate_question(query.question)
        answer = answer_csv_question(query.question, query.agent_type)
        return {
            "answer": answer,
            "question": query.question,
            "agent_type": query.agent_type
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
