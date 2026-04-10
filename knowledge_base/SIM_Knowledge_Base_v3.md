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
10. [Sale Returns, Refunds & Credit Notes](#10-sales-return-refunds--credit-notes)
11. [Sub Users & Approvals](#11-sub-users--approvals)
12. [GST Compliance — India](#12-gst-compliance--india)

---

## 1. Company / Business Setup

### What It Is
A feature that lets you set up and manage your business details either during first-time onboarding or later from the app settings (Primary Settings, Invoice Header & Footer).

### When & Who
Filled by the business owner during initial app setup (onboarding) and updated anytime later from settings whenever business information changes.

---

### 🔁 A. Flow for Onboarding: 

1. Install the App you can see Onboarding Screen.
2. Upload your **company logo** and **owner signature** (can be added manually).
3. Fill in the required business details (see Field Reference below).
4. Set your preferences (country, currency, financial year, date format).
5. Tap **Save / Update**. Wait a moment for the database to update.
6. Note:- [If you want access this information inside the app]

    1. Go to Settings >> Primary Setting (Transaction No., Tax Identification Type, Country, Financial Year, Currency Format, Bumber Format, Date Format)

    2. Go to Settings >> Invoice Header/Footer (Logo, Company Name, Address, Phone Number, Email Address, Website, Head Note/Foot Note, Signature and Paid Stamp)

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
| **Tax Identification Type** | Simply means the kind of tax ID format being used based on a country’s system. |
| **Date Format** | How dates appear on documents (e.g., DD/MM/YYYY or MM/DD/YYYY). |
| **Company Logo** | Uploaded image that appears on all generated documents for branding. |
| **Owner Signature** | Can be drawn manually in the app or uploaded as an image. Appears at the bottom of invoices. |
| **Paid Stamp** | Paid Stamp feature display a clear **PAID** mark on document to indicate that the payment has been completed. |

### Concepts

**Financial Year (Fiscal Year):** A Financial Year (Fiscal Year) is a 12-month accounting period used for bookkeeping and tax reporting, which may differ from the calendar year. The app uses this period to filter dashboard data and reports

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

* Clients – businesses that receive invoices for sales. 
* Suppliers – businesses from whom purchases are made. 

Once a contact is added, it can be selected instantly while creating invoices or purchases, without entering details again. 

### When & Who Use it
This feature is useful for businesses that regularly deal with the same clients or suppliers. 

* Contacts can be added in advance, or 
* Created instantly while making an invoice or purchase. 

---

### 🔁 Flow

1. Tap the **hamburger menu (☰)** (three lines, top-left) on the dashboard.
2. Select **Client / Supplier**.
3. To add a **client**,click on the **Add Client** and fill the details and save.
4. To add a **supplier**, switch to the Supplier tab and follow the same steps.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Opening Balance** | Choose what applies: - To Receive: You will get money from the client - To Give: You will pay money to the client
| **GST Number (GSTIN)/ Tax ID** | Enter your business tax identification number (e.g., GSTIN, VAT, or TIN) |


### Alternate Terms

| App Term | Also Known As |
|---|---|
| Client | Customer, Buyer, Party, Consumer, Account |
| Supplier | Vendor, Seller, Creditor, Distributor, Wholesaler |
| Client/Supplier List | Party Master, Contact Book, Ledger, Account Directory |
| Opening Balance | Carried Forward Balance, Prior Balance, Outstanding Balance |

### Optional Sub-Features: 

**Transaction history-** It shows the sales and payment that were recorded in a table format. User can select the transaction by tapping the rows that he wants to refer to and add changes if necessary 


### Export Client/Supplier List to Excel: - 
You can easily download your Client/Supplier list using the Export Excel option. 

---

### Interaction with other features - dependency , side effects 

#### Customer/Supplier Insight: -  
Gives a complete summary of transactions, including credit limits, upcoming dues, overdue/long overdue amounts, pending items, payment behavior, and activity—all in one place. 

| Section | What It Shows | Why It’s Useful |
|---|---|---|
| Pending Sale Orders | Orders that are created but not yet completed, grouped by pending days | Helps track unfinished orders and delays |
| Pending Estimates | Total value of quotations not yet converted into sales | Shows potential future business |
| Average Days to Pay | Average time a customer takes to make payments | Helps understand payment behavior and reliability |
| Customer Activity | Graph of monthly or periodic transactions | Helps track customer engagement and business trends |
| Top Selling Products  | Most frequently purchased products by the customer  | Helps identify customer preferences and popular items |

**Credit limit**: Up to what limit would you allow the client to obtain credit from you against invoices. The customer insight records and shows for each client to remind you if the client has crossed the threshold limit that you have set for the client 


Report – Top 5 customers on the basis 

- **Customer Category-** If there are existing client, you can create categories to sort the client list to prioritize at different levels 

- **Payment received/ Payment Paid-** To record the payment you have to have a client/supplier against whom the payment is recorded 

- **Receivables / Payables–** That shown a list of clients that owes you and a total receivable about 

### Batch Upload: 
Easily upload multiple clients at once using the Batch Upload feature—simply select the Client option, download the template, fill in client details, and upload the file to add them in bulk. 

--- 

### 🎥 Video Tutorial
[How to Add Client & Supplier](https://www.youtube.com/watch?v=hTjFjCd4FKM&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=3)

---

## 3. Products & Services

### What It Is
The Products & Services section helps you manage all the goods and services your business offers. You can save each item’s key details—like name, description, price, and tax—and reuse them in invoices to make billing faster and more consistent. 

### Who should use this? 
All businesses—whether selling physical goods (a shop), digital products (a SaaS), or services (a consultant or salon).

### When do you use it? 
Set up before creating your first invoice or add products directly while creating an invoice. 

---

### 🔁 Flow — Adding a Single Product or Service

1. Go to Dashboard >> Menu (☰) >> Product >> Product List
2. Go to Product List >> Add New Product
3. Tap Add New Product
4. Fill required fields (Name, Price, Category, etc.)
5. Enable or disable inventory tracking as needed
6. Tap Save

---

### Key Fields

| Field | What It Means |
|---|---|
| **Sale Rate** | Price at which the item is sold to clients. |
| **Purchase Rate** | Price at which the item is purchased from suppliers; used for profit calculation. |
| **Tax Rate** | Applicable GST or VAT percentage. Automatically applied invoices. |
| **Opening Stock** | Initial stock quantity when the product is added. |
| **Minimum Alert Level** | Stock threshold that triggers a low-stock warning for reordering. |
| **HSN Code** | A number that identifies a product. |

### Optional Features

**Product Categorization:** 
- This feature lets you group your products into categories (e.g., Electronics, Services, Raw Materials). 
- It is not visible by default. To use it, go to Settings → Product Categorization Setting and enable it.Once enabled, you can create categories using the “Add Category” button and assign them to products. You can also enable “Group Line Items by Product Category” to automatically group items by category invoices and other documents.

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

### Manage Product Rates: 
Let's quickly set or update the selling price (Sale Rate) and purchase cost (Buy Rate) for your products. 

**How to use**: 
1. Go to Product → Manage Product Rates.  
2. Find the product using the search box or scroll in the list.  
3. Enter the selling price under Sale Rate and the cost price under Buy Rate.  
4. Click Done to save or cancel discard changes. 


### Export Product List to Excel:  
You can easily download your Product List using the Export Excel option. 

### Batch Upload (Products via Excel) 
- Add multiple products at once using an Excel file. 
- Go to Settings → Batch Upload → Create New Product. 
Download the template, fill in product details, and upload it. 
Confirm, review the preview, then tap Save Products. 

### Online store:  
Products added to the Product List automatically appear in the Online Store


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

1. From the dashboard, **swipe right to left** to find the **Invoice** section.
2. Tap **Add New Invoice** Set the invoice date. Optionally add a due date.
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
| **Due Date** | The deadline by which the client must make payment. |
| **Items** | The goods or services being sold. Each line includes name, quantity, rate, tax, and total. |
| **Discount** | A reduction applied to the price. Can be a flat amount (e.g., ₹200 off) or a percentage (e.g., 10% off). Applied per item or on the total. |
| **Tax** | GST, VAT, or other tax added to the invoice. Applies based on the tax rate set on each product. |
| **Shipping Charges** | Additional charges for delivery or freight. Added as a separate line item. |
| **Custom Fields** | User-defined labels and values that appear at the top of the invoice — e.g., PO Number, Vehicle Number, LR Number. |

### Invoice Statuses

| Status | Meaning |
|---|---|
| **Not Received** | Payment has not been collected yet. |
| **Partially Received** | Some payment has been collected; a balance remains. |
| **Fully Received / Paid** | The complete invoice amount has been collected. |


### Optional Features

**NOTE**: This feature will be reflected in invoices once the setting is enabled from the main settings

- **Recurring Invoice-** A recurring invoice is an invoice that is automatically created and sent at regular intervals.

- **B2B Invoice-** An e-invoice (electronic invoice) is a digitally created and government-validated invoice used mainly for GST reporting.

- **e-way Bills-** An e-way bill is a digital document required for transporting goods
  Commission is an amount of money paid to someone for making a sale or helping complete a deal.

- **Delivery Note-** A delivery note is a document sent along with goods when they are delivered to a customer.

- **Credit Note-** A credit note is a document issued by a seller to a buyer to reduce the amount the buyer owes.

- **Sale Return-** A sale return happens when a customer returns goods they bought from a seller.

- **Reports-** Sale/Payment Report, sales by client, sales by product,sales by category,History of sales/payment, invoice aging, detailed sales report.


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
A sale order is created when a customer confirms they want to buy from you, but you haven’t delivered the goods or raised the final invoice yet. It serves as an internal record that reserves stock and initiates the fulfillment process.

### When & Who
Wholesalers, distributors, manufacturers, or any business where orders are placed in advance and fulfilled later. Common in B2B trade. When: When a customer sends you an order and you want to formally accept it, reserve inventory, and track delivery.

---

### 🔁 Flow for creating the Sale Order

1. From the dashboard, **swipe right to left** to find the **Sale Order** section.
2. Tap **Create Sale Order** → fill in client and item details → **Save**.
3. Status: **Pending** (order accepted, not yet delivered/invoiced).

---

### 🔁 Flow for creating the Sale Order to Invoice
1. When ready to deliver: tap the Sale order → **Make Invoice** → save.
2. Once payment is recieved, Sale order status updates to **Completed**.

---

### Sale Order Statuses

| Status | Meaning |
|---|---|
| **Pending** | Order accepted but goods not yet delivered or invoiced. |
| **Completed** | Invoice has been raised and payment received. |
| **Manually Completed** | You force-close the sale order manually, even if it’s not fully fulfilled or completed. |
| **Cancelled** | The sale order is completely cancelled and will not be processed. |

### Concepts

**Sale Order vs. Invoice:** A sale order is a *commitment to sell* — it records the customer's confirmed intent to purchase. An invoice is the *formal bill* generated after delivery and requesting payment. A sale order does not affect inventory or accounts until it is converted to an invoice.

**Reference Number on Invoice:**
When you create an invoice from a sale order, the invoice is automatically assigned the corresponding sale order reference number.
This helps you easily track and search for invoices linked to a specific sale order from the invoice list.
Using two sale orders with same customer we can create a single invoice record.

### 🎥 Video Tutorial
[How to Create a Sale Order](https://www.youtube.com/watch?v=swWyOktSWvg&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=22)

---

## 7. Purchase Orders

### What It Is
A Purchase Order (PO) is a document sent by the business to a supplier to formally request goods before they are received. It records what is being ordered, in what quantity, and at what agreed price. It serves as a binding commitment between the buyer and supplier before any physical exchange takes place.

### When & Who
Used by retailers, wholesalers, manufacturers, and any business that procures stock from suppliers in advance. A PO is raised when the business wants to formalize an order before goods are dispatched by the supplier. Common in formal B2B procurement where documentation is required at every step.

---

### 🔁 Flow for creating the Purchase Order

1. From the dashboard, **swipe right to left** to find the **Purchase Order** section.
2. Tap **Create Purchase Order** → fill in client and item details → **Save**.
3. Status: **Pending** (order accepted, not yet delivered/invoiced).

---

### 🔁 Flow for creating the Purchase Order to Purchase Record
1. When ready to deliver: tap the Purchase order → **Make Purchase Record** → save.
2. Once payment is paid, Purchase order status updates to **Completed**.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Buy Rate / Purchase Rate** | The agreed price per unit with the supplier at the time of ordering. |
| **Discount** | Any price reduction agreed upon with the supplier for this order. |

### Purchase Order Statuses

| Status | Meaning |
|---|---|
| **Pending** | Order has been created and sent but goods have not yet been received. |
| **Completed** | Goods have been received and a purchase record has been created against this PO. |
| **Manually Completed** | You force-close the PO manually, even if it’s not fully fulfilled or completed. |
| **Cancelled** | The purchase order is completely cancelled and will not be processed. |

### Concepts

**Purchase Order vs. Purchase Record:** A PO is a *request* — it is created before goods arrive and does not affect inventory or accounts. A purchase record is the *accounting entry* made after goods are physically received. Many small businesses skip POs entirely and go straight to purchase records. Formal procurement workflows use both.

**Why use a Purchase Order:** A PO protects both parties. The supplier has a documented commitment to fulfill. The buyer has a record of what was agreed — price, quantity, items — which can be verified when goods arrive. Discrepancies between the PO and what is received are caught at the point of entry.

**Reference Number on Purchase Record:**
When you create an purchase record from a purchase order, the purchase record is automatically assigned the corresponding purchase order reference number.
This helps you easily track and search for purchase linked to a specific purchase order from the purchase list.
Using two purchase orders with same supplier we can create a single purchase record.

### 🎥 Video Tutorial
- [Purchase Order & Record](https://www.youtube.com/watch?v=lKUJ9sprbJU&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=21)

---

## 8. Purchase Records

### What It Is
A Purchase Record is the accounting entry created when goods are actually received from a supplier. It formally records the inward movement of stock, updates inventory quantities, and tracks the payment owed to the supplier. It can be created either by converting a completed Purchase Order or directly as a standalone entry.

### When & Who
Used by any business that buys physical goods from suppliers — shops, wholesalers, distributors, manufacturers. A purchase record is created at the moment goods arrive, regardless of whether a PO was raised beforehand.

---

### 🔁 Flow

1. From the dashboard, **swipe right to left** to find the **Purchase** section.
2. Tap **Add New Purchase Record** Set the purchase date. Optionally add a due date.
3. Tap Supplier Name → select an existing supplier or create a new one inline.
4. Tap Add Items → select products/services or add new ones on the spot.
5. Apply discount, tax, and shipping charges if applicable.
6. In the Payment section, record any advance or instant payment Paid.
7. Optionally customize the purchase record (header, footer, signature, image, notes, custom fields).
8. Tap Preview → then Save, Send, Print, or Change Template.

---

### Key Fields

| Field | What It Means |
|---|---|
| **Opening Stock** | The quantity already in possession when the product was first set up in the app. Should only be entered once — during initial product creation. Never enter it again in a purchase record for an existing product, as it will double-count inventory. |
| **Minimum Alert Level** | The reorder threshold for this product. The app notifies when stock drops below this quantity. |

### Purchase Record Statuses

| Status | Meaning |
|---|---|
| **Unpaid** | Supplier has not yet been paid for this purchase. |
| **Partially Paid** | Some payment has been made; a remaining balance is outstanding. |
| **Paid** | Supplier has been fully paid. |

### Important Rule: Opening Stock
If a product's opening stock was already entered during product creation, **do not enter it again in a purchase record**. The app will count it twice, resulting in an inflated inventory figure. Opening stock is a one-time entry made only during the initial product setup.

### Concepts

**Purchase Record:** A document that confirms goods ordered from a supplier have been physically received and inspected. A purchase record in SIM serves this function — it is the internal proof that stock came in.

**Buy Rate vs. Sale Rate:** The buy rate is what the business paid the supplier per unit. The sale rate is what the business charges its customers. The difference between the two is the gross profit per unit. Example: Buy at ₹100, sell at ₹150 → gross profit = ₹50 per unit (33% margin).

**Discount types:** Amount-based discount: A fixed rupee/dollar value subtracted (e.g., ₹100 off). - Percentage discount: A proportion of the item or total price subtracted (e.g., 5% off).

**Note-**
Reports - You can check purchase/ payment report, detailed purchase report, Purchase order report.

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

### Flow — Automatic Inventory Adjustment
When a user creates a purchase record, the stock quantity for the respective products is automatically updated in the inventory.


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

### Interaction with Other Features (Dependencies & Side Effects)

- **Reorder Management:**
This feature allows you to generate purchase orders based on the minimum stock level set when enabling inventory for a product.

- **Batch Upload (Inventory Data):**
You can update the existing product list or add inventory-related data during product creation using batch upload.

- **Sales Return:**
If a sales return is generated from an invoice (i.e., goods are returned by the customer), the corresponding sales return document will update the inventory.

- **Cost of Goods Sold (COGS):**
COGS is directly related to the inventory valuation method used.

### Optional Sub-Feature

- **Physical Stock-Take:**
At the end of the day, there may be differences between the inventory calculated by the app and the actual physical stock in your warehouse.
This feature allows you to correct such differences by adding Reconciliation Edits to the product list along with their current stock.

Also add Reconciliation Edit in the Field References section of Inventory Management.


### 🎥 Video Tutorials
- [How to Enable Inventory](https://www.youtube.com/watch?v=wU3bhD1PhSs&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=8)
- [Add or Remove Inventory Manually](https://www.youtube.com/watch?v=pFQdvYH_mok&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=10)

---

## 10. Sales Return, Refunds & Credit Notes 
 

### What It Is 

Sales Return 

When a customer returns goods, you should not delete the original invoice, as it is part of your accounting records. 

Instead, you need to create a Sales Return. 
- A Sales Return is a document linked to the original invoice 
- It records the goods that have been returned 
- It keeps your original sale intact 
- It automatically updates your stock (inventory increases) 

In simple terms: 

Goods come back → create a Sales Return → stock is updated 

 
### Credit Note 
A Credit Note is used to handle the money value of the returned goods. 
- It records how much amount is owed back to the customer 
- You can: 
    - Refund the amount (cash/bank), or 
    - Adjust it in the next invoice 

Please Note: To use this feature, make sure Credit Note is enabled in your settings. 

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

### 🔁 Flow — Adjust Refund During Payment 

When recording a payment from a client, you can adjust the refund amount from a Sales Return. 
- Go to Payment Received 
- Select the client 
- Choose the Sales Return (Credit Note) 
- Adjust the refund amount to update the receivable for that invoice  

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
| **Adjustment** | Refund is not made, instead the credit amount is reduced from the client's next invoice total. The credit note is marked as adjusted. | 
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

### Interaction with other features - dependency , side effects 

- **Invoice:** 
The sales return is always linked to the original invoice against which the return is made. 
- **Credit Note:** 
A credit note is created for every sales return to record the amount to be refunded or adjusted. 
- **Reports:**
Sales returns are reflected in reports, helping you track returns and their impact on your business. 
- **Client / Transaction History:**
The client’s transaction history shows the sales return and updates their current balance (reduces the amount they owe). 
- **Inventory:** 
Stock is automatically updated when a sales return is created (items are added back to inventory). 
- **Payment Received:**
While recording payments, the sales return amount can be adjusted since it affects the total receivable from the client. 

---

## 11. Sub Users & Approvals

### What It Is
Sub users allow a business owner to give other people (staff, accountants, sales team) limited access to the app. Instead of sharing your owner credentials, you create separate logins for each team member with specific roles and permissions. The approval workflow ensures that all transactions made by staff require sign-off by the owner before becoming final. 

Who should use this: Business owners with employees, accountants, or sales staff who need to use the app. Especially useful for businesses where financial control and oversight are important. 

### When & Who
- When your business grows beyond a single user. 
- When staff create invoices but only you approve/finalize them. 
- When different employees handle specific tasks (e.g., invoicing, payments) and require oversight to prevent errors. 
- When managing multiple sales reps and restricting access to sensitive data (e.g., financial reports). 

---

### 🔁 Flow — Creating Sub Users

1. Tap hamburger menu (☰) → Sub User Management → Manage Sub Users. 
2. Tap + → enter the required sub user details → select a role (check permissions/you can create a custom role with you choice of permission)→ tap Submit. 

Please Note: 

- Sub user receives login credentials and can access the app with their assigned permissions. 
- Create unique login credentials for sub-user, (share the details with only the respective person to ensure privacy ) 
- You can disable, edit, or delete a sub user at any time.

---

### 🔁 Flow — Transaction Approval Workflow

- Enable Transaction Requires Approval in Sub User Management. 

SUB-USER STEPS- 

1. Sub user creates an invoice / estimate → it enters the Approval Pending queue 
2. Sub-user can check for the status of the documents created by him –  
Go to cloud account → Approval Pending Transaction 
3. Sub-User can also check if the document was rejected by selecting Approval Rejected Transaction. 
4. Sub user can update the documents present in Approval pending Transactions 
5. Edit the document and tap on Update .Also once he does the required changes, document moves back to the  
‘Approval Pending Transaction’ section, for the Owner to approve 
 
OWNER / MAIN USER STEPS- 

6. Owner logs in → Cloud Account → Approval Pending Transactions. 
7. If the transaction involves a newly created client or product (not yet in the database), approve the client/product first, then approve the invoice. 
8. Once approved, the invoice is added to the main transaction list and is live. 

---

🔁 Flow — Selecting Role for the Sub user you are creating 

1. Use the predefined roles: Partner/Manager, Sales and Billing, Purchase manager, Payment collector, Accountant 
2. Go to manage Sub- user settings, tap on Add Sub-User 
3. Under Role tap on the dropdown ‘Please select a role before proceeding 
4. Select from the list of roles available 

---

🔁 Flow — Creating a custom category of sub-user: By Add Custom Role 

1. Go to manage Sub- user settings, tap on Add Sub-User 
2. Under Role tap on the dropdown ‘Please select a role before proceeding 
3. Tap ‘+Add Custom Role’ 
4. Write the Name of the type of role- To create a category 
5. Check or un-check the list of documents or permission that this role can access 
6. Tap on ‘Save Role’ 

--- 

🔁 Flow — Specify the type of access /permission granted to the Sub-user Role 

- Go to manage Sub- user settings, tap on Add Sub-User 
- You can edit a custom role you have created OR You can create a fresh custom role 

---

🔁 Flow —For Rejected Transactions 

1. Tap hamburger menu (☰)
2. Go to cloud account → Tap on ‘Approval Rejected Transaction’ 
3. Sub user can edit tap on edit icon and → Tap on update 
(The document moves back to Approval Pending) 
4. Or delete the record 

---

⚙️ Optional Sub-Features: 

- Predefined Roles: Choose from built-in roles (e.g., salesperson, accountant) that come with preset permissions. 

- Custom Role: Define your own role with exactly the permissions you want — granular control over what each sub user can see and do. 

- Disable Sub User: Temporarily remove access without deleting the account (e.g., for a seasonal employee). 

- Approval for New Parties/Products: When a sub user creates a new client or product that doesn’t exist in the database, the owner must approve the new record before approving any related transaction. 

- Switch user – if a single device is used by multiple sub-users they can user Switch user to login two accounts at the same time 

---

### Key Fields & Settings

| Field | What It Means |
|---|---|
| **Sub User Name** | The display name of the team member. |
| **Role** | The assigned position that determines the sub user's permission set. |
| **Permissions** | Individual access controls — e.g., can create invoices, cannot delete, cannot view reports. - Allow Individual access controls (Access Invoice document but not Payment ) - You also specify the type – View, edit, delete |
| **Transaction Requires Approval** | When enabled, all transactions created by sub users enter a pending queue and are not live until the owner approves them. |
| **Approval Status** | Pending = awaiting owner review. Approved = live in the system. Rejected = not accepted. |

### Sub User Limits
- Maximum **5 sub users** can be added to an account.
- Only **3 sub users** can be active at the same time.
- Sub users can be disabled, re-enabled, edited, or deleted at any time.

### Roles
- **Predefined Roles:** Built-in roles with preset permissions (e.g., salesperson, accountant).
- **Custom Role:** The owner can define a role with exactly the permissions required — granular control over each feature.

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


### Interaction with Other Features — Dependencies & Side Effects 

- When Transaction Approval is enabled for a sub user, all their transactions require owner approval. 
- Proper device syncing is required to reflect updates across users. 
- Clients/products created by a sub user must be approved; otherwise, they cannot be used by the main user. 
- Payment approval depends on the approval of the related invoice. 
- Sub users cannot access features not enabled by the main user (e.g., Inventory, Commission, Delivery Note, Cash/Bank Transfer, Other Income). 
- If restricted, sub users cannot edit rates in invoices, estimates, sales orders, or purchases. 
- The main user can reset/change a sub user’s password to revoke access. 

 --- 

### Logical Behaviors (Different Scenarios) 

- Maximum 3 active sub users allowed. 
- Feature available only for paid users. 
- Sub users have limited access to settings. 
- If a client is rejected, related documents (Invoice, delivery note,etc.)are permanently deleted from approval list. Sub-user will have to recreate the document. 
- Sub user can edit documents in Approval Pending, but cannot modify them after approval. 

--- 

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
### A. GSP Setup for E-Invoice

#### What It Is
A one-time setup that creates GSP credentials on the government e-invoice portal and links them to SIM. Without this, SIM cannot communicate with the government system to generate IRNs.


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

#### Key Fields

| Field | Explanation |
|---|---|
| **GSTIN** | Your 15-digit GST Identification Number. Used to validate your business on the portal. |
| **GSP** | The authorized provider used by SIM: **BVM IT Consultancy Services India Private Limited** |
| **GSP Username** | Created on the e-invoice portal. Always prefixed with `API_` (e.g., `API_yourusername`). |
| **GSP Password** | The password linked to your GSP username. Keep it secure. Update it in the app if changed on the portal. |
| **Validate Seller GSTIN** | Verifies your GSTIN against the government database and auto-fills your legal business name and address. |

> **Important:** GSP credentials are completely separate from your regular GST portal login. They are used only for app-to-portal integration.

#### 🎥 Video Tutorial
[GSP Username & Password for E-Invoice](https://www.youtube.com/watch?v=dPSmtTALqQE&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=19)

---

### B. Generating an E-Invoice (IRN)

#### What It Is
An e-invoice is a B2B invoice that has been officially registered with the government's IRP and assigned a unique IRN. It is legally required for businesses with annual turnover above ₹5 crore. Once generated, the invoice is locked — it cannot be edited or deleted, ensuring authenticity and tamper-proof records.


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
| **Unique Quantity Code (UQC)** | A fixed, mandatory format for measurement units in e-invoice creation in India. The Invoice Registration Portal (IRP) requires units to be reported using a standardized Unique Quantity Code (UQC). |

#### E-Invoice Rules
- Once an IRN is generated, the invoice **cannot be edited or deleted**.
- Cancellation is only possible within **24 hours** of IRN generation.
- After 24 hours, the IRN is permanent and cannot be reversed.

##### Invoice Statuses — E-Invoice

| Status | Meaning |
|---|---|
| **Ready for E-Invoice** | Invoice saved and eligible; IRN not yet generated. |
| **IRN Generated** | E-invoice successfully registered with the government. |
| **Cancelled** | IRN cancelled within the 24-hour window. |

#### 🎥 Video Tutorial
[How to Generate E-Invoice (IRN)](https://www.youtube.com/watch?v=nobz4DVwbzc&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=20)

---

### C. GSP Setup for E-Way Bill

#### What It Is
Similar to e-invoice setup, generating e-way bills from SIM requires GSP credentials created on the government e-way bill portal. The setup process is identical, but it is done on a separate government portal.

> If you are already an e-invoice user, you can use those same portal login credentials to log in to the e-way bill portal as well. However, GSP credentials (API username/password) need to be created separately on each portal.

### 🔁 Flow 

1. Go to **evwaybill.gst.gov.in** → log in. 
    - Existing e-invoice users: same credentials work here too. 
    - New users: click **New Registration.** 
2. **Left Menu → Registration → For GSP.**
3. Verify the OTP. 
4. Select GSP: **BVMIT Consulting Services India Private Limited.** 
5. Create GSP Username and Password → save. 
6. Add credentials in SIM under **Settings** → E-Way Bill. 

#### 🎥 Video Tutorial
[GSP Username & Password for E-Way Bill](https://www.youtube.com/watch?v=dPSmtTALqQE&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=19)

---

### D. Generating an E-Way Bill

#### What It Is
An e-way bill is a mandatory digital document required before transporting goods worth more than ₹50,000 within India. It must be generated before goods leave the business premises. Without a valid e-way bill, goods can be held at checkpoints and the business may face penalties.

---

### 🔁 Flow 

1. Settings → E-Way Bill → toggle on. 
2. Enter GSTIN, GSP Username, GSP Password → tap Validate Seller GSTIN. 
3. Validate the buyer: 
    - Client List → tap client → add Legal Name + GSTIN → Validate Buyer GSTIN. 
4. Create an invoice: 
    - Add HSN code (mandatory) and measurement unit (mandatory) for each product. 
    - Apply GST. 
5. Generate e-way bill directly from the invoice, or save and generate later: 
    - Hamburger menu → Invoices → E-Way Bill section → select invoice → fill required details → Generate E-Way Bill. 
6. If validation fails: check all mandatory fields, correct, and retry. 
7. Once generated, the e-way bill appears in the E-Way Bill section. 

---

### 🔁 1. Flow:Create E-Way Bill 
You can generate an e-way bill in two ways: 
  - From E-Way Bill Section: Go to E-Way Bill → select an invoice → generate e-way bill 

  - From Invoice Form: Fill invoice details → tap “Generate E-Way Bill” → e-way bill form opens and invoice is auto-saved 

 
### 🔁 2. Flow Validate Client GSTIN 
You can validate GSTIN in two ways: 
  - From Client Section: Go to Clients → select customer → tap “Validate GSTIN” → enter details → validate → ✔️ success shown 

  - From Invoice Form: Select client → tap edit icon → enter details → validate GSTIN 

---

#### Key Fields

| Field | Explanation |
|---|---|
| **Seller GSTIN** | Your GST number. Validated against government records. |
| **Buyer GSTIN** | The client's GST number. Both seller and buyer must be GST-validated before an e-way bill can be generated. |
| **Legal Name** | The official registered business name of the seller or buyer, as per GST records. Auto-fetched after GSTIN validation. |
| **HSN Code** | Mandatory. Classifies the goods being transported. |
| **Measurement Unit (UQC)** | Mandatory. The standardized unit in which goods are measured (e.g., KGS, NOS, LTR). |
| **Transporter Details** | Information about the vehicle or courier carrying the goods. Required to complete the e-way bill. |
| **E-Way Bill Number** | The unique number generated upon successful submission. Must physically accompany the goods during transport. |

#### GSTIN Validation — Two Ways
A buyer's GSTIN can be validated from two places:
- **From the Client section:** Go to Clients → select the client → tap **Validate GSTIN** → enter details → validate.
- **From the Invoice form:** Select the client → tap the edit icon → enter GSTIN details → validate.

#### E-Way Bill Generation — Two Ways
- **From the E-Way Bill section:** Go to hamburger menu → Invoices → E-Way Bill → select an invoice → fill required details → Generate E-Way Bill.
- **From the Invoice form directly:** Fill invoice details → tap **Generate E-Way Bill** — the e-way bill form opens and the invoice is auto-saved simultaneously.

#### Key Rules for E-Way Bill

| Rule | Detail |
|---|---|
| **Value threshold** | Required for goods worth more than ₹50,000 being transported. |
| **Timing** | Must be generated before goods leave your premises. |
| **Validity** | 1 day per 200 km (or part thereof) for normal cargo vehicles. 1 day per 20 km for over-dimensional cargo. |
| **Validation errors** | If mandatory fields are missing, the system shows a specific error. Fix the flagged fields and retry — no penalty for failed attempts. |

#### 🎥 Video Tutorial
[How to Generate E-Way Bill](https://www.youtube.com/watch?v=nobz4DVwbzc&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=20)

---

### GSP Credentials: E-Invoice vs. E-Way Bill — Quick Comparison

| | E-Invoice Portal | E-Way Bill Portal |
|---|---|---|
| **Website** | einvoice1.gst.gov.in | ewaybill.gst.gov.in |
| **Can share portal login?** | If already an e-way bill user, same portal login works here | If already an e-invoice user, same portal login works here |
| **GSP credentials** | Must be created separately on this portal | Must be created separately on this portal |

> **Key distinction:** Your portal login (GSTIN + password) and your GSP credentials (API username + password) are two entirely different things. The portal login is for manually accessing the government website. The GSP credentials are exclusively for app integration.

---

### Alternate Terms

| App Term | Also Known As |
|---|---|
| E-Invoice | Electronic Invoice, IRN Invoice, Tax Invoice with IRN |
| E-Way Bill | EWB, Electronic Way Bill, Goods Movement Document |
| GSTIN | GST Number, GST ID, Tax ID, GST Registration Number |
| GSP | GST Suvidha Provider, API Provider, GST Intermediary |
| IRP | Invoice Registration Portal, Government E-Invoice Portal |
| IRN | Invoice Reference Number, E-Invoice Number |
| HSN Code | Harmonised System Nomenclature, Tariff Code, Product Classification Code |
| UQC | Unique Quantity Code, Measurement Unit Code |
| ITC | Input Tax Credit, GST Credit, Tax Set-Off |
| Acknowledgement Number | ACK Number, Confirmation Number |

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
    "answer": "Yes, you can rename field labels shown on your documents. Go to Settings >> Manage Fields >> Rename Field. This allows you to customize the label text for fields that appear on invoices, estimates, and other documents — for example, changing 'Shipping Charges' to 'Freight' or 'Client' to 'Customer' to match your business terminology.",
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