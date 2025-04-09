from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from api import tasks
import database
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import logging


app = FastAPI()

app.include_router(tasks.router)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.get("/health")
def health_check(db: Session = Depends(database.get_db)):
    try:
        # Use text() to explicitly declare the SQL query
        result = db.execute(text("SELECT 1")).scalar()  # .scalar() retrieves the first column value
        if result == 1:
            return {"status": "healthy"}
        else:
            return {"status": "unhealthy"}
    except SQLAlchemyError as e:
        # Log the SQLAlchemy-specific error
        logging.error(f"Database connection error: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}
    except Exception as e:
        # Catch unexpected errors and log them
        logging.error(f"Unexpected error: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}