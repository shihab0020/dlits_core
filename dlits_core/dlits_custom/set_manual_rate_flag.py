# store user changed price value to solve isshue in override mannual change of pricing rule.
def set_manual_rate_flag(doc, method):
    for item in doc.items:
        # If user changed rate, and it's different from saved rate, mark it
        if item.rate and (
            not item.custom_user_set_rate or float(item.rate) != float(item.custom_user_set_rate)
        ):
            item.custom_manual_rate = 1
            item.custom_user_set_rate = item.rate