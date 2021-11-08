from pydantic import BaseModel
from typing import Optional,List
#none_or_str: Optional[str] = None

class ActorMod(BaseModel):
    actor_type: str
    actor_id: str

class ContentMod(BaseModel):
    content: str

class MPartsMod(BaseModel):
    text: Optional[ContentMod] = None

class MsgMod(BaseModel):
    message_parts: List[MPartsMod] = []
    app_id: str
    actor_id: str
    id: str
    channel_id: str
    conversation_id: str
    message_type: str
    actor_type: str
    created_time: str
    user_id: str
    message_source: str

class DataMod(BaseModel):
    message: Optional[MsgMod] = None

class SampleRequest(BaseModel):
    actor: Optional[ActorMod] = None
    action: str
    action_time: str
    data: Optional[DataMod] = None
