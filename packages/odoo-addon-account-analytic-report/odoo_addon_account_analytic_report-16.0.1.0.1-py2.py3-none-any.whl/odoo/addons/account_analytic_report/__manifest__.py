# Author: Som It Cooperatiu SCCL
# Copyright 2024-SomItCoop SCCL(<https://gitlab.com/somitcoop>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Analytic Reports",
    "version": "16.0.1.0.1",
    "category": "Reporting",
    "summary": "Account Analytic Multilevel Reports",
    "author": "Som It Cooperatiu SCCL",
    'website': 'https://somit.coop',
    "depends": [
        "account",
        "web",
        "report_xlsx",
        "account_analytic_parent"
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "wizards/analytic_multilevel_report_wizard_views.xml",
        "views/menuitems.xml",
        "views/reports.xml",
        "reports/templates/layouts.xml",
        "reports/templates/analytic_multilevel.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "account_analytic_report/static/src/js/*",
            "account_analytic_report/static/src/xml/**/*",
            "account_analytic_report/static/src/css/main.css",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "AGPL-3",
}
