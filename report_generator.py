def generate_report(target, direct, indirect):
    report = {
        "changed_component": target,
        "direct_impacts": direct,
        "indirect_impacts": indirect,
        "risk_level": "HIGH" if len(direct) > 0 else "LOW"
    }
    return report