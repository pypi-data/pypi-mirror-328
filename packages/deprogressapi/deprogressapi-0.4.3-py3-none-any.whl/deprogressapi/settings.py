# SPDX-FileCopyrightText: 2020-2024 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences
# SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: Apache-2.0

"""Settings for the DASF progress API."""
from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def is_running_in_notebook():
    """Test if we are running inside a notebook."""


class ShowReportMethod(str, Enum):
    """Methods for reporting."""

    # do not show any report
    none = "NONE"

    # automatically determine what to show
    auto = "AUTO"

    # use pythons built-in print function
    print_ = "PRINT"

    # use python built-in curses module
    curses = "WINDOWED"

    # use ipywidgets (not yet implemented)
    jupyter = "JUPYTER"


class ReportSettings(BaseSettings):
    """Settings for displaying the reports."""

    model_config = SettingsConfigDict(env_prefix="dasf_report_")

    show_method: ShowReportMethod = Field(
        ShowReportMethod.auto,
        description="The method to use for printing the reports.",
    )
    use_curses: bool = Field(
        True,
        description="Whether to use curses or not for displaying reports.",
    )

    @property
    def auto_report_method(self) -> ShowReportMethod:
        """Automatically determine the report method."""
        method = (
            ShowReportMethod.curses
            if self.use_curses
            else ShowReportMethod.print_
        )
        try:
            from IPython import get_ipython
        except (ImportError, ModuleNotFoundError):
            return ShowReportMethod.curses
        try:
            shell = get_ipython().__class__.__name__
            if shell == "ZMQInteractiveShell":
                method = ShowReportMethod.jupyter
        except NameError:
            pass
        return method

    def get_show_method(self) -> ShowReportMethod:
        if self.show_method == ShowReportMethod.auto:
            return self.auto_report_method
        else:
            return self.show_method
