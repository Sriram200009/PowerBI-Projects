# 📊 Customer Churn Analysis - Power BI Dashboard

Welcome to my Customer Churn Analysis project! This dashboard is the culmination of my exploration into the factors driving customer attrition within the banking sector, created using **Power BI** and **Power Query**.

## 📥 Project Overview

**Customer churn**—also known as customer attrition—is the rate at which customers discontinue their relationship with a business over a specific period. Understanding churn is crucial for financial institutions aiming to maintain a loyal customer base and enhance profitability.

### 🎯 Objective

The primary goal of this analysis is to uncover the key factors contributing to the increased customer churn rate at a commercial bank. By providing actionable insights, business stakeholders can develop informed strategies to improve customer retention and reduce churn.

## 🗄️ About the Data

- **Source**: A CSV file containing 10,000 records from a commercial bank seeking to address its churn challenges.
- **Privacy Note**: All personally identifiable information (PII) has been removed to ensure customer privacy and data security.
- **Limitations**: The dataset focuses solely on salary-earning customers, which may influence the generalizability of the findings.

### 📊 Data Dictionary

| **Column Name**     | **Description**                                                                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `customer_id`       | Unique identifier assigned to each customer by the bank.                                                                                              |
| `credit_score`      | Rating of the customer's creditworthiness based on their credit history.                                                                              |
| `country`           | Country of residence of the customer.                                                                                                                 |
| `gender`            | Gender of the customer (`Male` or `Female`).                                                                                                          |
| `age`               | Age of the customer in years.                                                                                                                         |
| `tenure`            | Number of years the customer has been with the bank.                                                                                                  |
| `balance`           | Current balance in the customer's bank account.                                                                                                       |
| `products_number`   | Number indicating the bank account type the customer has (`Prod 1`, `Prod 2`, `Prod 3`, `Prod 4`).                                                    |
| `credit_card`       | Indicates if the customer has a credit card (`Yes` or `No`).                                                                                          |
| `active_member`     | Account activity status (`Active` or `Dormant`).                                                                                                      |
| `estimated_salary`  | Approximate annual salary deposited into the customer's account (removed during data cleaning for being less relevant).                               |
| `churn`             | Indicates if the customer has left the bank (`Churned` or `Not Churned`).                                                                             |

## 🛠️ Tools Used

- **Power BI Desktop**: For data visualization and interactive dashboard creation.
- **Power Query**: For data cleaning, transformation, and modeling.
- **DAX (Data Analysis Expressions)**: For creating calculated measures.

## 📝 Analytical Approach

### 1. **Data Preparation**

Data preparation is a critical step in any data analysis project. It ensures that the data is clean, consistent, and ready for meaningful analysis. Here's how I prepared the dataset for this project:

#### 1. **Importing and Initial Transformation**

##### Data Import:

##### Imported the raw data into Power BI Desktop.

Opened the Power Query editor to begin the data transformation process.

##### Renaming the Dataset:

Renamed the dataset from customer_churn_data to Customer_Data for clarity and better representation of its content.

##### Promoting Headers:

The dataset had an auto-generated header. Promoted the first row to serve as the header, ensuring column names accurately reflected the data they contained.

This was done using the "Use First Row as Headers" option in both the Home and Transform tabs of Power Query Editor.

##### Data Cleaning and Reduction

##### Removing Irrelevant Columns:

###### Eliminated the estimated_salary column:

Rationale: The column contained estimated values, and with the balance column available—which provides actual account balances—the estimated_salary was considered less reliable and potentially redundant.

Action: Right-clicked on the estimated_salary column header and selected "Remove" to eliminate it from the dataset.

#### 2. **Data Categorization and Grouping**

Organizing data into meaningful categories enhances the analysis process. Here's how I categorized and grouped specific columns:

##### Categorizing products_number
###### Re-labeling Product Numbers:

The products_number column indicated the type of account a customer owns, represented numerically (1, 2, 3, 4).

Used the "Replace Values" option to change numeric identifiers to more descriptive labels:

Replaced 1 with "Product 1"

Replaced 2 with "Product 2"

Replaced 3 with "Product 3"

Replaced 4 with "Product 4"

Deleted the original numeric column after re-labeling to maintain data cleanliness.

##### Grouping Continuous Variables

To facilitate better analysis and visualization, I grouped continuous variables into categories.

##### Analyzing Column Profiles:

From the View tab, enabled Column Profile to examine the distribution and distinct values in each column.

##### Summary of Key Columns:

###### age:

60 distinct values ranging from 18 to 82.

###### credit_score:

354 distinct values ranging from 376 to 850.

###### balance:

649 distinct values ranging from 0 to 213,146.20.

##### Grouping Using Conditional Columns:

Employed the "Conditional Column" feature to create bins or groups for:

Age Groups (e.g., < 20, 21 - 30, 31 - 40, 41 - 50, 51 - 60, 61 - 70, > 71)

