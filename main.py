import uvicorn

from typing import Optional
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models import Base, Planning
from databse import SessionLocal, engine
from datetime import datetime
from fastapi.templating import Jinja2Templates

# should use migrations using lib like alembic to manage db changes
Base.metadata.create_all(bind=engine)
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Dependency for database injection for every request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def fetch_db_records(
        request: Request,
        db: Session = Depends(get_db),
):
    try:
        model_data = db.query(Planning).all()
        for data in model_data:
            data.start_date = datetime.strptime(data.start_date, "%m/%d/%Y %H:%M").strftime('%m/%d/%Y %I:%M %p')
            data.end_date = datetime.strptime(data.end_date, "%m/%d/%Y %H:%M").strftime('%m/%d/%Y %I:%M %p')
            # need to figure out json conversion from string
            print(data)
        context = {"request": request, "model_data": model_data}
        return templates.TemplateResponse("index.html", context)
    except Exception as ex:
        print(ex)


@app.get('/fetch')
def fetch_records(
        request: Request,
        query: Optional[int],
        db: Session = Depends(get_db),
):
    model_data = db.query(Planning).limit(query)
    context = {"request": request, "model_data":model_data}
    return templates.TemplateResponse("index.html", context)


@app.get('/search')
def search_records(
        request: Request,
        query: Optional[str],
        db: Session = Depends(get_db),
):
    model_data = db.query(Planning).filter(Planning.original_id==query)
    context = {"request": request, "model_data":model_data}
    return templates.TemplateResponse("search_items.html", context)


@app.get('/sort')
def sort_records(
        request: Request,
        db: Session = Depends(get_db),
):

    model_data = db.query(Planning).order_by(Planning.id.desc())
    context = {"request": request, "model_data": model_data}
    return templates.TemplateResponse("sort_items.html", context)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)