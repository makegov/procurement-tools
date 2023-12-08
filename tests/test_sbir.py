from procurement_tools import SBIR


def test_sbir_get_solicitations(sbir_solicitations_api_results):
    res = SBIR.get_solicitations()
    assert len(res.results) == 41
    assert res.results[10].solicitation_title == (
        "Investigational New Drug (IND)-enabling and Early-Stage Development of "
        "Medications to Treat Alcohol Use disorder and Alcohol-Associated Organ Damage "
        "(U43/U44 Clinical Trial Optional)"
    )


def test_sbir_get_solicitations_keyword(sbir_solicitations_api_results):
    res = SBIR.get_solicitations(keyword="water")
    assert len(res.results) == 10
    assert (
        res.results[9].solicitation_title
        == "NOAA FY 2024 Small Business Innovation Research Phase I NOFO"
    )


def test_sbir_get_solicitations_keyword(sbir_solicitations_api_results):
    res = SBIR.get_solicitations(keyword="water", agency="Department of Commerce")
    assert len(res.results) == 1
    assert (
        res.results[0].solicitation_title
        == "NOAA FY 2024 Small Business Innovation Research Phase I NOFO"
    )


def test_sbir_get_awards(sbir_awards_api_results):
    res = SBIR.get_awards()
    assert len(res.results) == 200
    assert (
        res.results[0].award_title
        == "SBIR Phase I:An inclusive machine learning-based digital platform to credential soft skills"
    )
    assert res.results[0].firm == "LIVEDX INC."
    assert res.results[100].firm == "L-Infinity Labs, Inc."