Credit Score Ranges (e.g., <=400, 401 - 500, 501 - 600, 601 - 700, 701 - 800, > 800)

3. Formatting

Ensuring data is intuitive and easy to interpret is essential, especially when presenting findings.

##### Converting Boolean Columns

The columns churn, active_member, and credit_card used binary values (0 and 1) to represent statuses. To make the data more understandable:

##### active_member:

Replaced 0 with "InActive"

Replaced 1 with "Active"

##### churn:

Replaced 0 with "Yes"

Replaced 1 with "No"

##### credit_card:

Replaced 0 with "Not Owned"

Replaced 1 with "Owned"

##### Adjusting Data Types
Verified and adjusted data types for all columns to ensure accuracy in calculations and visualizations.

For example, ensured that numerical data was set to Whole Number or Decimal Number as appropriate, and categorical data was set to Text.

4. Data Transformation

Further transformations were performed to enhance data usability and reporting capabilities.

##### Handling Custom Sorting Issues

###### Problem:

After grouping some columns and introducing symbols (e.g., <, >=) in group labels, sorting became inconsistent because the system sorted alphanumerically, not logically.

###### Solution:

Creating Reference Tables:

For each affected column (age, credit_score, balance), created a new reference table:

Right-clicked on the original query in the Queries pane and selected "Reference".

##### Removing Unnecessary Columns:

In each reference table, removed all columns except the one of interest.

##### Eliminating Duplicates:

Removed duplicate rows to have a list of unique group labels.

##### Adding Index for Custom Sort Order:

Added an Index Column that assigns a numerical value representing the desired sort order.

Used the "Conditional Column" option to manually set index values based on logical order.

##### Changing Data Types:

Ensured the index columns were set to Whole Number data type for proper sorting.

##### Implementing Custom Sort in the Model:

In the main data table, used the "Sort By Column" feature to sort the grouped column based on the index from the reference table.

##### Renaming Columns for Clarity

Updated column names to be more descriptive, enhancing readability in reports and visualizations:

active_member ➔ "Active Status"

customer_id ➔ "Customer ID"

balance ➔ "Account Balance"

products_number ➔ "Product"

5. Finalizing Data Preparation

After completing all transformations and verifications:

Clicked on "Close & Apply" in Power Query Editor.

Loaded the cleaned and transformed data into Power BI for analysis and visualization.

Result:

Ended up with four well-structured tables ready for data modeling and report creation.

### 2. **Data Modeling**

Understanding and defining relationships between tables is crucial for accurate data analysis and visualization.

#### **Exploring Table Relationships**

- **Assessing Relationships**:
  - Examined the relationships between the tables created during data preparation.
  - Ensured that all fact tables were positioned above the dimension tables in the model view for clarity.

- **Configuring Relationships**:
  - **Cardinality**:
    - Power BI automatically detected the cardinality as **Many-to-One**, which is correct for this dataset.
  - **Arranging Tables**:
    - Organized the tables logically to reflect their relationships, making the data model easier to understand and maintain.

![Data Model Diagram]("D:\Data Modeling .png")

### 3. **Visualization — Report**

Visualization transforms data into actionable insights. Here's how I built the report:

#### **Creating DAX Measures**

**DAX** (Data Analysis Expressions) is a formula language in Power BI used for calculations and data analysis.

##### **Measures Created**:

1. **Customers (Number of Customers)**

   - **Formula**:
     ```DAX
    No of Customers = count (Customer_Data[Customer_ID])
     ```
   - **Explanation**:
     - Counts the unique customer IDs to determine the total number of customers.
   - **Result**:
     - **Customers**: **10,000**

2. **Customers Churned**

   - **Formula**:
     ```DAX
    Customer Churned = CALCULATE(COUNT(Customer_Data[Churn]), Customer_Data[Churn] = "Yes")
       )
     ```
   - **Explanation**:
     - Calculates the number of customers who have churned.
   - **Result**:
     - **Customers Churned**: **2,037**

3. **Churn Rate (%)**

   - **Formula**:
     ```DAX
     Churn Rate = 'Customer Data'[Customers Churned] / 'Customer Data'[Customers]
     ```
   - **Explanation**:
     - Computes the churn rate as a percentage of total customers.
   - **Result**:
     - **Churn Rate**: **20.4%** (Formatted as a percentage)

#### **Building the Report**

- **Key Factors Analyzed**:
  - Account Balance
  - Age Group
  - Activity Status
  - Gender
  - Credit Score
  - Product Type

- **Visualizations Used**:
  - **Bar Charts**: To compare churn rates across different categories.
  - **Pie Charts**: To show the proportion of churned vs. retained customers.
  - **Slicers**: For interactive filtering by country, gender, and product type.
  - **Line Charts**: To observe trends over age groups or credit score ranges.

- **Interactive Elements**:
  - Enabled cross-filtering to see how different factors influence churn collectively.
  - Included tooltips with additional insights when hovering over data points.

