from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.model
    def get_analytic_entries_action(self, domain=None):
        """
        Get the action entries for the account analytic lines.
        """
        action = self.env.ref(
            "analytic.account_analytic_line_action_entries", raise_if_not_found=False
        )
        if not action:
            return False

        action = action.read()[0]
        action["domain"] = [tuple(rule) for rule in eval(domain)] if domain else False
        return action
