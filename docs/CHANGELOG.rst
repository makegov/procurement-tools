CHANGELOG
=========

0.1.6
-----

New
~~~
- Access to the SBIR API with two methods (:code:`SBIR.get_awards` and :code:`SBIR.get_solicitations`), that allow for downloading SBIR awards and solicitations, respectively
- Added new pydantic models related to SBIR

0.1.5
-----

New
~~~
- A basic CLI.
- A new USASpending method (:code:`USASpending.get_recipient_profile`), that gets a recipient profile from the USASpending.gov API
- A new USASpending method (:code:`USASpending.get_latest_recipient_awards`), that gets the most recent 10 awards within the last 90 days from the USASpending.gov API
