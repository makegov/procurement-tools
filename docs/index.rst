procurement-tools
=================

A handy collection of python utilities and tools to navigate federal contracting.

Installation
------------

.. code-block:: sh

   pip install procurement-tools

Example Usage
-------------
.. code-block:: python

   from procurement_tools import FAR, UEI, USASpending
   print(UEI.is_valid("J7M9HPTGJ1S9"))
   # True

   print(USASpending.get_usaspending_URL("J7M9HPTGJ1S9"))
   # 'https://www.usaspending.gov/recipient/bf1220c1-2373-042a-e8e1-33d5a29639d0-P/latest'

   print(FAR.get_section("17.502-2"))
   # Returns a pydantic model with the title, section number, url, and text of the section

   from procurement_tools import get_entity
   res = get_entity({"ueiSAM":"XRVFU3YRA2U5"})
   print(res)
   # Returns a pydantic model with the latest SAM data for a given Entity

It also comes with a CLI (though the *design* of CLI is still very much conceptual). Right now you can, e.g., run the following command:

.. code-block:: sh

   fargo sam XRVFU3YRA2U5
   # Get an entity's details dumped into a JSON object

Contents
--------

.. toctree::
   :maxdepth: 1

   roadmap
   api
   cli
   entity
