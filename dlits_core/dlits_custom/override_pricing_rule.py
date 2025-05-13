# import frappe
# from frappe.utils import flt
# import erpnext.accounts.doctype.pricing_rule.pricing_rule as pricing_rule_module
# from dlits_core.dlits_custom.logger import logger

# logger.info("Loading monkey patches for pricing rule")

# # Store the original functions BEFORE patching
# _original_apply_pricing_rule = pricing_rule_module.apply_pricing_rule
# _original_get_pricing_rule_for_item = pricing_rule_module.get_pricing_rule_for_item

# def apply_pricing_rule_patch(args, doc=None):
#     logger.info("apply_pricing_rule_patch called")

#     if not args:
#         return

#     # Skip pricing rule logic if manually edited
#     if getattr(args, "custom_manual_rate", False):
#         logger.info("Manual rate detected — skipping pricing rule")
#         args.pricing_rule = ""
#         args.discount_percentage = 0
#         args.margin_type = ""
#         args.margin_rate_or_amount = 0
#         args.rate = flt(args.rate)  # preserve the manually entered rate
#         return

#     # Call original function
#     return _original_apply_pricing_rule(args, doc)


# def get_pricing_rule_for_item_patch(args, doc=None, for_validate=False, **kwargs):
#     logger.info("get_pricing_rule_for_item_patch called")

#     if not args:
#         return

#     if getattr(args, "custom_manual_rate", False):
#         logger.info("Manual rate detected — skipping pricing rule fetch")
#         return None

#     return _original_get_pricing_rule_for_item(args, doc, for_validate=for_validate, **kwargs)


# def override_pricing_rule():
#     logger.info("Overriding pricing rule functions in ERPNext")
#     pricing_rule_module.apply_pricing_rule = apply_pricing_rule_patch
#     pricing_rule_module.get_pricing_rule_for_item = get_pricing_rule_for_item_patch






############
## Customisation for controlling item sell price override even pricing rule applied. 
## Called using initi py as monky patches. as use js for updating and getting mannual edits.
import frappe
from frappe.utils import flt
import erpnext.accounts.doctype.pricing_rule.pricing_rule as pricing_rule_module
# from dlits_core.dlits_core.logger import logger

# Store original references so we can restore them later
_original_apply_pricing_rule = None
_original_get_pricing_rule_for_item = None
_patch_applied = False

def apply_pricing_rule_patch(args, doc=None):
    if getattr(args, "custom_manual_rate", False):
        args.pricing_rule = ""
        args.discount_percentage = 0
        args.margin_type = ""
        args.margin_rate_or_amount = 0
        args.rate = flt(args.rate)
        return
    return _original_apply_pricing_rule(args, doc)

def get_pricing_rule_for_item_patch(args, doc=None, for_validate=False, **kwargs):
    if not args:
        return
    if getattr(args, "custom_manual_rate", False):
        return None
    return _original_get_pricing_rule_for_item(args, doc, for_validate=for_validate, **kwargs)

def override_pricing_rule():
    """Apply monkey patches to override ERPNext pricing rule logic."""
    global _original_apply_pricing_rule, _original_get_pricing_rule_for_item, _patch_applied

    if _patch_applied:
        # logger.info("Pricing rule patch already applied. Skipping.")
        return

    _original_apply_pricing_rule = pricing_rule_module.apply_pricing_rule
    _original_get_pricing_rule_for_item = pricing_rule_module.get_pricing_rule_for_item

    pricing_rule_module.apply_pricing_rule = apply_pricing_rule_patch
    pricing_rule_module.get_pricing_rule_for_item = get_pricing_rule_for_item_patch

    _patch_applied = True
    # logger.info("Custom pricing rule patch applied successfully.")

def undo_pricing_rule_override():
    """Restore original ERPNext pricing rule logic."""
    global _patch_applied

    if not _patch_applied:
        # logger.info("No patch to undo.")
        return

    pricing_rule_module.apply_pricing_rule = _original_apply_pricing_rule
    pricing_rule_module.get_pricing_rule_for_item = _original_get_pricing_rule_for_item

    _patch_applied = False
    # logger.info("Custom pricing rule patch undone successfully.")







##############

