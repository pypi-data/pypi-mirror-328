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

ACCOUNT_ANALYTIC_LINE = "account.analytic.line"
ACCOUNT_ANALYTIC_ACCOUNT = "account.analytic.account"
ACCOUNT_ANALYTIC_PLAN = "account.analytic.plan"

ACCOUNT_ANALYTIC_MODELS = [
    ACCOUNT_ANALYTIC_LINE,
    ACCOUNT_ANALYTIC_ACCOUNT,
    ACCOUNT_ANALYTIC_PLAN,
]
