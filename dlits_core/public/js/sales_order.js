// for detecting mannual price edit and store edited values
frappe.ui.form.on('Sales Order Item', {
    rate: function(frm, cdt, cdn) {
        let item = locals[cdt][cdn];
        if (item.rate) {
            frappe.model.set_value(cdt, cdn, 'custom_manual_rate', 1);
            frappe.model.set_value(cdt, cdn, 'custom_user_set_rate', item.rate);
        }
    }
});
