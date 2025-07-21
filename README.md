# 🥗 HealthyBites Weekly Meal Scheduler  
**YBI Internship Project — Meal Planning and Ingredient Tracking System**

## 📘 Project Overview

This repository contains the theoretical foundation and design summary of a Python-based Command-Line Interface (CLI) application developed as part of the YBI Foundation Internship. The tool is designed to assist **HealthyBites Kitchen** in efficiently organizing weekly meal plans, managing ingredient inventories, and generating procurement-ready reports.

The system enables users to schedule meals with associated dates and ingredients, view upcoming meal plans, and generate a summary of ingredient usage across all scheduled meals.

---

## 🎯 Objectives

- To develop a digital system for scheduling weekly meals.
- To provide accurate tracking of ingredient usage for inventory and procurement.
- To ensure data consistency through validation and structured data storage.
- To enable CSV export of ingredient summaries for operational efficiency.

---

## 🧩 Core Features

### 1. Meal Scheduling
Users can input meals by specifying:
- A unique meal name.
- A valid, non-past scheduled date in `YYYY-MM-DD` format.
- A list of ingredients associated with the meal.

### 2. Data Validation
- Dates are strictly validated to ensure they follow the correct format and represent actual calendar dates.
- Past dates are rejected to maintain scheduling relevance.
- Empty or invalid ingredient entries are not accepted.

### 3. Unique Identifier Assignment
- Each meal is automatically assigned a unique identifier.
- A global counter and a tracking set are used to prevent duplicate entries.

### 4. Meal Visualization
- Scheduled meals can be displayed in chronological order.
- Each meal entry includes its name, scheduled date, and list of ingredients.

### 5. Ingredient Aggregation
- The system uses tabular aggregation to compute the frequency of each ingredient across all meals.
- This aids in understanding ingredient demand over time.

### 6. CSV Export Capability
- Users can generate and export a `.csv` file summarizing the total count of each ingredient.
- This file serves as a shopping or procurement list for operational teams.

---

## 🛠️ Technical Stack

### Programming Language:
- **Python 3.7+**

### Libraries Used:
- **`datetime`**: For date parsing and validation.
- **`pandas`**: For ingredient aggregation and data export functionality.

---

## 📊 Data Structures

- **Meal Records**: Stored as a list of dictionaries, each containing:
  - A unique ID
  - Meal name
  - Scheduled date
  - List of ingredients

- **Identifier Set**: A set is used to track unique IDs and prevent duplication.

---

## 💡 Benefits

- **Operational Efficiency**: Streamlines the weekly planning process and improves ingredient forecasting.
- **Data Integrity**: Ensures consistent and accurate data entry through validation.
- **Procurement Readiness**: Provides actionable insights into ingredient needs via exportable reports.
- **Extensibility**: The project is designed to support future features such as:
  - Persistent storage integration (e.g., databases or files)
  - Edit and delete functionalities
  - Web interface using frameworks like Streamlit or Flask

---

## 🧭 Future Enhancements

- Integration of a web-based interface for improved accessibility.
- Implementation of meal editing and deletion functionality.
- Addition of user authentication for personalized meal tracking.
- Deployment to cloud platforms for remote access and scalability.

---

## 📌 Internship Context

This project was developed during the **YBI Foundation Internship** by **Akshay Kumar**, a B.Tech student from Dhanbad, Jharkhand, India. The project demonstrates practical knowledge in software development, data handling, and user-centered design.

---

## 📃 License

This project is released under the **MIT License**, allowing for open use, modification, and distribution.
