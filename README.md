<div align="center">
  
```
███╗   ███╗███████╗██╗  ██╗ ██████╗    ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
████╗ ████║██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██╔████╔██║█████╗   ╚███╔╝ ██║         ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
██║╚██╔╝██║██╔══╝   ██╔██╗ ██║         ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
██║ ╚═╝ ██║███████╗██╔╝ ██╗╚██████╗    ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
```

![License: Proprietary](https://img.shields.io/badge/license-proprietary-red)
![Private Code](https://img.shields.io/badge/source-private-orange)
![Paid Access](https://img.shields.io/badge/access-paid-blue)

</div>

<div align="center">

<a href="#"><img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript"></a>
<a href="#"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"></a>

</div>

# 🔷 MEXC Futures API (Bypassed)

This API is for making requests that have been marked as [Under maintenance](https://mexcdevelop.github.io/apidocs/contract_v1_en/#order-under-maintenance) in MEXC API docs.

<br>

> [!NOTE]
> Get access by contacting me on Telegram: [@vecful](https://t.me/vecful)

<br>

## 🎖 Features

- ⚡ **Fast** — 200-300ms response times
- 🔐 **No third-party requests** — Direct communication with MEXC
- 🌐 **Mainnet & Testnet** — Works on both environments
- ⌨️ **TypeScript or Python** — Fully typed libraries
- 📦 **Postman Collection** — Ready-to-use API collection

---

## 💳 Pricing

| Option          | Price   | Duration | Description               |
| --------------- | ------- | -------- | ---------------------- |
| 💾 Futures API SDK Source Code | $120    | Lifetime | API code for managing orders |
| 💾 Spot API SDK Source Code | $120    | Lifetime | Want to create orders for newly listed spot coins? |
| 🪞 Multi-Account Copy bot  | $400  | Lifetime | Propagates created orders of one account to others |

📬 **[Contact me on Telegram »](https://t.me/vecful)**

---

## 📖 Available Endpoints

### User Assets

| Endpoint                            | Status       |
| ----------------------------------- | ------------ |
| `/private/account/assets`           | ✅ Available |
| `/private/account/asset/{currency}` | ✅ Available |
| `/private/account/transfer_record`  | ✅ Available |

### Positions

| Endpoint                                   | Status       |
| ------------------------------------------ | ------------ |
| `/private/position/list/history_positions` | ✅ Available |
| `/private/position/open_positions`         | ✅ Available |

### Order Management

| Endpoint                              | Status          |
| ------------------------------------- | --------------- |
| `/private/order/list/open_orders`     | ✅ Available    |
| `/private/order/list/history_orders`  | ✅ Available    |
| `/private/order/create`               | 🔓 **Bypassed** |
| `/private/order/cancel`               | 🔓 **Bypassed** |
| `/private/order/cancel_all`           | 🔓 **Bypassed** |
| `/private/order/cancel_with_external` | 🔓 **Bypassed** |

### Trigger & Stop-Limit Orders

| Endpoint                         | Status          |
| -------------------------------- | --------------- |
| `/private/planorder/list/orders` | ✅ Available    |
| `/private/planorder/place`       | 🔓 **Bypassed** |
| `/private/planorder/cancel`      | 🔓 **Bypassed** |
| `/private/planorder/cancel_all`  | 🔓 **Bypassed** |
| `/private/stoporder/list/orders` | ✅ Available    |
| `/private/stoporder/cancel`      | 🔓 **Bypassed** |
| `/private/stoporder/cancel_all`  | 🔓 **Bypassed** |

### Risk Limits & Leverage

| Endpoint                                 | Status       |
| ---------------------------------------- | ------------ |
| `/private/account/risk_limit`            | ✅ Available |
| `/private/position/change_margin`        | ✅ Available |
| `/private/position/leverage`             | ✅ Available |
| `/private/position/change_leverage`      | ✅ Available |
| `/private/position/position_mode`        | ✅ Available |
| `/private/position/change_position_mode` | ✅ Available |

---

## 🚀 Quick Start

### TypeScript

```typescript
import { MexcFutureAPI } from "./mexc";
import { OrderSide } from "./mexcTypes";

async function main() {
  const key = 'your key'
  const api = new MexcFutureAPI(key);
  await api.createMarketOrder('BTC_USDT', OrderSide.OpenLong, 1000, 20);
}

if (require.main === module) {
  main()
}
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

if __name__ == "__main__": 
    asyncio.run(main())
```


## 🔗 Related Projects

Looking for **Spot** trading bypass instead?

👉 **[mexc-spot-bypass](https://github.com/vecful/mexc-spot-bypass)**

👉 **[overview-page](https://www.mexc-bypass.com/)**

---

## 💌 Contact

<a href="https://t.me/vecful"><img src="https://img.shields.io/badge/Telegram-@vecful-2CA5E0?logo=telegram&logoColor=white" alt="Telegram"></a>

For access, questions, or custom integrations — reach out on Telegram: **[@vecful](https://t.me/vecful)**
