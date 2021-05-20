

from odoo import models, fields, api
from datetime import datetime




class FleetCustom1(models.Model):
    _name = 'vehicel.part'
    _rec_name='part'
    _order='rank asc'
    part=fields.Char(string="vehicle part")
    name=fields.Char(string="Name")
    rank=fields.Float(string="rank")
    part_id=fields.Many2one('check.form')
    serial=fields.Float()
    name1=fields.Char()
    check_box=fields.Boolean()
    description=fields.Text("Description")

class FleetCustom2(models.Model):
    _name = 'check.form'


    name=fields.Many2one('fleet.vehicle')
    x=fields.Boolean()
    licence=fields.Char(compute="fleet_form_compute")
    chassisnumber=fields.Char(compute="fleet_form_compute")
    vehicel_model=fields.Char(compute="fleet_form_compute",default=" ")
    color=fields.Char(compute="fleet_form_compute")
    driver=fields.Char(compute="fleet_form_compute")




    created_user=fields.Char(default=lambda self: self.env.user.name)
    check_date=fields.Date(default=datetime.today())
    signature=fields.Char()

    serial=fields.Float()
    name1=fields.Char()
    check_box=fields.Boolean()
    description=fields.Text("Description")
    part_grid= fields.One2many('vehicel.part' , 'part_id' ,string="Part grid")

    @api.onchange('name')
    def fleet_form_compute(self):
        # self.ensure_one()
        self.x='True'
        for item in self:
            item.licence=item.name.license_plate
            item.chassisnumber=item.name.vin_sn
            item.vehicel_model=str(item.name.model_id.brand_id.name) + '/' + str(item.name.model_id.name)
            item.color=item.name.color
            item.driver=item.name.driver_id.name





    @api.onchange('x')
    def grid_form(self):
        lines = [(5, 0, 0)]
        for line in self.env['vehicel.part'].search([]):
            if line.name:
                vals={
                'serial':line.rank,
                'name1':line.name,
                'check_box':self.check_box,
                'description':'',
                }
                lines.append((0,0,vals))

        self.part_grid=lines







    def print_report(self):
       data = {
       # 'vehicel_model':str(self.name.model_id.brand_id.name) + '/' + str(self.name.model_id.name),
       'licence':self.name.license_plate,
       'chassisnumber':self.name.vin_sn,
       'driver':self.name.driver_id.name,
       'color':self.name.color,
       'part_grid':self.part_grid,
       'created_user':self.created_user,
       'check_date':self.check_date,
       'signature':self.signature
       }

       return self.env.ref('fleet_customization.report_print_vehicel').report_action(None, data=data)
