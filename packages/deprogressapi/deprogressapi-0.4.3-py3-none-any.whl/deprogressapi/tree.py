# SPDX-FileCopyrightText: 2020-2024 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences
# SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: Apache-2.0

"""Tree-like progress report for the DASF progress API."""
from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field

from deprogressapi.base import BaseReport

try:
    from typing import Literal  # type: ignore
except ImportError:
    from typing_extensions import Literal  # type: ignore


class BaseProgressReport(BaseReport):
    """A tree-like structured progress report."""

    step_message: str = Field(description="The description of the process.")
    steps: int = Field(
        default=0, description="The number of subprocesses in this report."
    )
    children: List[BaseProgressReport] = Field(default_factory=list)

    _parent: Optional[BaseProgressReport] = None

    def submit(self):
        # reimplemented to use the parents submit method if there is a parent.
        if self._parent is not None:
            self._parent.submit()
        else:
            super().submit()

    submit.__doc__ = BaseReport.submit.__doc__

    def create_subreport(self, *args, **kwargs):
        """Create a child subreport.

        This method creates a new subreport and registers it as a child.
        Parameters are the same as for the :class:`ProgressReport`.

        Parameters
        ----------
        submit: Optional[bool]
            Keyword-only argument. If True (default False), submit the child
            report.
        ``*args, **kwargs``
            The same as for the :class:`ProgressReport`

        Returns
        -------
        ProgressReport
            The child report that has been created.
        """
        submit = kwargs.pop("submit", False)
        child = ProgressReport(*args, **kwargs)
        child._parent = self
        self.children.append(child)
        if submit:
            self.submit()
        return child

    @classmethod
    def get_dummy_arguments(cls) -> Dict:
        # reimplemented to add a step_message
        ret = super().get_dummy_arguments()
        ret["step_message"] = ""
        return ret

    get_dummy_arguments.__doc__ = BaseReport.__doc__


BaseProgressReport.model_rebuild()


class ProgressReport(BaseProgressReport):
    report_type: Literal["tree"] = Field(  # type: ignore
        "tree", description="Selector for the report type."
    )

    children: List[ProgressReport] = Field(default_factory=list)  # type: ignore[assignment]


ProgressReport.model_rebuild()
