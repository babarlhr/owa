let odoo:any;
let $:any;
let owa_control_panel:any;
odoo.define('owa.client', function (require) {
    let web_UserMenu = require("web.UserMenu");
    web_UserMenu.include({
        _onMenuOwaPannel: function () {
            owa_control_panel.show_owa_pannel();
        },
    })
});