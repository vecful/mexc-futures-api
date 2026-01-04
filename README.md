<div align="center">

# ⚡ MEXC Futures API Bypass

### Trade MEXC Futures even during official API maintenance

## 🌐 [mexc-bypass](https://mexc-demo.fly.dev/)

<br>

[![Live Demo](https://img.shields.io/badge/🔗_Live_Demo-mexc--bypass.com-10B981?style=for-the-badge)](https://mexc-demo.fly.dev/)
[![Telegram](https://img.shields.io/badge/Telegram-@vecful-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vecful)

<br>

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-proprietary-red)

</div>

---

## 🎯 What is this?

This API bypasses MEXC's [Under Maintenance](https://mexcdevelop.github.io/apidocs/contract_v1_en/#order-under-maintenance) restrictions, allowing you to create orders, manage positions, and trade futures even when the official API is blocked.

**Try it out:** [https://mexc-demo.fly.dev/](https://mexc-demo.fly.dev/)

---

## ✨ Features

| Feature                    | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| ⚡ **Fast**                | 200-300ms response times *(you can get it under <100ms given the right region)*                                |
| 🔐 **Direct Connection**   | No third-party requests — communicates directly with MEXC |
| 🌐 **Mainnet & Testnet**   | Works on both environments                                |
| ⌨️ **TypeScript & Python** | Fully typed libraries available                           |
| 📦 **Postman Collection**  | Ready-to-use API collection included                      |

---

## 💳 Pricing

| Product                                    | Price          | Description                                                 |
| ------------------------------------------ | -------------- | ----------------------------------------------------------- |
| 💾 **Futures API SDK**                     | $120           | Full source code for futures order management               |
| 💾 **Spot API SDK**                        | $120           | Full source code. Create orders for newly listed spot coins |
| 🪞 **Multi-Account Copy Bot**              | $400           | Mirror trades across multiple accounts                      |
| 🪞 **Multi-Account Copy Bot Subscription** | Coming soon... | Mirror trades across multiple accounts                      |
| ✈️ **Signal Trading Bot**                  | Custom         | Auto-copy trades from Telegram signals                      |
| 🔍 **OCR Trading Bot**                     | Custom         | Read signals from screenshots or messages                   |

**Payment:** USDT, USDC

📬 **[Contact on Telegram →](https://t.me/vecful)**

---

## 🔓 Bypassed Endpoints

### Order Management

| Method | Endpoint                              | Status          |
| ------ | ------------------------------------- | --------------- |
| POST   | `/private/order/create`               | 🔓 **Bypassed** |
| POST   | `/private/order/cancel`               | 🔓 **Bypassed** |
| POST   | `/private/order/cancel_with_external` | 🔓 **Bypassed** |
| POST   | `/private/order/cancel_all`           | 🔓 **Bypassed** |

### Trigger Orders (Plan Orders)

| Method | Endpoint                        | Status          |
| ------ | ------------------------------- | --------------- |
| POST   | `/private/planorder/place`      | 🔓 **Bypassed** |
| POST   | `/private/planorder/cancel`     | 🔓 **Bypassed** |
| POST   | `/private/planorder/cancel_all` | 🔓 **Bypassed** |

### Stop Limit Orders

| Method | Endpoint                               | Status          |
| ------ | -------------------------------------- | --------------- |
| POST   | `/private/stoporder/cancel`            | 🔓 **Bypassed** |
| POST   | `/private/stoporder/cancel_all`        | 🔓 **Bypassed** |
| POST   | `/private/stoporder/change_price`      | 🔓 **Bypassed** |
| POST   | `/private/stoporder/change_plan_price` | 🔓 **Bypassed** |

### Position Management

| Method | Endpoint                                 | Status          |
| ------ | ---------------------------------------- | --------------- |
| POST   | `/private/position/change_margin`        | 🔓 **Bypassed** |
| POST   | `/private/position/change_leverage`      | 🔓 **Bypassed** |
| POST   | `/private/position/change_position_mode` | 🔓 **Bypassed** |

---

## ✅ Available Endpoints

### Account

| Method | Endpoint                            | Description          |
| ------ | ----------------------------------- | -------------------- |
| GET    | `/private/account/assets`           | Get all user assets  |
| GET    | `/private/account/asset/{currency}` | Get specific asset   |
| GET    | `/private/account/transfer_record`  | Get transfer records |
| GET    | `/private/account/risk_limit`       | Get risk limits      |
| GET    | `/private/account/tiered_fee_rate`  | Get trading fee info |

### Position

| Method | Endpoint                                   | Description              |
| ------ | ------------------------------------------ | ------------------------ |
| GET    | `/private/position/list/history_positions` | Get historical positions |
| GET    | `/private/position/open_positions`         | Get open positions       |
| GET    | `/private/position/funding_records`        | Get funding records      |
| GET    | `/private/position/leverage`               | Get leverage settings    |
| GET    | `/private/position/position_mode`          | Get position mode        |

### Orders

| Method | Endpoint                                 | Description                |
| ------ | ---------------------------------------- | -------------------------- |
| GET    | `/private/order/list/open_orders`        | Get pending orders         |
| GET    | `/private/order/list/history_orders`     | Get historical orders      |
| GET    | `/private/order/external/{symbol}/{oid}` | Get order by external ID   |
| GET    | `/private/order/get/{order_id}`          | Get order by ID            |
| GET    | `/private/order/batch_query`             | Get orders by IDs          |
| GET    | `/private/order/deal_details/{order_id}` | Get order transactions     |
| GET    | `/private/order/list/order_deals`        | Get transactions by symbol |

### Trigger Orders (Plan Orders)

| Method | Endpoint                         | Description        |
| ------ | -------------------------------- | ------------------ |
| GET    | `/private/planorder/list/orders` | Get trigger orders |

### Stop Limit Orders

| Method | Endpoint                         | Description           |
| ------ | -------------------------------- | --------------------- |
| GET    | `/private/stoporder/list/orders` | Get stop limit orders |

---

## 🚀 Quick Start

### TypeScript

```typescript
import { MexcFutureAPI } from "./mexc";
import { OrderSide } from "./mexcTypes";

async function main() {
  const key = "your key";
  const api = new MexcFutureAPI(key);
  await api.createMarketOrder("BTC_USDT", OrderSide.OpenLong, 1000, 20);
}

main();
```

### Python

```python
import asyncio
from mexcpy.mexcTypes import OrderSide
from mexcpy.api import MexcFuturesAPI

async def main():
    key = 'your key'
    api = MexcFuturesAPI(key)
    await api.create_market_order("BTC_USDT", OrderSide.OpenLong, 1000, 20)

asyncio.run(main())
```

---

## 🔗 Links

- 🌐 **Website:** [https://mexc-demo.fly.dev/](https://mexc-demo.fly.dev/)
- 💬 **Telegram:** [@vecful](https://t.me/vecful)
- 📈 **Spot API:** [mexc-spot-bypass](https://github.com/vecful/mexc-spot-bypass)

---

<div align="center">

**[🌐 https://mexc-demo.fly.dev/](https://mexc-demo.fly.dev/)** · **[💬 @vecful](https://t.me/vecful)**

</div>
