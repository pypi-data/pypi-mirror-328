# (generated with --quick)

import datetime
from typing import Any, Optional

_lazy_re_compile: Any
date_re: Any
datetime_re: Any
get_fixed_timezone: Any
iso8601_duration_re: Any
postgres_interval_re: Any
standard_duration_re: Any
time_re: Any

def parse_date(value) -> Optional[datetime.date]: ...
def parse_datetime(value) -> Optional[datetime.datetime]: ...
def parse_duration(value) -> None: ...
def parse_time(value) -> Optional[datetime.time]: ...
