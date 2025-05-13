import frappe
from frappe import _
#fungtion to check selling pricing higherthan cost price
def validate_item_prices(doc, method):
    # Roles allowed to bypass the validation
    # allowed_roles = ["Sales Manager", "Accounts Manager"]

    # user_roles = frappe.get_roles(frappe.session.user)
    # if any(role in allowed_roles for role in user_roles):
    #     return

    for item in doc.get("items", []):
        item_master = frappe.get_value("Item", item.item_code, ["valuation_rate", "last_purchase_rate"], as_dict=True)

        valuation_rate = item_master.valuation_rate or 0
        last_purchase_rate = item_master.last_purchase_rate or 0

        #  Block if both rates are zero
        if valuation_rate == 0 and last_purchase_rate == 0:
            frappe.throw(_(
                f"Item <b>{item.item_code}</b>: Both Valuation Rate and Last Purchase Rate are missing or zero. "
                "Cannot proceed without cost reference."
            ))

        #  Compare against the higher of the two
        allowed_rate = max(valuation_rate, last_purchase_rate)

        if item.rate < allowed_rate:
            frappe.throw(_(
                f"Item <b>{item.item_code}</b>: Selling rate ({item.rate}) is less than allowed rate ({allowed_rate}). "
                "It must be ≥ highest of Valuation Rate or Last Purchase Rate."
            ))
