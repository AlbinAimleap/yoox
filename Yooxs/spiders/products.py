from typing import Iterable
import scrapy
from scrapy import Request, FormRequest
from scrapy.http import JsonRequest
from pprint import pprint
import json
import pandas as pd
from datetime import datetime
import re

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'optimizelyEndUserId=oeu1727511452719r0.9518978653073176; LAYERFIRSTVISIT=LAYERFIRSTVISIT=True; NAVIGATED=1; USERINFO=SESSO=D&SESSOBAMBINO=D; OLDVISIT=1; tc_YAB_test=UpgradeV1vsV2_B; _ALGOLIA=anonymous-c3dedd5e-e08f-432f-a934-39cc6207ad90; mn_u=5.1245425455.1727511455636; rskxRunCookie=0; rCookie=zcmcasyv6l3ryugbtfcoem1lvpucz; _gcl_au=1.1.1877572904.1727511456; _mibhv=anon-1727511456398-4076264761_9612; _ga=GA1.1.27234611.1727511457; _cs_c=1; _scid=kzCBGEOtvtJwc344HVr_gblFTZKHn-1g; __lt__cid=009a4aaa-2add-4f97-9b4c-633686952176; _yjsu_yjad=1727511458.3eb94d63-4aad-4b11-960e-258503eb06c2; ORA_FPC=id=b6903cb9-e9c2-41e3-a674-b22084f071a4; _tt_enable_cookie=1; _ttp=ac6jYB4vPy4FqxDWRE_L3gpwYrG; _fbp=fb.1.1727511459164.699433888471550982; fita.sid.yoox=Jb-bLWZcw8KkFUZ2UcrRPDNwqqxz75Zg; TCPID=12410212542793771456; TC_PRIVACY=0%40006%7C66%7C645%401%2C2%2C3%2C4%2C5%40%401727764542508%2C1727764542508%2C1761460542508%40; TC_PRIVACY_CENTER=1%2C2%2C3%2C4%2C5; _pin_unauth=dWlkPVlXSTFOREV4WWpndE9UUmtNUzAwTXpWbExXSXpPR0V0TVRkaVptWTJOemd4WmpnNA; _ScCbts=%5B%5D; GENERIC_USER_ID=d3143dc6-2e0d-4bdf-b8ff-ba761c7fcd0e; _sctr=1%7C1728325800000; __gads=ID=5427474f53b4d792:T=1727764542:RT=1728580735:S=ALNI_MavOMmcMQShyXIEGD6elkHktDktJQ; __gpi=UID=00000f2c81787579:T=1727764542:RT=1728580735:S=ALNI_MYHZkEqsvXNZ6lykGL5Hdh_4IqTUw; __eoi=ID=db6bb31fc86728a4:T=1727511489:RT=1728580735:S=AA-AfjZ_kmRjkTTIzVHjladnRWLD; YEDGESESSION=5f39201758c43400962d0b6726010000d39a0000; PIM-SESSION-ID=qQ5v8D9Axtvw0GxX; FEATURE_DISABLED_BAYNOTE=true; SESSIONS=FIRSTTIMEUSER=0; rxVisitor=1728785818872HBIEDLVAFU8G7MVTIPB6UGJU18OBDU65; dtSa=-; VISIT=TSKAY=3FD17CD7&NAZIONE=UNITED+STATES&ID%5FNAZIONE=38&ID%5FMERCATO=19&SIGLA%5FVALUTA=%24&CURRENCYCODE=USD&REFERENCE%5FCURRENCYCODE=USD&ID%5FMERCATO%5FPER%5FLISTINO=19&MERCATO%5FPATH=%2fus%2f&VALUTA%5FID=22&DYN%5FPATH=%2fus%2f&SITE%5FCODE=YOOX_US&ANONYMOUS%5FCHECKOUT=True&NAZIONE%5FISO=US&WAREHOUSES=2715%2c2805%2c4800%2c20611%2c21140%2c70%2c271&TWOLETTERISOCODE=EN&LASTQUERY=; ABTEST=%7b%22AbTests%22%3a%5b%7b%22Name%22%3a%22SmsMultiChannel%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%2c%7b%22Name%22%3a%22myooxNew%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%2c%7b%22Name%22%3a%22paypalExpressNewHead%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%5d%2c%22Reloaded%22%3afalse%2c%22ReloadedTime%22%3anull%7d; TrackingNavigation=Token=5484420b-0e9d-4039-b168-f38fae76d31b; SizeFitTracking=Token=92e53382-131f-47b0-b49f-8694af28ee2f; _cs_cvars=%7B%221%22%3A%5B%22Subsection%22%2C%22women%22%5D%2C%222%22%3A%5B%22Country%20Code%22%2C%22US%22%5D%2C%223%22%3A%5B%22Language%20Code%22%2C%22EN%22%5D%2C%224%22%3A%5B%22Currency%22%2C%22USD%22%5D%2C%227%22%3A%5B%22AB%20Test%22%2C%22SmsMultiChannel_ON%2CmyooxNew_ON%2CpaypalExpressNewHead_ON%22%5D%2C%228%22%3A%5B%22Gender%22%2C%22D%22%5D%2C%229%22%3A%5B%22Page%22%2C%22women%3AItem%22%5D%2C%2210%22%3A%5B%22Page%20Type%22%2C%22Item%22%5D%2C%2211%22%3A%5B%22Prod%20Cod%208%22%2C%2249535591%22%5D%2C%2212%22%3A%5B%22Prod%20Cod%2010%22%2C%2249535591QF%22%5D%2C%2213%22%3A%5B%22Prod%20Brand%22%2C%22FRANKIE%20MORELLO%22%5D%2C%2214%22%3A%5B%22Prod%20Cat%22%2C%22Blazers%22%5D%2C%2215%22%3A%5B%22Prod%20Cat%20Code%22%2C%22gcc%22%5D%2C%2217%22%3A%5B%22Prod%20Macro%20Cat%22%2C%22Coats%20%26%20Jackets%22%5D%2C%2218%22%3A%5B%22Prod%20Macro%20Cat%20Code%22%2C%22cpspll%22%5D%2C%2219%22%3A%5B%22Area%20Dept%22%2C%22women%22%5D%2C%2220%22%3A%5B%22Env%20Channel%22%2C%22web%22%5D%7D; QSI_HistorySession=https%3A%2F%2Fwww.yoox.com%2Fus%2F49535591QF%2Fitem%23dept%3Dwomen%26queryID%3Dundefined%26cod10%3D49535591QF%26sizeId%3D-1~1728785823871; dtCookie=v_4_srv_19_sn_45D70B773AB15A66C44CA3985FFDE076_app-3A8caa4d99ff5d944a_1_ol_0_perc_100000_mul_1; _abck=2DF5E5ACA8357BBDB30FD71AE5380E92~0~YAAQRAHARW50w2+SAQAAcS/HiQzUpfr8R9TBvxkNk0wWGk9QIL51JPADuG/rLvRSOVBSUnRK74RJvVLZ2nNV0F4lTJtMH2vmeKv/cLWO+DKiC4tlxZfsSYaxDUPL+ci0mbyDJeAuxfvawcQqloVOQNc5MzWXSdHtZ7VTv7UXldg+Mwfq8BkHul3gbXOKOETu747npEIylQF8KGwcePwzpxshcMDNWL8Uv2KmC9pW2iv5/YjBEI8uL/QBhPOZbqoq5qZxUkRNy83i1hSLhdAtAJMHfhQbetEi5cRhc12pVOn3JUb1bH82Ft0m3NO/br5BYr5cFe0/yBVGi8kkTKD6p4wiwGFfM3eE0Ox46NTYQFvEc4o+e5rRtszxV3Lsnl9uM37Z9MN9L0BXzctsScf1umJFcKEQGOu9zEnz9a6L2IDmoDw6PvQgsMpCTxSP8FjB7yGd0+3nqA==~-1~-1~1728891985; AKA_A2=A; bm_ss=ab8e18ef4e; bm_so=356D153C0759E14016EAA401C45D69286792FC833871AD09A7A4A3D97DCAD26A~YAAQRAHARWB4w2+SAQAAT+fLiQGAiaW7S2ydtePafQdZ8VBF/5Jaknb5YNrCZr0lx/n+gnOkCvUJv7hq09PzmMq3rPHb1IelyEHLrMy151M9sFO/6npi8edaeLZNcJoPy0kDQ4Tv3gdK4JMVPqrxSSejyDy17xH8oyE8TxR7mOROsLYRYYKXOj/VIvfPRMdbYvbFw/LAX2I9Bi7QB3FeA9THfZ6LwhAdpRFxKCFhtHKIMJ2PxDRMf0UmDmXIaW4RC1lqGoxd8CkD42pMbgyUcNeDH4mXy3Bqpq0M05CFJytjWi4DwdPIDEIzefVAuyQzb0hTjFhkHuV54N3srjJ3yhaenegZDzeFBLDJAdqPoG07UVNiPhDbOEDjj24pgjNNyQT8vIu8MLZL0tn99NWSWUMEONgJNHHeYv/9kUVL//ANYhv/r8SfaShTpIRFgMBsqN0FgJJiyhI36eA=; bm_sz=E761B96B78761414BE6330108B4E54AF~YAAQRAHARWF4w2+SAQAAT+fLiRk0aEA5ZDy989x++VuNrvdiS5cQAKKP8JHWIUg99uY9u0M/7gmi2R3OhNAX1uYvLkTDdSTYGVJuVpf95sdEnoFVteI2Mx+/rlMoPOfe46p6xyTVL9c5vavldGkjUQVJjTujT4SQNzzuYWubclbLkVCkIVawSqiwyiYkdNx3ne62hSgyZ/yYCxSlN0Quyn5HSQjP7KlCBvdRYNSPa5gvmETTNtxFbaNzUCBxYq8JP5u0BjRfkCInxVs443tYMGbEXWFaxIfajSdjQ6CIB2ChuVr5V9xpeJ6Bl3HtMbLKovrvn0Ki2RCEx8WjV/6JvVCVZeVo3qA/NMn3YTMGqgIoNts9DDmKjEn4588UXrQsr8ITAmTubrJ1/E6zAxRIuxs=~3228997~3356979; bm_s=YAAQRAHARX14w2+SAQAA0u/LiQIsuz/Rq1RHrXx5QWJd5TtRFaOXclbcOUL9zvPiHM73mwi6nW9STxqCDDF56EK0mbrnihl5XxSGxnv6Ao4pPejrsYR2sF+6pm2Ob0gdHmOgfRhPx2TnTwG08wlT8UoJBPL11hVhZtsr6xkRIFTqcjjUx1WBYjauI6llaQ8IoPywQ7OMslfx9JANsPT0/YyYNdNOaRxmVvqn6nltDuKcZf9tcYO3+RfuRWs8YxDfLDrWZuMq90h/ToMlt5kGYXmXJrPYaXsGiATucb/udV97IPBcF3F/YEPedHTx5zg6vMPqGSiKFl1DQrvJWOCv2YVpFtg=; ak_bmsc=D13911B950C9D40998A241E2A739D0C5~000000000000000000000000000000~YAAQRAHARYB4w2+SAQAAe/DLiRnbiDmeU7yaDRZ0Yu+ov7FVacBmIRLTcGj+IFgvlUIjA71+2Sj7qem0rl3ainWVJKKJuCU+8AxIBJpuTXNnULziNc1mcXq0uRYIIC90jvAvorach30Ff4pa2Ghlo22EBAruB5WtYyzkyxjsor1OHqhuu/vwgRN1LxXDAHjocd707ZTvi42qY9NkNkcHgtIVGOt79aCzMrqqs27thP1tAne71yVsXgq/KfK4qyZSt3YngeVk7DV1HwFACCe802DLKL8jZoNFCHjuANl3Ey7HA5Z4yyba8gKdUAmmyRzOToFnpZRTsx33lCBnIsoBm8NeS0R4/NTODQzwhlhNyw7ZpdLMTIKEIrJju+RqD7Pqpf7bYDXjy/ZWrrLCGpk3Y7hM/EkkE8WOZN61CwpLvHAG9y9NcvqcuIOokEm4JnAZgcg=; bm_sv=96C5B7EC8CD14E6CCAE5C38764ED217A~YAAQRAHARYJ4w2+SAQAApvHLiRkPukk8m67OJVo2ExSQhV5r8u+/I96334I8L1d1pFDBAbTNGtI8QOAWLbvFfS3iKsalsdeZFjl+5v3N2XwlhDS+RhUML20f0qvRcb5t9dzZiPL83HO5cF/2PpVVlocFe6rxdBERm9OdSLnkPgcwI9yxikbTUaYFAqs51iwZ6BC7gpMIB6eMR9NiAdvISP/peydxQsBOV/m4u5kWYYqeHY6uvTpr/Clq0sudPg==~1; _uetsid=3b10c470890911efab8dfb662e290b9b; _uetvid=d6fabc007eed11ef8bb59788c3c344b4; lastRskxRun=1728888697367; _ga_JPNZR0P362=GS1.1.1728888697.30.0.1728888697.60.0.0; _ga_XXXXXXXXXXX=GS1.1.1728888697.29.0.1728888697.0.0.2145140052; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22b3TrcMDJ8DIfFs17V608%22%2C%22expiryDate%22%3A%222025-10-14T06%3A51%3A37.578Z%22%7D; _scid_r=vrCBGEOtvtJwc344HVr_gblFTZKHn-1g2EIMLA; cto_bundle=nCLhfl9KTG5xOVdhV1NLSjBTa2VTbUttVFc0MkVib0NYNmRMZ3FHam1VZmFJUUxEM2g1dkQlMkJ2TFlNTThIMjRzeTU0JTJCYks1MmM0NUlDZlFpUGJnYmZLSVl2cXFkRVpqZWJ5Wnc5OVdYcHlEZk45aGduUmYxc3JOc1pJSlYzUXpEbG5OQXZmM243dTZkQWdtbkdGbmZJZGh6dXZ2bjJZOFRRcTBlb1lpZTVzS1BVJTJCaWhrbFZ4SEpxNFhzQkZPWmZTNndkOUYwZjYxajc4ZjJPMUhpSTE4ZklyN21ZdlduZHdhR2VPcWhWcWVRMjdPR3ppM1JUUDhvWVV3c0owRzJ4MVZqMXI0YyUyRmRDa3NIc054VFRLdnRoY05kYTQlMkZBSUNhR3RCaE5GVEc1cE00NnVSb1Q1ellaaVVIUkFhdlRHQlpzWmFvVU4; _cs_id=097428bd-4686-a995-e674-3652b51d83c5.1727511458.36.1728888698.1728888698.1.1761675458392.1; fita.short_sid.yoox=-3LH029iwG0WzCLqfmiD5mpEe2amEOD_; rxvt=1728890502338|1728886941034; dtPC=19$288695104_481h-vAJLWEFCPCKTQKBHHVWEUSPQSOFERHVAO-0e0; bm_lso=356D153C0759E14016EAA401C45D69286792FC833871AD09A7A4A3D97DCAD26A~YAAQRAHARWB4w2+SAQAAT+fLiQGAiaW7S2ydtePafQdZ8VBF/5Jaknb5YNrCZr0lx/n+gnOkCvUJv7hq09PzmMq3rPHb1IelyEHLrMy151M9sFO/6npi8edaeLZNcJoPy0kDQ4Tv3gdK4JMVPqrxSSejyDy17xH8oyE8TxR7mOROsLYRYYKXOj/VIvfPRMdbYvbFw/LAX2I9Bi7QB3FeA9THfZ6LwhAdpRFxKCFhtHKIMJ2PxDRMf0UmDmXIaW4RC1lqGoxd8CkD42pMbgyUcNeDH4mXy3Bqpq0M05CFJytjWi4DwdPIDEIzefVAuyQzb0hTjFhkHuV54N3srjJ3yhaenegZDzeFBLDJAdqPoG07UVNiPhDbOEDjj24pgjNNyQT8vIu8MLZL0tn99NWSWUMEONgJNHHeYv/9kUVL//ANYhv/r8SfaShTpIRFgMBsqN0FgJJiyhI36eA=^1728888702844; RT="z=1&dm=yoox.com&si=2cbf5544-ddca-4a2c-ab73-92c39adc1f20&ss=m27fzl5w&sl=0&tt=0&bcn=%2F%2F684d0d4a.akstat.io%2F"; _cs_s=1.0.0.1728891977062',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}
cookies = {
    'optimizelyEndUserId': 'oeu1727511452719r0.9518978653073176',
    'LAYERFIRSTVISIT': 'LAYERFIRSTVISIT=True',
    'NAVIGATED': '1',
    'USERINFO': 'SESSO=D&SESSOBAMBINO=D',
    'OLDVISIT': '1',
    'tc_YAB_test': 'UpgradeV1vsV2_B',
    '_ALGOLIA': 'anonymous-c3dedd5e-e08f-432f-a934-39cc6207ad90',
    'mn_u': '5.1245425455.1727511455636',
    'rskxRunCookie': '0',
    'rCookie': 'zcmcasyv6l3ryugbtfcoem1lvpucz',
    '_gcl_au': '1.1.1877572904.1727511456',
    '_mibhv': 'anon-1727511456398-4076264761_9612',
    '_ga': 'GA1.1.27234611.1727511457',
    '_cs_c': '1',
    '_scid': 'kzCBGEOtvtJwc344HVr_gblFTZKHn-1g',
    '__lt__cid': '009a4aaa-2add-4f97-9b4c-633686952176',
    '_yjsu_yjad': '1727511458.3eb94d63-4aad-4b11-960e-258503eb06c2',
    'ORA_FPC': 'id=b6903cb9-e9c2-41e3-a674-b22084f071a4',
    '_tt_enable_cookie': '1',
    '_ttp': 'ac6jYB4vPy4FqxDWRE_L3gpwYrG',
    '_fbp': 'fb.1.1727511459164.699433888471550982',
    'fita.sid.yoox': 'Jb-bLWZcw8KkFUZ2UcrRPDNwqqxz75Zg',
    'TCPID': '12410212542793771456',
    'TC_PRIVACY': '0%40006%7C66%7C645%401%2C2%2C3%2C4%2C5%40%401727764542508%2C1727764542508%2C1761460542508%40',
    'TC_PRIVACY_CENTER': '1%2C2%2C3%2C4%2C5',
    '_pin_unauth': 'dWlkPVlXSTFOREV4WWpndE9UUmtNUzAwTXpWbExXSXpPR0V0TVRkaVptWTJOemd4WmpnNA',
    '_ScCbts': '%5B%5D',
    'GENERIC_USER_ID': 'd3143dc6-2e0d-4bdf-b8ff-ba761c7fcd0e',
    '_sctr': '1%7C1728325800000',
    '__gads': 'ID=5427474f53b4d792:T=1727764542:RT=1728580735:S=ALNI_MavOMmcMQShyXIEGD6elkHktDktJQ',
    '__gpi': 'UID=00000f2c81787579:T=1727764542:RT=1728580735:S=ALNI_MYHZkEqsvXNZ6lykGL5Hdh_4IqTUw',
    '__eoi': 'ID=db6bb31fc86728a4:T=1727511489:RT=1728580735:S=AA-AfjZ_kmRjkTTIzVHjladnRWLD',
    'YEDGESESSION': '5f39201758c43400962d0b6726010000d39a0000',
    'PIM-SESSION-ID': 'qQ5v8D9Axtvw0GxX',
    'FEATURE_DISABLED_BAYNOTE': 'true',
    'SESSIONS': 'FIRSTTIMEUSER=0',
    'rxVisitor': '1728785818872HBIEDLVAFU8G7MVTIPB6UGJU18OBDU65',
    'dtSa': '-',
    'VISIT': 'TSKAY=3FD17CD7&NAZIONE=UNITED+STATES&ID%5FNAZIONE=38&ID%5FMERCATO=19&SIGLA%5FVALUTA=%24&CURRENCYCODE=USD&REFERENCE%5FCURRENCYCODE=USD&ID%5FMERCATO%5FPER%5FLISTINO=19&MERCATO%5FPATH=%2fus%2f&VALUTA%5FID=22&DYN%5FPATH=%2fus%2f&SITE%5FCODE=YOOX_US&ANONYMOUS%5FCHECKOUT=True&NAZIONE%5FISO=US&WAREHOUSES=2715%2c2805%2c4800%2c20611%2c21140%2c70%2c271&TWOLETTERISOCODE=EN&LASTQUERY=',
    'ABTEST': '%7b%22AbTests%22%3a%5b%7b%22Name%22%3a%22SmsMultiChannel%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%2c%7b%22Name%22%3a%22myooxNew%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%2c%7b%22Name%22%3a%22paypalExpressNewHead%22%2c%22Mode%22%3a%22Auto%22%2c%22Enabled%22%3a%22on%22%2c%22Threshold%22%3a%22100%22%7d%5d%2c%22Reloaded%22%3afalse%2c%22ReloadedTime%22%3anull%7d',
    'TrackingNavigation': 'Token=5484420b-0e9d-4039-b168-f38fae76d31b',
    'SizeFitTracking': 'Token=92e53382-131f-47b0-b49f-8694af28ee2f',
    '_cs_cvars': '%7B%221%22%3A%5B%22Subsection%22%2C%22women%22%5D%2C%222%22%3A%5B%22Country%20Code%22%2C%22US%22%5D%2C%223%22%3A%5B%22Language%20Code%22%2C%22EN%22%5D%2C%224%22%3A%5B%22Currency%22%2C%22USD%22%5D%2C%227%22%3A%5B%22AB%20Test%22%2C%22SmsMultiChannel_ON%2CmyooxNew_ON%2CpaypalExpressNewHead_ON%22%5D%2C%228%22%3A%5B%22Gender%22%2C%22D%22%5D%2C%229%22%3A%5B%22Page%22%2C%22women%3AItem%22%5D%2C%2210%22%3A%5B%22Page%20Type%22%2C%22Item%22%5D%2C%2211%22%3A%5B%22Prod%20Cod%208%22%2C%2249535591%22%5D%2C%2212%22%3A%5B%22Prod%20Cod%2010%22%2C%2249535591QF%22%5D%2C%2213%22%3A%5B%22Prod%20Brand%22%2C%22FRANKIE%20MORELLO%22%5D%2C%2214%22%3A%5B%22Prod%20Cat%22%2C%22Blazers%22%5D%2C%2215%22%3A%5B%22Prod%20Cat%20Code%22%2C%22gcc%22%5D%2C%2217%22%3A%5B%22Prod%20Macro%20Cat%22%2C%22Coats%20%26%20Jackets%22%5D%2C%2218%22%3A%5B%22Prod%20Macro%20Cat%20Code%22%2C%22cpspll%22%5D%2C%2219%22%3A%5B%22Area%20Dept%22%2C%22women%22%5D%2C%2220%22%3A%5B%22Env%20Channel%22%2C%22web%22%5D%7D',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.yoox.com%2Fus%2F49535591QF%2Fitem%23dept%3Dwomen%26queryID%3Dundefined%26cod10%3D49535591QF%26sizeId%3D-1~1728785823871',
    'dtCookie': 'v_4_srv_19_sn_45D70B773AB15A66C44CA3985FFDE076_app-3A8caa4d99ff5d944a_1_ol_0_perc_100000_mul_1',
    '_abck': '2DF5E5ACA8357BBDB30FD71AE5380E92~0~YAAQRAHARW50w2+SAQAAcS/HiQzUpfr8R9TBvxkNk0wWGk9QIL51JPADuG/rLvRSOVBSUnRK74RJvVLZ2nNV0F4lTJtMH2vmeKv/cLWO+DKiC4tlxZfsSYaxDUPL+ci0mbyDJeAuxfvawcQqloVOQNc5MzWXSdHtZ7VTv7UXldg+Mwfq8BkHul3gbXOKOETu747npEIylQF8KGwcePwzpxshcMDNWL8Uv2KmC9pW2iv5/YjBEI8uL/QBhPOZbqoq5qZxUkRNy83i1hSLhdAtAJMHfhQbetEi5cRhc12pVOn3JUb1bH82Ft0m3NO/br5BYr5cFe0/yBVGi8kkTKD6p4wiwGFfM3eE0Ox46NTYQFvEc4o+e5rRtszxV3Lsnl9uM37Z9MN9L0BXzctsScf1umJFcKEQGOu9zEnz9a6L2IDmoDw6PvQgsMpCTxSP8FjB7yGd0+3nqA==~-1~-1~1728891985',
    'AKA_A2': 'A',
    'bm_ss': 'ab8e18ef4e',
    'bm_so': '356D153C0759E14016EAA401C45D69286792FC833871AD09A7A4A3D97DCAD26A~YAAQRAHARWB4w2+SAQAAT+fLiQGAiaW7S2ydtePafQdZ8VBF/5Jaknb5YNrCZr0lx/n+gnOkCvUJv7hq09PzmMq3rPHb1IelyEHLrMy151M9sFO/6npi8edaeLZNcJoPy0kDQ4Tv3gdK4JMVPqrxSSejyDy17xH8oyE8TxR7mOROsLYRYYKXOj/VIvfPRMdbYvbFw/LAX2I9Bi7QB3FeA9THfZ6LwhAdpRFxKCFhtHKIMJ2PxDRMf0UmDmXIaW4RC1lqGoxd8CkD42pMbgyUcNeDH4mXy3Bqpq0M05CFJytjWi4DwdPIDEIzefVAuyQzb0hTjFhkHuV54N3srjJ3yhaenegZDzeFBLDJAdqPoG07UVNiPhDbOEDjj24pgjNNyQT8vIu8MLZL0tn99NWSWUMEONgJNHHeYv/9kUVL//ANYhv/r8SfaShTpIRFgMBsqN0FgJJiyhI36eA=',
    'bm_sz': 'E761B96B78761414BE6330108B4E54AF~YAAQRAHARWF4w2+SAQAAT+fLiRk0aEA5ZDy989x++VuNrvdiS5cQAKKP8JHWIUg99uY9u0M/7gmi2R3OhNAX1uYvLkTDdSTYGVJuVpf95sdEnoFVteI2Mx+/rlMoPOfe46p6xyTVL9c5vavldGkjUQVJjTujT4SQNzzuYWubclbLkVCkIVawSqiwyiYkdNx3ne62hSgyZ/yYCxSlN0Quyn5HSQjP7KlCBvdRYNSPa5gvmETTNtxFbaNzUCBxYq8JP5u0BjRfkCInxVs443tYMGbEXWFaxIfajSdjQ6CIB2ChuVr5V9xpeJ6Bl3HtMbLKovrvn0Ki2RCEx8WjV/6JvVCVZeVo3qA/NMn3YTMGqgIoNts9DDmKjEn4588UXrQsr8ITAmTubrJ1/E6zAxRIuxs=~3228997~3356979',
    'bm_s': 'YAAQRAHARX14w2+SAQAA0u/LiQIsuz/Rq1RHrXx5QWJd5TtRFaOXclbcOUL9zvPiHM73mwi6nW9STxqCDDF56EK0mbrnihl5XxSGxnv6Ao4pPejrsYR2sF+6pm2Ob0gdHmOgfRhPx2TnTwG08wlT8UoJBPL11hVhZtsr6xkRIFTqcjjUx1WBYjauI6llaQ8IoPywQ7OMslfx9JANsPT0/YyYNdNOaRxmVvqn6nltDuKcZf9tcYO3+RfuRWs8YxDfLDrWZuMq90h/ToMlt5kGYXmXJrPYaXsGiATucb/udV97IPBcF3F/YEPedHTx5zg6vMPqGSiKFl1DQrvJWOCv2YVpFtg=',
    'ak_bmsc': 'D13911B950C9D40998A241E2A739D0C5~000000000000000000000000000000~YAAQRAHARYB4w2+SAQAAe/DLiRnbiDmeU7yaDRZ0Yu+ov7FVacBmIRLTcGj+IFgvlUIjA71+2Sj7qem0rl3ainWVJKKJuCU+8AxIBJpuTXNnULziNc1mcXq0uRYIIC90jvAvorach30Ff4pa2Ghlo22EBAruB5WtYyzkyxjsor1OHqhuu/vwgRN1LxXDAHjocd707ZTvi42qY9NkNkcHgtIVGOt79aCzMrqqs27thP1tAne71yVsXgq/KfK4qyZSt3YngeVk7DV1HwFACCe802DLKL8jZoNFCHjuANl3Ey7HA5Z4yyba8gKdUAmmyRzOToFnpZRTsx33lCBnIsoBm8NeS0R4/NTODQzwhlhNyw7ZpdLMTIKEIrJju+RqD7Pqpf7bYDXjy/ZWrrLCGpk3Y7hM/EkkE8WOZN61CwpLvHAG9y9NcvqcuIOokEm4JnAZgcg=',
    'bm_sv': '96C5B7EC8CD14E6CCAE5C38764ED217A~YAAQRAHARYJ4w2+SAQAApvHLiRkPukk8m67OJVo2ExSQhV5r8u+/I96334I8L1d1pFDBAbTNGtI8QOAWLbvFfS3iKsalsdeZFjl+5v3N2XwlhDS+RhUML20f0qvRcb5t9dzZiPL83HO5cF/2PpVVlocFe6rxdBERm9OdSLnkPgcwI9yxikbTUaYFAqs51iwZ6BC7gpMIB6eMR9NiAdvISP/peydxQsBOV/m4u5kWYYqeHY6uvTpr/Clq0sudPg==~1',
    '_uetsid': '3b10c470890911efab8dfb662e290b9b',
    '_uetvid': 'd6fabc007eed11ef8bb59788c3c344b4',
    'lastRskxRun': '1728888697367',
    '_ga_JPNZR0P362': 'GS1.1.1728888697.30.0.1728888697.60.0.0',
    '_ga_XXXXXXXXXXX': 'GS1.1.1728888697.29.0.1728888697.0.0.2145140052',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22b3TrcMDJ8DIfFs17V608%22%2C%22expiryDate%22%3A%222025-10-14T06%3A51%3A37.578Z%22%7D',
    '_scid_r': 'vrCBGEOtvtJwc344HVr_gblFTZKHn-1g2EIMLA',
    'cto_bundle': 'nCLhfl9KTG5xOVdhV1NLSjBTa2VTbUttVFc0MkVib0NYNmRMZ3FHam1VZmFJUUxEM2g1dkQlMkJ2TFlNTThIMjRzeTU0JTJCYks1MmM0NUlDZlFpUGJnYmZLSVl2cXFkRVpqZWJ5Wnc5OVdYcHlEZk45aGduUmYxc3JOc1pJSlYzUXpEbG5OQXZmM243dTZkQWdtbkdGbmZJZGh6dXZ2bjJZOFRRcTBlb1lpZTVzS1BVJTJCaWhrbFZ4SEpxNFhzQkZPWmZTNndkOUYwZjYxajc4ZjJPMUhpSTE4ZklyN21ZdlduZHdhR2VPcWhWcWVRMjdPR3ppM1JUUDhvWVV3c0owRzJ4MVZqMXI0YyUyRmRDa3NIc054VFRLdnRoY05kYTQlMkZBSUNhR3RCaE5GVEc1cE00NnVSb1Q1ellaaVVIUkFhdlRHQlpzWmFvVU4',
    '_cs_id': '097428bd-4686-a995-e674-3652b51d83c5.1727511458.36.1728888698.1728888698.1.1761675458392.1',
    'fita.short_sid.yoox': '-3LH029iwG0WzCLqfmiD5mpEe2amEOD_',
    'rxvt': '1728890502338|1728886941034',
    'dtPC': '19$288695104_481h-vAJLWEFCPCKTQKBHHVWEUSPQSOFERHVAO-0e0',
    'bm_lso': '356D153C0759E14016EAA401C45D69286792FC833871AD09A7A4A3D97DCAD26A~YAAQRAHARWB4w2+SAQAAT+fLiQGAiaW7S2ydtePafQdZ8VBF/5Jaknb5YNrCZr0lx/n+gnOkCvUJv7hq09PzmMq3rPHb1IelyEHLrMy151M9sFO/6npi8edaeLZNcJoPy0kDQ4Tv3gdK4JMVPqrxSSejyDy17xH8oyE8TxR7mOROsLYRYYKXOj/VIvfPRMdbYvbFw/LAX2I9Bi7QB3FeA9THfZ6LwhAdpRFxKCFhtHKIMJ2PxDRMf0UmDmXIaW4RC1lqGoxd8CkD42pMbgyUcNeDH4mXy3Bqpq0M05CFJytjWi4DwdPIDEIzefVAuyQzb0hTjFhkHuV54N3srjJ3yhaenegZDzeFBLDJAdqPoG07UVNiPhDbOEDjj24pgjNNyQT8vIu8MLZL0tn99NWSWUMEONgJNHHeYv/9kUVL//ANYhv/r8SfaShTpIRFgMBsqN0FgJJiyhI36eA=^1728888702844',
    'RT': '"z=1&dm=yoox.com&si=2cbf5544-ddca-4a2c-ab73-92c39adc1f20&ss=m27fzl5w&sl=0&tt=0&bcn=%2F%2F684d0d4a.akstat.io%2F"',
    '_cs_s': '1.0.0.1728891977062',
}

