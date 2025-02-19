from odoo import _, models


class AnalyticPlanXSLX(models.AbstractModel):
    _name = "report.a_a_r.report_analytic_multilevel_xlsx"
    _description = "Analytic Plan XLSX Report"
    _inherit = "report.account_analytic_report.abstract_report_xlsx"

    def _get_report_name(self, report, data=False):
        report_name = _("Analytic Multilevel Report")

        company_id = data.get("company_id", False)
        if not company_id:
            return report_name

        company = self.env["res.company"].browse(company_id)
        suffix = " - {} - {}".format(company.name, company.currency_id.name)
        report_name = report_name + suffix

        return report_name

    def _get_report_columns(self, report):
        return {
            0: {"header": _("Analytic Plan"), "field": "plan_id", "width": 20},
            1: {"header": _("Analytic Account"), "field": "account_id", "width": 60},
            3: {
                "header": _("Debit"),
                "field": "debit",
                "type": "amount",
                "width": 14,
            },
            4: {
                "header": _("Credit"),
                "field": "credit",
                "type": "amount",
                "width": 14,
            },
            5: {
                "header": _("Balance"),
                "field": "balance",
                "type": "amount",
                "width": 14,
            },
        }

    def _get_report_filters(self, report):
        return [
            [
                _("Date range filter"),
                _("From: %(date_from)s To: %(date_to)s")
                % ({"date_from": report.date_from, "date_to": report.date_to}),
            ],
            [
                _("Analytic account at 0 filter"),
                _("Hide") if report.hide_analytic_account_at_0 else _("Show"),
            ],
        ]

    def _get_col_count_filter_name(self):
        return 2

    def _get_col_count_filter_value(self):
        return 3

    def _generate_report_content(self, workbook, report, data, report_data):
        res_data = self.env[
            "report.account_analytic_report.analytic_multilevel"
        ]._get_xls_report_values(report, data)

        self.write_array_header(report_data)
        for balance in res_data["analytic_balance"]:
            self.write_line_from_dict(balance, report_data)
