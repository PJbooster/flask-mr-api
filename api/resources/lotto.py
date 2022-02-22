from flask_restful import Resource, reqparse
import requests
import json

parser = reqparse.RequestParser()

parser.add_argument('game', type=str, location='args', required=True, help="game argument is required!")
parser.add_argument('index', type=int, location='args', required=True, help="index argument is required!")
parser.add_argument('size', type=str, location='args', required=True, help="size argument is required!")
parser.add_argument('sort', type=str, location='args', required=True, help="sort argument is required!")
parser.add_argument('order', type=str, location='args', required=True, help="order argument is required!")


LOTTO_API_URL = 'https://www.lotto.pl'


def api_url_builder(game, index, size, sort, order='DESC'):
    return LOTTO_API_URL + '/api/lotteries/draw-results/by-gametype?game=' + game + '&index=' + index + '&size=' + size + '&sort=' + sort + '&order=' + order

class Lotto(Resource):
    def get(self):
        args = parser.parse_args()

        url = api_url_builder(args['game'], str(args['index']), args['size'], args['sort'], args['order'])
        headers = {'user-agent': 'my-app/0.0.1'}

        lotto_request = requests.get(url, headers=headers)

        return lotto_request.json()