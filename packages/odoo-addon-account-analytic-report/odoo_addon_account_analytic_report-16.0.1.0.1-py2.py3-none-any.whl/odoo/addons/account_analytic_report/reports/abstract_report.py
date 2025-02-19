from odoo import api, models


class AbstractReport(models.AbstractModel):
    _name = "report.account_analytic_report.abstract_report"
    _description = "Abstract Report"
