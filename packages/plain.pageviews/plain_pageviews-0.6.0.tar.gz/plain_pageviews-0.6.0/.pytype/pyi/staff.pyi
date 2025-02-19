# (generated with --quick)

from typing import Any

Card: Any
DailyTrendCard: Any
Pageview: Any
PageviewStaff: Any
StaffModelDetailView: Any
StaffModelListView: Any
StaffModelViewset: Any
register_viewset: Any

class DailyPageviewsCard(Any):
    datetime_field: str
    model: Any
    size: Any
    title: str

class UserPageviewsCard(Any):
    template_name: str
    title: str
    def get_template_context(self) -> Any: ...
