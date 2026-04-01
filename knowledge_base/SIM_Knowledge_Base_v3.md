# Simple Invoice Manager (SIM) — Knowledge Base

> **Purpose:** This is a pure reference knowledge base for the Simple Invoice Manager app. It contains feature descriptions, field definitions, business concepts, alternate terminology, and contextual background. Step-by-step instructions are handled separately in the prompt layer.

---

## Table of Contents

1. [Company / Business Setup](#1-company--business-setup)
2. [Clients & Suppliers](#2-clients--suppliers)
3. [Products & Services](#3-products--services)
4. [Invoices](#4-invoices)
5. [Estimates / Proforma Invoices](#5-estimates--proforma-invoices)
6. [Sale Orders](#6-sale-orders)
7. [Purchase Orders](#7-purchase-orders)
8. [Purchase Records](#8-purchase-records)
9. [Inventory Management](#9-inventory-management)
10. [Sale Returns, Refunds & Credit Notes](#10-sale-returns-refunds--credit-notes)
11. [Sub Users & Approvals](#11-sub-users--approvals)
12. [GST Compliance — India](#12-gst-compliance--india)

---

## 1. Company / Business Setup

### What It Is
The company profile is the business identity stored in the app. It appears on every document the app generates — invoices, estimates, purchase orders, delivery notes and etc.. It includes the business name, owner details, contact information, logo, signature, and regional preferences.

### When & Who
This is a one-time setup done by the business owner immediately after installing the app. It should be updated whenever business details change.

---

### 🔁 A. Flow for Onboarding: 

1. Install the App you can see Onboarding Screen.
2. Upload your **company logo** and **owner signature** (can be added manually).
3. Fill in the required business details (see Field Reference below).
4. Set your preferences (country, currency, financial year, date format).
5. Tap **Save / Update**. Wait a moment for the database to update.

--- 

### Key Fields

| Field | What It Means |
|---|---|
| **Business / Company Name** | The legal or trade name of the business. Printed on all documents. |
| **Owner Name** | Name of the proprietor or authorized signatory. |
| **Business Address** | Registered or operating address. Appears on invoices for legal and delivery purposes. |
| **Contact Number** | Displayed on invoices for client communication. |
| **Country** | Sets regional defaults — currency symbol, tax label, date format. |
| **Currency Format** | How monetary amounts are displayed (e.g., ₹1,000.00 or $1,000.00). |
| **Financial Year Range** | The start and end months of the business's accounting period. |
| **Date Format** | How dates appear on documents (e.g., DD/MM/YYYY or MM/DD/YYYY). |
| **Company Logo** | Uploaded image that appears on all generated documents for branding. |
| **Owner Signature** | Can be drawn manually in the app or uploaded as an image. Appears at the bottom of invoices. |

### Concepts

**Financial Year (Fiscal Year):** A 12-month accounting period used for bookkeeping and tax filing. It does not have to follow the calendar year. In India, the financial year runs from **April 1 to March 31**. In the US and many other countries, it is January to December. The app uses this period to filter dashboard data and reports.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Company / Business Setup | Company Profile, Business Profile, Organization Setup |
| Financial Year | Fiscal Year, Accounting Year, Tax Year |
| Owner Signature | Authorized Signature, Signatory |

### 🎥 Video Tutorial
[How to Add Company or Business](https://www.youtube.com/watch?v=H8D5DLmF58o&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=1)

---

## 2. Clients & Suppliers

### What It Is
All business contacts are managed in one place. 

* Clients – People or businesses that receive invoices for sales. 
* Suppliers – People or businesses from whom purchases are made. 

Once a contact is added, it can be selected instantly while creating invoices or purchases, without entering details again. 

### When & Who Use it
This feature is useful for businesses that regularly deal with the same clients or suppliers. 

* Contacts can be added in advance, or 
* Created instantly while making an invoice or purchase. 

---

### 🔁 Flow

1. Tap the **hamburger menu** (three lines, top-left) on the dashboard.
2. Select **Client / Supplier**.
3. To add a **client**, tap the client tab and fill in the details.
4. Tap **Add This Client** to save.
5. To add a **supplier**, switch to the Supplier tab and follow the same steps.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Name** | Full name or business name of the client or supplier. |
| **Email ID** | Used to send invoices, estimates, or purchase orders directly from the app. |
| **Address** | Billing or shipping address. Appears on documents. |
| **Contact Number** | Phone number for reference. |
| **Opening Balance** | Choose whether the business needs to receive money from the client or if it needs to pay money to the client. - To Receive: The client owes money to the business. - To Give: The business owes money to the client. |
| **GST Number (GSTIN)/ Tax ID** | Enter your business tax identification number (e.g., GSTIN, VAT, or TIN) |

### Optional Details (via "Add More Info")
Additional fields available for richer party profiles: home address, clothing size, alternate contact, and other custom information. Useful for businesses like boutiques or tailors who maintain detailed client records.

### Concepts

**Opening Balance:** When a business starts using a new accounting app, existing clients or suppliers may already have an outstanding balance from prior transactions. Instead of recreating old invoices, this balance is entered directly as an opening figure. It carries forward into the ledger and is factored into payment tracking from day one.

**Client vs. Supplier distinction:** The same business entity can sometimes be both a client and a supplier (e.g., a business that both buys from and sells to the same company). In SIM, they are stored as separate records under each category.

### Optional sub-feature: -  

**Client/Supplier Category:** This feature lets you group your clients and suppliers (e.g., Retail, e-Commerce, POS).
    - It is not visible by default  
    - To use it, go to Settings → Client/Supplier Categorization Settings and enable it 
    - Once enabled, you will see the Category Option in the Client/Supplier form  


### Alternate Terms

| App Term | Also Known As |
|---|---|
| Client | Customer, Buyer, Party, Consumer, Account |
| Supplier | Vendor, Seller, Creditor, Distributor, Wholesaler |
| Client/Supplier List | Party Master, Contact Book, Ledger, Account Directory |
| Opening Balance | Carried Forward Balance, Prior Balance, Outstanding Balance |

### Customer/Supplier Insight: -  
Gives a complete summary of transactions, including credit limits, upcoming dues, overdue/long overdue amounts, pending items, payment behavior, and activity—all in one place. 

| Section | What It Shows | Why It’s Useful |
|---|---|---|
| Pending Sale Orders | Orders that are created but not yet completed, grouped by pending days | Helps track unfinished orders and delays |
| Pending Estimates | Total value of quotations not yet converted into sales | Shows potential future business |
| Average Days to Pay | Average time a customer takes to make payments | Helps understand payment behavior and reliability |
| Customer Activity | Graph of monthly or periodic transactions | Helps track customer engagement and business trends |
| Top Selling Products  | Most frequently purchased products by the customer  | Helps identify customer preferences and popular items |

### Export Client/Supplier List to Excel: - 
You can easily download your Client/Supplier list using the Export Excel option. 

### Batch Upload: 
Easily upload multiple clients at once using the Batch Upload feature—simply select the Client option, download the template, fill in client details, and upload the file to add them in bulk. 

### 🎥 Video Tutorial
[How to Add Client & Supplier](https://www.youtube.com/watch?v=hTjFjCd4FKM&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=3)

---

## 3. Products & Services

### What It Is
The product/service catalogue is a master list of everything the business sells. Each entry stores the item's name, pricing, tax rate, unit of measurement, and whether inventory should be tracked for it. When creating an invoice or purchase record, items are selected from this list rather than entered manually each time.

### When & Who
Used by all business types — retailers, wholesalers, service providers, manufacturers. Products are typically set up before the first invoice. They can also be created on the fly during invoice creation.

### Product vs. Service Distinction
- **Product:** A physical item that can be stocked, counted, and tracked. Inventory management applies.
- **Service:** An intangible offering (e.g., consulting, design, repairs). No physical stock exists, so inventory tracking should not be enabled.

---

### 🔁 Flow — Adding a Single Product or Service

1. From the dashboard, tap **hamburger menu** → **Products** → **Show Product List** → **Create New Product**.
2. Choose **product** or **service** type.
3. Fill in the required details (see Field Reference below).
4. Enable or disable **Product Inventory** depending on whether stock tracking is needed.
5. Tap **Save**.

---

### 🔁 Flow — Batch Upload via Excel

1. Go to **Settings** → **Batch Upload** → **Create New Product**.
2. Download the **template file** (contains required column headers).
3. Fill in your products in the spreadsheet following the header format.
4. Upload the file → tap **Yes** to confirm.
5. Review the product preview → tap **Save Products**.

---

### 🔁 Flow — Product Categorization

1. Go to **Settings** → **Enable / Disable Features** → scroll to **Product Categorization** → toggle **on**.
2. Tap **Create Category** → enter a name and standard unit → save.
3. Open any product → find the **Product Category** field → assign a category.
4. When creating new products, you can assign or create categories on the spot.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Product Name** | What the item is called. Appears on invoices exactly as entered. |
| **Sale Rate** | The price at which the business sells the item to clients. |
| **Purchase Rate** | The price at which the business buys the item from suppliers. Used for profit calculation. |
| **Tax Rate** | The GST or VAT percentage applicable to this product/service. Applied automatically when added to an invoice. |
| **Measurement Unit** | The unit of quantity — e.g., pcs, kg, litre, box, hours. Required for inventory tracking and e-way bill compliance. |
| **Enable Product Inventory** | Toggle per product. When on, stock quantity is tracked automatically through purchases and sales. Should be off for services. |
| **Opening Stock** | The quantity already on hand when the product is first added to the app. Entered only once during setup. |
| **Minimum Alert Level** | The stock quantity below which the app triggers a low-stock warning, prompting reorder. |
| **HSN Code** | A standardized numeric code that classifies the product for GST and trade purposes. Mandatory for e-invoicing and e-way bills in India. |
| **Product Category** | A user-defined group for organizing products (e.g., Electronics, Furniture, Clothing). |

### Optional Features

**Batch Upload (Excel):** Multiple products can be uploaded at once using a spreadsheet template available in Settings → Batch Upload. The same method works for bulk-uploading clients, suppliers, or updating existing product details.

**Product Categorization:** Products can be grouped into custom categories. Categories can have a standard unit defined so it applies to all products in that category by default. Must be enabled in Settings → Enable/Disable Features.

### Concepts

**HSN Code (Harmonised System of Nomenclature):** A globally standardized 6–8 digit classification code for goods, used in customs, trade, and taxation. In India, HSN codes are mandatory on GST invoices and e-way bills. The number of digits required depends on the business's annual turnover (4-digit for smaller businesses, 6-digit for turnover above ₹5 crore). Example: Mobile phones fall under HSN code 8517.

**Sale Rate vs. Purchase Rate:** The sale rate is what the customer pays. The purchase rate is what the business paid the supplier. The difference drives the gross profit margin. Example: Purchase rate ₹100, sale rate ₹150 → gross margin = ₹50 (33%).

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Product | Item, Good, Article, SKU, Stock Item, Commodity |
| Service | Work, Task, Job, Offering, Service Item |
| Sale Rate | Selling Price, MRP, Unit Price, List Price |
| Purchase Rate | Cost Price, Buy Rate, Landed Cost |
| HSN Code | Tariff Code, Commodity Code, Product Classification Code |
| Product Catalogue | Item Master, Price List, Inventory List, Product Database |
| Measurement Unit | Unit of Measure (UOM), Unit |

### 🎥 Video Tutorials
- [How to Add Product or Service](https://www.youtube.com/watch?v=EmURS_9WiG4&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=4)
- [Batch Upload Multiple Products](https://www.youtube.com/watch?v=-zSq_ioaw8A&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=5)
- [Setup Product Categorization](https://www.youtube.com/watch?v=Lyt9zfVnRHM&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=23)

---

## 4. Invoices

### What It Is
An invoice is a formal, legally binding document issued by a seller to a buyer, requesting payment for goods delivered or services rendered. It details what was sold, the quantities, prices, applicable taxes, and the total amount due. In India, a GST-registered business must issue a **tax invoice** for all taxable supplies.

### When & Who
Used by any business that sells goods or services — freelancers, retailers, wholesalers, manufacturers, service providers. An invoice is raised after a sale is made or a service is delivered.

---

### 🔁 Flow

1. Tap the **+ (plus) button** on the dashboard.
2. Set the **invoice date**. Optionally add a **due date**.
3. Tap **Client Name** → select an existing client or create a new one inline.
4. Tap **Add Items** → select products/services or add new ones on the spot.
5. Apply discount, tax, and shipping charges if applicable.
6. In the **Payment** section, record any advance or instant payment received.
7. Optionally customize the invoice (header, footer, signature, image, notes, custom fields).
8. Tap **Preview** → then **Save**, **Send**, **Print**, or **Change Template**.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Invoice Date** | The official date the invoice is raised. Used for accounting, GST filing, and payment tracking. |
| **Due Date** | The deadline by which the client must make payment. |
| **Client Name** | The party being billed. Linked to their record in the client list. |
| **Items** | The goods or services being sold. Each line includes name, quantity, rate, tax, and total. |
| **Discount** | A reduction applied to the price. Can be a flat amount (e.g., ₹200 off) or a percentage (e.g., 10% off). Applied per item or on the total. |
| **Tax** | GST, VAT, or other tax added to the invoice. Applies based on the tax rate set on each product. |
| **Shipping Charges** | Additional charges for delivery or freight. Added as a separate line item. |
| **Advance Payment** | An amount already received from the client before the invoice is finalized. Reduces the outstanding balance shown on the invoice. |
| **Header / Footer** | Custom text added above and below the invoice body — for greetings, branch details, or messages. |
| **Terms & Conditions** | Legal or business terms governing the transaction — e.g., return policy, payment terms. |
| **Custom Fields** | User-defined labels and values that appear at the top of the invoice — e.g., PO Number, Vehicle Number, LR Number. |
| **Client Signature Field** | A signature box for the client to acknowledge receipt of goods or services. |
| **Catalog Image** | An image of the business's product/service brochure attached to the invoice for branding. |

### Invoice Statuses

| Status | Meaning |
|---|---|
| **Not Received** | Payment has not been collected yet. |
| **Partially Received** | Some payment has been collected; a balance remains. |
| **Fully Received / Paid** | The complete invoice amount has been collected. |

### Concepts

**Invoice vs. Receipt:** An invoice is a *request* for payment — it says "you owe me this amount." A receipt is a *confirmation* of payment — it says "I received this amount." When an invoice is marked as paid in SIM, it serves as the payment record.

**Tax Invoice:** In India, a tax invoice is issued by a GST-registered business for taxable sales. It must include the seller's GSTIN, HSN codes, and a breakdown of GST components (CGST + SGST for intra-state, IGST for inter-state). It is the document a buyer needs to claim Input Tax Credit (ITC).

**B2B vs. B2C:**
- **B2B (Business to Business):** Invoice raised to another GST-registered business. Required for e-invoicing compliance in India.
- **B2C (Business to Consumer):** Invoice raised to an individual or unregistered buyer. Different GST reporting rules apply.

**Discount types:**
- **Amount-based discount:** A fixed rupee/dollar value subtracted (e.g., ₹100 off).
- **Percentage discount:** A proportion of the item or total price subtracted (e.g., 5% off).

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Invoice | Bill, Tax Invoice, Sales Invoice, Commercial Invoice, Tax Bill |
| Due Date | Payment Deadline, Payment Due Date |
| Discount | Rebate, Concession, Price Reduction |
| Advance Payment | Partial Payment, Token Amount, Deposit, Down Payment |
| Terms & Conditions | Payment Terms, T&C, Conditions of Sale |
| Shipping Charges | Freight, Delivery Charges, Logistics Cost |

### 🎥 Video Tutorial
[How to Create an Invoice](https://www.youtube.com/watch?v=SurVRuMIkUg&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=2)

---

## 5. Estimates / Proforma Invoices

### What It Is
An estimate is a non-binding price proposal sent to a potential client before work begins or an order is confirmed. It shows what the client will likely be charged, but it has no legal payment obligation and cannot be used for tax claims. It is used to get client approval on pricing before a final invoice is raised.

### When & Who
Used by freelancers, contractors, agencies, service providers, and any business that quotes prices before delivery. Sent when a client asks "how much will this cost?" before confirming an order.

---

### 🔁 Flow

1. Go to the **Estimate** window from the dashboard.
2. Tap **Create Estimate**.
3. Set the date (top-right).
4. Add a new or existing client.
5. Add products/services, apply taxes and discounts.
6. Optionally customize (header, footer, notes, catalog image, payment options).
7. Tap **Preview** → then **Send** via email or other method.
8. Customize the email template if needed → click **Send**.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Estimate Date** | The date the quote is prepared. Used to track the age and validity of the quote. |
| **Client Name** | The party receiving the price proposal. |
| **Items / Services** | What is being quoted — name, quantity, rate, and tax for each line. |
| **Discount** | A price reduction offered as part of the proposal. |
| **Banking Details** | The business's bank account information added so the client knows how to pay upon acceptance. |
| **UPI QR Code** | A scannable QR code linked to the business's UPI ID. The client can scan and pay instantly using any UPI-enabled app. |
| **Pay Now Button (PayPal)** | An embedded direct payment link added to the estimate for online payment. |

### Concepts

**Estimate vs. Invoice:** An estimate is a *quote* — tentative, no legal obligation. An invoice is a *bill* — legally binding, payment is due. A client can reject an estimate; once an invoice is issued, payment is expected.

**Proforma Invoice:** A document that looks like a real invoice but is issued *before* delivery of goods or services. It is used to request advance payments, for customs documentation in import/export, or to give the client a formal price confirmation. Estimates in SIM serve this purpose.

**UPI (Unified Payments Interface):** India's real-time digital payment system operated by NPCI. A UPI QR code lets clients pay directly to the business's bank account by scanning the code with any UPI app (Google Pay, PhonePe, Paytm, etc.).

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Estimate | Quote, Quotation, Price Quote, Proforma Invoice, Proposal, Price Offer |
| Banking Details | Bank Account Details, Payment Information, Beneficiary Details |
| UPI QR Code | Payment QR, Scan-to-Pay Code |

### 🎥 Video Tutorial
[How to Create an Estimate / Proforma Invoice](https://www.youtube.com/watch?v=J7f9U3ozE4M&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=6)

---

## 6. Sale Orders

### What It Is
A sale order is an internal record created when a customer confirms they want to buy, but the goods have not yet been delivered and no final invoice has been raised. It captures the order details, reserves stock intent, and initiates the fulfillment process. Once goods are delivered and an invoice is created, the sale order is linked to it and marked complete.

### When & Who
Used by wholesalers, distributors, manufacturers, and B2B businesses where orders are placed in advance and fulfilled over time. Common when a customer sends a formal Purchase Order (PO) that the business needs to acknowledge and act on.

---

### 🔁 Flow

1. From the dashboard, **swipe right to left** to find the **Sale Order** section.
2. Tap **Create Sale Order** → fill in client and item details → **Save**.
3. Status: **Pending** (order accepted, not yet delivered/invoiced).
4. When ready to deliver: tap the sale order → **Make Invoice**.
5. Go to the invoice list → tap the invoice → create a **Delivery Note** → save.
6. Once payment is received, tap the invoice → **Mark as Received**.
7. Sale order status updates to **Completed**.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Sale Order Date** | The date the customer's order was accepted. |
| **Client** | The customer who placed the order. |
| **Items** | Products/services ordered — with quantity, rate, and tax. |
| **Status** | Current stage of the order (see statuses below). |
| **Delivery Note** | A document created at the time of dispatch listing items being delivered. Accompanies physical goods. |

### Sale Order Statuses

| Status | Meaning |
|---|---|
| **Pending** | Order accepted but goods not yet delivered or invoiced. |
| **Completed** | Invoice has been raised and payment received. |

### Concepts

**Sale Order vs. Invoice:** A sale order is a *commitment to sell* — it records the customer's confirmed intent to purchase. An invoice is the *formal bill* generated after delivery and requesting payment. A sale order does not affect inventory or accounts until it is converted to an invoice.

**Typical B2B Order Fulfillment Cycle:**
Customer sends Purchase Order → Business creates Sale Order → Goods packed and dispatched with Delivery Note → Final Invoice raised → Payment collected → Sale Order marked Completed.

**Delivery Note (Challan):** A document that travels with the physical goods being dispatched. It lists items and quantities delivered and serves as proof of delivery. It is separate from the invoice — it does not request payment. The buyer signs it to acknowledge receipt.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Sale Order | Sales Order, SO, Customer Order, Work Order, Booking |
| Delivery Note | Challan, Dispatch Note, Packing Slip, Delivery Challan, Goods Dispatch Note (GDN) |
| Pending | Open, Unfulfilled, In Progress |

### 🎥 Video Tutorial
[How to Create a Sale Order](https://www.youtube.com/watch?v=swWyOktSWvg&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=22)

---

## 7. Purchase Orders

### What It Is
A Purchase Order (PO) is a document sent by the business to a supplier to formally request goods before they are received. It records what is being ordered, in what quantity, and at what agreed price. It serves as a binding commitment between the buyer and supplier before any physical exchange takes place.

### When & Who
Used by retailers, wholesalers, manufacturers, and any business that procures stock from suppliers in advance. A PO is raised when the business wants to formalize an order before goods are dispatched by the supplier. Common in formal B2B procurement where documentation is required at every step.

### Key Fields

| Field | What It Means |
|---|---|
| **Supplier** | The vendor the order is being placed with. |
| **Purchase Order Date** | The date the order is officially created and sent. |
| **Items** | Products being ordered — name, quantity, agreed rate, and applicable tax. |
| **Buy Rate / Purchase Rate** | The agreed price per unit with the supplier at the time of ordering. |
| **Discount** | Any price reduction agreed upon with the supplier for this order. |

### Purchase Order Statuses

| Status | Meaning |
|---|---|
| **Pending** | Order has been created and sent but goods have not yet been received. |
| **Completed** | Goods have been received and a purchase record has been created against this PO. |

### Concepts

**Purchase Order vs. Purchase Record:** A PO is a *request* — it is created before goods arrive and does not affect inventory or accounts. A purchase record is the *accounting entry* made after goods are physically received. Many small businesses skip POs entirely and go straight to purchase records. Formal procurement workflows use both.

**Why use a Purchase Order:** A PO protects both parties. The supplier has a documented commitment to fulfill. The buyer has a record of what was agreed — price, quantity, items — which can be verified when goods arrive. Discrepancies between the PO and what is received are caught at the point of entry.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Purchase Order | PO, Procurement Order, Supply Request, Indent |
| Supplier | Vendor, Seller, Distributor, Creditor |
| Buy Rate | Agreed Rate, Order Price, Purchase Price |

### 🎥 Video Tutorial
- [Purchase Order & Record](https://www.youtube.com/watch?v=lKUJ9sprbJU&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=21)

---

## 8. Purchase Records

### What It Is
A Purchase Record is the accounting entry created when goods are actually received from a supplier. It formally records the inward movement of stock, updates inventory quantities, and tracks the payment owed to the supplier. It can be created either by converting a completed Purchase Order or directly as a standalone entry.

### When & Who
Used by any business that buys physical goods from suppliers — shops, wholesalers, distributors, manufacturers. A purchase record is created at the moment goods arrive, regardless of whether a PO was raised beforehand.

### Key Fields

| Field | What It Means |
|---|---|
| **Supplier** | The vendor from whom goods were received. |
| **Purchase Date** | The date the goods were received and the record is created. |
| **Items** | Products received — name, quantity, buy rate, and tax. |
| **Buy Rate / Purchase Rate** | The price paid to the supplier per unit. Used for inventory cost and profit tracking. |
| **Opening Stock** | The quantity already in possession when the product was first set up in the app. Should only be entered once — during initial product creation. Never enter it again in a purchase record for an existing product, as it will double-count inventory. |
| **Minimum Alert Level** | The reorder threshold for this product. The app notifies when stock drops below this quantity. |
| **Discount** | Price reduction received from the supplier on this purchase. |
| **Payment Status** | Whether the supplier has been fully paid, partially paid, or not yet paid. |

### Purchase Record Statuses

| Status | Meaning |
|---|---|
| **Unpaid** | Supplier has not yet been paid for this purchase. |
| **Partially Paid** | Some payment has been made; a remaining balance is outstanding. |
| **Paid** | Supplier has been fully paid. |

### Important Rule: Opening Stock
If a product's opening stock was already entered during product creation, **do not enter it again in a purchase record**. The app will count it twice, resulting in an inflated inventory figure. Opening stock is a one-time entry made only during the initial product setup.

### Concepts

**GRN (Goods Received Note):** A document that confirms goods ordered from a supplier have been physically received and inspected. A purchase record in SIM serves this function — it is the internal proof that stock came in.

**Buy Rate vs. Sale Rate:** The buy rate is what the business paid the supplier per unit. The sale rate is what the business charges its customers. The difference between the two is the gross profit per unit. Example: Buy at ₹100, sell at ₹150 → gross profit = ₹50 per unit (33% margin).

**Partial Receipt:** If a supplier sends only part of an order, only the received items are recorded in the purchase record. The original PO remains open until the rest of the goods arrive.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Purchase Record | Purchase Entry, Purchase Invoice, Goods Receipt, GRN, Inward Entry |
| Supplier | Vendor, Seller, Distributor, Creditor |
| Buy Rate | Cost Price, Purchase Price, Landed Cost |
| Unpaid | Outstanding, Due, Payable |

### 🎥 Video Tutorials
- [How to Create a Purchase Record](https://www.youtube.com/watch?v=282YfFsveQs&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=7)
- [Purchase Order & Record](https://www.youtube.com/watch?v=lKUJ9sprbJU&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=21)

---

## 9. Inventory Management

### What It Is
Inventory management in SIM tracks the quantity of physical goods a business holds at any point in time. Stock levels update automatically — increasing when purchases are recorded and decreasing when sales (invoices) are made. The feature also supports manual adjustments and low-stock alerts.

### When & Who
Relevant only for businesses dealing in physical goods — shops, wholesalers, distributors, manufacturers. Not applicable to pure service businesses. Should be enabled as part of initial app setup.

### What Affects Inventory

| Action | Effect on Inventory |
|---|---|
| Invoice (Sale) | ✅ Stock decreases |
| Purchase Record | ✅ Stock increases |
| Manual Adjustment | ✅ Increases or decreases |
| Estimate / Quotation | ❌ No effect |
| Sale Order | ❌ No effect |
| Purchase Order | ❌ No effect |
| Delivery Note | ❌ No effect |


---

### 🔁 Flow — Enabling Inventory

1. Go to **Settings** → **Inventory Management** → toggle **on**.
2. Enable **Low Inventory Alert** if you want to receive notifications.
3. Select the **inventory valuation method** (see Concepts below).
4. When adding or editing a product, toggle **Enable Product Inventory** and set opening stock and minimum alert level.

---

### 🔁 Flow — Manual Inventory Adjustment

1. Go to the product in the product list.
2. Tap **Add Inventory Manually**.
3. Choose to **increase** (stock in) or **decrease** (stock out) the quantity.
4. Enter the quantity and reason.
5. Save — the change is applied instantly.

---

### 🔁 Flow — Low Inventory Alerts

1. Go to **Inventory** → tap **Alert**.
2. All products below their minimum alert level will appear here.
3. Use this to prioritize reordering before you run out.

---


### Key Fields

| Field | What It Means |
|---|---|
| **Enable Product Inventory** | Per-product toggle. When on, the app tracks quantity for this item. Should be off for services. |
| **Opening Stock** | Quantity on hand when the product is first added. Entered once during product setup only. |
| **Minimum Alert Level** | Reorder threshold. App notifies when stock falls below this number. |
| **Stock-In** | An increase in stock quantity — from purchases or manual addition. |
| **Stock-Out** | A decrease in stock quantity — from sales or manual removal. |
| **Inventory Valuation Method** | The accounting rule used to assign a cost value to stock when it is sold. |

### Manual Inventory Adjustment
Allows stock levels to be updated without creating a sale or purchase transaction. Used for:
- Items consumed internally or personally
- Damaged or expired goods
- Free samples given out
- Inventory corrections after physical stock count
- Lost or stolen goods
- Opening stock adjustments

### Inventory Valuation Methods

**1. Actual Average Buy Rate (Weighted Average Cost) — Recommended**
Calculates the average cost of all units purchased over time. When an item is sold, its cost is recorded at this average.

*Example:* 10 units bought at ₹100, then 10 more at ₹120.
Weighted average = (10×100 + 10×120) / 20 = **₹110 per unit**
Every unit sold is costed at ₹110 regardless of which batch it came from.

*Best for:* Most businesses. Smooths out price fluctuations over time.

---

**2. FIFO (First In, First Out)**
Assumes the *oldest* stock purchased is always sold *first*.

*Example:* 10 units at ₹100 (Batch 1), then 10 units at ₹120 (Batch 2).
When selling, cost is taken from Batch 1 first (₹100 each), then Batch 2 (₹120 each).

*Best for:* Perishable goods (food, medicine, cosmetics) where older stock must be sold before expiry.

*Financial effect:* In a rising-price environment, FIFO results in a lower cost of goods sold → higher reported profit compared to average cost.

---

**3. Fixed Buy Rate**
Uses a single manually defined cost price regardless of actual purchase price fluctuations.

*Example:* Fixed rate set at ₹100. Even if you later buy at ₹130, cost is still recorded at ₹100.

*Best for:* Businesses with stable, predictable purchase prices who prefer simplified cost tracking.

### Concepts

**Why inventory valuation matters:** The method chosen affects the reported cost of goods sold (COGS) and therefore the reported profit. It also affects the balance sheet value of unsold stock. This has implications for financial statements and, in some jurisdictions, tax calculations.

**Reorder Point / Minimum Alert Level:** The stock level at which a business should place a new order to avoid running out. It accounts for the time it takes to receive new stock and the expected demand during that lead time.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Inventory | Stock, Goods, Merchandise, Stockroom, Store |
| Stock-In | Goods Received, Inward, Purchase Entry, Positive Adjustment |
| Stock-Out | Goods Issued, Outward, Sales Deduction, Negative Adjustment |
| Minimum Alert Level | Reorder Point, Safety Stock Level, Low Stock Threshold |
| FIFO | First In First Out, Queue Method |
| Weighted Average | Moving Average, Average Cost Method, WAC |
| Inventory Valuation | Stock Valuation, Cost Method |

### 🎥 Video Tutorials
- [How to Enable Inventory](https://www.youtube.com/watch?v=wU3bhD1PhSs&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=8)
- [Add or Remove Inventory Manually](https://www.youtube.com/watch?v=pFQdvYH_mok&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=10)

---

## 10. Sale Returns, Refunds & Credit Notes

### What It Is
When a client returns goods, the transaction must be recorded formally — not by deleting the original invoice, which would break the accounting record. A **sale return** is a document linked to the original invoice that records the goods coming back. It keeps the original sale intact while accounting for the reversal.

A **credit note** is the monetary counterpart to a sale return — it formally records the value owed back to the client. That credit can be returned as cash (refund) or held as a balance to reduce a future invoice.

### When & Who
Used by any business that accepts returns — retailers, wholesalers, e-commerce sellers. Also used to issue goodwill credits, discount coupons, or adjustments for quality complaints, without any physical return of goods.

---

### 🔁 Flow — Recording a Sale Return

1. Tap on the original invoice → select **Make Sale Return**.
2. Enter return quantities → tap **Next** → review preview → tap **Save**.
3. A separate sale return entry is created. The original invoice remains unchanged.
4. Status of sale return: **Not Refunded**.

---

### 🔁 Flow — Issuing a Refund

1. Tap on the sale return entry → tap **Mark as Refund** → enter amount → save.
2. Status updates to **Refunded**.

---

### 🔁 Flow — Adjusting a Credit Note Against a Future Invoice

1. Enable **Credit Note** feature in settings.
2. Create a new invoice for the same client — a **Credit Note section** appears below the total.
3. Check the option to adjust or carry forward the credit.
4. Invoice shows **Partially Received** if only part was covered by credit. Collect the remaining balance and mark as paid.

---

### 🔁 Flow — Issuing a Credit Note Directly to a Client

1. Go to **Credit Note List** → tap **Create**.
2. Select client → enter amount → save. Status: **Not Adjusted**.
3. When the client makes a future purchase, create an invoice — available credit appears.
4. Apply the credit → save. Status updates to **Adjusted**.

---

### 🔁 Flow — Adjusting One Credit Note Against Multiple Invoices

1. Create or open a credit note → tap **Adjust Credit Note Against Invoice**.
2. Only invoices with unpaid or partially paid status will appear.
3. For each invoice: enter the adjustment amount.
4. Review the summary (total credit, amount adjusting, remaining balance).
5. Tap **Next** to confirm. Once fully applied, the credit note balance becomes zero.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Return Quantity** | Number of units being returned. Cannot exceed the quantity in the original invoice. |
| **Refund Amount** | The monetary value returned to the client in cash or via bank transfer. |
| **Credit Note Amount** | The value of credit issued to the client for future use. |
| **Credit Note Status** | Whether the credit has been used against an invoice yet. |
| **Sale Return Status** | Whether the monetary value of returned goods has been refunded or not. |
| **Adjustment Amount** | The portion of a credit note being applied to a specific invoice. |
| **Remaining Credit Balance** | The unused portion of a credit note still available for future transactions. |

### Statuses

| Document | Status | Meaning |
|---|---|---|
| Sale Return | Not Refunded | Return recorded; money not yet returned to client. |
| Sale Return | Refunded | Money has been returned to client. |
| Credit Note | Not Adjusted | Credit exists but has not yet been applied to an invoice. |
| Credit Note | Adjusted | Credit has been fully applied against invoice(s). |

### Credit Note Use Cases
A credit note can be issued in the following situations:
- Client returned goods (linked automatically to a sale return)
- Overcharged on a previous invoice
- Goodwill gesture or loyalty reward
- Quality complaint settlement
- Promotional discount applied after a sale

### Credit Note: Refund vs. Adjustment

| Method | What Happens |
|---|---|
| **Refund** | Money is physically returned to the client (cash, bank, UPI). The credit note is marked as refunded. |
| **Adjustment** | No money changes hands. The credit reduces the client's next invoice total. The credit note is marked as adjusted. |
| **Partial Adjustment** | Part of the credit is used on one invoice; the remaining balance carries forward. |
| **Multi-Invoice Adjustment** | A single credit note can be split and applied across multiple unpaid or partially paid invoices. |

### Concepts

**Why not delete the original invoice:** Deleting an invoice when goods are returned misrepresents financial history. The original sale happened and must remain in the books. A sale return is a *contra entry* — it offsets the original without erasing it. This is a fundamental principle of double-entry bookkeeping.

**Credit Note:** A formal document issued by a seller to a buyer, reducing the amount the buyer owes or crediting their account. It is the reverse of an invoice. Example: Invoice raised for ₹10,000 (10 items at ₹1,000 each). Client returns 2 items. Credit note issued for ₹2,000. The client now either receives ₹2,000 back or has ₹2,000 to offset a future purchase.

**Credit Note Feature Toggle:** When this feature is enabled in Settings, every sale return automatically generates a linked credit note. When disabled, sale returns are recorded without generating a credit note — only simple refunds are possible.

**Which invoices appear in multi-invoice adjustment:** Only invoices where payment is *not received* or *partially received* are shown. Fully paid invoices do not appear because there is nothing to adjust against.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Sale Return | Sales Return, Return Inward, Customer Return, Goods Return |
| Credit Note | CN, Credit Memo, Store Credit, Credit Voucher |
| Refund | Reimbursement, Cashback, Money Back |
| Adjust / Adjustment | Apply, Offset, Set Off, Redeem |
| Carry Forward | Roll Over, Defer, Pending Credit |

### 🎥 Video Tutorials
- [Record Sale Return & Refund](https://www.youtube.com/watch?v=GamzorLvw1s&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=15)
- [Adjust Sale Return with Credit Note](https://www.youtube.com/watch?v=GamzorLvw1s&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=16)
- [Issue a Credit Note to Client](https://www.youtube.com/watch?v=tIphGNPEiVs&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=17)
- [Adjust Credit Note Against Multiple Invoices](https://www.youtube.com/watch?v=mLJWo9v02Ro&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=18)

---

## 11. Sub Users & Approvals

### What It Is
Sub users are separate login accounts created by the business owner for team members — employees, sales staff, accountants. Each sub user is assigned a role that defines what they can and cannot do in the app. The Transaction Approval feature adds an additional layer of control — any action taken by a sub user requires the owner's sign-off before it becomes live in the system.

### When & Who
Relevant for businesses with more than one person using the app. Particularly important when financial control and oversight are needed — for example, when staff can create invoices but only the owner should approve and finalize them.

---

### 🔁 Flow — Creating Sub Users

1. Tap **hamburger menu** → **Sub User Management** → **Manage Sub Users**.
2. Tap **+** → enter sub user details → select a **role** → tap **Submit**.
3. Sub user receives login credentials and can access the app with their assigned permissions.
4. You can **disable, edit, or delete** a sub user at any time.

---

### 🔁 Flow — Transaction Approval Workflow

1. Enable **Transaction Requires Approval** in Sub User Management.
2. Sub user creates an invoice / estimate → it enters the **Approval Pending** queue (not yet live).
3. Sub user cannot edit or delete the transaction once submitted.
4. Owner logs in → **Cloud Account** → **Approval Pending Transactions**.
5. If the transaction involves a newly created client or product (not yet in the database), approve the client/product **first**, then approve the invoice.
6. Once approved, the invoice is added to the main transaction list and is live.

---

### Key Fields & Settings

| Field | What It Means |
|---|---|
| **Sub User Name** | The display name of the team member. |
| **Role** | The assigned position that determines the sub user's permission set. |
| **Permissions** | Individual access controls — what the sub user can create, view, edit, or delete. |
| **Transaction Requires Approval** | When enabled, all transactions created by sub users enter a pending queue and are not live until the owner approves them. |
| **Approval Status** | Pending = awaiting owner review. Approved = live in the system. Rejected = not accepted. |

### Sub User Limits
- Maximum **5 sub users** can be added to an account.
- Only **3 sub users** can be active at the same time.
- Sub users can be disabled, re-enabled, edited, or deleted at any time.

### Roles
- **Predefined Roles:** Built-in roles with preset permissions (e.g., salesperson, accountant).
- **Custom Role:** The owner can define a role with exactly the permissions required — granular control over each feature.

### Approval Workflow Logic
- When Transaction Requires Approval is enabled, a sub user's transactions do not appear in the main list until approved.
- Sub users cannot edit or delete a transaction once it has been submitted for approval.
- If a sub user creates a **new client or product** that doesn't yet exist in the database, the owner must approve the new record *before* approving the transaction linked to it.
- Fully approved transactions are then visible and active in the system like any owner-created transaction.

### Concepts

**Role-Based Access Control (RBAC):** A security model where each user is assigned a role, and each role carries a defined set of permissions. This ensures team members only access what is relevant to their function — a salesperson can create invoices but cannot view profit reports or delete records.

**Maker-Checker Principle:** A financial control mechanism where one person creates (makes) a transaction and another person reviews and approves (checks) it. This reduces errors and prevents unauthorized or fraudulent transactions. The Transaction Requires Approval feature in SIM implements this principle.

**Why approve new clients/products first:** When a sub user creates a new client or product during a transaction, those records exist only in a pending state — they are not yet official entries in the database. The owner validates them before they become permanent records. This prevents duplicate entries, typographical errors, or unauthorized additions to the system.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| Sub User | Staff Account, Employee Login, Team Member, Secondary User |
| Role | User Role, Access Level, Permission Level, Profile |
| Transaction Requires Approval | Maker-Checker, Dual Control, Approval Workflow, Authorization Workflow |
| Approval Pending | Awaiting Review, Under Approval, Pending Authorization |

### 🎥 Video Tutorials
- [How to Create Sub Users](https://www.youtube.com/watch?v=rfirjho4Njs&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=11)
- [Transaction Requires Approval](https://www.youtube.com/watch?v=SAFW1J735_s&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=12)

---

## 12. GST Compliance — India

### What It Is
SIM integrates directly with India's government GST infrastructure, enabling businesses to generate GST-compliant documents — E-Invoices and E-Way Bills — without logging into government portals separately. All GST compliance features are specific to Indian GST regulations and apply only to GST-registered businesses in India.

### Who It Applies To
- **E-Invoice (IRN):** Mandatory for GST-registered businesses with annual turnover exceeding ₹5 crore, for all B2B transactions.
- **E-Way Bill:** Required when transporting goods valued above ₹50,000 anywhere in India (inter-state; intra-state rules vary by state).

---

### Core GST Concepts

**GSTIN (GST Identification Number):** A 15-digit unique identifier assigned to every GST-registered business in India. It encodes the state code, the business's PAN number, and an entity type indicator. It is mandatory on all tax invoices.

**GSP (GST Suvidha Provider):** A government-authorized intermediary company that provides a secure API channel between third-party apps (like SIM) and the GST portal. A GSP allows SIM to submit and receive data from the GST system on behalf of the business. The GSP used by SIM is: **BVMIT Consulting Services India Private Limited**.

**GSP Credentials (Username & Password):** Separate from the regular GST portal login. Created specifically for API-based integration. Must be generated on the respective government portal (e-invoice or e-way bill) and then entered once in SIM. These credentials authorize SIM to act on behalf of the business on the GST portal.

**API (Application Programming Interface):** The technical communication layer between SIM and the government GST portal. The GSP username and password authenticate this connection.

**IRP (Invoice Registration Portal):** The government portal where B2B invoices are submitted and registered to receive an IRN.

**IRN (Invoice Reference Number):** A unique 64-character hash generated by the IRP for each registered B2B invoice. Once generated, the IRN is printed on the invoice along with a QR barcode and an acknowledgement number. An IRN confirms that the invoice has been officially registered with the GST system.

**E-Invoice:** A B2B invoice that has been registered with the IRP and assigned an IRN. The invoice itself is created in SIM; the IRN is obtained from the government portal via the GSP integration.

**E-Way Bill (EWB):** A digitally generated document required before transporting goods worth more than ₹50,000. It is submitted to the government e-way bill portal and contains details about the goods, origin, destination, and transporter. It must accompany the goods during transit.

**Input Tax Credit (ITC):** A mechanism that allows GST-registered businesses to reduce their GST liability by the GST they have already paid on their purchases. For a buyer to claim ITC, the seller must have issued a valid tax invoice with a proper IRN (for applicable cases).

---

#### 🔁 Flow- A. GSP Setup for E-Invoice

1. Go to the **e-invoice portal** → log in.
   - If already an e-Way Bill user: use the same credentials.
   - If new: click **New Registration** and complete registration.
2. After login: **Left Menu** → **API Registration** → **User Credentials**.
3. Verify the OTP sent to your registered mobile number.
4. Select **Through GSP** radio button.
5. From the GSP dropdown, choose: **BVMIT Consulting Services India Private Limited**.
6. Create your GSP Username and Password → click **Submit**.
7. Add these credentials in SIM under **Settings** → **E-Invoice Settings**.

---

#### 🔁 Flow- B. Generating an E-Invoice (IRN)

1. **Settings** → **E-Invoice Settings** → toggle **on**.
2. Enter GSTIN, GSP Username, GSP Password → tap **Validate Seller GSTIN**.
3. Create an invoice:
   - Select client → set **Invoice Type: B2B**.
   - Add products with **HSN code** (mandatory), unit, quantity, tax rate.
4. Save → status: **Ready for E-Invoice**.
5. B2B Invoice List → **Action column** → three dots → **Generate IRN**.
6. Status updates to confirmed. Preview shows IRN, barcode, acknowledgement number.
7. Print, save, or download from the app.

**To cancel an E-Invoice:**
1. Must be done within **24 hours** of generation.
2. B2B Invoice List → Action → three dots → **Cancel IRN**.
3. Choose reason → add remarks → tap **OK**.
4. Status updates to **Cancelled**.


### Key Fields — E-Invoice

| Field | What It Means |
|---|---|
| **GSTIN (Seller)** | The business's own GST number. Validated against government records before use. |
| **GSP Username** | Created on the e-invoice portal. Always prefixed with `API_` (e.g., `API_yourusername`). |
| **GSP Password** | The password for the GSP username. Must be updated in the app if changed on the portal. |
| **Invoice Type** | Must be set to **B2B** to be eligible for e-invoicing. B2B = transaction between two GST-registered businesses. |
| **HSN Code** | Mandatory for e-invoice. Classifies the goods or service for GST purposes. |
| **IRN** | The 64-character unique code generated by the IRP. Printed on the e-invoice. |
| **Acknowledgement Number** | A sequential confirmation number issued alongside the IRN. |
| **QR Barcode** | Machine-readable code printed on the e-invoice, encoding key invoice data for verification. |

### E-Invoice Rules
- Once an IRN is generated, the invoice **cannot be edited or deleted**.
- Cancellation is only possible within **24 hours** of IRN generation.
- After 24 hours, the IRN is permanent and cannot be reversed through the app.

### Invoice Statuses — E-Invoice

| Status | Meaning |
|---|---|
| **Ready for E-Invoice** | Invoice saved and eligible; IRN not yet generated. |
| **IRN Generated** | E-invoice successfully registered with the government. |
| **Cancelled** | IRN cancelled within the 24-hour window. |

---

### Key Fields — E-Way Bill

| Field | What It Means |
|---|---|
| **Seller GSTIN** | The business's GST number. Validated against government records. |
| **Buyer GSTIN** | The client's GST number. Both parties must be GST-validated to generate an e-way bill. |
| **Legal Name** | Official registered business name of the seller or buyer, as per GST records. Auto-fetched after GSTIN validation. |
| **HSN Code** | Mandatory field classifying the goods being transported. |
| **Measurement Unit** | The unit in which goods are measured (kg, pcs, litre, etc.). Mandatory for e-way bill generation. |
| **Transporter Details** | Information about the vehicle or courier carrying the goods. Required for a complete e-way bill. |
| **E-Way Bill Number** | The unique number generated upon successful submission. Must accompany the goods during transit. |

### E-Way Bill Rules
- Required for goods valued above **₹50,000** being transported.
- Must be generated **before goods leave the business premises**.
- Validity is based on distance — approximately **1 day per 100 km**.
- If mandatory fields are missing, the system shows a validation error. No penalty for failed attempts — correct and retry.

### GSP Credentials: E-Invoice vs. E-Way Bill

| Portal | Website | Same as other portal? |
|---|---|---|
| E-Invoice | einvoice1.gst.gov.in | If already an e-way bill user, same credentials can be used to log in to e-invoice portal. |
| E-Way Bill | ewaybill.gst.gov.in | If already an e-invoice user, same credentials can be used to log in to e-way bill portal. |

> **Important distinction:** The portal login (GSTIN + password) and the GSP credentials (API username + password) are two separate things. The portal login is for manual access to the government website. The GSP credentials are for app integration only.

### Alternate Terms

| App Term | Also Known As |
|---|---|
| E-Invoice | Electronic Invoice, IRN Invoice, Tax Invoice with IRN |
| E-Way Bill | EWB, Electronic Way Bill, Goods Movement Document |
| GSTIN | GST Number, GST ID, Tax ID, GST Registration Number |
| GSP | GST Suvidha Provider, API Provider, GST Intermediary |
| IRP | Invoice Registration Portal, Government E-Invoice Portal |
| IRN | Invoice Reference Number, E-Invoice Number |
| HSN Code | Harmonised System Nomenclature, Tariff Code, Product Code |
| ITC | Input Tax Credit, GST Credit, Tax Set-Off |
| Acknowledgement Number | ACK Number, Confirmation Number |

### 🎥 Video Tutorials
- [GSP Setup for E-Invoice](https://www.youtube.com/watch?v=dPSmtTALqQE&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=19)
- [Generate E-Invoice (IRN)](https://www.youtube.com/watch?v=nobz4DVwbzc&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=20)
- [GSP Setup for E-Way Bill](https://www.youtube.com/watch?v=dPSmtTALqQE&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=19)
- [Generate E-Way Bill](https://www.youtube.com/watch?v=nobz4DVwbzc&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=20)

---

*This knowledge base will be updated as more documentation becomes available.*

---

## FAQs

```json
[
  {
    "id": "faq_001",
    "question": "How to create an invoice?",
    "alternate_questions": [
      "How do I make an invoice?",
      "Create bill in app",
      "Generate invoice steps",
      "How to make a bill?",
      "Invoice banane ka tarika"
    ],
    "answer": "To create an invoice, go to the Invoice section on the dashboard and tap the + (Create New) button. Select an existing client or enter new client details on the spot. Add your products or services, apply tax, discount, and shipping charges if needed. You can also record an advance payment in the Payment section. Once done, tap Preview to review, then Save, Send, or Print the invoice. The invoice will appear in your invoice list with a payment status of Not Received until payment is collected.",
    "module": "invoice",
    "intent": "create_invoice",
    "tags": ["invoice", "billing", "create", "bill", "new invoice"],
    "related_concepts": ["invoice_definition", "invoice_statuses", "tax_invoice"],
    "priority": "high"
  },
  {
    "id": "faq_002",
    "question": "Can I add products and clients in bulk via Excel sheet?",
    "alternate_questions": [
      "How to import multiple products at once?",
      "Bulk upload clients",
      "Upload products from Excel",
      "Batch upload feature",
      "How to add many products together?"
    ],
    "answer": "Yes, SIM supports bulk uploading of products, clients, and suppliers through the Batch Upload feature. Go to Settings >> Batch Upload, select whether you want to upload Products or Clients/Suppliers, then download the provided template file. Fill in your data following the column headers in the template, then upload the completed file. The app will show a preview before saving. This is the fastest way to set up a large catalogue or client list without entering records one by one.",
    "module": "products_and_services",
    "intent": "batch_upload",
    "tags": ["batch upload", "bulk import", "excel", "products", "clients", "import"],
    "related_concepts": ["batch_upload_products", "batch_upload_clients"],
    "priority": "high"
  },
  {
    "id": "faq_003",
    "question": "How to add company details like company name, tax, logo, signature?",
    "alternate_questions": [
      "How to set up my business profile?",
      "Add company logo to invoice",
      "Where do I enter my business name?",
      "Company setup in app",
      "Add GST number to company"
    ],
    "answer": "Your company details are configured in Settings. Go to Settings >> Invoice Header & Footer (also referred to as the Company/Business Profile section), where you can add your business name, owner name, address, contact number, email, company logo, and owner signature. You can also set your country, currency format, financial year range, and date format here. These details will appear on every invoice, estimate, and document the app generates.",
    "module": "company_setup",
    "intent": "setup_company",
    "tags": ["company setup", "business profile", "logo", "signature", "company name", "settings"],
    "related_concepts": ["company_profile", "financial_year"],
    "priority": "high"
  },
  {
    "id": "faq_004",
    "question": "Is there any way to rename field names in the app?",
    "alternate_questions": [
      "Can I change field labels?",
      "How to rename invoice fields?",
      "Customize field names",
      "Change label on invoice",
      "Rename columns in documents"
    ],
    "answer": "Yes, you can rename field labels shown on your documents. Go to Settings >> Manage Fields in Documents >> Rename Field. This allows you to customize the label text for fields that appear on invoices, estimates, and other documents — for example, changing 'Shipping Charges' to 'Freight' or 'Client' to 'Customer' to match your business terminology.",
    "module": "settings",
    "intent": "customize_fields",
    "tags": ["rename field", "customize", "settings", "field names", "document labels"],
    "related_concepts": ["custom_fields"],
    "priority": "medium"
  },
  {
    "id": "faq_005",
    "question": "What is Online Store and what is it used for?",
    "alternate_questions": [
      "What is the online store feature?",
      "How does the online store work?",
      "Can customers order from my store?",
      "Online store in SIM",
      "How to share products with customers online?"
    ],
    "answer": "The Online Store feature allows you to create a digital storefront that you can share with your customers via a link. You can list your products with images in the store. When a customer places an order through your store link, it is automatically received inside the app under Online Store Sale Order List — so you can track and fulfill it just like any other sale order. It is useful for businesses that want a simple way to let customers browse and order without needing a separate e-commerce platform.",
    "module": "online_store",
    "intent": "understand_online_store",
    "tags": ["online store", "customer orders", "e-commerce", "share link", "sale order"],
    "related_concepts": ["sale_orders"],
    "priority": "medium"
  },
  {
    "id": "faq_006",
    "question": "How to create a payment receipt?",
    "alternate_questions": [
      "How do I generate a receipt?",
      "Make payment receipt in app",
      "Where are receipts in SIM?",
      "Receipt banaye",
      "How to give receipt to customer?"
    ],
    "answer": "To create a payment receipt, go to the Payments (Received) section, tap on a payment entry that has been received, and select Make Receipt. The generated receipt will be saved and can be accessed anytime from the Receipts section — open the Side Menu (three lines, top left) and tap Receipts. Receipts serve as formal confirmation that a payment was collected and can be shared with the client.",
    "module": "payments",
    "intent": "create_receipt",
    "tags": ["receipt", "payment receipt", "payment confirmation", "received payment"],
    "related_concepts": ["invoice_vs_receipt"],
    "priority": "high"
  },
  {
    "id": "faq_007",
    "question": "Can we use the app on a laptop or desktop?",
    "alternate_questions": [
      "Is there a web version?",
      "Can I use SIM on PC?",
      "Desktop version of Simple Invoice Manager",
      "How to use app on computer?",
      "Web access for SIM"
    ],
    "answer": "Yes, SIM has a web version available at www.simpleinvoiceweb.com. To use it, you need an active subscription and a registered cloud account. Once set up, you can log in from any browser on your laptop or desktop and access all your data — the same data syncs across the web version and your Android device(s) at no extra cost. Multiple Android devices can also be used under the same subscription.",
    "module": "account_and_subscription",
    "intent": "use_on_desktop",
    "tags": ["web version", "desktop", "laptop", "PC", "cloud account", "simpleinvoiceweb"],
    "related_concepts": ["cloud_account", "subscription"],
    "priority": "high"
  },
  {
    "id": "faq_008",
    "question": "How can I get the client statement or ledger?",
    "alternate_questions": [
      "How to see client transaction history?",
      "View customer ledger",
      "Client account statement in SIM",
      "Party ledger report",
      "How to check what a client owes?"
    ],
    "answer": "You can view a complete statement or ledger for any client from the Reports section. Go to Reports >> Sales >> Transaction History / Ledger, then tap on the specific client. This will show all transactions — invoices, payments, credit notes, and returns — associated with that client, along with the current outstanding balance. It is useful for reconciling accounts and sharing statements with clients.",
    "module": "reports",
    "intent": "view_client_ledger",
    "tags": ["client ledger", "statement", "transaction history", "report", "outstanding balance"],
    "related_concepts": ["customer_supplier_insight", "opening_balance"],
    "priority": "high"
  },
  {
    "id": "faq_009",
    "question": "Can we add product images in the app?",
    "alternate_questions": [
      "How to add photo to product?",
      "Product image upload",
      "Show product picture on invoice",
      "Add image to item",
      "Product photo kaise add kare?"
    ],
    "answer": "Yes, product images can be added in the app, but this requires POS (Point of Sale) mode to be enabled first. Go to Side Menu >> Switch to POS Mode >> Enable >> OK. Once POS mode is active, go to the Products section, tap on any product, and you will see the option to add a product image. Product images help customers visually identify items, especially useful in retail and POS environments.",
    "module": "products_and_services",
    "intent": "add_product_image",
    "tags": ["product image", "photo", "POS mode", "product picture", "visual"],
    "related_concepts": ["pos_mode", "product_catalogue"],
    "priority": "medium"
  },
  {
    "id": "faq_010",
    "question": "Can I change the font size of the invoice PDF?",
    "alternate_questions": [
      "How to increase invoice font size?",
      "Change text size on invoice",
      "Invoice PDF font customization",
      "Make invoice text bigger",
      "Adjust font in invoice template"
    ],
    "answer": "Yes, you can customize the font size of your invoice. Go to Settings >> Invoice Template Setting >> Invoice Theme. From here you can adjust Overall Sizes (affects the entire invoice uniformly) or Individual Sizes (lets you change specific elements independently). Scroll to the bottom to find the Change Font Size option, make your adjustments, tap Done, then Save. This applies to the PDF that is generated when you print or share an invoice.",
    "module": "settings",
    "intent": "customize_invoice_font",
    "tags": ["font size", "invoice template", "PDF", "customize invoice", "text size"],
    "related_concepts": ["invoice_template"],
    "priority": "low"
  },
  {
    "id": "faq_011",
    "question": "Can we show the outstanding balance on the invoice?",
    "alternate_questions": [
      "How to display pending dues on invoice?",
      "Show client outstanding on invoice",
      "Display total due amount on bill",
      "Outstanding payment on invoice PDF",
      "Show how much client owes on invoice"
    ],
    "answer": "Yes, SIM can display a client's total outstanding balance on their invoice. Go to Settings >> Invoice Template Setting, then look for the Total Outstanding Payment (of the client) option and enable it, then tap Done. Once enabled, every invoice generated for that client will show their cumulative outstanding balance at the bottom of the document. This is useful for reminding clients of any previous unpaid dues at the time of billing.",
    "module": "settings",
    "intent": "show_outstanding_on_invoice",
    "tags": ["outstanding balance", "invoice template", "pending dues", "total due", "client balance"],
    "related_concepts": ["invoice_statuses", "opening_balance"],
    "priority": "medium"
  },
  {
    "id": "faq_012",
    "question": "Can we add the opening balance of clients and suppliers?",
    "alternate_questions": [
      "How to set prior balance for client?",
      "Add existing dues for customer",
      "Opening balance kaise add kare?",
      "Set starting balance for supplier",
      "How to enter balance before using app?"
    ],
    "answer": "Yes, you can add an opening balance for both clients and suppliers. Open the Side Menu (three lines, top left) >> Clients >> tap on an existing client or add a new one >> Edit Client Details >> tap Edit (top right corner) >> Opening Balance. Here you can specify whether the balance is 'To Give' (you owe the client) or 'To Receive' (the client owes you), then tap Update. Opening balance is the amount outstanding between you and the party before you started using SIM, and it carries forward into all future transaction tracking.",
    "module": "clients_and_suppliers",
    "intent": "add_opening_balance",
    "tags": ["opening balance", "prior balance", "client balance", "supplier balance", "outstanding"],
    "related_concepts": ["opening_balance_concept", "client_supplier_ledger"],
    "priority": "high"
  },
  {
    "id": "faq_013",
    "question": "How to manage inventory?",
    "alternate_questions": [
      "How to enable stock tracking?",
      "Inventory management in SIM",
      "Track product stock in app",
      "Stock management kaise kare?",
      "How to check inventory status?"
    ],
    "answer": "To use inventory management in SIM, first enable it in Settings >> Inventory Settings >> Enable and Save. After enabling, you must also turn on inventory tracking for each individual product — open the product and toggle Enable Product Inventory on, then set the opening stock quantity and minimum alert level. Once set up, the app automatically increases stock when you record a purchase and decreases it when you raise an invoice. You can view the current stock status of all products from Side Menu >> Inventory >> Check Inventory Status. Note that estimates, sale orders, purchase orders, and delivery notes do not affect inventory — only actual invoices and purchase records do.",
    "module": "inventory",
    "intent": "manage_inventory",
    "tags": ["inventory", "stock", "stock tracking", "inventory management", "enable inventory"],
    "related_concepts": ["inventory_valuation_methods", "manual_adjustment", "low_stock_alert"],
    "priority": "high"
  },
  {
    "id": "faq_014",
    "question": "Can we add commission in this app?",
    "alternate_questions": [
      "How to track agent commission?",
      "Commission feature in SIM",
      "Add salesperson commission",
      "Commission report kaise dekhe?",
      "How to manage sales agent commission?"
    ],
    "answer": "Yes, SIM has a Commission feature. First enable it by going to Settings >> Commission Setting >> Enable Commission Setting >> Done. Then set up your agents by going to Side Menu >> Commission >> Add New Agent, and filling in the agent's details and commission rate. Once an agent is created, you can assign them when creating an invoice — the commission is calculated automatically based on the invoice value. To view commission summaries and reports, go to Reports >> Other >> Commission Report.",
    "module": "commission",
    "intent": "setup_commission",
    "tags": ["commission", "agent", "sales commission", "commission report", "salesperson"],
    "related_concepts": ["sub_users", "reports"],
    "priority": "medium"
  },
  {
    "id": "faq_015",
    "question": "Can I create a sub-user with restrictions?",
    "alternate_questions": [
      "How to add staff with limited access?",
      "Create employee login in app",
      "Sub user with permissions",
      "How to restrict access for team member?",
      "Add accountant access to app"
    ],
    "answer": "Yes, you can create sub-users and assign them specific roles and permissions. Go to Side Menu >> Sub User Management >> Manage Sub User, then tap + to add a new sub-user. Enter their details and select a role — either a predefined role (like salesperson or accountant) or a custom role you define with exactly the permissions you want. You can control what each sub-user can view, create, edit, or delete. You can also enable the Transaction Requires Approval setting, which means any transaction a sub-user creates must be approved by the owner before it becomes active. Up to 5 sub-users can be added, with 3 active at a time.",
    "module": "sub_users",
    "intent": "create_sub_user",
    "tags": ["sub user", "staff", "employee", "permissions", "role", "restrictions", "access control"],
    "related_concepts": ["rbac", "maker_checker", "approval_workflow"],
    "priority": "high"
  }
]
```