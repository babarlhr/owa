var odoo;
var $;
var owa_control_panel;
odoo.define('owa.client', function (require) {
    var web_UserMenu = require("web.UserMenu");
    web_UserMenu.include({
        _onMenuOwaPannel: function () {
            owa_control_panel.show_owa_pannel();
        }
    });
});
