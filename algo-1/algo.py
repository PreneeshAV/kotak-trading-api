import pathlib
import json
from ks_api_client import ks_api

filepath = pathlib.Path(__file__).resolve().parent.parent
configFile= str(filepath)+"/common/config.json"

with open(configFile) as config_file:
    config = json.load(config_file)


kotak = ks_api.KSTradeApi(access_token=config['kotak_access_token'],\
                        userid=config['kotak_user'],\
                        consumer_key=config['kotak_consumer_key'], \
                        ip="127.0.0.1", app_id="")


kotak.one_time_token = config['kotak_one_time_token']
kotak.session_token = config['kotak_session_token']

print(kotak.positions(position_type = "TODAYS"))



