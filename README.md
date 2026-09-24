# CoreBankingApplicationProject

## Project Overview

This project is a banking application designed for bank employees to log in to their accounts and securely access the system.

On the Login page, employees enter their account information. A CAPTCHA is used to verify the user before continuing. If the user does not have an account, they can register through the Registration page.

After registration or login, the user proceeds to the OTP verification section, where a verification code is sent to their phone via SMS.

## Features

* Employee Login
* User Registration
* CAPTCHA verification
* OTP verification via SMS
* SQL Server database connection
* Employee data management
* Graphical User Interface using Tkinter

## Technologies Used

* Python
* Tkinter
* SQL Server
* PyMSSQL
* Requests
* Python-dotenv
* CAPTCHA
* Pillow

## Project Structure

The project is organized into different layers, including:

* **Presentation** – User interface and application views
* **DataAccess** – Database connection and repositories
* **Common** – Shared services and utilities

## Authentication Flow

```text
Login
  ↓
CAPTCHA Verification
  ↓
Account Verification
  ↓
OTP Sent via SMS
  ↓
OTP Verification
  ↓
Access to the System
```

New users can register first and then continue with the authentication process.

## Project Goal

The goal of this project is to develop a secure employee authentication system while practicing Python programming, GUI development, database connectivity, and multi-step user authentication.

