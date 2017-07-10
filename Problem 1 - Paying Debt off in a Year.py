# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:34:10 2017

@author: Марианна
"""

balance = float(input("Please, enter the outstanding balance on the credit card: "))
annualInterestRate = float(input("Please, enter the annual interest rate as a decimal: "))
monthlyPaymentRate = float(input("Please, enter the minimum monthly payment rate as a decimal: "))

for number in range (12):
    monthlyInterestRate= annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
print("Remaining balance: ", round(balance, 2))
