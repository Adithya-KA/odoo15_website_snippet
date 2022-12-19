import time

from odoo import http
from odoo.http import request


class Snippet(http.Controller):

    @http.route('/customer/snippet', type='json', auth='public', website=True)
    def cust_snippet(self, partners_per_slide=4):
        partner = request.env['res.partner'].sudo().search([], limit=10, order='sale_count DESC')
        partner_list_1 = []
        partner_list_1.clear()
        if not partner_list_1:
            for rec in partner:
                customer = {
                    'img': rec.image_1920,
                    'name': rec.name,
                    'id': rec.id,
                    'sale_count': rec.sale_count
                }
                partner_list_1.append(customer)
            partners = []
            partners_list = []
            for index, record in enumerate(partner_list_1, 1):
                partners_list.append(record)
                if index % partners_per_slide == 0:
                    partners.append(partners_list)
                    partners_list = []
            if any(partners_list):
                partners.append(partners_list)
            data = {
                "objects": partners,
                "partners_per_slide": partners_per_slide,
                "num_slides": len(partners),
                "uniqueId": "pc-%d" % int(time.time() * 10000),
            }
            res = http.Response(template='website_snippet.snippet_view', qcontext=data)
            return res.render()
