# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _ , api
import datetime
from datetime import timedelta, date

class Procurmentt(models.Model):
    _name = 'code.code'
    name = fields.Char(string="Name")



class Procurmenttwizard(models.TransientModel):
    _name = 'procurment.print'
    project_no = fields.Char(string="Project Number")
    product = fields.Many2one("product.product", string="Product Name")
    submittal_type= fields.Selection(string="Dc Type", selection=[('dc', 'Document Control'), ('mt', 'Material'),('dw','Drawing') ], required=False )
    scope_of_work_id = fields.Many2one("work.scope", string="Scope Of Work", required=False)
    division = fields.Many2one("division.scope", string="Division", required=False)
    job_type_id =  fields.Many2one("job.type", string="Job Type", required=False)
    action_code = fields.Selection(string="Action Code", required=False,selection=[('a', 'A'), ('b', 'B'),('c','C'),('d','D') ,('e','E') ,('P','P')])

    def print_dc_xls(self):

        return self.env.ref('procurment_report.dc_xlsx_procurment').report_action(self)

class ProcurmentReportXls(models.AbstractModel):
    _name = 'report.procurment_report.dc_xlsx_procurment'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):


        worksheet = workbook.add_worksheet("Procurment List Report")
        f1 = workbook.add_format({'bold': True, 'font_color': '#000000', 'border': True, 'align': 'vcenter'})
        f2 = workbook.add_format({'bold': True, 'font_color': '#000000', 'border': False, 'align': 'vcenter'})

        cell_text_format = workbook.add_format({'align': 'center',
                                                'bold': True,
                                                'size': 12, })
        cell_text_format_values = workbook.add_format({'align': 'center',
                                                'bold': False,
                                                'size': 10, })

        worksheet.set_column('A:A', 1)
        worksheet.set_column('B:B', 23)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('D:D', 10)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:F', 18)
        worksheet.set_column('G:G', 15)
        worksheet.set_column('H:H', 18)
        worksheet.set_column('I:I', 20)
        worksheet.set_column('J:J', 20)
        worksheet.set_column('K:K', 15)
        worksheet.set_column('L:L', 15)

        row = 0
        col = 0


        worksheet.write(row + 5, col + 1, 'Project ID', cell_text_format)
        worksheet.write(row + 5, col + 2, 'Product', cell_text_format)
        worksheet.write(row + 5, col + 3, 'DC Type', cell_text_format)
        worksheet.write(row + 5, col + 4, 'Scope Of Work', cell_text_format)
        worksheet.write(row + 5, col + 5, 'Division', cell_text_format)
        worksheet.write(row + 5, col + 6, 'Job Type', cell_text_format)
        worksheet.write(row + 5, col + 7, 'Action Code', cell_text_format)

        row = 6
        seq = 0
        domain = []
        if lines.project_no:
            domain.append(('project_no', '=', lines.project_no))
        if lines.product:
            domain.append(('product', '=',lines.product.id))
        if lines.submittal_type:
            domain.append(('submittal_type', '=', lines.submittal_type))
        if lines.scope_of_work_id:
            domain.append(('scope_of_work_id', '=', lines.scope_of_work_id.id))
        if lines.division:
            domain.append(('division', '=',lines.division))
        if lines.job_type_id:
            domain.append(('job_type_id', '=', lines.job_type_id))
        if lines.action_code:
            domain.append(('action_code', '=', lines.action_code))
        if lines.product or lines.project_no or lines.submittal_type or lines.scope_of_work_id or lines.division or lines.job_type_id or lines.action_code  :
            row += 1
            seq += 1
            worksheet.write(row, col + 1, str(lines.project_no or ' '), cell_text_format_values)
            worksheet.write(row, col + 2, str(lines.product.name or ' '), cell_text_format_values)
            worksheet.write(row, col + 3, str(lines.submittal_type or ' '), cell_text_format_values)
            worksheet.write(row, col + 4, str(lines.scope_of_work_id.name or ' '), cell_text_format_values)
            worksheet.write(row, col + 5, str(lines.division.name or ' '), cell_text_format_values)
            worksheet.write(row, col + 6, str(lines.job_type_id.name or ' '), cell_text_format_values)
            worksheet.write(row, col + 7, str(lines.action_code or ' '), cell_text_format_values)
        else:
           no = self.env['procurment.list'].search(domain)
           submittal_items = self.env['procurment.list.lines'].search(domain)

           for sub_no in no:
               for sub_item in sub_no.procurment_lines:
                   row += 1
                   seq += 1
                   worksheet.write(row, col + 1, str(sub_no.project_no or ' '), cell_text_format_values)
                   worksheet.write(row, col + 2, str(sub_item.product.name or ' '), cell_text_format_values)
                   worksheet.write(row, col + 3, str(sub_item.submittal_type or ' '), cell_text_format_values)
                   worksheet.write(row, col + 4, str(sub_item.scope_of_work_id.name or ' '), cell_text_format_values)
                   worksheet.write(row, col + 5, str(sub_item.division.name or ' '), cell_text_format_values)
                   worksheet.write(row, col + 6, str(sub_item.job_type_id.name or ' '), cell_text_format_values)
                   worksheet.write(row, col + 7, str(sub_item.action_code or ' '), cell_text_format_values)
