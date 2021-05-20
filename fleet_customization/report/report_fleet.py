

from odoo import models, fields, api
from datetime import datetime


class Reportfleet(models.AbstractModel):
    _name = 'report.fleet_customization.report_vehicel_form'
    def _get_report_values(self, docids, data=None):
        docs = self.env['check.form'].browse(docids)
        return {
              'doc_ids': docids,
              'doc_model':'check.form',
              'docs': docs,
              'data': data,
              'get_something': self.get_something,
        }
    def get_something(self):
        return 5
