import random
from binance.client import Client


def create_orders(api_key, api_secret, data):
    client = Client(api_key, api_secret)
    volume = data['volume']
    num_orders = data['number']
    amount_dif = data['amountDif']
    side = data['side']
    price_min = data['priceMin']
    price_max = data['priceMax']

    # Calculate the volume per order
    vol_per_order = volume / num_orders

    # Loop through the number of orders
    for i in range(num_orders):
        # Calculate the random price and volume for the current order
        price = round(random.uniform(price_min, price_max), 2)
        vol = round(random.uniform(max(0, vol_per_order - amount_dif), vol_per_order + amount_dif), 2)

        # Place the order on the exchange
        try:
            order = client.create_order(
                symbol='BTCUSDT',
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=vol,
                price=price
            )
            print(f'Order {i + 1}: {order}')
        except Exception as e:
            print(f'Error placing order {i + 1}: {e}')

# api_key = 'your_api_key'
# api_secret = 'your_api_secret'
#
# data = {
#     "volume" : 10000.0 ,
#     "number" : 5 ,
#     "amountDif" : 50.0 ,
#     "side" : "SELL" ,
#     "priceMin" : 200.0 ,
#     "priceMax" : 300.0
# }
#
# create_orders(api_key, api_secret, data)