![Dashboard Screenshot]("D:\Dashboard.png")

### 4. **Insights**

Analyzing the visualizations led to several significant findings:

1. **Gender Influence**:
   - **Male Customers**:
     - Churn rate within male customers is **44%**.
     - Overall male churn rate stands at **54.57%**, indicating males are more likely to churn compared to females.

2. **Credit Score Impact**:
   - Customers with **credit scores >=400** who have credit card facilities exhibit the highest churn rates.
   - Suggests that lower creditworthiness customers might be struggling with credit card debt, leading to account closure.

3. **Age Group Trends**:
   - Churn rate peaks at **57.5%** among middle-aged customers between **51–60 years**.
   - May correlate with life changes such as approaching retirement.

4. **Product Type Analysis**:
   - **Prod 1 Group**:
     - Churn rate is high at **27.7%**.
     - Similar patterns observed in age and credit score factors.
   - **Prod 2 Group**:
     - Notably, a **100% churn rate** among customers with account balances between **1k-10k**.
     - Indicates a critical issue with this product segment that needs immediate attention.

### 5. **Recommendations**

Based on the insights, the following strategies are recommended:

1. **Targeted Products for Seniors**:
   - Develop financial products tailored for customers aged **51–60** to address their specific needs as they approach retirement.
   - Could include retirement planning services, investment advisory, or favorable savings accounts.

2. **Incentive Programs for Long-Term Customers**:
   - Introduce loyalty programs rewarding customers with longer tenures.
   - Benefits could include fee waivers, higher interest rates on deposits, or exclusive offers.

3. **Exclusive Packages for High-Balance Customers**:
   - Offer perks such as travel packages, discounted investment opportunities, or concierge services to customers with balances over **200k**.
   - Aims to increase satisfaction and reduce churn among valuable customers.

4. **Investigate Prod 2 Issues**:
   - Conduct in-depth analysis to understand why there's a **100% churn rate** for **Prod 2** customers with low account balances.
   - Possible actions include customer surveys, reviewing product features, or market comparisons.

5. **Credit Score Support**:
   - Provide financial education or assistance programs for customers with low credit scores.
   - Helps improve their financial health and strengthens their relationship with the bank.

### 6. **Conclusion**

This Power BI analysis provided valuable insights into the major factors influencing customer churn at the bank:

- **Key Findings**:
  - High churn rates are associated with certain age groups, lower credit scores, and specific product types.
  - Middle-aged customers and those with lower account balances are particularly at risk.

- **Strategic Impact**:
  - By focusing on the identified areas, the bank can implement targeted strategies to improve customer retention.
  - Regular evaluation of these strategies is essential to adapt to changing customer needs and market conditions.

- **Data Quality Assurance**:
  - Throughout the analysis, ensured data quality by thorough cleaning and proper modeling.
  - Accurate insights depend on reliable data, making this step crucial.

### 7. **Next Steps**

- **Broaden Data Scope**:
  - Include data from non-salary-earning customers for a more comprehensive analysis.
- **Predictive Modeling**:
  - Utilize machine learning techniques to predict churn and proactively engage at-risk customers.
- **Continuous Monitoring**:
  - Set up dashboards for real-time monitoring of churn rates and other key performance indicators.

## 📈 Dashboard Preview

*(Include updated screenshots or images of your dashboard here)*

![Customer Churn Dashboard](link-to-your-dashboard-image)

## 📂 Project Structure

```
Customer-Churn-Analysis/
├── Data/
│   └── customer_churn_data.csv
├── Bank-Customer-Churn-Analysis.pbix
├── Images/
│   ├── Data_Model_Diagram.png
│   ├── Dashboard_Screenshot.png
│   └── ...
└── README.md
```

## 📥 Getting Started

To explore the dashboard and analysis:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Sriram200009/Customer-Churn-Analysis.git
   ```

2. **Open the Dashboard**:

   - Ensure you have the latest version of [Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/) installed.
   - Open the `Customer_Churn_Dashboard.pbix` file located in the `Dashboard` folder.

3. **Explore the Data**:

   - Interact with the visualizations to uncover insights.
   - Review the data model and DAX formulas for a deeper understanding.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements:

- **Fork** the repository.
- **Create** a new branch: `git checkout -b feature/YourFeature`
- **Commit** your changes: `git commit -m 'Add your feature'`
- **Push** to the branch: `git push origin feature/YourFeature`
- **Open** a pull request.

## 🎉 Acknowledgements

- **Inspiration**: This project was inspired by a comprehensive youtube tutorial on [customer churn analysis](https://www.youtube.com/watch?v=HHu0FLM6Fp0&t=4s), which provided valuable insights and methodologies.
- **Data Source**: Appreciation to the anonymous commercial bank for providing the dataset, enabling practical application of analytical techniques.

## 📜 License

You can use this dataset to build your own project and practice your PowerBI skills.
