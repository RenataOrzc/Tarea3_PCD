from sqlalchemy import Column, Integer, String, Text
from database import Base 
import json 


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    recommendations = Column(Text, nullable=True)
    zip_code = Column(String, nullable=True)

    def set_recommendations(self, recommendations:list):
        self.recommendations = json.dumps(recommendations)

    def get_recommendarions(self):
        return json.loads(self.recommendations) if self.recommendations else []