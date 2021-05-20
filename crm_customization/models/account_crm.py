

from odoo import models, fields, api

class SurveyAccess(models.Model):
    _name = 'sale.survey'



class AccountCRM(models.Model):
    _inherit = 'res.partner.category'

    preferred_products=fields.Many2many('product.product',string='preferred products')

class Accountsale(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _get_domain_product(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.partner_id.category_id.preferred_products:
                vals={
                'product_id':line.id,
                'name':line.name,
                'product_uom':line.uom_id
                }
                lines.append((0,0,vals))
            rec.order_line=lines



    def action_confirm(self):
        ret = super(Accountsale,self).action_confirm()
        self.env['survey.survey'].create(
            {
            'title':self.name,

            }
        )


class Accountsurvat(models.Model):
    _inherit = 'mail.activity'

    def user_survey_222(self):

        users=self.env['res.users'].search([])
        for line in users:
            if line.has_group('crm_customization.group_sale_survey_add'):
                user=line.id
        return user

    @api.onchange('assigneduser')
    def user_compute(self):
        self.user_id=self.assigneduser

    assigneduser = fields.Many2one('res.users', string='user',
    default=lambda item:item.user_survey_222(), readonly=False)
