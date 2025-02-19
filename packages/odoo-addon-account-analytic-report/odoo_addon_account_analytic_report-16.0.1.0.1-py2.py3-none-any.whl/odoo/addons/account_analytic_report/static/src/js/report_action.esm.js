/** @odoo-module **/
import {ReportAction} from "@web/webclient/actions/reports/report_action";
import {patch} from "web.utils";
import {useEnrichWithActionLinks} from "./report.esm";

const MODULE_NAME = "account_analytic_report";

patch(ReportAction.prototype, "account_analytic_report.ReportAction", {
    setup() {
        this._super.apply(this, arguments);
        this.isAccountAnalyticReport = this.props.report_name.startsWith(
            `${MODULE_NAME}.`
        );
        useEnrichWithActionLinks(this.iframe);
    },

    printView() {
        const printWindow = window.open(this.reportUrl, "_blank");

        const contentDocument = this.iframe.el.contentDocument
            || this.iframe.el.contentWindow.document;
        const script = contentDocument.createElement("script");
        script.innerHTML = `
            window.onload = function() {
                window.print();
                window.onafterprint = function() {
                    window.close();
                }
            };
        `;
        contentDocument.body.appendChild(script);
        contentDocument.body.style.paddingTop = "10px";
        contentDocument.title = `Odoo - ${this.title}`;

        printWindow.document.title = `Odoo - ${this.title}`;
        printWindow.document.write(`${contentDocument.documentElement.outerHTML}`);
        printWindow.document.close();
    },

    export() {
        this.action.doAction({
            type: "ir.actions.report",
            report_type: "xlsx",
            report_name: this._get_xlsx_name(this.props.report_name),
            report_file: this._get_xlsx_name(this.props.report_file),
            data: this.props.data || {},
            context: this.props.context || {},
            display_name: this.title,
        });
    },

    /**
     * @param {String} str
     * @returns {String}
     */
    _get_xlsx_name(str) {
        if (!_.isString(str)) {
            return str;
        }
        const parts = str.split(".");
        return `a_a_r.report_${parts[parts.length - 1]}_xlsx`;
    },
});
