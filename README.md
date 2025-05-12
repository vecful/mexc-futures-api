# MEXC Futures API (Bypassed)

This API is for making requests that have been marked as `Under maintenance` in MEXC API docs. (example [here](https://mexcdevelop.github.io/apidocs/contract_v1_en/#order-under-maintenance))


## Overview
The **MEXC Contract API** allows you to access and manage various aspects of the MEXC Futures trading platform programmatically. The API provides access to functionalities such as managing assets, orders, positions, and account settings.

This document details all available endpoints. Those that are marked `Under maintenance` have been **bypassed**, which means they are available to use without any restrictions.

*Code is currently only available in Typescript, Python and as Postman collection (more [here](#postman-collection)). Python version is fully typed. Other languages available upon request.*


### To get access or if you have any questions or you want to test yourself contact at:

* Telegram: [@vecful](https://t.me/vecful) (I am usually on here)
* Discord: @vecful

If you don't feel comfortable with the simple way, we can always do escrow services.

### Testimonials

<img width="77" alt="image" src="https://github.com/user-attachments/assets/6cb2150c-a0c9-4422-868a-4b71ac06596a" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/d9f56180-bd4b-414f-9fcc-d1190f7cad89" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/bcd74fa6-56e8-448a-8eb2-7bea525d6414" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/f4e026b2-21f9-4ded-94fa-d618ba88605a" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/5fc57065-8db6-4008-86f5-968a5054572b" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/46a1d169-3873-429b-a1c5-6f892f2cc6e2" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/220dde35-33a6-4671-9a3f-d8c59bfca85a" />
<img width="111" alt="image" src="https://github.com/user-attachments/assets/c1f94546-6341-4229-9b64-f702ab2c319f" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/149e57ce-b210-4e26-9adb-41ca308d54f0" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/182b5ce1-683a-463c-9112-0f1c417055ab" />
<img width="77" alt="image" src="https://github.com/user-attachments/assets/e0e13c82-69f8-4eca-9b94-0261eaf1c824" />


If you are interested in spot bypass instead, you can find more information here: [mexc-spot-bypass](https://github.com/vecful/mexc-spot-bypass)

---

## FAQ
> Does it fully support placing, cancelling, and tracking all types of futures orders (market, limit, stop-limit, etc.)?

Yes. For more info, look at [endpoints overview](#endpoints-overview) section.

> Can the bypass API fetch account info, open positions, and adjust leverage/margin?

Yes. For more info, look at [endpoints overview](#endpoints-overview) section.

> How does authentication work – do I need an API key, or does it use something else?

It doesn't use API keys.

> Is there any setup guide or quick demo so I know what I’m getting?

Brief setup guide can be seen in the example files. For a quick demo, I can send you one in a private message.

> Is the library provided as open source or as compiled/obfuscated code?

Currently, everything is open-sourced, nothing is obfuscated.

> Can the library be used with multiple accounts, or is the authentication tied to a single one?

No limitation on number of accounts.

> Does it use anything third-party to make those requests?

No.

 
---

![assets/demo.gif](assets/demo.gif)

---

## Endpoints Overview

### 1. **User Assets**

#### Get All Information of User's Assets
- **Endpoint**: `/private/account/assets`
  
#### Get Single Currency Asset Information
- **Endpoint**: `/private/account/asset/{currency}`

---

### 2. **Asset Transfer Records**

#### Get User's Asset Transfer Records
- **Endpoint**: `/private/account/transfer_record`

---

### 3. **User Positions**

#### Get Historical Positions
- **Endpoint**: `/private/position/list/history_positions`

#### Get Open Positions
- **Endpoint**: `/private/position/open_positions`

---

### 4. **Order Management**

#### Get Current Pending Orders
- **Endpoint**: `/private/order/list/open_orders`

#### Get Historical Orders
- **Endpoint**: `/private/order/list/history_orders`

#### Create a New Order (Bypassed under maintenance)
- **Endpoint**: `/private/order/create`

#### Cancel Orders (Bypassed under maintenance)
- **Endpoint**: `/private/order/cancel`

#### Cancel All Orders (Bypassed under maintenance)
- **Endpoint**: `/private/order/cancel_all`

#### Cancel the order according to the external order ID (Bypassed under maintenance)
- **Endpoint**: `/private/order/cancel_with_external`

---

### 5. **Trigger Orders and Stop-Limit Orders**

#### Get Trigger Orders
- **Endpoint**: `/private/planorder/list/orders`

#### Create a Trigger Order (Bypassed under maintenance)
- **Endpoint**: `/private/planorder/place`

#### Cancel Trigger Order (Bypassed under maintenance)
- **Endpoint**: `/private/planorder/cancel`
  
#### Cancel All Trigger Orders (Bypassed under maintenance)
- **Endpoint**: `/private/planorder/cancel_all`

#### Get Stop-Limit Orders
- **Endpoint**: `/private/stoporder/list/orders`

#### Cancel single Stop-Limit trigger order (Bypassed under maintenance)
- **Endpoint**: `/private/stoporder/cancel`

#### Cancel All Stop-Limit Orders (Bypassed under maintenance)
- **Endpoint**: `/private/stoporder/cancel_all`

---

### 6. **Risk Limits and Leverage**

#### Get Risk Limits
- **Endpoint**: `/private/account/risk_limit`

#### Change Margin
- **Endpoint**: `/private/position/change_margin`

#### Get Leverage
- **Endpoint**: `/private/position/leverage`

#### Change Leverage
- **Endpoint**: `/private/position/change_leverage`

#### Get Position Mode
- **Endpoint**: `/private/position/position_mode`

#### Change Position Mode
- **Endpoint**: `/private/position/change_position_mode`

---

## Postman collection

![image](https://github.com/user-attachments/assets/5ef3f585-c043-42ba-827d-1e435c1167ae)


