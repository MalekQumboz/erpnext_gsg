frappe.ui.form.on("Payment Entry", {
	setup: function(frm) {
//        frm.set_df_property("naming_series", "options", [ "GSG-JV-.YYYY.-"])
        frm.set_df_property("naming_series", "options", [ "GSG-JV-.YYYY.-","ACC-PAY-.YYYY.-"])
    }
})