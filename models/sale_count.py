from odoo import fields, models, api


class SaleOrderCount(models.Model):
    _inherit = 'res.partner'

    sale_count = fields.Integer(compute='_compute_sale_count', string='Sale Order Count', store=True)

    def _compute_sale_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        sale_order_groups = self.env['sale.order'].read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in sale_order_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.sale_count += group['partner_id_count']
                    partners |= partner
                partner = partner.parent_id
        (self - partners).sale_count = 0
