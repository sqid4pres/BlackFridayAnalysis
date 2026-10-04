### Black Friday Promotional Analysis: Retail Discount Integrity Audit

###  Project Overview

This project engineers an automated data pipeline to audit Black Friday promotional structures. By leveraging combined Python automation and relational SQL modeling, the system extracts transaction schemas, processes volume distributions, audits statistical outlier thresholds, and formats data frames for interactive business intelligence dashboards. 

###  Visual Dashboard

*Review the fully interactive visual layout here:* **(https://public.tableau.com/views/BlackFridayTableauDisplay/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** 

###  Automated Technical Stack

* **Database Layer (SQL):** Aggregated pricing distribution models, isolated conditional statements (WHERE is_black_friday = 1), and built dynamic conditional flags using CASE clauses to evaluate data sample density.
* **Pipeline Layer (Python/Pandas):** Automated connection layers using sqlite3, parsed SQL relational queries straight into data structures, managed missing array values, and handled string structural formatting.
* **Visualization Layer (Tableau):** Developed structured layout dashboards mapping high-level KPIs alongside categorized horizontal bar graphs to verify markdown depth.

###  Standard Deployment Execution

To launch this data infrastructure engine locally, execute the following commands within your terminal environment: 

bash

source venv/bin/activate
pip install pandas
python3 run_analytics.py

Use code with caution.