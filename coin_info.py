from poloniex import Poloniex
from wex import Client

def wex():
    client = Client()
    exchange_pairs = list(('btc_usd btc_rur btc_eur ltc_btc ltc_usd ltc_rur ltc_eur nmc_btc nmc_usd\
                              nvc_btc nvc_usd usd_rur eur_usd ppc_btc dsh_btc dsh_usd dsh_rur dsh_eur\
                              dsh_ltc dsh_eth dsh_zec eth_btc eth_usd eth_eur eth_ltc eth_rur eth_zec\
                           bch_usd bch_btc bch_rur bch_eur bch_ltc bch_eth bch_dsh bch_zec zec_btc zec_usd\
                            zec_ltc').split())
    a = ''
    for coin in exchange_pairs:
        market_ticket = client.ticker(coin)
        ticket = market_ticket[coin]
        buy = '<i>Buy bid: </i>' + str(ticket['buy']) + '\n'
        sell = '<i>Sell bid: </i>' + str(ticket['sell']) +'\n'
        pair_name = '<b>Pair of ' + coin.replace('_', '/').upper() + '</b>\n'
        a += pair_name + buy + sell
    return a

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
    parse_polo_eth()
if __name__=='__main__':
    main()
