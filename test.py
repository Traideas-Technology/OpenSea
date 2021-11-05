from datetime import datetime
import json









def data_parser():
    now = datetime.now()
    f = open('data.json', )
    data = json.load(f)
    HH = int(data['time']["HH"])
    mm = int(data['time']["mm"])
    cHH = int(now.strftime("%H"))
    cmm = int(now.strftime("%M"))
    HH = HH+cHH
    mm = mm+cmm
    dict = {"time": f"{HH}:{mm}", "amount": data['weth']}
    return dict

print(data_parser())