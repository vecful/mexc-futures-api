<div align="center">

# ⚡ MEXC Futures API Bypass

### Trade MEXC Futures even during official API maintenance

## 🌐 [mexc-bypass.com](https://mexc-bypass.com)

<br>

[![Live Demo](https://img.shields.io/badge/🔗_Live_Demo-mexc--bypass.com-10B981?style=for-the-badge)](https://mexc-bypass.com)
[![Telegram](https://img.shields.io/badge/Telegram-@vecful-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vecful)

<br>

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-proprietary-red)

</div>

---

## 🎯 What is this?

This API bypasses MEXC's [Under Maintenance](https://mexcdevelop.github.io/apidocs/contract_v1_en/#order-under-maintenance) restrictions, allowing you to create orders, manage positions, and trade futures even when the official API is blocked.

**Try it out:** [mexc-bypass.com](https://mexc-bypass.com)

---

## ✨ Features

| Feature                    | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| ⚡ **Fast**                | 200-300ms response times                                  |
| 🔐 **Direct Connection**   | No third-party requests — communicates directly with MEXC |
| 🌐 **Mainnet & Testnet**   | Works on both environments                                |
| ⌨️ **TypeScript & Python** | Fully typed libraries available                           |
| 📦 **Postman Collection**  | Ready-to-use API collection included                      |

---

## 💳 Pricing

| Product                       | Price | Description                                   |
| ----------------------------- | ----- | --------------------------------------------- |
| 💾 **Futures API SDK**        | $120  | Full source code for futures order management |
| 💾 **Spot API SDK**           | $120  | Full source code. Create orders for newly listed spot coins     |
| 🪞 **Multi-Account Copy Bot** | $400  | Mirror trades across multiple accounts        |
| 🪞 **Multi-Account Copy Bot Subscription** | Coming soon...  | Mirror trades across multiple accounts        |
| ✈️ **Signal Trading Bot**     | Custom | Auto-copy trades from Telegram signals        |
| 🔍 **OCR Trading Bot**        | Custom | Read signals from screenshots or messages     |


**Payment:** USDT, USDC

📬 **[Contact on Telegram →](https://t.me/vecful)**

---

## 🔓 Bypassed Endpoints

### Order Management

| Endpoint                    | Status          |
| --------------------------- | --------------- |
| `/private/order/create`     | 🔓 **Bypassed** |
| `/private/order/cancel`     | 🔓 **Bypassed** |
| `/private/order/cancel_all` | 🔓 **Bypassed** |

### Trigger & Stop Orders

| Endpoint                    | Status          |
| --------------------------- | --------------- |
| `/private/planorder/place`  | 🔓 **Bypassed** |
| `/private/planorder/cancel` | 🔓 **Bypassed** |
| `/private/stoporder/cancel` | 🔓 **Bypassed** |

### Available Endpoints

| Endpoint                            | Status       |
| ----------------------------------- | ------------ |
| `/private/account/assets`           | ✅ Available |
| `/private/position/open_positions`  | ✅ Available |
| `/private/order/list/open_orders`   | ✅ Available |
| `/private/position/change_leverage` | ✅ Available |

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

- 🌐 **Website:** [mexc-bypass.com](https://mexc-bypass.com)
- 💬 **Telegram:** [@vecful](https://t.me/vecful)
- 📈 **Spot API:** [mexc-spot-bypass](https://github.com/vecful/mexc-spot-bypass)

---

<div align="center">

**[🌐 mexc-bypass.com](https://mexc-bypass.com)** · **[💬 @vecful](https://t.me/vecful)**

</div>
