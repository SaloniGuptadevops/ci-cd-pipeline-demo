from log_parser import parse_log, get_health_status, format_report


def test_parse_log_counts_errors():
    log = "ERROR something went wrong\nERROR another error"
    result = parse_log(log)
    assert result["ERROR"] == 2


def test_parse_log_counts_warnings():
    log = "WARNING high memory\nWARN disk space low"
    result = parse_log(log)
    assert result["WARNING"] == 2


def test_parse_log_counts_info():
    log = "INFO app started\nINFO connected"
    result = parse_log(log)
    assert result["INFO"] == 2


def test_parse_log_empty():
    result = parse_log("")
    assert result == {"ERROR": 0, "WARNING": 0, "INFO": 0}


def test_health_status_critical():
    counts = {"ERROR": 5, "WARNING": 0, "INFO": 0}
    assert get_health_status(counts) == "CRITICAL"


def test_health_status_degraded():
    counts = {"ERROR": 1, "WARNING": 0, "INFO": 0}
    assert get_health_status(counts) == "DEGRADED"


def test_health_status_warning():
    counts = {"ERROR": 0, "WARNING": 3, "INFO": 0}
    assert get_health_status(counts) == "WARNING"


def test_health_status_healthy():
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 5}
    assert get_health_status(counts) == "HEALTHY"


def test_format_report_contains_status():
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 3}
    report = format_report(counts)
    assert "HEALTHY" in report
    assert "ERROR" in report