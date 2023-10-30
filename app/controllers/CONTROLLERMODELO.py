from models import City
from dao import CityDao, CountryDao

class CityController:
    def __init__(self):
        self.city_dao = CityDao()
        self.country_dao = CountryDao()

    def register_city(self, new_city_data: City):
        if (not self.country_dao.country_exists_id(new_city_data.country_id)):
            return 2

        self.city_dao.register(new_city_data)
        return 1
    
    def update_city(self, city: str, new_city_data: City):
        if (not self.country_dao.country_exists_id(new_city_data.country_id)):
            return 2
        
        if (not self.city_dao.get(city)):
            return 3
        
        self.city_dao.update(city, new_city_data)
        return 1

    def delete_city(self, city):
        if (not self.city_dao.get(city)):
            return 2
        
        self.city_dao.delete(city)
        return 1

    def get_city(self, city):
        city = self.city_dao.get(city)
        if (not city):
            return 2, None
        
        return 1, city

    def get_cities_by_country(self, country):
        if (not self.country_dao.country_exists(country)):
            return 2, None
     
        cities = self.city_dao.get_all_by_country(country)
        return 1, cities