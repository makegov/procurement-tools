import pytest
import requests
from procurement_tools.far import FAR
from procurement_tools.models.far_clause import Clause

SECTION_TEXT = """(a) Written agreement on responsibility for management and administration—.\n(1) Assisted acquisitions .\n(i) Prior to the issuance of a solicitation, the servicing agency and the requesting agency shall both sign a written interagency agreement that establishes the general terms and conditions governing the relationship between the parties, including roles and responsibilities for acquisition planning, contract execution, and administration and management of the contract(s) or order(s). The requesting agency shall provide to the servicing agency any unique terms, conditions, and applicable agency-specific statutes, regulations, directives, and other applicable requirements for incorporation into the order or contract. In the event there are no agency unique requirements beyond the FAR, the requesting agency shall so inform the servicing agency contracting officer in writing. For acquisitions on behalf of the Department of Defense, also see subpart\xa0 17.7 . For patent rights, see 27.304-2 . In preparing interagency agreements to support assisted acquisitions, agencies should review the Office of Federal Procurement Policy (OFPP) guidance, Interagency Acquisitions, available at https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/assets/OMB/procurement/interagency_acq/iac_revised.pdf .\n(ii) Each agency’s file shall include the interagency agreement between the requesting and servicing agency, and shall include sufficient documentation to ensure an adequate audit consistent with 4.801 (b).\n(2) Direct acquisitions . The requesting agency administers the order; therefore, no written agreement with the servicing agency is required.\n(b) Business-case analysis requirements for multi-agency contracts and governmentwide acquisition contracts . In order to establish a multi-agency or governmentwide acquisition contract, a business-case analysis must be prepared by the servicing agency and approved in accordance with the OFPP business case guidance, available at https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/procurement/memo/development-review-and-approval-of-business-cases-for-certain-interagency-and-agency-specific-acquisitions-memo.pdf . The business-case analysis shall—\n(1) Consider strategies for the effective participation of small businesses during acquisition planning (see 7.103 (u));\n(2) Detail the administration of such contract, including an analysis of all direct and indirect costs to the Government of awarding and administering such contract;\n(3) Describe the impact such contract will have on the ability of the Government to leverage its purchasing power, e.g. , will it have a negative effect because it dilutes other existing contracts;\n(4) Include an analysis concluding that there is a need for establishing the multi-agency contract; and\n(5) Document roles and responsibilities in the administration of the contract."""


@pytest.fixture
def clause():
    return Clause(
        number="17.502-1",
        title="17.502-1 General.",
        body=SECTION_TEXT,
    )


def test_clause_url(clause):
    assert clause.url == "https://www.acquisition.gov/far/17.502-1"


class MockGithubResponse(object):
    def __init__(self, status_code: int):
        self.status_code = status_code
        with open("./tests/data/far_17.502-1.html", "r") as fp:
            self.text = fp.read()


class MockSubpartResponse(object):
    def __init__(self, status_code: int):
        self.status_code = status_code
        with open("./tests/data/far_subpart_17_5.html", "r") as fp:
            self.text = fp.read()


def test_get_section(monkeypatch):
    def mock_get(*args, **kwargs):
        if (
            args[0]
            == "https://raw.githubusercontent.com/GSA/GSA-Acquisition-FAR/master/html/copypaste-AllTopic/17.502-1.html"
        ):
            return MockGithubResponse(status_code=200)
        else:
            return MockGithubResponse(status_code=404)

    monkeypatch.setattr(requests, "get", mock_get)

    res = FAR.get_section("17.502-1")
    assert res.title == "17.502-1 General."
    assert res.body == SECTION_TEXT

    # Test that it raises an ValueError if you have a fake section
    with pytest.raises(ValueError) as error:
        FAR.get_section("55.101")

    assert (
        str(error.value) == "Section '55.101' does not appear to be a valid FAR section"
    )


def test_get_subpart(monkeypatch):
    def mock_get(*args, **kwargs):
        if (
            args[0]
            == "https://raw.githubusercontent.com/GSA/GSA-Acquisition-FAR/master/html/copypaste-SubParts/FAR_Subpart_17_5.html"
        ):
            return MockSubpartResponse(status_code=200)
        else:
            return MockSubpartResponse(status_code=404)

    monkeypatch.setattr(requests, "get", mock_get)

    res = FAR.get_subpart("17.5")
    assert res.title == "Subpart 17.5 - Interagency Acquisitions"
    assert res.clauses[0] == Clause(
        number="17.500",
        title="17.500 Scope of subpart.",
        body="17.500 Scope of subpart. (a) This subpart prescribes policies and procedures applicable to all interagency acquisitions under any authority, except as provided for in paragraph (c) of this section. In addition to complying with the interagency acquisition policy and procedures in this subpart, nondefense agencies acquiring supplies and services on behalf of the Department of Defense shall also comply with the policy and procedures at subpart 17.7 . (b) This subpart applies to interagency acquisitions, see 2.101 for definition, when- (1) An agency needing supplies or services obtains them using another agency’s contract; or (2) An agency uses another agency to provide acquisition assistance, such as awarding and administering a contract, a task order, or delivery order. (c) This subpart does not apply to- (1) Interagency reimbursable work performed by Federal employees (other than acquisition assistance), or interagency activities where contracting is incidental to the purpose of the transaction; or (2) Orders of $600,000 or less issued against Federal Supply Schedules.",
    )

    # Test that it raises an ValueError if you have a fake subpart
    with pytest.raises(ValueError) as error:
        FAR.get_subpart("17.100")
    assert (
        str(error.value) == "Subpart '17_100' does not appear to be a valid FAR subpart"
    )
