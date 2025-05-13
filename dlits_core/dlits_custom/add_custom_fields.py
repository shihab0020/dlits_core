from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Quotation Item": [
            {
                "fieldname": "custom_manual_rate",
                "label": "Manual Rate",
                "fieldtype": "Check",
                "insert_after": "item_name",
                "default": "0"
            },
            {
                "fieldname": "custom_user_set_rate",
                "label": "User Set Rate",
                "fieldtype": "Currency",
                "insert_after": "custom_manual_rate"
            }
        ],
        "Sales Order Item": [
            {
                "fieldname": "custom_manual_rate",
                "label": "Manual Rate",
                "fieldtype": "Check",
                "insert_after": "item_name",
                "default": "0"
            },
            {
                "fieldname": "custom_user_set_rate",
                "label": "User Set Rate",
                "fieldtype": "Currency",
                "insert_after": "custom_manual_rate"
            }
        ],
        "Sales Invoice Item": [
            {
                "fieldname": "custom_manual_rate",
                "label": "Manual Rate",
                "fieldtype": "Check",
                "insert_after": "item_name",
                "default": "0"
            },
            {
                "fieldname": "custom_user_set_rate",
                "label": "User Set Rate",
                "fieldtype": "Currency",
                "insert_after": "custom_manual_rate"
            }
        ]
    }

    create_custom_fields(custom_fields, update=True)
