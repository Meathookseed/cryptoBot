import urllib.request
from bs4 import BeautifulSoup
from poloniex import Poloniex

def parse_wex(html):
    values = ''
    soup = BeautifulSoup(html,'lxml')
    values = ''
    #print buy value
    for inlbock_buy_price in soup.find_all('div',class_='inblock order_header')[1:]:
        for price_buy in inlbock_buy_price.find_all('b'):
            buy_price = price_buy.find('span')

     #print sell value
    for inlbock_sell_price in soup.find_all('div',class_='inblock order_header')[:1]:
        for price_sell in inlbock_sell_price.find_all('b'):
            sell_price = price_sell.find('span')
    print('Sell_price:{0}\nBuy price:{1}\n'.format(sell_price.text,buy_price.text))


def get_html(url):
    response = urllib.request.urlopen(url)
    a = "Pair of " + url.split('/')[-1].upper().replace('_','/')
    print(a)
    return response.read()

#--------------------------------------------btc parser------------------------------------------------------
def parse_polo_btc():
    polo = Poloniex()
    exchange_coins_btc =['BTC_ETH','BTC_XRP','BTC_STR','BTC_LTC','BTC_XMR','BTC_ETC',
                     'BTC_LSK','BTC_OMNI','BTC_DOGE','BTC_BCH','BTC_SC','BTC_XEM',
                     'BTC_ZEC','BTC_DASH','BTC_BTS','BTC_OMG','BTC_STRAT','BTC_ZRX',
                     'BTC_FCT','BTC_DGB']
    a = ''
    for coin_eth in exchange_coins_btc:
        ticket = dict(polo('returnTicker')[coin_eth])
        lowbid2 = '<i>Lowest bid: </i>' + ticket['lowestAsk'] + '\n'
        highbid2 = '<i>Highest bid: </i>' + ticket['highestBid'] + '\n'
        tkin = '<b>Pair of ' + coin_eth.replace('_', '/') + '</b>\n'
        a += tkin + lowbid2 + highbid2
    return a

#--------------------------------------------eth parser-----------------------------------------------------
def parse_polo_eth():
    polo = Poloniex()
    exchange_coins_eth=['ETH_ETC','ETH_OMG','ETH_LSK','ETH_BCH','ETH_ZRX','ETH_GNT',
                        'ETH_ZEC','ETH_GNO','ETH_REP','ETH_CVC','ETH_GAS','ETH_STEEM']
    a = ''
    for coin_eth in exchange_coins_eth:
        ticket = dict(polo('returnTicker')[coin_eth])
        lowbid2 = '<i>Lowest bid: </i>'+ticket['lowestAsk']+'\n'
        highbid2 ='<i>Highest bid: </i>'+ticket['highestBid']+'\n'
        tkin = '<b>Pair of '+coin_eth.replace('_','/')+'</b>\n'
        a +=tkin+lowbid2+highbid2
    return a

#---------------------------------------------xmr parse---------------------------------------------------------



def main():
    """wex_urls =['https://wex.nz/exchange/btc_usd','https://wex.nz/exchange/btc_rur','https://wex.nz/exchange/ltc_btc',
 'https://wex.nz/exchange/ltc_usd','https://wex.nz/exchange/ltc_rur','https://wex.nz/exchange/ltc_eur','https://wex.nz/exchange/nmc_btc',
'https://wex.nz/exchange/nmc_usd','https://wex.nz/exchange/nvc_btc','https://wex.nz/exchange/nvc_usd','https://wex.nz/exchange/usd_rur',
'https://wex.nz/exchange/eur_usd','https://wex.nz/exchange/eur_rur','https://wex.nz/exchange/ppc_btc','https://wex.nz/exchange/ppc_usd',
'https://wex.nz/exchange/dsh_btc','https://wex.nz/exchange/dsh_usd','https://wex.nz/exchange/dsh_rur','https://wex.nz/exchange/dsh_eur',
'https://wex.nz/exchange/dsh_ltc','https://wex.nz/exchange/dsh_eth','https://wex.nz/exchange/dsh_zec','https://wex.nz/exchange/eth_btc',
'https://wex.nz/exchange/eth_usd','https://wex.nz/exchange/eth_usd','https://wex.nz/exchange/eth_eur','https://wex.nz/exchange/eth_ltc',
'https://wex.nz/exchange/eth_rur','https://wex.nz/exchange/eth_zec','https://wex.nz/exchange/bch_usd','https://wex.nz/exchange/bch_btc',
'https://wex.nz/exchange/bch_rur','https://wex.nz/exchange/bch_eur','https://wex.nz/exchange/bch_ltc','https://wex.nz/exchange/bch_eth',
'https://wex.nz/exchange/bch_dsh','https://wex.nz/exchange/bch_zec','https://wex.nz/exchange/zec_btc','https://wex.nz/exchange/zec_usd',
'https://wex.nz/exchange/zec_ltc']
    for url in wex_urls:
        parse_wex(get_html(url))"""
    parse_polo_eth()


if __name__=='__main__':
    main()

wex_pairs = ['btc_usd','btc_rur','ltc_btc']
