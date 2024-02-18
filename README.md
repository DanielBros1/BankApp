# BankApp

## Short Description
The BankApp is a Python project that enables users to manage their finances by adding money, withdrawing virtual funds, and currency exchange using the <b>Frankfurter API.</b> 
The latest currency exchange rate data is retrieved from the Frankfurter API every time a user logs into the app.<br>
The application features its own authentication system, and user data, accounts, and transaction history are stored in a local SQLite database. In file `currency_exchange.db` 

## Features
- <b>New user registration:</b> Users can register new accounts by providing their personal information and creating unique login credentials.
- <b>Login:</b> Registered users can log in to their accounts using their login credentials.
- <b>Adding Funds:</b> Logged-in users can add money to their bank accounts.
- <b>Withdrawal:</b> Logged-in users can withdraw funds from their bank accounts.
- <b>Currency exchange:</b> The application allows users to exchange currencies using current exchange rates retrieved from the Frankfurter API.
- <b>Transaction history:</b> Users can check the history of their transactions, including adding, withdrawing, and exchanging currencies.

## The following libraries are required
- pip install customtkinter
- pip install requests
- pip install matplotlib
- pip install pandas
- pip install Pillow
- pip install CTkMessageBox
- pip install CTkTable

App was created on Python 3.9

## Installation
- Download the repository
- Install the required libraries
- Run the `main.py` file

## Usage
- In order to test application, you can use the following credentials:
  - Username: admin
  - Password: admin
  
or register a new account. Data is stored in a local SQLite database.

## Project Status
The project is completed and no further development is planned.

### App Preview

#### LOGIN SYSTEM
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/4259510e-459f-4e58-92cd-c8a774b87b02" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/4be8724c-a197-4d9f-b837-4116085766ad" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/0d90aff8-846d-469d-a453-e71fd0b353c6" width="300">

<p>When logging in, login credentials are checked in the database. If login credentials are correct, the user is 
redirected to the main menu. If the user does not have an account, they can register a new one.
Register system checks if the username is unique and requires strong password; at least 8 characters, one uppercase 
letter, one lowercase letter, one number, and one special character. If the user meets the requirements, the account is
created and the user is redirected to the main menu. If the user does not meet the requirements, the user is informed
about the requirements and asked to try again.
</p>


#### MAIN MENU - HOME SCREEN
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/38161ea1-db41-41d7-893c-5eb537397ba7" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/4d375c2d-110d-4473-8afd-a737f4b18a19" width="300">

#### MAIN MENU - CURRENCY EXCHANGE SCREEN. Appearance and check exchange rate history
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/969673d2-806f-40bf-aa75-79140972a781" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/2780db06-4de6-4125-9a1a-c8b5475d7e62" width="300">

#### MAIN MENU - CURRENT EXCHANGE SCREEN. Calculate and exchange currency
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/7ff67f76-071d-4d06-b80a-acd84e302033" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/4dec93e5-6536-46ea-80d0-d9ebbcc80b07" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/f944845a-4d07-4797-9c98-56401221195b" width="300">

#### MAIN MENU - MY ACCOUNT SCREEN, SETTING SCREEN
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/617efefb-8aa9-4899-a5c6-9f5dfb6a62d3" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/3b4cc524-a8e2-4b6f-8711-0e5d8126e139" width="300">

#### MAIN MENU - CHECK TRANSACTION HISTORY, WITHDRAWAL SCREEN
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/5a0fa35c-3797-422c-b5bb-ad32651df270" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/7fccb436-0d18-4227-9081-220d827529e8" width="300">
<img src="https://github.com/DanielBros1/BankApp/assets/112472952/41546172-08c9-4ea4-bcfd-87a629e64a4b" width="300">


