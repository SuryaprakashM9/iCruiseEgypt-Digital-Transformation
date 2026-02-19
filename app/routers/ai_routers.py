from typing import List

from fastapi import APIRouter,Depends
from sqlmodel import Session
from app.database.connection import get_db
from  app.schemas.user_input import user_input
from app.models.ai_intent_model import ai_intents
from app.models.planner_session import PlannerSession
from app.models.cruise_metadata import cruise_metadata
import nltk
import re
from  nltk.corpus import stopwords
from app.schemas.wizaard import wizards
router=APIRouter()
nltk.download('stopwords')


@router.post("/ai/parse")
def search(input:user_input,db:Session=Depends(get_db)):
    
    temp_id=input.user_id
    temp_value=input.user_value
    
    text=temp_value.lower()
    text=re.sub(r'[^\w\s]', '', text)
    stop_words=set(stopwords.words("english"))
    words=text.split()
    filter_words=[w for w in words if w not in stop_words]
    
    final_text=' '.join(filter_words)
    # temp=[final_text]
    # return final_text
    
    booking_keywords = ["trip", "cruise", "book", "travel"]
    support_keywords = ["help", "problem", "issue", "support"]
    explore_keywords = ["info", "explore", "know", "learn"]
    
    booking_count=0
    support_count=0
    explore_count=0
    for w in filter_words:
       if w in booking_keywords:
            booking_count+=1
        #    return booking_count
       elif w in support_keywords:
           support_count+=1
       elif w in explore_keywords:
            explore_count+=1
    counts={"booking":booking_count,"support":support_count,"explore":explore_count}
    detect_intent=max(counts,key=counts.get)
    
    total_match=sum(counts.values())
    if len(filter_words) > 0:
        confidence=total_match/len(filter_words) 
    else :
        confidence=0
    
    new_records=ai_intents(
        user_id=temp_id,
        raw_text=temp_value,
        detected_intent=detect_intent,
        confidence_score=confidence
    )
    
    db.add(new_records)
    db.commit()
    db.refresh(new_records)
    
    return new_records


@router.post("/destination",response_model=wizards)#this is used to putput format

def  wizard(user_inputs:wizards,user_id:int,db:Session=Depends(get_db)):
    
     new_value=db.query(PlannerSession).filter(PlannerSession.user_id==user_id).first()
     
     if not new_value:
         new_value=PlannerSession(user_id=user_id)
         db.add(new_value)
         db.commit()
         db.refresh(new_value)
         
         
     if user_inputs.Destination is not None:
         new_value.destination=user_inputs.Destination     
         
     if user_inputs.tavel_date is not None:
         new_value.travel_date=user_inputs.tavel_date
      
     if user_inputs.Duration is not None:
         new_value.duration_nights=user_inputs.Duration
     if user_inputs.Budget is not None:
         new_value.budget_range=user_inputs.Budget
         
     if user_inputs.Trip is not None:
         new_value.trip_style=user_inputs.Trip
         
     db.commit()
     db.refresh(new_value)
                   
     return user_inputs 
 
@router.get("/")

def get_values(user_value:str,db:Session=Depends(get_db)):
    values=db.query(cruise_metadata).filter(cruise_metadata.key==user_value).first()
    if not values:
        return {"message":"no values"}
    return values

        

    
    
    
    