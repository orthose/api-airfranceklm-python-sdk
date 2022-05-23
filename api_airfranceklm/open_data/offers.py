import requests
from api_airfranceklm.utils import \
    Context, Connection, Passenger, CommercialCabin, BookingFlow, FareOption, funutils, RequestException, FlatteningException
from typing import Optional, List, Union, Dict
import pandas as pd


def reference_data(context: Context,
                   booking_flow: Optional[type(BookingFlow)] = None,
                   output_format: str = 'dataframe',
                   verbose: bool = False) -> Union[pd.DataFrame, Dict]:
    """
    Fournit les codes possibles pour les villes et aéroports
    :param context: Contexte de connexion à l'API Airfrance KLM
    :param booking_flow: Type de réservation (ex: loisir, travail)
    :param output_format: Type d'objet retourné par la fonction
    'json' -> Réponse complète de l'API
    'dataframe' -> Table Pandas nettoyée
    :param verbose: Afficher les paramètres de la requête
    :return: Réponse de l'API
    """
    assert output_format in ('json', 'dataframe')

    headers = context.get_headers()
    params = dict()
    if booking_flow is not None:
        params['bookingFlow']: booking_flow.name
    if verbose:
        print(params)

    url = 'https://api.airfranceklm.com/opendata/offers/v1/reference-data'
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    RequestException.check(json_data)

    if output_format == 'json':
        return json_data

    # Applanissement du JSON
    elif output_format == 'dataframe':
        try:
            flatten_data = {
                'code': [],
                'name': [],
                'location_type': []
            }
            assert len(json_data['countries']) == 1
            assert len(json_data['countries'][0]['areas']) == 1
            countries = json_data['countries'][0]['areas'][0]['countries']
            for i in range(len(countries)):
                country = countries[i]
                cities = country['cities']
                for j in range(len(cities)):
                    city = cities[j]
                    flatten_data['code'].append(city['code'])
                    flatten_data['name'].append(city['label'])
                    flatten_data['location_type'].append('CITY')
                    stopovers = city['stopovers']
                    for k in range(len(stopovers)):
                        stopover = stopovers[k]
                        flatten_data['code'].append(stopover['code'])
                        flatten_data['name'].append(stopover['label'])
                        flatten_data['location_type'].append(stopover['type'])

            return pd.DataFrame(data=flatten_data).sort_values(by=['location_type'], ascending=True).reset_index()

        except Exception:
            raise FlatteningException()


def all_available_offers(context: Context,
                         connections: List[type(Connection)],
                         passengers: List[type(Passenger)],
                         commercial_cabins: Optional[List[type(CommercialCabin)]] = [CommercialCabin.ALL],
                         booking_flow: Optional[type(BookingFlow)] = None,
                         fare_option: Optional[type(FareOption)] = None,
                         currency: str = 'EUR',
                         output_format: str = 'dataframe',
                         verbose: bool = False) -> Union[pd.DataFrame, Dict]:
    """
    Toutes les offres disponibles pour un itinéraire donné et ses passagers
    Les autres paramètres optionnels sont susceptibles de faire varier les tarifs et vols proposés
    https://docs.airfranceklm.com/docs/read/opendata/offers/POST_availableoffers_all_v1
    :param context: Contexte de connexion à l'API Airfrance KLM
    :param connections: Itinéraires désirés entre 2 lieux avec une date de départ
    :param passengers: Passagers avec leur classe d'âge renseignée
    :param commercial_cabins: Type de cabine (ex: première classe, classe économique)
    :param booking_flow: Type de réservation (ex: loisir, travail)
    :param fare_option: Option tarifaire (ex: tarif famille)
    :param currency: Devise tarifaire (ex: euros)
    :param output_format: Type d'objet retourné par la fonction
    'json' -> Réponse complète de l'API
    'dataframe' -> Table Pandas nettoyée
    :param verbose: Afficher les paramètres de la requête
    :return: Réponse de l'API
    """
    assert output_format in ('json', 'dataframe')

    headers = context.get_headers()
    params = {
        'commercialCabins': funutils.names_from_enums(commercial_cabins),
        'requestedConnections': funutils.dicts_from_objs(connections),
        'passengers': funutils.dicts_from_objs(passengers),
        'currency': currency
    }
    if booking_flow is not None:
        params['bookingFlow'] = booking_flow.name
    if fare_option is not None:
        params['fareOption'] = fare_option.name
    if verbose:
        print(params)

    url = 'https://api.airfranceklm.com/opendata/offers/v1/available-offers/all'
    response = requests.post(url, headers=headers, json=params)
    json_offers = response.json()
    RequestException.check(json_offers)

    if output_format == 'json':
        return json_offers

    # Applanissement du JSON
    elif output_format == 'dataframe':
        try:
            flatten_offers = {
                'departure_datetime': [],
                'arrival_datetime': [],
                'departure_city_code': [],
                'departure_airport_code': [],
                'departure_city_name': [],
                'departure_airport_name': [],
                'arrival_city_code': [],
                'arrival_airport_code': [],
                'arrival_city_name': [],
                'arrival_airport_name': [],
                'number_segments': [],
                'duration': [],
                'total_price': [],
                'currency': []
            }
            for i in range(len(json_offers['itineraries'])):
                # 1 seul flight_product par itinéraire ?
                assert len(json_offers['itineraries'][i]['flightProducts']) == 1
                # Tous les passagers par itinéraire ?
                assert len(json_offers['itineraries'][i]['flightProducts'][0]['passengers']) == len(passengers)
                flight_product = json_offers['itineraries'][i]['flightProducts'][0]
                flatten_offers['total_price'].append(flight_product['price']['totalPrice'])
                flatten_offers['currency'].append(flight_product['price']['currency'])
                # 1 seule connection par itinéraire ?
                assert len(json_offers['itineraries'][i]['connections']) == 1
                connection = json_offers['itineraries'][i]['connections'][0]
                flatten_offers['departure_datetime'].append(connection['segments'][0]['departureDateTime'])
                flatten_offers['arrival_datetime'].append(connection['segments'][0]['arrivalDateTime'])
                flatten_offers['departure_city_code'].append(connection['segments'][0]['origin']['city']['code'])
                flatten_offers['departure_airport_code'].append(connection['segments'][0]['origin']['code'])
                flatten_offers['departure_city_name'].append(connection['segments'][0]['origin']['city']['name'])
                flatten_offers['departure_airport_name'].append(connection['segments'][0]['origin']['name'])
                flatten_offers['arrival_city_code'].append(connection['segments'][-1]['destination']['city']['code'])
                flatten_offers['arrival_airport_code'].append(connection['segments'][-1]['destination']['code'])
                flatten_offers['arrival_city_name'].append(connection['segments'][-1]['destination']['city']['name'])
                flatten_offers['arrival_airport_name'].append(connection['segments'][-1]['destination']['name'])
                flatten_offers['number_segments'].append(len(connection['segments']))
                flatten_offers['duration'].append(connection['duration'])

            return pd.DataFrame(data=flatten_offers).sort_values(by=['total_price', 'duration'], ascending=True).reset_index()

        except Exception:
            raise FlatteningException()

