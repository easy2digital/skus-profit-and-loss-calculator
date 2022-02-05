from flask import Flask, render_template, request, flash, send_file
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

class item:

	def __init__(
		self,  
		landedCost, 
		shippingCost, 
		paymentCost, 
		refundCost,
		CPA,
		discount,
		price
		):

		## Assign to self object
		self.landedCost = landedCost
		self.shippingCost = shippingCost
		self.paymentCost = paymentCost
		self.refundCost = refundCost
		self.CPA = CPA
		self.discount = discount
		self.price = price

	def calculate_profitmargin(self):
		return (self.price - self.landedCost - self.shippingCost - self.price * self.paymentCost - self.shippingCost * 2 * self.refundCost - self.CPA - self.discount * self.price) / self.price

app = Flask(__name__)
app.secret_key = "lousieasy2digital_8888001"

@app.route("/hello")
def index():
	flash("Sponsored by www.easy2digital.com : Please enter the sku's variable cost (input must be greater or equal to 0)")
	return render_template("index.html")

@app.route("/StoreUrl", methods=["POST", "GET"])
def StoreUrl():
	price1 = float(request.form['name_input'])
	landedCost1 = float(request.form['landed_cost'])
	shippingCost1 = float(request.form['shipping_cost'])
	paymentCost1 = float(request.form['payment_cost'])
	refundCost1 = float(request.form['refund_cost'])
	CPA1 = float(request.form['cpa'])
	discount1 = float(request.form['discount'])

	profitMargin1 = item(landedCost1, shippingCost1, paymentCost1, refundCost1, CPA1, discount1, price1)
	result = "{:.2%}".format(round(profitMargin1.calculate_profitmargin(), 2))
	return render_template("result.html", price1=price1, landedCost1=landedCost1, shippingCost1=shippingCost1, paymentCost1=paymentCost1, refundCost1=refundCost1, CPA1=CPA1, discount1=discount1, result=result)



