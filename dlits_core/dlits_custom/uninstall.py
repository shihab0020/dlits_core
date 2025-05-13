# to remove custom fileds created by dlits
import frappe

def cleanup_custom_fields():
    fields = ["custom_manual_rate", "custom_user_set_rate"]
    doctypes = ["Quotation Item", "Sales Order Item", "Sales Invoice Item"]

    for doctype in doctypes:
        for field in fields:
            try:
                frappe.db.delete(
                    "Custom Field",
                    {"dt": doctype, "fieldname": field}
                )
            except Exception as e:
                frappe.log_error(f"Error removing {field} from {doctype}: {e}")
