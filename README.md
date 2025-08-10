# 🛒 End-to-End E-Commerce Checkout Automation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.10%2B-green?logo=selenium)

---

## 📌 Overview
This project automates the **end-to-end checkout flow** for the [Demo Web Shop](https://demowebshop.tricentis.com/) using **Selenium WebDriver** with **Python**.  

It follows the **Page Object Model (POM)** design pattern for **maintainability** and **reusability**, incorporates **explicit waits** for dynamic elements, and includes **logging**, **assertions**, and **error handling** for robust execution.  

**Key highlights:** 
- Explicit Waits for dynamic elements
- Logging & Screenshot capture on failure
- Allure report integration for professional test reporting
- External test data management (`JSON` file)
- GitHub-ready project with `.gitignore` and virtual environment

---

## 📑 Table of Contents
1. [System Under Test (SUT)](#system-under-test-sut)
2. [Objective](#objective)
3. [Scenario](#scenario)
4. [Folder Structure](#folder-structure)
5. [Tools & Versions](#tools--versions)
6. [Setup Instructions](#setup-instructions)
7. [Execution](#execution)
8. [Test Reporting](#test-reporting)
9. [Assumptions](#assumptions)
10. [Notes](#notes)
11. [Future Improvements](#future-improvements)

---

## 🖥 System Under Test (SUT)
- **Website:** [Demo Web Shop](https://demowebshop.tricentis.com/)
- **Credentials:** A new test user account should be created manually.
- **Browser:** Chrome (ChromeDriver required)

---

## 🎯 Objective
This task is designed to assess the ability to automate a **functional end-to-end checkout flow** for an e-commerce application.  

It demonstrates:
- Proficiency in Selenium WebDriver
- Page Object Model (POM) for modular, maintainable code
- Handling of synchronization & dynamic elements
- Assertion-based validations
- Logging & error handling
- Reporting integration

---

## 📜 Scenario: End-to-End Checkout Automation
The script automates the complete checkout flow:

1. Login with newly created credentials
2. Search for a product or choose from the homepage
3. Add multiple items to the cart
4. Navigate to cart summary & validate item count and pricing
5. Proceed to checkout
6. Fill shipping/billing address details (from `test_data.json`)
7. Submit the order
8. Assert confirmation message & validate order completion

---

## 📂 Folder Structure
```plaintext
Web_Automation/
│
├── End_to_End_Checkout_Automation/
│   ├── allure-results/             # Allure report files
│   ├── logs/                        # Execution logs
│   ├── pages/                       # Page Object Model classes
│   │   ├── home_page.py
│   │   ├── login_page.py
│   │   ├── cart_summary_page.py
│   │   ├── checkout_page.py
│   │   ├── order_completion_page.py
│   │   ├── search_and_add_multiple_products.py
│   │   ├── shipping_billing_address_page.py
│   │   └── submit_order_page.py
│   ├── screenshots/                 # Captured screenshots
│   ├── tests/                       # Test scripts
│   │   ├── main.py
│   │   ├── conftest.py
│   ├── utils/                       # Helper utilities
│   │   ├── driver_factory.py
│   │   ├── json_reader.py
│   ├── test_data.json               # Test data file
│
├── .gitignore
├── README.md
``` 

---

## 🛠 Tools & Versions
- **Python** : 3.9+
- **Selenium WebDriver:** 4.10+
- **ChromeDriver:** Compatible with installed Chrome version
- **IDE:** VSCode / PyCharm
- **Test Framework:** `unittest`
- **Logging:** Python built-in logging
- **Reporting:** Allure

## ⚙ Setup Instructions 

1. ### Install Python 
- Download and Install Python 3.9+ from [Python.org](https://python.org   

2. ### Clone Repository 
<pre> ```bash git clone https://github.com/user/repo.git cd Web_Automation/End_to_End_Checkout_Automation ``` </pre>

3. ### Create a Virtual Environment 
<pre> ```bash python -m venv venv ``` </pre>

Activate it : 

- **Windows* : 
<pre> ```bash source .venv/Scripts/activate ``` <pre>
- **Mac/Linux**: 
<pre> ```bash source .venv/bin/activate ``` </pre> 

4. ### Install Dependencies 
<pre> ```bash pip install -r requirements.txt ``` </pre>

5. ### Download ChromeDriver 
- Download ChromeDriver from [ChromeDriver.org](https://chromedriver.org/downloads 
- Ensure it's added to your **system PATH** 

6. ### Configure Test Data (Optional)
Update `test_data.json`: 
<pre> ``` json {"email": "your_email.com", "password": "your_password"} ``` </pre>

7. ### Execute Code 
Run the automation test: 
 <pre> ``` bash pytest tests/main.py ``` </pre>

## 📊 Test Reporting : 
 Generate an **Alure Report**
 <pre> ``` bash allure serve allure-results ``` </pre>

## 📌 Assumptions 
- The user has manually created a new test account and updated `test_data.json` with valid credentials **OR** you can use credentials already provided in the file. 
- Product URLs in `test_data.json` are valid and exists on teh website. 

## 📝 Notes

- The script uses explicit waits to handle dynamic elements, ensuring reliability.
- Screenshots are captured on test failure and order confirmation in screenshots/.
- Logs are saved in logs/test.log for traceability.
- Allure reports are generated in allure-results/ and viewable via allure serve.
- The project follows professional coding standards with POM, OOP, and GitHub best practices. 



