// Everything, requests, responses, possible paramaters is typed

import { MexcFutureAPI } from "./mexc";
import { OpenType, OrderSide, OrderType } from "./mexcTypes";

const key = 'your key'

const api = new MexcFutureAPI(key, true);

// Market order
const marketOrderResponse = await api.createMarketOrder('BTC_USDT', OrderSide.OpenLong, 1000, 20);

console.log(marketOrderResponse.data.orderId)

// Limit order
const limitOrderResponse = await api.createOrder({
    symbol: "BTC_USDT",
    side: OrderSide.CloseLong,
    vol: 1000,
    leverage: 20,
    price: 119000,
    openType: OpenType.Isolated,
    type: OrderType.PriceLimited,
  });

console.log(limitOrderResponse.data.orderId)
