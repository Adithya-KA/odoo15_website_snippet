odoo.define("website_snippet.dynamic_snippet", function (require) {
  "use strict";
  console.log("start");
  var publicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  console.log("running");
  var Dynamic = publicWidget.Widget.extend({
    selector: ".top_snippet_view",
//      console.log("ENTER")
      start: function () {
           var self = this;
           rpc.query({
               route: '/customer/snippet',
               params: {},
           }).then(function (result) {
          self.$target.empty().append(result);
           });
       },
   });

  publicWidget.registry.top_customer_snippet = Dynamic;
//  console.log("end");
  return Dynamic;
});