def correct_image(img):
    matchObj = re.search(r"(items/\d{2}/\d{2})",img)
    if not matchObj:
        return img
    to_be_replaced = matchObj.group()
    replaced_with = f"{to_be_replaced.split('/')[0]}/{to_be_replaced.split('/')[2]}/{to_be_replaced.split('/')[2]}"
    image = img.replace(to_be_replaced, replaced_with)
    return image


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.yoox.com"]

    custom_settings = {
        'FEEDS': {
            f'../output/Yoox_{datetime.now().strftime("%Y%m%d")}.csv': {
                'format': 'csv',
                'encoding': 'utf-8'
            }
        },
        # 'LOG_FILE':f'Yoox_log_{datetime.now().strftime("%H%M%S")}.log',
        'LOG_LEVEL':"INFO"
    }

    def start_requests(self) -> Iterable[Request]:
        urls = list(pd.read_csv(r'C:\Users\Administrator\Desktop\Yooxs\Yooxs\spiders\sku.csv', encoding='latin-1')['SKU'])
        for url in urls[:1000]:
            link='https://www.yoox.com/us/'+str(url)+'/item'
            # url = url.replace('com/us', 'com/jp')
            # url = url.replace('com/jp', 'com/us')
            yield Request(link, headers=headers, cookies=cookies,
                        #   meta= {'playwright':True, 
                        #          "playwright_context": "persistent",
                        #   }
                          )

    def parse(self, response):

        script = response.xpath('//script[@type = "application/ld+json"]/text()').get()
        if script:
            data = json.loads(script)
            productId = "-"
            product_url = response.url,
            javascript = response.xpath('//script[contains(@id, "__NEXT_DATA__")]/text()').get()
            data_2 = json.loads(javascript)

            data_2 = data_2['props']['pageProps']['initialState']['itemApi']
            
            # sizes = [(item['default']['classFamily'], item['default']['text']) for item in data_2['sizes']]

            brand = data.get('brand', {}).get('name', '')
            discounted_price = data_2['priceFinal']['transactional']['amount'] 
            try:
                actual_price = data_2['priceOriginal']['transactional']['amount']
            except:
                actual_price = ""
            if actual_price == "":
                actual_price = discounted_price
                discounted_price = "-" 

            
            Currency = data_2['priceFinal']['transactional']['currency']
            category1 = data_2['descriptions']['MacroCategory']
            category2 = data_2['descriptions']['MicroCategory']
            category3 = data_2['descriptions']['MicroCategoryPlural']
            gender = data_2['macroCategory']['url']['prefixes'][0]
                    
            try:
                name = data_2['microCategory']['pluralDescription']
            except:
                name = ""
            availble_color_list = data_2['colors']
            all_sizes_info_list = data_2['sizes']
            imagesFormatValues = data_2['imagesFormatValues'] 

            color_df = pd.DataFrame()
            for color_info in availble_color_list:
                color_size_id = [color_tag['id'] for color_tag in color_info['availableSizesIds']]
                sku = color_info['code10']
                color = color_info['name']
                description0 = data_2.get('descriptions', {}).get('ItemDescription', '-')
                image_urls = ["https://www.yoox.com/images/items/"+'17/'+str(sku)+"_14"+imgevalue+".jpg" for imgevalue in imagesFormatValues]
                size_list = []
                for size_id in color_size_id:
                    size = [size_tag for size_tag in all_sizes_info_list if size_tag['id'] == size_id][0]['default']['text']
                    size_list.append(size)
                color_dict = {"color":color,"sku":sku,"size":" ".join(size_list),"image_urls":"|".join(image_urls),'description0':description0}
                temp_df = pd.DataFrame(color_dict,index=[0],columns=['color','sku','size',"image_urls",'description0'])
                color_df = pd.concat([color_df, temp_df], ignore_index=True)
            # If color_df is empty, create a default dataframe
            if len(color_df) == 0:
                color_dict = {"color": "-", "sku": "-", "size": "-", "image_urls": "-",'description0':'-'}
                color_df = pd.DataFrame(color_dict, index=[0], columns=['color', 'sku', 'size', "image_urls",'description0'])
            for index, row in color_df.iterrows():
                color = row['color']
                sku = row['sku']
                sizeId = row['size']
                image_urls = [image_tag.strip() for image_tag in row['image_urls'].split("|")]
                image_dict = {}
                for image in range(1,13):
    
                    try:
                        img = correct_image(image_urls[image-1])
                        image_dict['Image'+str(image)] = img
                    except:
                        image_dict['Image'+str(image)] = "-"
                
                data_dict = {"NO":"-","pcurl":product_url,'mburl':'-',"Name":name,"Brand":brand,"ProductCode1":productId,"ProductCode2":"-",'ProductCode3':'-','ProductCode4':'-', 'ProductCode5':'-',"Sku":sku,"Color":color,"Width":'-',"Gender":gender,"Category1":category1,"Category2":category2,"Category3":category3,"Category4":"-","Category5":"-","Category6":"-","facetCategory":'-',"Price":actual_price,"SalePrice":discounted_price,"Currency":Currency,'Description0':description0,'Description1':"-", 'Description2':'-','Description3':'-','Description4':"-", 'Description5':'-','Description6':'-','Description7':"-",'Description8':'-', 'Description9':'-', 'Description10':'-', 'Description11':'-','Description12':'-', 'Description13':'-', 'Description14':'-', 'Description15':'-','Description16':'-', 'Description17':'-','Description18':'-', 'Description19':'-', 'Description20':'-',"Size":sizeId}
                data_dict.update(image_dict)
                data_dict.update({"Thumbnail":'-'})

                yield data_dict  
            
            
            # item =  {'Brand': ,
            #         'Description': data.get('description', ''),
            #         'pcurl':data.get('url', []),
            #         'Images': data.get('image', []),
            #         'Type': data.get('name', ''),
            #         'Price':data.get('offers', {}).get('price', ''),
            #         'Currency':data.get('offers', {}).get('priceCurrency', ''),
            #         'Sku': data.get('sku', ''),
            #         'Sizes': sizes
            #         }
            
            


    



    




