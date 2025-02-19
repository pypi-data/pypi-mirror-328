from odoo import models, fields, api, _


class AnalyticMultilevelReportWizard(models.TransientModel):
    _name = "analytic.multilevel.report.wizard"
    _inherit = "account_analytic_report.abstract_wizard"
    _description = "Account Analytic Multilevel Report Wizard"

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)
    hide_analytic_account_at_0 = fields.Boolean(
        string="Hide Analytic Accounts at 0",
        default=False,
        help="When this option is enabled, the report will "
        "not display analytic accounts that have initial balance = "
        "debit = credit = end balance = 0",
    )
    account_analytic_plan_ids = fields.Many2many(
        comodel_name="account.analytic.plan",
        string="Filter Analytic Plans",
        domain="['|', ('company_id', '=', company_id), ('company_id', '=', False)]",
    )

    @api.onchange("date_from", "date_to")
    def _onchange_date(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            self.date_to = False
            return {
                "warning": {
                    "title": _("Warning"),
                    "message": _("Date To must be greater than Date From."),
                }
            }

    def _print_report(self, report_type):
        self.ensure_one()
        data = self._prepare_report_analytic_multilevel()
        if report_type == "xlsx":
            report_name = "a_a_r.report_analytic_multilevel_xlsx"
        else:
            report_name = "account_analytic_report.analytic_multilevel"
        return (
            self.env["ir.actions.report"]
            .search(
                [("report_name", "=", report_name), ("report_type", "=", report_type)],
                limit=1,
            )
            .report_action(self, data=data)
        )

    def _prepare_report_analytic_multilevel(self):
        self.ensure_one()
        return {
            "wizard_id": self.id,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "company_id": self.company_id.id,
            "account_analytic_report_lang": self.env.lang,
            "hide_analytic_account_at_0": self.hide_analytic_account_at_0,
            "account_analytic_plan_ids": self.account_analytic_plan_ids.ids or [],
        }

    def _export(self, report_type):
        """Default export is PDF."""
        return self._print_report(report_type)
