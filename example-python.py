# Everything, requests, responses, possible paramaters is typed

import asyncio
from mexcpy.mexcTypes import CreateOrderRequest, OpenType, OrderSide, OrderType
from mexcpy.api import MexcFuturesAPI

key = 'your key'

api = MexcFuturesAPI(token, testnet=True)

async def main():
    market_order_response = await api.create_market_order("BTC_USDT", OrderSide.OpenLong, 1000, 20)

    # Uses dataclasses for types
    print(market_order_response.data.orderId)

    limitOrderResponse = await api.create_order(CreateOrderRequest(
        symbol=symbol,
        side=OrderSide.CloseLong,
        vol=1000,
        leverage=20,
        price=119_000,
        openType=OpenType.Isolated,
        type=OrderType.PriceLimited,
    ))

    # Uses dataclasses for types
    print(limitOrderResponse.data.orderId)


if __name__ == "__main__": 
    asyncio.run(main())