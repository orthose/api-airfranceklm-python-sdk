from api_airfranceklm.open_data import offers
import api_airfranceklm.utils as afkl
import datetime
import pickle


all_offers_json = offers.all_available_offers(
    context=afkl.Context(api_key_file='./api_key.txt'),
    connections=[afkl.Connection(
        departure_date=datetime.date(2022, 5, 25),
        departure_location=afkl.Location(type=afkl.LocationType.CITY, code='PAR'),
        arrival_location=afkl.Location(type=afkl.LocationType.CITY, code='NBO'))],
    passengers=[afkl.Passenger(
        id=0, type=afkl.PassengerType.ADT, birth_date=datetime.date(2000, 1, 1))],
    commercial_cabins=[afkl.CommercialCabin.FIRST],
    booking_flow=afkl.BookingFlow.LEISURE,
    fare_option=afkl.FareOption.FAMILY,
    output_format='json',
    verbose=True
)

print(all_offers_json)
with open('./example_all_offers', 'wb') as f:
    pickle.dump(all_offers_json, f)

all_offers_pandas = offers.all_available_offers(
    context=afkl.Context(api_key_file='./api_key.txt'),
    connections=[afkl.Connection(
        departure_date=datetime.date(2022, 5, 25),
        departure_location=afkl.Location(type=afkl.LocationType.CITY, code='PAR'),
        arrival_location=afkl.Location(type=afkl.LocationType.CITY, code='LON'))],
    passengers=[afkl.Passenger(
        id=0, type=afkl.PassengerType.ADT, birth_date=datetime.date(2000, 1, 1))],
    commercial_cabins=[afkl.CommercialCabin.FIRST],
    booking_flow=afkl.BookingFlow.LEISURE,
    fare_option=afkl.FareOption.FAMILY,
    output_format='dataframe',
    verbose=True
)

print(all_offers_pandas.to_string())
