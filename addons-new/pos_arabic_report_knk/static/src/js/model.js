odoo.define('pos_arabic_report_knk.model', function(require) {
    "use strict";

    var models = require("point_of_sale.models");
    var rpc = require('web.rpc');
    var core = require('web.core');
    var _t = core._t;

    models.load_fields("res.company", [
        "arabic_name",
        "company_footer",
        "company_heading_1",
        "company_heading_2",
        "company_heading_3",
        "company_heading_4"
    ]);
    
    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        export_for_printing: function() {
            var qrcode_order_ref = '';

            var orders = _super_order.export_for_printing.apply(this, arguments);
            orders.company.arabic_name = this.pos.company.arabic_name;
            orders.company.currency_id = this.pos.company.currency_id;
	    var currentDate = new Date();
            var formattedDate = currentDate.toLocaleString('en-US', { timeZone: 'Africa/Cairo' }); // Adjust timezone as needed
	    orders.datee = formattedDate;
            // console.log(JSON.stringify(orders.name));

// Function to make an HTTP request to retrieve ETA UUIDs
           // Assuming you're using jQuery for simplicity
          
                // Define the order reference
                var orderReference = orders.name;


                
            // Make an AJAX request to the server
                $.ajax({
                    type: "GET",
                    async: false,
                    url: "/get_eta_uuid", // The URL to the Python route
                    data: { order_reference: orderReference }, // Send the order reference as a parameter
                    success: function(response) {
                        qrcode_order_ref = String(response)
                        console.log(response)
                        var cleanQrcodeOrderRef = qrcode_order_ref.replace(/["\[\]]/g, '');
                        console.log("final",cleanQrcodeOrderRef);
                        localStorage.setItem('eta_uuid', "");
                        localStorage.setItem('eta_uuid', cleanQrcodeOrderRef);
                        
                    },
                    error: function(xhr, status, error) {
                        console.error("Error:", error);
                    }
                });
        

            const codeWriter = new window.ZXing.BrowserQRCodeSvgWriter()
            let qr_values = "http://invoicing.eta.gov.eg/receipts/search/" + localStorage.getItem('eta_uuid') + "/share/" + (orders.date.isostring.split('T')[0])  + "Total:" + (orders.total_paid)  + "IssuerRIN:"+ (orders.company.vat);

            console.log(qr_values + 111111);
            
            
                        let qr_code_svg = new XMLSerializer().serializeToString(codeWriter.write(qr_values, 150, 150));
            orders.qrcode_img = "data:image/svg+xml;base64," + window.btoa(qr_code_svg);

            // Barcode
            var canvas = document.createElement('canvas');
            JsBarcode(canvas, orders['name']);
            orders['barcode'] = canvas.toDataURL("image/png");

            return orders;
        },
        

    });

    models.load_fields("pos.payment.method", ["arabic_translate"]);

    var _super_paymentline = models.Paymentline.prototype;
    models.Paymentline = models.Paymentline.extend({
        initialize: function(attributes, options) {
            _super_paymentline.initialize.apply(this, arguments);
            this.arabic_translate = this.payment_method.arabic_translate;
        },
        export_for_printing: function() {
            var paymentline = _super_paymentline.export_for_printing.apply(this, arguments);
            paymentline['arabic_translate'] = this.arabic_translate;

            return paymentline;
        },
    });
});
