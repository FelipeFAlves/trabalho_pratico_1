from models import City
from db import create_model, make_engine
from sqlalchemy.orm import sessionmaker

class CityDao:
    def __init__(self):
        base = create_model()
        self.CitySchema = base.classes.city
        self.CountrySchema = base.classes.country
        Session = sessionmaker(bind=make_engine())
        self.session = Session()

    def register(self, new_city_data: City):
        try:
            newCity = self.CitySchema(city=new_city_data.city, country_id=new_city_data.country_id)
            self.session.add(newCity)
            self.session.commit()       
        except Exception as e:
            self.session.rollback()
            print('Error:', e) 

    def update(self, city: str, new_city_data: City):
        try:
            current_city = self.session.query(self.CitySchema).filter_by(city=city).first()
            if (current_city):
                current_city.city = new_city_data.city
                current_city.country_id = new_city_data.country_id
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            print('Error:', e)

    def delete(self, city: str):
        try:
            current_city = self.session.query(self.CitySchema).filter_by(city=city).first()
            if (current_city):
                self.session.delete(current_city)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            print('Error:', e)

    def get(self, city: str):
        result_city = self.session.query(self.CitySchema).filter_by(city=city).first()
        if (result_city is not None):
            return City(result_city.city_id, result_city.city, result_city.country_id, result_city.last_update)
        else:
            return None

    def get_all_by_country(self, country: str):
        country_id = self.session.query(self.CountrySchema).filter_by(country=country).first()
        result_cities = self.session.query(self.CitySchema).filter_by(country_id=country_id.country_id)
        if (result_cities is not None):
            results = []
            for city in result_cities:
                results.append(City(city.city_id, city.city, city.country_id, city.last_update))
            return results
        else:
            return None