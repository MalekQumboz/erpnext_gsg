# Copyright (c) 2023, Malek Qumboz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours, get_first_day, get_last_day, today

class EmployeeExcuseapplication(Document):
	def validate(self):
		self.hours = time_diff_in_hours(self.to_time, self.from_time)
		excuse_alowed = frappe.db.sql(f""" select excuse_hours_alowed as eha from `tabDepartment` where name = '{self.department}' """, as_dict=1)[0]['eha']
		total_submited_applications = frappe.db.sql(f""" select hours from `tabEmployee Excuse application` where employee = '{self.employee}' and excuse_date between '{get_first_day(today())}' and '{get_last_day(today())}' """, as_dict=1)
		total = 0.0
		for sub in total_submited_applications:
			total += sub['hours']
		if self.hours > excuse_alowed - total:
			frappe.throw('Excuse Hours Limit Reached')
		if self.from_time > self.to_time:
			frappe.throw(' From Time Cannot be To Time')
