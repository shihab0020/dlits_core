import frappe
from frappe import _

# #fungtion to auto fill valuation rate by py

def fill_valuation_rate_if_missing(doc, method):
    for item in doc.get("items", []):
        # Only proceed if valuation_rate is missing or zero
        if not item.get("valuation_rate") or item.get("valuation_rate") == 0:
            # Try getting from Stock Ledger
            stock_valuation = get_valuation_rate_from_stock_ledger(item.item_code, item.warehouse)

            # Fallback to Item Master if no stock valuation
            item_master_valuation = get_valuation_rate_from_item_master(item.item_code)

            # Use the higher of the two values
            valuation = max(stock_valuation, item_master_valuation)

            if valuation > 0:
                item.valuation_rate = valuation  # Set the valuation rate (not overriding manual entries)
                # frappe.db.commit()
              


def get_valuation_rate_from_stock_ledger(item_code, warehouse=None):
    conditions = "AND warehouse = %(warehouse)s" if warehouse else ""
    params = {"item_code": item_code}
    if warehouse:
        params["warehouse"] = warehouse

    result = frappe.db.sql("""
        SELECT valuation_rate FROM `tabStock Ledger Entry`
        WHERE item_code = %(item_code)s
        {conditions}
        AND valuation_rate > 0
        ORDER BY posting_date DESC, posting_time DESC
        LIMIT 1
    """.format(conditions=conditions), params, as_dict=True)

    return result[0].valuation_rate if result else 0


def get_valuation_rate_from_item_master(item_code):
    item = frappe.get_value("Item", item_code, ["valuation_rate", "last_purchase_rate"], as_dict=True)
    if not item:
        return 0
    # Use valuation_rate if available, else last_purchase_rate
    return item.valuation_rate or item.last_purchase_rate or 0

#fungtion to fill valuation rate using Js
@frappe.whitelist() 
def get_valuation_rate_for_item(item_code, warehouse=None):
    """Called from custom button or hook on item add."""
    stock_valuation = get_valuation_rate_from_stock_ledger(item_code, warehouse)
    item_master_valuation = get_valuation_rate_from_item_master(item_code)
    return max(stock_valuation, item_master_valuation)




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
