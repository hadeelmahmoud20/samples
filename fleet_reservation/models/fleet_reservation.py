

from odoo import models, fields, api ,_ , exceptions
from datetime import datetime
from odoo.exceptions import UserError, ValidationError, AccessError



class FleetReserve(models.Model):
    _name = 'vehicel.reserve'


    name=fields.Many2one('fleet.vehicle',string="Vehicel")

    def vehicel_model_compute(self):
        for item in self:
            item.vehicel_model=str(item.name.model_id.brand_id.name) + '/' + str(item.name.model_id.name)+ '/' + str(item.name.license_plate)

    vehicel_model=fields.Char(compute="vehicel_model_compute")
    datefrom=fields.Datetime(string="From")
    dateto=fields.Datetime(string="To")
    attendances=fields.Many2one(
        'res.users', 'Attendees',default=lambda self: self.env.user,
        readonly=False, required=True)

    duration=fields.Float(compute='_compute_duration')

    @api.depends('dateto', 'datefrom')
    def _compute_duration(self):
        for event in self.with_context(dont_notify=True):
            event.duration = self._get_duration_22(event.datefrom, event.dateto)
    def _get_duration_22(self,datefrom,dateto):
        duration = (dateto - datefrom).total_seconds() / 3600
        return round(duration, 2)




#creation in calendar
    @api.constrains('datefrom', 'dateto', 'name')
    def action_create_vehicel_reservation(self):
        for date in self:
            #start and end date
            datefrom = date.datefrom
            dateto = date.dateto
            if dateto <= datefrom:
                raise ValidationError(_('The ending date cannot be earlier or equal than the starting date.'))

            #overlap dates
            domain = [
                ('id', '!=', date.id),
                ('name', '=', date.name.id),
                '|', '|',
                '&', ('datefrom', '<=', date.datefrom), ('dateto', '>', date.datefrom),
                '&', ('datefrom', '<=', date.dateto), ('dateto', '>=', date.dateto),
                '&', ('datefrom', '<=', date.datefrom), ('dateto', '>=', date.dateto),
            ]
            if self.search_count(domain) > 0:
                raise ValidationError(_('Vehicel already reserved in this date.'))
            for line in self:
                self.env['calendar.event'].create(
                    {
                    'name':line.vehicel_model,
                    'start':line.datefrom,
                    'stop':line.dateto,
                    'duration':line.duration,


                    }
                )





        #
        # if self.dateto < self.datefrom:
        #     raise ValidationError(
        #         _('The ending date and time cannot be earlier than the starting date and time.'))
