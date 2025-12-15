# Copyright (c) 2025, Avinash and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


# enrolment.py

import frappe
from frappe.model.document import Document

class Enrolment(Document):
    def validate(self):
        # Example validation logic
        if not self.student_id:
            frappe.throw("Student id is required.")
        # Add more validation as needed
