from sqlalchemy import select
from sqlmodel import Session
from app.database.connection import get_db
from fastapi import Depends
from app.models.planner_session import PlannerSession
from app.models.cruises_models import cruises_table
from app.models.sailings import sailings

def itinerary_service(input_id:int,db:Session):
    get_value=db.query(PlannerSession).filter(PlannerSession.user_id==input_id).first()
    
    if not get_value:
        return {"message":"there is no plannersession data so first fill the form"}
    
    if not  get_value.is_completed:
        return {"message":"first fill the all values.."}
    
    user_destination=get_value.destination
    user_date=get_value.travel_date
    user_duration_night=get_value.duration_nights
    user_budget_range=get_value.budget_range
    user_trip_style=get_value.trip_style
    
    
    get_cruise_values=db.query(cruises_table).filter(cruises_table.destination==user_destination,cruises_table.duration==user_duration_night,cruises_table.travel_style==user_trip_style).first()
    # return {
    #     "destination": get_value.destination,
    #     "duration": get_value.duration_nights,
    #     "budget": get_value.budget_range
    # }
    if not get_cruise_values:
       return {"message": "No suitable cruise found"}
   
    # return {
    #     "cruise_name": get_cruise_values.cruises_name,
    #     "destination": get_cruise_values.destination,
    #     "duration": get_cruise_values.duration,
    #     "style": get_cruise_values.travel_style
    # }
    statement = (
        select(cruises_table, sailings)
        .join(sailings, sailings.cruises_id == cruises_table.id)
        .where(
            cruises_table.destination == user_destination,
            cruises_table.duration == user_duration_night,
            cruises_table.travel_style == user_trip_style,
            sailings.embarkation_date >= user_date,
            sailings.availability > 0
        )
    )

    results = db.execute(statement).all()
    if not results:
        return {"message": "No suitable cruises found for your preferences."}
    # formatted_results = []

    # for cruise, sailing in results:
    #    formatted_results.append({
    #     "cruise_name": cruise.cruises_name,
    #     "embarkation_date": sailing.embarkation_date,
    #     "price": sailing.price
    # })

    # return formatted_results

    scored_options=[]
    for cruise,sailing in results:
        score=0
        if cruise.duration==user_duration_night:
            score+=30
        if cruise.travel_style==user_trip_style:
            score+=25
        if cruise.price == user_budget_range:
            score += 20   
        days_diff = abs((sailing.embarkation_date.replace(tzinfo=None) - user_date).days)        
        score += max(0, 15 - days_diff)
        scored_options.append((score, cruise, sailing))

    scored_options.sort(key=lambda x: x[0], reverse=True)

    best_score, best_cruise, best_sailing = scored_options[0]
        
    ai_summary = (
    f"We found the best {user_trip_style} cruise for your "
    f"{user_duration_night}-night trip to {user_destination}. "
    f"Departure on {best_sailing.embarkation_date.date()}."
     )
    return {
    "recommendation_summary": ai_summary,
    "cruise": {
        "name": best_cruise.cruises_name,
        "departure": best_sailing.embarkation_date,
        "price": best_sailing.price
    }
    }
   