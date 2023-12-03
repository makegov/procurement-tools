from procurement_tools.periodic_table import PeriodicTable


def test_get_innovations():
    assert len(PeriodicTable.innovations) == 55
