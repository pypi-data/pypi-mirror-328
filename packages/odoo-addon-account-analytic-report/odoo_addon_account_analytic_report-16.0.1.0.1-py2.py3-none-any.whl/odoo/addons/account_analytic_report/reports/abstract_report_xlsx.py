from odoo import models


class AbstractReportXslx(models.AbstractModel):
    _name = "report.account_analytic_report.abstract_report_xlsx"
    _description = "Abstract XLSX Account Analytic Report"
    _inherit = "report.report_xlsx.abstract"

    def get_workbook_options(self):
        vals = super().get_workbook_options()
        vals.update({"constant_memory": True})
        return vals

    def generate_xlsx_report(self, workbook, data, objects):
        report_data = {
            k: None for k in ["workbook", "sheet", "columns", "row_pos", "formats"]
        }
        
        self._define_formats(workbook, report_data)

        report_name = self._get_report_name(objects, data=data)
        report_footer = self._get_report_footer()
        filters = self._get_report_filters(objects)
        report_data["columns"] = self._get_report_columns(objects)
        report_data["workbook"] = workbook
        report_data["sheet"] = workbook.add_worksheet(report_name[:31])
        self._set_column_width(report_data)
        # Fill report
        report_data["row_pos"] = 0
        self._write_report_title(report_name, report_data)
        self._write_filters(filters, report_data)
        self._generate_report_content(workbook, objects, data, report_data)
        self._write_report_footer(report_footer, report_data)

    def _handle_lazy_write_values(self, value):
        """Handle lazy values in data to be written in cells."""
        if hasattr(value, "_value"):
            return value._value
        return value

    def _define_formats(self, workbook, report_data):
        """Add cell formats to current workbook.
        Those formats can be used on all cell.
        Available formats are :
         * format_bold
         * format_right
         * format_right_bold_italic
         * format_header_left
         * format_header_center
         * format_header_right
         * format_header_amount
         * format_amount
         * format_percent_bold_italic
        """
        currency_id = self.env["res.company"]._default_currency_id()
        report_data["formats"] = {
            "format_bold": workbook.add_format({"bold": True}),
            "format_right": workbook.add_format({"align": "right"}),
            "format_left": workbook.add_format({"align": "left"}),
            "format_right_bold_italic": workbook.add_format(
                {"align": "right", "bold": True, "italic": True}
            ),
            "format_header_left": workbook.add_format(
                {"bold": True, "border": True, "bg_color": "#FFFFCC"}
            ),
            "format_header_center": workbook.add_format(
                {"bold": True, "align": "center", "border": True, "bg_color": "#FFFFCC"}
            ),
            "format_header_right": workbook.add_format(
                {"bold": True, "align": "right", "border": True, "bg_color": "#FFFFCC"}
            ),
            "format_header_amount": workbook.add_format(
                {"bold": True, "border": True, "bg_color": "#FFFFCC"}
            ),
            "format_amount": workbook.add_format(),
            "format_amount_bold": workbook.add_format({"bold": True}),
            "format_percent_bold_italic": workbook.add_format(
                {"bold": True, "italic": True}
            ),
        }
        report_data["formats"]["format_amount"].set_num_format(
            "#,##0." + "0" * currency_id.decimal_places
        )
        report_data["formats"]["format_header_amount"].set_num_format(
            "#,##0." + "0" * currency_id.decimal_places
        )
        report_data["formats"]["format_percent_bold_italic"].set_num_format("#,##0.00%")
        report_data["formats"]["format_amount_bold"].set_num_format(
            "#,##0." + "0" * currency_id.decimal_places
        )

    def _set_column_width(self, report_data):
        """Set width for all defined columns.
        Columns are defined with `_get_report_columns` method.
        """
        for position, column in report_data["columns"].items():
            report_data["sheet"].set_column(position, position, column["width"])

    def _write_report_title(self, title, report_data):
        """Write report title on current line using all defined columns width.
        Columns are defined with `_get_report_columns` method.
        """
        report_data["sheet"].merge_range(
            report_data["row_pos"],
            0,
            report_data["row_pos"],
            len(report_data["columns"]) - 1,
            title,
            report_data["formats"]["format_bold"],
        )
        report_data["row_pos"] += 3

    def _write_report_footer(self, footer, report_data):
        """Write report footer .
        Columns are defined with `_get_report_columns` method.
        """
        if footer:
            report_data["row_pos"] += 1
            report_data["sheet"].merge_range(
                report_data["row_pos"],
                0,
                report_data["row_pos"],
                len(report_data["columns"]) - 1,
                footer,
                report_data["formats"]["format_amount_bold"],
            )
            report_data["row_pos"] += 1

    def _write_filters(self, filters, report_data):
        """Write one line per filters on starting on current line.
        Columns number for filter name is defined
        with `_get_col_count_filter_name` method.
        Columns number for filter value is define
        with `_get_col_count_filter_value` method.
        """
        col_name = 1
        col_count_filter_name = self._get_col_count_filter_name()
        col_count_filter_value = self._get_col_count_filter_value()
        col_value = col_name + col_count_filter_name + 1
        for title, value in filters:
            report_data["sheet"].merge_range(
                report_data["row_pos"],
                col_name,
                report_data["row_pos"],
                col_name + col_count_filter_name - 1,
                title,
                report_data["formats"]["format_header_left"],
            )
            report_data["sheet"].merge_range(
                report_data["row_pos"],
                col_value,
                report_data["row_pos"],
                col_value + col_count_filter_value - 1,
                value,
            )
            report_data["row_pos"] += 1
        report_data["row_pos"] += 2

    def write_array_title(self, title, report_data):
        """Write array title on current line using all defined columns width.
        Columns are defined with `_get_report_columns` method.
        """
        report_data["sheet"].merge_range(
            report_data["row_pos"],
            0,
            report_data["row_pos"],
            len(report_data["columns"]) - 1,
            title,
            report_data["formats"]["format_bold"],
        )
        report_data["row_pos"] += 1

    def write_array_header(self, report_data):
        """Write array header on current line using all defined columns name.
        Columns are defined with `_get_report_columns` method.
        """
        for col_pos, column in report_data["columns"].items():
            report_data["sheet"].write(
                report_data["row_pos"],
                col_pos,
                column["header"],
                report_data["formats"]["format_header_center"],
            )
        report_data["row_pos"] += 1

    def write_line_from_dict(self, line_dict, report_data):
        """Write a line on current line"""
        for col_pos, column in report_data["columns"].items():
            value = line_dict.get(column["field"], False)

            cell_type = column.get("type", "string")
            if cell_type == "string":
                report_data["sheet"].write_string(
                    report_data["row_pos"],
                    col_pos,
                    self._handle_lazy_write_values(value) or "",
                    report_data["formats"]["format_amount"],
                )
            elif cell_type == "amount":
                cell_format = report_data["formats"]["format_amount"]
                report_data["sheet"].write_number(
                    report_data["row_pos"], col_pos, float(value), cell_format
                )
            else:
                self.write_non_standard_column(cell_type, col_pos, value)
        report_data["row_pos"] += 1

    def _generate_report_content(self, workbook, report, data, report_data):
        """
        Allow to fetch report content to be displayed.
        """
        raise NotImplementedError()

    def _get_report_complete_name(self, report, prefix, data=None):
        if report.company_id:
            suffix = " - {} - {}".format(
                report.company_id.name, report.company_id.currency_id.name
            )
            return prefix + suffix
        return prefix

    def _get_report_name(self, report, data=False):
        """
        Allow to define the report name.
        Report name will be used as sheet name and as report title.
        :return: the report name
        """
        raise NotImplementedError()

    def _get_report_footer(self):
        """
        Allow to define the report footer.
        :return: the report footer
        """
        return False

    def _get_report_columns(self, report):
        """
        Allow to define the report columns
        which will be used to generate report.
        :return: the report columns as dict
        :Example:
        {
            0: {'header': 'Simple column',
                'field': 'field_name_on_my_object',
                'width': 11},
            1: {'header': 'Amount column',
                 'field': 'field_name_on_my_object',
                 'type': 'amount',
                 'width': 14},
        }
        """
        raise NotImplementedError()

    def _get_report_filters(self, report):
        """
        :return: the report filters as list
        :Example:
        [
            ['first_filter_name', 'first_filter_value'],
            ['second_filter_name', 'second_filter_value']
        ]
        """
        raise NotImplementedError()

    def _get_col_count_filter_name(self):
        """
        :return: the columns number used for filter names.
        """
        raise NotImplementedError()

    def _get_col_count_filter_value(self):
        """
        :return: the columns number used for filter values.
        """
        raise NotImplementedError()

    def _get_col_pos_initial_balance_label(self):
        """
        :return: the columns position used for initial balance label.
        """
        raise NotImplementedError()

    def _get_col_count_final_balance_name(self):
        """
        :return: the columns number used for final balance name.
        """
        raise NotImplementedError()

    def _get_col_pos_final_balance_label(self):
        """
        :return: the columns position used for final balance label.
        """
        raise NotImplementedError()

    def write_non_standard_column(self, cell_type, col_pos, value):
        """
        Write columns out of the columns type defined here.
        """
        raise NotImplementedError()
