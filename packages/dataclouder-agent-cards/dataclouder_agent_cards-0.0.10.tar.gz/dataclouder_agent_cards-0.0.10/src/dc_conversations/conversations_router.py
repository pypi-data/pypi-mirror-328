from typing import Any
from bson import ObjectId
from dc_conversations.conversation_models import TranslateCardDTO
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from .agents import conversation_agents

# from app.database.mongo import db

from dataclouder_core.db.mongo import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix='/api/conversation', tags=['Conversation Card AI'])

from json import JSONEncoder
from datetime import datetime
from bson import ObjectId  # If you're also dealing with MongoDB ObjectIds

class MongoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)
    


@router.post("/translate_card")
async def translate_conversation(
    request: TranslateCardDTO, 
):
    # fb_admin.verify_token(token)    
    conversation_card = db.get_collection('conversation_cards').find_one({'_id': ObjectId(request.idCard)})
    caracterData = conversation_card['characterCard']['data']
    print(caracterData)
    response = await conversation_agents.translate_convenversation_card(caracterData, request.currentLang, request.targetLang)
    print(response.data)
    return response.data
    # return {"status": "serving"}


