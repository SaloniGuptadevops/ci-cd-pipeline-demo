def parse_log(log_content: str) -> dict:
    """
    Parse log content and count occurrences of each log level.
    Returns a dictionary with counts for ERROR, WARNING, and INFO.
    """
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    for line in log_content.splitlines():
        line_upper = line.upper()
        if "ERROR" in line_upper or "CRITICAL" in line_upper:
            counts["ERROR"] += 1
        elif "WARNING" in line_upper or "WARN" in line_upper:
            counts["WARNING"] += 1
        elif "INFO" in line_upper:
            counts["INFO"] += 1

    return counts


def get_health_status(counts: dict) -> str:
    """
    Return system health status based on error counts.
    """
    if counts["ERROR"] >= 5:
        return "CRITICAL"
    elif counts["ERROR"] >= 1:
        return "DEGRADED"
    elif counts["WARNING"] >= 3:
        return "WARNING"
    else:
        return "HEALTHY"


def format_report(counts: dict) -> str:
    """
    Format the parsed log counts into a readable report.
    """
    status = get_health_status(counts)
    report = [
        "=" * 40,
        "  LOG ANALYSIS REPORT",
        "=" * 40,
        f"  ERROR   : {counts['ERROR']}",
        f"  WARNING : {counts['WARNING']}",
        f"  INFO    : {counts['INFO']}",
        "-" * 40,
        f"  STATUS  : {status}",
        "=" * 40,
    ]
    return "\n".join(report)


if __name__ == "__main__":
    sample_log = """
2024-01-15 09:23:11 INFO  Application started
2024-01-15 09:23:14 INFO  Connected to database
2024-01-15 09:45:02 WARNING High memory usage: 87%
2024-01-15 09:45:45 ERROR Connection pool exhausted
2024-01-15 09:45:47 CRITICAL Health check failed
"""
    counts = parse_log(sample_log)
    print(format_report(counts))

    