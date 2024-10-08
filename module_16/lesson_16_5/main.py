from fastapi import FastAPI, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

messages_db: List = []


class Message(BaseModel):
    id: Optional[int] = None
    text: str


@app.get("/")
def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        'message.html',
        {'request': request, 'messages': messages_db}
        )


@app.get('/message/{message_id}')
def get_message(request: Request, message_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse(
            'message.html',
            {'request': request, 'message': messages_db[message_id]}
            )
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.post("/")
def create_message(request: Request, message: str = Form()) -> HTMLResponse:
    message_id = len(messages_db)
    messages_db.append(Message(id=message_id, text=message))
    return templates.TemplateResponse(
        'message.html',
        {'request': request, 'messages': messages_db}
        )


@app.put("/message/{message_id}")
def update_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return "Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/message/{message_id}")
def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/")
def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"
