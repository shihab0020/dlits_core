__version__ = "0.0.1"

# #monkey patching to allow item based  price changes
# def override_pricing_rule():
#     import erpnext.accounts.doctype.pricing_rule.pricing_rule as pricing_rule_module
#     from .dlits_custom.override_pricing_rule import (
#         apply_pricing_rule_patch,
#         get_pricing_rule_for_item_patch,
#     )

#     pricing_rule_module.apply_pricing_rule = apply_pricing_rule_patch
#     pricing_rule_module.get_pricing_rule_for_item = get_pricing_rule_for_item_patch

# override_pricing_rule()

from .dlits_custom.override_pricing_rule import override_pricing_rule
override_pricing_rule()
