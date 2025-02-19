from odoo import models


CHILD_RELATION_FIELD_MAP = {
    "account.analytic.line": [None],  # lowest level
    "account.analytic.account": ["child_ids", "line_ids"],
    "account.analytic.plan": ["children_ids", "account_ids"],
}

PARENT_RELATION_FIELD_MAP = {
    "account.analytic.line": ["account_id"],
    "account.analytic.account": ["parent_id", "plan_id"],
    "account.analytic.plan": ["parent_id"],
}


class AccountAnalyticMultilevelReport(models.AbstractModel):
    _name = "report.account_analytic_report.analytic_multilevel"
    _description = "Analytic Multilevel Report"
    _inherit = "report.account_analytic_report.abstract_report"

    def _get_analytic_lines_domain(self, data):
        """
        Get the analytic lines domain set by the user in the wizard.
        """
        domain = [
            ("date", ">=", data["date_from"]),
            ("date", "<=", data["date_to"]),
            ("company_id", "=", data["company_id"]),
        ]
        if data["hide_analytic_account_at_0"]:
            domain += [("amount", "!=", 0)]
        if data["account_analytic_plan_ids"]:
            domain += [("plan_id", "in", data["account_analytic_plan_ids"])]
        return domain

    def _get_analytic_models_filtered_ids(self, lines):
        """
        Get all the account and plan ids from the lines to filter the children.
        """
        accounts = self.env["account.analytic.account"]
        plans = self.env["account.analytic.plan"]

        for account in lines.mapped("account_id"):
            accounts |= account
            while account.parent_id:
                accounts |= account.parent_id
                account = account.parent_id

        for plan in lines.mapped("plan_id"):
            plans |= plan
            while plan.parent_id:
                plans |= plan.parent_id
                plan = plan.parent_id
        return {
            lines._name: lines.ids,
            accounts._name: accounts.ids,
            plans._name: plans.ids,
        }

    def _build_item_key(self, record, parent_level=0):
        """
        Build the key for the item.
        """
        parent_id = False
        for field in PARENT_RELATION_FIELD_MAP.get(record._name, []):
            parent_id = getattr(record, field, False)
            if parent_id:
                break

        return {
            "id": record.id,
            "name": record.name,
            "model": record._name,
            "parent_model": parent_id._name if parent_id else False,
            "parent_level": max(0, parent_level),
        }

    def _build_summary_key(self, record, balance=0, debit=0, credit=0):
        """
        Build the key for the summary.
        """
        plan_id, account_id = False, False
        if record._name == "account.analytic.line":
            plan_id = record.plan_id
            account_id = record.account_id
            balance = record.amount
            debit = max(0, record.amount)
            credit = min(0, record.amount)
        elif record._name == "account.analytic.account":
            plan_id = record.plan_id
            account_id = record
        elif record._name == "account.analytic.plan":
            plan_id = record

        return {
            "plan_id": plan_id.name if plan_id else False,
            "account_id": account_id.name if account_id else False,
            "balance": balance,
            "debit": debit,
            "credit": credit,
        }

    def fetch_children_rows(self, record, filters, level=0):
        """
        Fetch children rows recursively.
        """
        line_ids, children, balance, debit, credit, account_count = [], [], 0, 0, 0, 0
        for field in CHILD_RELATION_FIELD_MAP.get(record._name, []):
            if not field:
                item = self._build_item_key(record, level - 1)
                summary = self._build_summary_key(record)
                return {
                    "item": item,
                    "summary": summary,
                    "children": [],
                    "level": level,
                    "account_count": account_count,
                    "line_ids": [record.id],
                }
            child_ids = getattr(record, field, self.env[record._name]).filtered(
                lambda c: c.id in filters.get(c._name, [])
            )
            for child in child_ids:
                child_data = self.fetch_children_rows(child, filters, level + 1)
                if child_data["item"]["model"] != "account.analytic.line":
                    children.append(child_data)
                line_ids += child_data.get("line_ids", [])
                debit += child_data["summary"].get("debit", 0)
                credit += child_data["summary"].get("credit", 0)
                balance += child_data["summary"].get("balance", 0)
                if child_data["item"]["model"] == "account.analytic.account":
                    account_count += child_data.get("account_count", 0) + 1
                elif child_data["item"]["model"] == "account.analytic.plan":
                    account_count += child_data.get("account_count", 0)

        item = self._build_item_key(record, level - 1)
        summary = self._build_summary_key(record, balance, debit, credit)

        return {
            "item": item,
            "summary": summary,
            "children": children,
            "level": level,
            "account_count": account_count,
            "line_ids": line_ids,
        }

    def get_analytic_lines_balance(self, data):
        """
        Get analytic lines data grouped by plan and account.
        """
        line_ids = self.env["account.analytic.line"].search(
            self._get_analytic_lines_domain(data)
        )
        filters = self._get_analytic_models_filtered_ids(line_ids)

        analytic_balance = []
        for plan in line_ids.mapped("account_id.root_plan_id"):
            balance = self.fetch_children_rows(plan, filters, level=0)
            balance["item"]["is_root"] = True

            analytic_balance.append(balance)

        return analytic_balance

    def get_analytic_lines_flat_balance(self, data):
        """
        Get analytic lines data grouped by plan and account.
        """
        line_ids = self.env["account.analytic.line"].search(
            self._get_analytic_lines_domain(data)
        )

        analytic_balance = []
        for line in line_ids:
            plan_id = line.plan_id or line.account_id.plan_id
            if not plan_id:
                continue
            analytic_balance.append(
                {
                    "plan_id": plan_id.complete_name,
                    "account_id": line.account_id.name if line.account_id else False,
                    "balance": line.amount,
                    "debit": max(0, line.amount),
                    "credit": min(0, line.amount),
                }
            )

        return analytic_balance

    def _get_report_base_values(self, docids, data):
        """Get report values."""
        wizard_model = self.env["analytic.multilevel.report.wizard"]
        company_model = self.env["res.company"]

        wizard_id = data["wizard_id"]
        company_id = data["company_id"]
        date_from = data["date_from"]
        date_to = data["date_to"]
        hide_analytic_account_at_0 = data["hide_analytic_account_at_0"]
        account_analytic_plan_ids = data["account_analytic_plan_ids"]

        wizard = wizard_model.browse(wizard_id)
        company = company_model.browse(company_id)

        return {
            "doc_ids": [wizard_id],
            "doc_model": "analytic.plan.report.wizard",
            "docs": wizard,
            "company_name": company.display_name,
            "company_currency": company.currency_id,
            "currency_name": company.currency_id.name,
            "date_from": date_from,
            "date_to": date_to,
            "hide_analytic_account_at_0": hide_analytic_account_at_0,
            "account_analytic_plan_ids": account_analytic_plan_ids,
        }

    def _get_report_values(self, docids, data):
        """Get report values."""
        res = self._get_report_base_values(docids, data)
        analytic_balance = self.get_analytic_lines_balance(data)

        return {**res, "analytic_balance": analytic_balance}

    def _get_xls_report_values(self, docids, data):
        """
        Get the flattened report values.
        """
        res = self._get_report_base_values(docids, data)
        analytic_balance = self.get_analytic_lines_flat_balance(data)

        return {**res, "analytic_balance": analytic_balance}
