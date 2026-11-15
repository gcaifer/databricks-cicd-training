# Databricks notebook source

# Synthetic library loan data
loans = [
    {"loan_id": "LN-001", "days_late": 0},
    {"loan_id": "LN-002", "days_late": 3},
    {"loan_id": "LN-003", "days_late": 7},
]

# Identify overdue loans
overdue_loans = [
    loan for loan in loans
    if loan["days_late"] > 0
]

print(f"Total loans: {len(loans)}")
print(f"Overdue loans: {len(overdue_loans)}")
