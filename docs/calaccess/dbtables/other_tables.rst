.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the other_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Other tables
================================


The CAL-ACCESS database contains 23 tables not categorized
anywhere in the `official documentation <calaccess/officialdocumentation.html>`_ as
being specific to campaign finance filings, specific to lobbyist disclosure or common
to both domains.



------------

*********************
ACRONYMS_CD
*********************

Contains acronyms and their meaning.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>ACRONYM</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>ACRONYM</code></td>
            <td>String (up to 40)</td>
            <td>Yes</td>
            <td>Acronym text value</td>
        </tr>
    
    
    
        <tr>
            <td><code>STANDS_FOR</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Definition of the acronym</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for the acronym</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_DESC</code></td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Description of the acronym</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
ADDRESS_CD
*********************

This table holds all addresses for the system. This table can be used
for address-based searches and formes the bases for address information
desplayed by the AMS.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ADDRESS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>ADRID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>ADRID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address indentification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CITY</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>ST</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address state</td>
        </tr>
    
    
    
        <tr>
            <td><code>ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMAIL</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address email</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
BALLOT_MEASURES_CD
*********************

Ballot measure dates and times


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/BALLOT_MEASURES_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>ELECTION_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ballot measure election date</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEASURE_NO</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEASURE_NAME</code></td>
            <td>String (up to 163)</td>
            <td>No</td>
            <td>Ballot measure full name</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEASURE_SHORT_NAME</code></td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Ballot measure short name</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURISDICTION</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
EFS_FILING_LOG_CD
*********************

Electronic Filing Subsystem Log. The EFS accepts and validates electronic filings.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EFS_FILING_LOG_CD.TSV?footer=no&slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-400">Form 400</a>:
                Statement of Organization (Slate Mailer Organization)
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-402">Form 402</a>:
                Statement of Termination (Slate Mailer Organization)
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-410">Form 410</a>:
                Statement of Organization Recipient Committee
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-425">Form 425</a>:
                Semi-Annual Statement of no Activity
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-461">Form 461</a>:
                Independent Expenditure Committee & Major Donor Committee Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-496">Form 496</a>:
                Late Independent Expenditure Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-497">Form 497</a>:
                Late Contribution Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-498">Form 498</a>:
                Slate Mailer Late Payment Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-601">Form 601</a>:
                Lobbying Firm Registration Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-602">Form 602</a>:
                Lobbying Firm Activity Authorization
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-603">Form 603</a>:
                Lobbyist Employer or Lobbying Coalition Registration Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-604">Form 604</a>:
                Lobbyist Certification Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-606">Form 606</a>:
                Notice of Termination
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-607">Form 607</a>:
                Notice of Withdrawal
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-615">Form 615</a>:
                Lobbyist Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-635">Form 635</a>:
                Report of Lobbyist Employer or Report of Lobbying Coalition
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-645">Form 645</a>:
                Report of Person Spending $5,000 or More
            </td>
        </tr>
        
        
    </tbody>
    </table>



Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_DATE</code></td>
        
            <td><code>VENDOR</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILING_DATE</code></td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Date of filing</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILINGSTATUS</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Status of filing. This field is described in the docs as beingVARCHAR. However, its distinct values are 0, 1, 2 and 7.</td>
        </tr>
    
    
    
        <tr>
            <td><code>VENDOR</code></td>
            <td>String (up to 250)</td>
            <td>Yes</td>
            <td>Software vendor who submitted the electronic filing</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>ERROR_NO</code></td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Most records have a value of &quot;ACCEPTED&quot;. Other records include &quot;ERROR&quot;or &quot;BADFORMAT&quot; and a three-digit number.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``form_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>F400</code></td>
                <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F401</code></td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F402</code></td>
                <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>F425</code></td>
                <td>Form 425: Semi-Annual Statement of no Activity</td>
            </tr>
        
            <tr>
                <td><code>F450</code></td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td><code>F460</code></td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F461</code></td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F465</code></td>
                <td>Form 465: Supplemental Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>F496</code></td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>F497</code></td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td><code>F498</code></td>
                <td>Form 498: Slate Mailer Late Payment Report</td>
            </tr>
        
            <tr>
                <td><code>F601</code></td>
                <td>Form 601: Lobbying Firm Registration Statement</td>
            </tr>
        
            <tr>
                <td><code>F602</code></td>
                <td>Form 602: Lobbying Firm Activity Authorization</td>
            </tr>
        
            <tr>
                <td><code>F603</code></td>
                <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
            </tr>
        
            <tr>
                <td><code>F604</code></td>
                <td>Form 604: Lobbyist Certification Statement</td>
            </tr>
        
            <tr>
                <td><code>F606</code></td>
                <td>Form 606: Notice of Termination</td>
            </tr>
        
            <tr>
                <td><code>F607</code></td>
                <td>Form 607: Notice of Withdrawal</td>
            </tr>
        
            <tr>
                <td><code>F615</code></td>
                <td>Form 615: Lobbyist Report</td>
            </tr>
        
            <tr>
                <td><code>F625</code></td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>F635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>F645</code></td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
            <tr>
                <td><code>BADFORMAT 253</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>form</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Overview (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview.html#document/p4">4-8</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Overview (`1-2 <https://www.documentcloud.org/documents/2711624-Overview.html#document/p1>`_)

* CAL-ACCESS Tables, Columns and Indexes (`49-50 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p49>`_)






------------

*********************
FILERS_CD
*********************

This table is the parent table from which all links and associations
to a filer are derived.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILERS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
FILER_ACRONYMS_CD
*********************

Links acronyms to filers


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ACRONYMS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>ACRONYM</code></td>
        
            <td><code>FILER_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>ACRONYM</code></td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>AMS acronym</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
FILER_ADDRESS_CD
*********************

Links filers and addresses. This table maintains a history of when
addresses change.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ADDRESS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>ADRID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADRID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Address effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Address type</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``add_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>51</code></td>
                <td>PERMANENT</td>
            </tr>
        
            <tr>
                <td><code>7026</code></td>
                <td>BUSINESS</td>
            </tr>
        
            <tr>
                <td><code>7027</code></td>
                <td>HOME</td>
            </tr>
        
            <tr>
                <td><code>7050</code></td>
                <td>NOT IN USE</td>
            </tr>
        
            <tr>
                <td><code>7051</code></td>
                <td>PERMANENT</td>
            </tr>
        
            <tr>
                <td><code>7082</code></td>
                <td>MAILING ADDRESS</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p5">5</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `61-62 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p61>`_)






------------

*********************
FILER_ETHICS_CLASS_CD
*********************

This table stores lobbyist ethics training dates.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ETHICS_CLASS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>SESSION_ID</code></td>
        
            <td><code>ETHICS_DATE</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ETHICS_DATE</code></td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Date ethics training was accomplished</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
FILER_INTERESTS_CD
*********************

Links a filer to their interest codes.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_INTERESTS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>INTEREST_CD</code></td>
        
            <td><code>EFFECT_DATE</code></td>
        
            <td><code>SESSION_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_CD</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Interest code linked to the filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DATE</code></td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``interest_cd``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>40301</code></td>
                <td>AGRICULTURE</td>
            </tr>
        
            <tr>
                <td><code>40302</code></td>
                <td>EDUCATION</td>
            </tr>
        
            <tr>
                <td><code>40303</code></td>
                <td>ENTERTAINMENT/RECREATION</td>
            </tr>
        
            <tr>
                <td><code>40304</code></td>
                <td>FINANCE/INSURANCE</td>
            </tr>
        
            <tr>
                <td><code>40305</code></td>
                <td>GOVERNMENT</td>
            </tr>
        
            <tr>
                <td><code>40306</code></td>
                <td>HEALTH</td>
            </tr>
        
            <tr>
                <td><code>40307</code></td>
                <td>LABOR UNIONS</td>
            </tr>
        
            <tr>
                <td><code>40308</code></td>
                <td>LEGAL</td>
            </tr>
        
            <tr>
                <td><code>40309</code></td>
                <td>LODGING/RESTAURANTS</td>
            </tr>
        
            <tr>
                <td><code>40310</code></td>
                <td>MANUFACTURING/INDUSTRIAL</td>
            </tr>
        
            <tr>
                <td><code>40311</code></td>
                <td>MERCHANDISE/RETAIL</td>
            </tr>
        
            <tr>
                <td><code>40312</code></td>
                <td>MISCELLANEOUS</td>
            </tr>
        
            <tr>
                <td><code>40313</code></td>
                <td>OIL AND GAS</td>
            </tr>
        
            <tr>
                <td><code>40314</code></td>
                <td>POLITICAL ORGANIZATIONS</td>
            </tr>
        
            <tr>
                <td><code>40315</code></td>
                <td>PROFESSIONAL/TRADE</td>
            </tr>
        
            <tr>
                <td><code>40316</code></td>
                <td>PUBLIC EMPLOYEES</td>
            </tr>
        
            <tr>
                <td><code>40317</code></td>
                <td>REAL ESTATE</td>
            </tr>
        
            <tr>
                <td><code>40318</code></td>
                <td>TRANSPORTATION</td>
            </tr>
        
            <tr>
                <td><code>40319</code></td>
                <td>UTILITIES</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p19">19</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `66 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p66>`_)






------------

*********************
FILER_LINKS_CD
*********************

Links filers to each other and records their relationship type.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_LINKS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID_A</code></td>
        
            <td><code>FILER_ID_B</code></td>
        
            <td><code>ACTIVE_FLG</code></td>
        
            <td><code>SESSION_ID</code></td>
        
            <td><code>LINK_TYPE</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID_A</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the first filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID_B</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the second filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACTIVE_FLG</code></td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Indicates if the link is active</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINK_TYPE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Denotes the type of the link</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINK_DESC</code></td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the link became active</td>
        </tr>
    
    
    
        <tr>
            <td><code>DOMINATE_FILER</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td><code>TERMINATION_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``link_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>-12019</code></td>
                <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>-12018</code></td>
                <td>PROPONENT</td>
            </tr>
        
            <tr>
                <td><code>-12016</code></td>
                <td>TREASURER/RESPONSIBLE OFFICER FOR</td>
            </tr>
        
            <tr>
                <td><code>-12015</code></td>
                <td>ASSOCIATED</td>
            </tr>
        
            <tr>
                <td><code>-12014</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>-12013</code></td>
                <td>OPPOSE</td>
            </tr>
        
            <tr>
                <td><code>-12011</code></td>
                <td>CONTROLLING CANDIDATE</td>
            </tr>
        
            <tr>
                <td><code>-12008</code></td>
                <td>FIRM OF A LOBBYIST</td>
            </tr>
        
            <tr>
                <td><code>-12005</code></td>
                <td>FIRM OF A CLIENT (WHO IS ALSO A FIRM)</td>
            </tr>
        
            <tr>
                <td><code>-12004</code></td>
                <td>FIRM OF A CLIENT (WHO IS AN EMPLOYER)</td>
            </tr>
        
            <tr>
                <td><code>-12002</code></td>
                <td>EMPLOYER OF  AN IN-HOUSE LOBBYIST</td>
            </tr>
        
            <tr>
                <td><code>-12001</code></td>
                <td>CLIENT OF A FIRM</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>12001</code></td>
                <td>FIRM OF A CLIENT</td>
            </tr>
        
            <tr>
                <td><code>12002</code></td>
                <td>IN-HOUSE LOBBYIST OF AN EMPLOYER</td>
            </tr>
        
            <tr>
                <td><code>12004</code></td>
                <td>CLIENT (WHO IS AN EMPLOYER) OF A FIRM</td>
            </tr>
        
            <tr>
                <td><code>12005</code></td>
                <td>CLIENT (WHO IS ALSO A FIRM) OF ANOTHER FIRM</td>
            </tr>
        
            <tr>
                <td><code>12008</code></td>
                <td>LOBBYIST OF A FIRM</td>
            </tr>
        
            <tr>
                <td><code>12011</code></td>
                <td>CANDIDATE CONTROLS THIS COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>12013</code></td>
                <td>OPPOSE</td>
            </tr>
        
            <tr>
                <td><code>12014</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>12015</code></td>
                <td>ASSOCIATED</td>
            </tr>
        
            <tr>
                <td><code>12016</code></td>
                <td>TREASURER/RESPONSIBLE OFFICER</td>
            </tr>
        
            <tr>
                <td><code>12018</code></td>
                <td>PROPONENT</td>
            </tr>
        
            <tr>
                <td><code>12019</code></td>
                <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p6">6-7</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `67 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p67>`_)






------------

*********************
FILER_STATUS_TYPES_CD
*********************

This is an undocumented model that contains a small number
of codes and definitions that map to values in FILERNAME_CD.STATUS.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_STATUS_TYPES_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>STATUS_TYPE</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>STATUS_TYPE</code></td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>STATUS_DESC</code></td>
            <td>String (up to 11)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
FILER_TO_FILER_TYPE_CD
*********************

This table links a filer to a set of characteristics that describe the
filer. This table maintains a history of changes and allows the filer
to change characteristics over time.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TO_FILER_TYPE_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>FILER_TYPE</code></td>
        
            <td><code>SESSION_ID</code></td>
        
            <td><code>EFFECT_DT</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_TYPE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACTIVE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if the filer is currently active</td>
        </tr>
    
    
    
        <tr>
            <td><code>RACE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>If applicable indicates the race in which the filer is running</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CATEGORY</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Defines the filer&#39;s category such as controlled, jointly controlled, etc. (subset of filer&#39;s type)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CATEGORY_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable, the category type specifies additional information about the category. (e.g. state, local, etc.)</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_CATEGORY</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies general purpose, primarily formed, etc.</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>The date the filer assumed the current class or type</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_CATEGORY_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies broad based or small contributor</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECTION_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates type of election (general, primary, special)</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_CATEGORY_A</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if sponsored or not</td>
        </tr>
    
    
    
        <tr>
            <td><code>NYQ_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Indicates the date when a committee reached its qualifying level of activity</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARTY_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s political party</td>
        </tr>
    
    
    
        <tr>
            <td><code>COUNTY_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s county code</td>
        </tr>
    
    
    
        <tr>
            <td><code>DISTRICT_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s district number for the office being sought. Populated for Senate, Assembly or Board of Equalization races</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``race``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>30002</code></td>
                <td>GOVERNOR</td>
            </tr>
        
            <tr>
                <td><code>30003</code></td>
                <td>LIEUTENANT GOVERNOR</td>
            </tr>
        
            <tr>
                <td><code>30004</code></td>
                <td>SECRETARY OF STATE</td>
            </tr>
        
            <tr>
                <td><code>30005</code></td>
                <td>CONTROLLER</td>
            </tr>
        
            <tr>
                <td><code>30006</code></td>
                <td>TREASURER</td>
            </tr>
        
            <tr>
                <td><code>30007</code></td>
                <td>ATTORNEY GENERAL</td>
            </tr>
        
            <tr>
                <td><code>30008</code></td>
                <td>SUPERINTENDENT OF PUBLIC INSTRUCTION</td>
            </tr>
        
            <tr>
                <td><code>30009</code></td>
                <td>MEMBER BOARD OF EQUALIZATION</td>
            </tr>
        
            <tr>
                <td><code>30010</code></td>
                <td>OXNARD HARBOR COMMISSIONER</td>
            </tr>
        
            <tr>
                <td><code>30011</code></td>
                <td>CITY CONTROLLER</td>
            </tr>
        
            <tr>
                <td><code>30012</code></td>
                <td>STATE SENATE</td>
            </tr>
        
            <tr>
                <td><code>30013</code></td>
                <td>ASSEMBLY</td>
            </tr>
        
            <tr>
                <td><code>30014</code></td>
                <td>INSURANCE COMMISSIONER</td>
            </tr>
        
            <tr>
                <td><code>30015</code></td>
                <td>JUDGE</td>
            </tr>
        
            <tr>
                <td><code>30016</code></td>
                <td>BOARD MEMBER</td>
            </tr>
        
            <tr>
                <td><code>30017</code></td>
                <td>TAX COLLECTOR</td>
            </tr>
        
            <tr>
                <td><code>30018</code></td>
                <td>TRUSTEE</td>
            </tr>
        
            <tr>
                <td><code>30019</code></td>
                <td>SUPERVISOR</td>
            </tr>
        
            <tr>
                <td><code>30020</code></td>
                <td>SHERIFF</td>
            </tr>
        
            <tr>
                <td><code>30021</code></td>
                <td>CORONER</td>
            </tr>
        
            <tr>
                <td><code>30022</code></td>
                <td>MARSHALL</td>
            </tr>
        
            <tr>
                <td><code>30023</code></td>
                <td>CITY CLERK</td>
            </tr>
        
            <tr>
                <td><code>30024</code></td>
                <td>SCHOOL BOARD</td>
            </tr>
        
            <tr>
                <td><code>30025</code></td>
                <td>HARBOR COMMISSIONER</td>
            </tr>
        
            <tr>
                <td><code>30026</code></td>
                <td>DISTRICT ATTORNEY</td>
            </tr>
        
            <tr>
                <td><code>30027</code></td>
                <td>COUNTY CLERK</td>
            </tr>
        
            <tr>
                <td><code>30028</code></td>
                <td>AUDITOR</td>
            </tr>
        
            <tr>
                <td><code>30029</code></td>
                <td>MAYOR</td>
            </tr>
        
            <tr>
                <td><code>30030</code></td>
                <td>CITY ATTORNEY</td>
            </tr>
        
            <tr>
                <td><code>30031</code></td>
                <td>DEMOCRATIC COUNTY CENTRAL COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>30032</code></td>
                <td>TOWN COUNCIL</td>
            </tr>
        
            <tr>
                <td><code>30033</code></td>
                <td>ASSESSOR</td>
            </tr>
        
            <tr>
                <td><code>30034</code></td>
                <td>CITY TREASURER</td>
            </tr>
        
            <tr>
                <td><code>30035</code></td>
                <td>CITY COUNCIL</td>
            </tr>
        
            <tr>
                <td><code>30036</code></td>
                <td>COMMISSIONER</td>
            </tr>
        
            <tr>
                <td><code>30037</code></td>
                <td>REPUBLICAN COUNTY CENTRAL COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>30038</code></td>
                <td>DIRECTOR</td>
            </tr>
        
            <tr>
                <td><code>30039</code></td>
                <td>DIRECTOR OF ZONE 7</td>
            </tr>
        
            <tr>
                <td><code>30040</code></td>
                <td>COMMUNITY COLLEGE BOARD</td>
            </tr>
        
            <tr>
                <td><code>30041</code></td>
                <td>POLICE CHIEF</td>
            </tr>
        
            <tr>
                <td><code>30042</code></td>
                <td>CHIEF OF POLICE</td>
            </tr>
        
            <tr>
                <td><code>30043</code></td>
                <td>CENTRAL COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>30044</code></td>
                <td>BOARD OF EDUCATION</td>
            </tr>
        
            <tr>
                <td><code>30045</code></td>
                <td>BOARD OF DIRECTORS</td>
            </tr>
        
            <tr>
                <td><code>30046</code></td>
                <td>COLLEGE BOARD</td>
            </tr>
        
            <tr>
                <td><code>30047</code></td>
                <td>BART BOARD DIRECTOR</td>
            </tr>
        
            <tr>
                <td><code>30048</code></td>
                <td>BOARD OF TRUSTEES</td>
            </tr>
        
            <tr>
                <td><code>30049</code></td>
                <td>IRRIGATION</td>
            </tr>
        
            <tr>
                <td><code>30050</code></td>
                <td>WATER BOARD</td>
            </tr>
        
            <tr>
                <td><code>30051</code></td>
                <td>COMMUNITY PLANNING GROUP</td>
            </tr>
        
            <tr>
                <td><code>30052</code></td>
                <td>BOARD OF SUPERVISORS</td>
            </tr>
        
            <tr>
                <td><code>30053</code></td>
                <td>SUPERIOR COURT JUDGE</td>
            </tr>
        
            <tr>
                <td><code>30054</code></td>
                <td>DISTRICT ATTORNEY/PUBLIC DEFENDER</td>
            </tr>
        
            <tr>
                <td><code>30055</code></td>
                <td>MEASURE</td>
            </tr>
        
            <tr>
                <td><code>30056</code></td>
                <td>CITY PROSECUTOR</td>
            </tr>
        
            <tr>
                <td><code>30057</code></td>
                <td>SUPREME COURT JUDGE</td>
            </tr>
        
            <tr>
                <td><code>30058</code></td>
                <td>PUBLIC EMPLOYEES RETIREMENT BOARD</td>
            </tr>
        
            <tr>
                <td><code>30059</code></td>
                <td>APPELLATE COURT JUDGE</td>
            </tr>
        
            <tr>
                <td><code>50001</code></td>
                <td>Ag</td>
            </tr>
        
            <tr>
                <td><code>50002</code></td>
                <td>Assembly</td>
            </tr>
        
            <tr>
                <td><code>50003</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>50004</code></td>
                <td>Assessor/Clerk/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50005</code></td>
                <td>Assessor/County Clerk/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50006</code></td>
                <td>Assessor/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50007</code></td>
                <td>Associate Justice</td>
            </tr>
        
            <tr>
                <td><code>50008</code></td>
                <td>Auditor</td>
            </tr>
        
            <tr>
                <td><code>50009</code></td>
                <td>Auditor/Controller</td>
            </tr>
        
            <tr>
                <td><code>50010</code></td>
                <td>Auditor/Controller/Clerk/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50011</code></td>
                <td>Auditor/Controller/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50012</code></td>
                <td>Auditor/Controller/Treasurer/Tax Collector</td>
            </tr>
        
            <tr>
                <td><code>50013</code></td>
                <td>Auditor/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50014</code></td>
                <td>Board Member</td>
            </tr>
        
            <tr>
                <td><code>50015</code></td>
                <td>Board Of Director</td>
            </tr>
        
            <tr>
                <td><code>50016</code></td>
                <td>Board Of Supervisor</td>
            </tr>
        
            <tr>
                <td><code>50017</code></td>
                <td>Boe</td>
            </tr>
        
            <tr>
                <td><code>50018</code></td>
                <td>Chief Justice</td>
            </tr>
        
            <tr>
                <td><code>50019</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>50020</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>50021</code></td>
                <td>City Auditor</td>
            </tr>
        
            <tr>
                <td><code>50022</code></td>
                <td>City Clerk</td>
            </tr>
        
            <tr>
                <td><code>50023</code></td>
                <td>City Council</td>
            </tr>
        
            <tr>
                <td><code>50024</code></td>
                <td>City Of Los Angeles</td>
            </tr>
        
            <tr>
                <td><code>50025</code></td>
                <td>City Of South El Monte</td>
            </tr>
        
            <tr>
                <td><code>50026</code></td>
                <td>City Prosecutor</td>
            </tr>
        
            <tr>
                <td><code>50027</code></td>
                <td>City Treasurer</td>
            </tr>
        
            <tr>
                <td><code>50028</code></td>
                <td>Clerk/Auditor</td>
            </tr>
        
            <tr>
                <td><code>50029</code></td>
                <td>Clerk/Record/Public Admin</td>
            </tr>
        
            <tr>
                <td><code>50030</code></td>
                <td>Clerk/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50031</code></td>
                <td>Clerk/Recorder/Registar</td>
            </tr>
        
            <tr>
                <td><code>50032</code></td>
                <td>Clerk/Recorder/Registrar</td>
            </tr>
        
            <tr>
                <td><code>50033</code></td>
                <td>Commissioner</td>
            </tr>
        
            <tr>
                <td><code>50034</code></td>
                <td>Controller</td>
            </tr>
        
            <tr>
                <td><code>50035</code></td>
                <td>Costa Mesa</td>
            </tr>
        
            <tr>
                <td><code>50036</code></td>
                <td>Council Member</td>
            </tr>
        
            <tr>
                <td><code>50037</code></td>
                <td>County Clerk</td>
            </tr>
        
            <tr>
                <td><code>50038</code></td>
                <td>County Clerk/Auditor</td>
            </tr>
        
            <tr>
                <td><code>50039</code></td>
                <td>County Clerk/Auditor/Controller</td>
            </tr>
        
            <tr>
                <td><code>50040</code></td>
                <td>County Clerk/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50041</code></td>
                <td>County Clerk/Recorder/Assessor</td>
            </tr>
        
            <tr>
                <td><code>50042</code></td>
                <td>County Clerk/Recorder/Public Admin</td>
            </tr>
        
            <tr>
                <td><code>50043</code></td>
                <td>Democratic County Central Committee</td>
            </tr>
        
            <tr>
                <td><code>50044</code></td>
                <td>Director</td>
            </tr>
        
            <tr>
                <td><code>50045</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>50046</code></td>
                <td>District Attorney/Public Administrator</td>
            </tr>
        
            <tr>
                <td><code>50047</code></td>
                <td>Gccc</td>
            </tr>
        
            <tr>
                <td><code>50048</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>50049</code></td>
                <td>Harbor Commissioner</td>
            </tr>
        
            <tr>
                <td><code>50050</code></td>
                <td>Ic</td>
            </tr>
        
            <tr>
                <td><code>50051</code></td>
                <td>Irrigation Dist</td>
            </tr>
        
            <tr>
                <td><code>50052</code></td>
                <td>Judge</td>
            </tr>
        
            <tr>
                <td><code>50053</code></td>
                <td>Justice</td>
            </tr>
        
            <tr>
                <td><code>50054</code></td>
                <td>Legislature</td>
            </tr>
        
            <tr>
                <td><code>50055</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>50056</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>50057</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>50058</code></td>
                <td>Placentia</td>
            </tr>
        
            <tr>
                <td><code>50059</code></td>
                <td>Public Administrator</td>
            </tr>
        
            <tr>
                <td><code>50060</code></td>
                <td>Public Administrator/Guardian</td>
            </tr>
        
            <tr>
                <td><code>50061</code></td>
                <td>Rent Stabilization Board</td>
            </tr>
        
            <tr>
                <td><code>50062</code></td>
                <td>Republican Central Committee</td>
            </tr>
        
            <tr>
                <td><code>50063</code></td>
                <td>San Francisco Dccc</td>
            </tr>
        
            <tr>
                <td><code>50064</code></td>
                <td>Sanger</td>
            </tr>
        
            <tr>
                <td><code>50065</code></td>
                <td>School Board</td>
            </tr>
        
            <tr>
                <td><code>50066</code></td>
                <td>Secretary Of State</td>
            </tr>
        
            <tr>
                <td><code>50067</code></td>
                <td>Senator</td>
            </tr>
        
            <tr>
                <td><code>50068</code></td>
                <td>Sheriff</td>
            </tr>
        
            <tr>
                <td><code>50069</code></td>
                <td>Sheriff/Coroner</td>
            </tr>
        
            <tr>
                <td><code>50070</code></td>
                <td>Sheriff/Coroner/Marshall</td>
            </tr>
        
            <tr>
                <td><code>50071</code></td>
                <td>Sheriff/Coroner/Public Administrator</td>
            </tr>
        
            <tr>
                <td><code>50072</code></td>
                <td>Solana Beach</td>
            </tr>
        
            <tr>
                <td><code>50073</code></td>
                <td>Superintendent</td>
            </tr>
        
            <tr>
                <td><code>50074</code></td>
                <td>Supervisor</td>
            </tr>
        
            <tr>
                <td><code>50075</code></td>
                <td>Supt Of Schools</td>
            </tr>
        
            <tr>
                <td><code>50076</code></td>
                <td>Tax Collector</td>
            </tr>
        
            <tr>
                <td><code>50077</code></td>
                <td>Town Council</td>
            </tr>
        
            <tr>
                <td><code>50078</code></td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td><code>50079</code></td>
                <td>Treasurer/Tax Collector</td>
            </tr>
        
            <tr>
                <td><code>50080</code></td>
                <td>Treasurer/Tax Collector/Clerk</td>
            </tr>
        
            <tr>
                <td><code>50081</code></td>
                <td>Treasurer/Tax Collector/Public Administrator</td>
            </tr>
        
            <tr>
                <td><code>50082</code></td>
                <td>Treasurer/Tax Collector/Public Administrator/County Clerk</td>
            </tr>
        
            <tr>
                <td><code>50083</code></td>
                <td>Treasurer/Tax Collector/Recorder</td>
            </tr>
        
            <tr>
                <td><code>50084</code></td>
                <td>Trustee</td>
            </tr>
        
            <tr>
                <td><code>50085</code></td>
                <td>Weed Recreation Board Member</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p16">16-18</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p20">20-22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``category``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>40000</code></td>
                <td>CATEGORY</td>
            </tr>
        
            <tr>
                <td><code>40001</code></td>
                <td>JOINTLY CONTROLLED</td>
            </tr>
        
            <tr>
                <td><code>40002</code></td>
                <td>CONTROLLED</td>
            </tr>
        
            <tr>
                <td><code>40003</code></td>
                <td>CAUCUS COMMITTEE</td>
            </tr>
        
            <tr>
                <td><code>40004</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``category_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>40501</code></td>
                <td>LOCAL</td>
            </tr>
        
            <tr>
                <td><code>40502</code></td>
                <td>STATE</td>
            </tr>
        
            <tr>
                <td><code>40503</code></td>
                <td>COUNTY</td>
            </tr>
        
            <tr>
                <td><code>40504</code></td>
                <td>MULTI-COUNTY</td>
            </tr>
        
            <tr>
                <td><code>40505</code></td>
                <td>CITY</td>
            </tr>
        
            <tr>
                <td><code>40506</code></td>
                <td>FEDERAL</td>
            </tr>
        
            <tr>
                <td><code>40507</code></td>
                <td>SUPERIOR COURT JUDGE</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p19">19-20</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sub_category``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>40101</code></td>
                <td>PRIMARILY FORMED MEASURE</td>
            </tr>
        
            <tr>
                <td><code>40102</code></td>
                <td>PRIMARILY FORMED CANDIDATE</td>
            </tr>
        
            <tr>
                <td><code>40103</code></td>
                <td>GENERAL PURPOSE</td>
            </tr>
        
            <tr>
                <td><code>40104</code></td>
                <td>GENERAL PURPOSE POLITICAL PARTY</td>
            </tr>
        
            <tr>
                <td><code>40105</code></td>
                <td>GENERAL PURPOSE MEASURE</td>
            </tr>
        
            <tr>
                <td><code>40112</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sub_category_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>40202</code></td>
                <td>BROAD-BASED</td>
            </tr>
        
            <tr>
                <td><code>40203</code></td>
                <td>SMALL CONTRIBUTOR</td>
            </tr>
        
            <tr>
                <td><code>40204</code></td>
                <td>MPO - NON PROFIT</td>
            </tr>
        
            <tr>
                <td><code>40205</code></td>
                <td>MPO - NON PROFIT CY</td>
            </tr>
        
            <tr>
                <td><code>40206</code></td>
                <td>MPO - OTHER</td>
            </tr>
        
            <tr>
                <td><code>40207</code></td>
                <td>MPO - OTHER CY</td>
            </tr>
        
            <tr>
                <td><code>40208</code></td>
                <td>FEDERAL PAC</td>
            </tr>
        
            <tr>
                <td><code>40209</code></td>
                <td>OUT OF STATE PAC</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p18">18-19</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``election_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>3001</code></td>
                <td>GENERAL</td>
            </tr>
        
            <tr>
                <td><code>3002</code></td>
                <td>PRIMARY</td>
            </tr>
        
            <tr>
                <td><code>3003</code></td>
                <td>RECALL</td>
            </tr>
        
            <tr>
                <td><code>3004</code></td>
                <td>SPECIAL ELECTION</td>
            </tr>
        
            <tr>
                <td><code>3005</code></td>
                <td>OFFICEHOLDER</td>
            </tr>
        
            <tr>
                <td><code>3006</code></td>
                <td>SPECIAL RUNOFF</td>
            </tr>
        
            <tr>
                <td><code>3010</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>3007</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p3">3-4</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``party_cd``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>16001</code></td>
                <td>DEMOCRATIC</td>
            </tr>
        
            <tr>
                <td><code>16002</code></td>
                <td>REPUBLICAN</td>
            </tr>
        
            <tr>
                <td><code>16003</code></td>
                <td>GREEN PARTY</td>
            </tr>
        
            <tr>
                <td><code>16004</code></td>
                <td>REFORM PARTY</td>
            </tr>
        
            <tr>
                <td><code>16005</code></td>
                <td>AMERICAN INDEPENDENT PARTY</td>
            </tr>
        
            <tr>
                <td><code>16006</code></td>
                <td>PEACE AND FREEDOM</td>
            </tr>
        
            <tr>
                <td><code>16007</code></td>
                <td>INDEPENDENT</td>
            </tr>
        
            <tr>
                <td><code>16008</code></td>
                <td>LIBERTARIAN</td>
            </tr>
        
            <tr>
                <td><code>16009</code></td>
                <td>NON PARTISAN</td>
            </tr>
        
            <tr>
                <td><code>16010</code></td>
                <td>NATURAL LAW</td>
            </tr>
        
            <tr>
                <td><code>16011</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>16012</code></td>
                <td>NO PARTY PREFERENCE</td>
            </tr>
        
            <tr>
                <td><code>16013</code></td>
                <td>AMERICANS ELECT</td>
            </tr>
        
            <tr>
                <td><code>16020</code></td>
                <td>PEACE AND FREEDOM</td>
            </tr>
        
            <tr>
                <td><code>16014</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>None</code></td>
                <td>NONE</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p10">10-11</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``county_cd``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>18001</code></td>
                <td>01</td>
            </tr>
        
            <tr>
                <td><code>18002</code></td>
                <td>12</td>
            </tr>
        
            <tr>
                <td><code>18003</code></td>
                <td>23</td>
            </tr>
        
            <tr>
                <td><code>18004</code></td>
                <td>34</td>
            </tr>
        
            <tr>
                <td><code>18005</code></td>
                <td>45</td>
            </tr>
        
            <tr>
                <td><code>18006</code></td>
                <td>55</td>
            </tr>
        
            <tr>
                <td><code>18007</code></td>
                <td>56</td>
            </tr>
        
            <tr>
                <td><code>18008</code></td>
                <td>57</td>
            </tr>
        
            <tr>
                <td><code>18009</code></td>
                <td>58</td>
            </tr>
        
            <tr>
                <td><code>18010</code></td>
                <td>02</td>
            </tr>
        
            <tr>
                <td><code>18011</code></td>
                <td>03</td>
            </tr>
        
            <tr>
                <td><code>18012</code></td>
                <td>04</td>
            </tr>
        
            <tr>
                <td><code>18013</code></td>
                <td>05</td>
            </tr>
        
            <tr>
                <td><code>18014</code></td>
                <td>06</td>
            </tr>
        
            <tr>
                <td><code>18015</code></td>
                <td>07</td>
            </tr>
        
            <tr>
                <td><code>18016</code></td>
                <td>08</td>
            </tr>
        
            <tr>
                <td><code>18017</code></td>
                <td>09</td>
            </tr>
        
            <tr>
                <td><code>18018</code></td>
                <td>10</td>
            </tr>
        
            <tr>
                <td><code>18019</code></td>
                <td>11</td>
            </tr>
        
            <tr>
                <td><code>18020</code></td>
                <td>13</td>
            </tr>
        
            <tr>
                <td><code>18021</code></td>
                <td>14</td>
            </tr>
        
            <tr>
                <td><code>18022</code></td>
                <td>15</td>
            </tr>
        
            <tr>
                <td><code>18023</code></td>
                <td>16</td>
            </tr>
        
            <tr>
                <td><code>18024</code></td>
                <td>17</td>
            </tr>
        
            <tr>
                <td><code>18025</code></td>
                <td>18</td>
            </tr>
        
            <tr>
                <td><code>18026</code></td>
                <td>19</td>
            </tr>
        
            <tr>
                <td><code>18027</code></td>
                <td>20</td>
            </tr>
        
            <tr>
                <td><code>18028</code></td>
                <td>21</td>
            </tr>
        
            <tr>
                <td><code>18029</code></td>
                <td>22</td>
            </tr>
        
            <tr>
                <td><code>18030</code></td>
                <td>24</td>
            </tr>
        
            <tr>
                <td><code>18031</code></td>
                <td>25</td>
            </tr>
        
            <tr>
                <td><code>18032</code></td>
                <td>26</td>
            </tr>
        
            <tr>
                <td><code>18033</code></td>
                <td>27</td>
            </tr>
        
            <tr>
                <td><code>18034</code></td>
                <td>28</td>
            </tr>
        
            <tr>
                <td><code>18035</code></td>
                <td>29</td>
            </tr>
        
            <tr>
                <td><code>18036</code></td>
                <td>30</td>
            </tr>
        
            <tr>
                <td><code>18037</code></td>
                <td>31</td>
            </tr>
        
            <tr>
                <td><code>18038</code></td>
                <td>32</td>
            </tr>
        
            <tr>
                <td><code>18039</code></td>
                <td>33</td>
            </tr>
        
            <tr>
                <td><code>18040</code></td>
                <td>35</td>
            </tr>
        
            <tr>
                <td><code>18041</code></td>
                <td>36</td>
            </tr>
        
            <tr>
                <td><code>18042</code></td>
                <td>37</td>
            </tr>
        
            <tr>
                <td><code>18043</code></td>
                <td>38</td>
            </tr>
        
            <tr>
                <td><code>18044</code></td>
                <td>39</td>
            </tr>
        
            <tr>
                <td><code>18045</code></td>
                <td>40</td>
            </tr>
        
            <tr>
                <td><code>18046</code></td>
                <td>41</td>
            </tr>
        
            <tr>
                <td><code>18047</code></td>
                <td>42</td>
            </tr>
        
            <tr>
                <td><code>18048</code></td>
                <td>43</td>
            </tr>
        
            <tr>
                <td><code>18049</code></td>
                <td>44</td>
            </tr>
        
            <tr>
                <td><code>18050</code></td>
                <td>46</td>
            </tr>
        
            <tr>
                <td><code>18051</code></td>
                <td>47</td>
            </tr>
        
            <tr>
                <td><code>18052</code></td>
                <td>48</td>
            </tr>
        
            <tr>
                <td><code>18053</code></td>
                <td>49</td>
            </tr>
        
            <tr>
                <td><code>18054</code></td>
                <td>50</td>
            </tr>
        
            <tr>
                <td><code>18055</code></td>
                <td>51</td>
            </tr>
        
            <tr>
                <td><code>18056</code></td>
                <td>52</td>
            </tr>
        
            <tr>
                <td><code>18057</code></td>
                <td>53</td>
            </tr>
        
            <tr>
                <td><code>18058</code></td>
                <td>54</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p13">13-15</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``district_cd``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>17001</code></td>
                <td>01</td>
            </tr>
        
            <tr>
                <td><code>17002</code></td>
                <td>13</td>
            </tr>
        
            <tr>
                <td><code>17003</code></td>
                <td>24</td>
            </tr>
        
            <tr>
                <td><code>17004</code></td>
                <td>35</td>
            </tr>
        
            <tr>
                <td><code>17005</code></td>
                <td>46</td>
            </tr>
        
            <tr>
                <td><code>17006</code></td>
                <td>57</td>
            </tr>
        
            <tr>
                <td><code>17007</code></td>
                <td>68</td>
            </tr>
        
            <tr>
                <td><code>17008</code></td>
                <td>79</td>
            </tr>
        
            <tr>
                <td><code>17009</code></td>
                <td>02</td>
            </tr>
        
            <tr>
                <td><code>17010</code></td>
                <td>05</td>
            </tr>
        
            <tr>
                <td><code>17011</code></td>
                <td>04</td>
            </tr>
        
            <tr>
                <td><code>17013</code></td>
                <td>06</td>
            </tr>
        
            <tr>
                <td><code>17014</code></td>
                <td>07</td>
            </tr>
        
            <tr>
                <td><code>17015</code></td>
                <td>08</td>
            </tr>
        
            <tr>
                <td><code>17016</code></td>
                <td>19</td>
            </tr>
        
            <tr>
                <td><code>17017</code></td>
                <td>10</td>
            </tr>
        
            <tr>
                <td><code>17018</code></td>
                <td>11</td>
            </tr>
        
            <tr>
                <td><code>17019</code></td>
                <td>12</td>
            </tr>
        
            <tr>
                <td><code>17020</code></td>
                <td>14</td>
            </tr>
        
            <tr>
                <td><code>17021</code></td>
                <td>15</td>
            </tr>
        
            <tr>
                <td><code>17022</code></td>
                <td>16</td>
            </tr>
        
            <tr>
                <td><code>17023</code></td>
                <td>17</td>
            </tr>
        
            <tr>
                <td><code>17024</code></td>
                <td>18</td>
            </tr>
        
            <tr>
                <td><code>17026</code></td>
                <td>20</td>
            </tr>
        
            <tr>
                <td><code>17027</code></td>
                <td>21</td>
            </tr>
        
            <tr>
                <td><code>17028</code></td>
                <td>22</td>
            </tr>
        
            <tr>
                <td><code>17029</code></td>
                <td>23</td>
            </tr>
        
            <tr>
                <td><code>17030</code></td>
                <td>25</td>
            </tr>
        
            <tr>
                <td><code>17031</code></td>
                <td>26</td>
            </tr>
        
            <tr>
                <td><code>17032</code></td>
                <td>27</td>
            </tr>
        
            <tr>
                <td><code>17033</code></td>
                <td>28</td>
            </tr>
        
            <tr>
                <td><code>17034</code></td>
                <td>29</td>
            </tr>
        
            <tr>
                <td><code>17035</code></td>
                <td>30</td>
            </tr>
        
            <tr>
                <td><code>17036</code></td>
                <td>31</td>
            </tr>
        
            <tr>
                <td><code>17037</code></td>
                <td>32</td>
            </tr>
        
            <tr>
                <td><code>17038</code></td>
                <td>33</td>
            </tr>
        
            <tr>
                <td><code>17039</code></td>
                <td>34</td>
            </tr>
        
            <tr>
                <td><code>17040</code></td>
                <td>36</td>
            </tr>
        
            <tr>
                <td><code>17041</code></td>
                <td>37</td>
            </tr>
        
            <tr>
                <td><code>17042</code></td>
                <td>38</td>
            </tr>
        
            <tr>
                <td><code>17043</code></td>
                <td>39</td>
            </tr>
        
            <tr>
                <td><code>17044</code></td>
                <td>40</td>
            </tr>
        
            <tr>
                <td><code>17045</code></td>
                <td>41</td>
            </tr>
        
            <tr>
                <td><code>17046</code></td>
                <td>42</td>
            </tr>
        
            <tr>
                <td><code>17047</code></td>
                <td>43</td>
            </tr>
        
            <tr>
                <td><code>17048</code></td>
                <td>44</td>
            </tr>
        
            <tr>
                <td><code>17049</code></td>
                <td>45</td>
            </tr>
        
            <tr>
                <td><code>17050</code></td>
                <td>47</td>
            </tr>
        
            <tr>
                <td><code>17051</code></td>
                <td>48</td>
            </tr>
        
            <tr>
                <td><code>17052</code></td>
                <td>49</td>
            </tr>
        
            <tr>
                <td><code>17053</code></td>
                <td>50</td>
            </tr>
        
            <tr>
                <td><code>17054</code></td>
                <td>51</td>
            </tr>
        
            <tr>
                <td><code>17055</code></td>
                <td>52</td>
            </tr>
        
            <tr>
                <td><code>17056</code></td>
                <td>53</td>
            </tr>
        
            <tr>
                <td><code>17057</code></td>
                <td>54</td>
            </tr>
        
            <tr>
                <td><code>17058</code></td>
                <td>55</td>
            </tr>
        
            <tr>
                <td><code>17059</code></td>
                <td>56</td>
            </tr>
        
            <tr>
                <td><code>17060</code></td>
                <td>03</td>
            </tr>
        
            <tr>
                <td><code>17061</code></td>
                <td>59</td>
            </tr>
        
            <tr>
                <td><code>17062</code></td>
                <td>60</td>
            </tr>
        
            <tr>
                <td><code>17063</code></td>
                <td>61</td>
            </tr>
        
            <tr>
                <td><code>17064</code></td>
                <td>62</td>
            </tr>
        
            <tr>
                <td><code>17065</code></td>
                <td>63</td>
            </tr>
        
            <tr>
                <td><code>17066</code></td>
                <td>64</td>
            </tr>
        
            <tr>
                <td><code>17067</code></td>
                <td>65</td>
            </tr>
        
            <tr>
                <td><code>17068</code></td>
                <td>66</td>
            </tr>
        
            <tr>
                <td><code>17069</code></td>
                <td>67</td>
            </tr>
        
            <tr>
                <td><code>17070</code></td>
                <td>69</td>
            </tr>
        
            <tr>
                <td><code>17071</code></td>
                <td>70</td>
            </tr>
        
            <tr>
                <td><code>17072</code></td>
                <td>71</td>
            </tr>
        
            <tr>
                <td><code>17073</code></td>
                <td>72</td>
            </tr>
        
            <tr>
                <td><code>17074</code></td>
                <td>73</td>
            </tr>
        
            <tr>
                <td><code>17075</code></td>
                <td>74</td>
            </tr>
        
            <tr>
                <td><code>17076</code></td>
                <td>75</td>
            </tr>
        
            <tr>
                <td><code>17077</code></td>
                <td>76</td>
            </tr>
        
            <tr>
                <td><code>17078</code></td>
                <td>77</td>
            </tr>
        
            <tr>
                <td><code>17079</code></td>
                <td>78</td>
            </tr>
        
            <tr>
                <td><code>17080</code></td>
                <td>80</td>
            </tr>
        
            <tr>
                <td><code>17081</code></td>
                <td>09</td>
            </tr>
        
            <tr>
                <td><code>17090</code></td>
                <td>58</td>
            </tr>
        
            <tr>
                <td><code>17091</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17083</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17093</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17094</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17088</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17096</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17012</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17095</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17092</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17086</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17099</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17082</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17025</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17085</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17084</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17087</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17098</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>17089</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p11">11-13</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `69-70 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p69>`_)






------------

*********************
FILER_TYPES_CD
*********************

This lookup table describes filer types.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPES_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILTER_TYPE</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
        <tr>
            <td><code>FILER_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer type identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>DESCRIPTION</code></td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Description of the filer type</td>
        </tr>
    
    
    
        <tr>
            <td><code>GRP_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Group type assocated with the filer type</td>
        </tr>
    
    
    
        <tr>
            <td><code>CALC_USE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Use checkbox flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>GRACE_PERIOD</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``grp_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>58</code></td>
                <td>LOBBY PERIODS</td>
            </tr>
        
            <tr>
                <td><code>59</code></td>
                <td>CAMPAIGN PERIODS</td>
            </tr>
        
            <tr>
                <td><code>60</code></td>
                <td>DEFAULT PERIOD FOR ERRONEOUS DATA</td>
            </tr>
        
            <tr>
                <td><code>61</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p4">4</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `71-72 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p71>`_)






------------

*********************
FILER_XREF_CD
*********************

This table maps legacy filer identification numbers to the system's filer
identification numbers. Although 60 percent of the FILER_ID and XREF_ID values
are equal.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_XREF_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>XREF_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_ID</code></td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>MIGRATION_SOURCE</code></td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Source of the XREF_ID. Migration or generated by the AMS.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
FILING_PERIOD_CD
*********************

An undocumented table that contains metadata for a variety
of filing periods.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILING_PERIOD_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>PERIOD_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>PERIOD_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique period identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>START_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for period</td>
        </tr>
    
    
    
        <tr>
            <td><code>END_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date of period</td>
        </tr>
    
    
    
        <tr>
            <td><code>PERIOD_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>PER_GRP_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Period group type</td>
        </tr>
    
    
    
        <tr>
            <td><code>PERIOD_DESC</code></td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Period description</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEADLINE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Deadline date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``period_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>1500</code></td>
                <td>Standard period</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p3">3</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``per_grp_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>1500</code></td>
                <td>STANDARD PERIOD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p3">3</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `74-75 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p74>`_)






------------

*********************
GROUP_TYPES_CD
*********************

This lookup table stores group type information. Most (but not all) of the GRP_ID/
GRP_NAME value pairs in this table match the FILER_TYPE/DESCRIPTION value pairs in
the FILER_TYPE_CD table.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/GROUP_TYPES_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>GRP_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>GRP_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Group identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>GRP_NAME</code></td>
            <td>String (up to 28)</td>
            <td>No</td>
            <td>Group name. Many of the values in this column are empty strings.</td>
        </tr>
    
    
    
        <tr>
            <td><code>GRP_DESC</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Group Description. This column contains only empty strings.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
IMAGE_LINKS_CD
*********************

This table links images to filers and accounts.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/IMAGE_LINKS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>IMG_LINK_ID</code></td>
        
            <td><code>IMG_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>IMG_LINK_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image link identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>IMG_LINK_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of image link</td>
        </tr>
    
    
    
        <tr>
            <td><code>IMG_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>IMG_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of image</td>
        </tr>
    
    
    
        <tr>
            <td><code>IMG_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Image date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``img_link_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>6501</code></td>
                <td>FILING ID</td>
            </tr>
        
            <tr>
                <td><code>6502</code></td>
                <td>FILER ID</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p5">5</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``img_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>6001</code></td>
                <td>FAX</td>
            </tr>
        
            <tr>
                <td><code>6002</code></td>
                <td>PERSONAL PHOTO</td>
            </tr>
        
            <tr>
                <td><code>6004</code></td>
                <td>SCANNED CHECK</td>
            </tr>
        
            <tr>
                <td><code>6005</code></td>
                <td>SCANNED LETTER</td>
            </tr>
        
            <tr>
                <td><code>6007</code></td>
                <td>IMAGE TYPES</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p4">4</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `80 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p80>`_)






------------

*********************
LEGISLATIVE_SESSIONS_CD
*********************

Legislative session, begin and end dates look up table.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEGISLATIVE_SESSIONS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>SESSION_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>BEGIN_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session start date</td>
        </tr>
    
    
    
        <tr>
            <td><code>END_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session end date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOOKUP_CODES_CD
*********************

The description of some lookup codes in the system.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOOKUP_CODES_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>CODE_ID</code></td>
        
            <td><code>CODE_TYPE</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>CODE_TYPE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>CODE_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>The code&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CODE_DESC</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Code description</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
NAMES_CD
*********************

The name of all entities in the system. Used for searches when
the name has an identification number.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/NAMES_CD.TSV?footer=no&slice=0:10"></script>





Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>NAMID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number unique to the name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMF</code></td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMT</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMS</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>MONIKER</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td><code>MONIKER_POS</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Location of the entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMM</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Middle name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FULLNAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAML_SEARCH</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
RECEIVED_FILINGS_CD
*********************

This table is undocumented.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RECEIVED_FILINGS_CD.TSV?footer=no&slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-400">Form 400</a>:
                Statement of Organization (Slate Mailer Organization)
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-402">Form 402</a>:
                Statement of Termination (Slate Mailer Organization)
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-410">Form 410</a>:
                Statement of Organization Recipient Committee
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-425">Form 425</a>:
                Semi-Annual Statement of no Activity
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-461">Form 461</a>:
                Independent Expenditure Committee & Major Donor Committee Campaign Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-496">Form 496</a>:
                Late Independent Expenditure Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-497">Form 497</a>:
                Late Contribution Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-498">Form 498</a>:
                Slate Mailer Late Payment Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-601">Form 601</a>:
                Lobbying Firm Registration Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-602">Form 602</a>:
                Lobbying Firm Activity Authorization
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-603">Form 603</a>:
                Lobbyist Employer or Lobbying Coalition Registration Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-604">Form 604</a>:
                Lobbyist Certification Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-606">Form 606</a>:
                Notice of Termination
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-607">Form 607</a>:
                Notice of Withdrawal
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-615">Form 615</a>:
                Lobbyist Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-635">Form 635</a>:
                Report of Lobbyist Employer or Report of Lobbying Coalition
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-645">Form 645</a>:
                Report of Person Spending $5,000 or More
            </td>
        </tr>
        
        
    </tbody>
    </table>




Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_FILE_NAME</code></td>
            <td>String (up to 14)</td>
            <td>No</td>
            <td>The field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECEIVED_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_DIRECTORY</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_ID</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECEIVE_COMMENT</code></td>
            <td>String (up to 51)</td>
            <td>No</td>
            <td>A comment</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``form_id``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>F400</code></td>
                <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F401</code></td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F402</code></td>
                <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>F425</code></td>
                <td>Form 425: Semi-Annual Statement of no Activity</td>
            </tr>
        
            <tr>
                <td><code>F450</code></td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td><code>F460</code></td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F461</code></td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F465</code></td>
                <td>Form 465: Supplemental Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>F496</code></td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>F497</code></td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td><code>F498</code></td>
                <td>Form 498: Slate Mailer Late Payment Report</td>
            </tr>
        
            <tr>
                <td><code>F601</code></td>
                <td>Form 601: Lobbying Firm Registration Statement</td>
            </tr>
        
            <tr>
                <td><code>F602</code></td>
                <td>Form 602: Lobbying Firm Activity Authorization</td>
            </tr>
        
            <tr>
                <td><code>F603</code></td>
                <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
            </tr>
        
            <tr>
                <td><code>F604</code></td>
                <td>Form 604: Lobbyist Certification Statement</td>
            </tr>
        
            <tr>
                <td><code>F606</code></td>
                <td>Form 606: Notice of Termination</td>
            </tr>
        
            <tr>
                <td><code>F607</code></td>
                <td>Form 607: Notice of Withdrawal</td>
            </tr>
        
            <tr>
                <td><code>F615</code></td>
                <td>Form 615: Lobbyist Report</td>
            </tr>
        
            <tr>
                <td><code>F625</code></td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>F635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>F645</code></td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Overview (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview.html#document/p4">4-8</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`13 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p13>`_, `121 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p121>`_)






------------

*********************
REPORTS_CD
*********************

This is an undocumented model.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/REPORTS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>RPT_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>RPT_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_NAME</code></td>
            <td>String (up to 74)</td>
            <td>No</td>
            <td>Name of the report</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DESC_</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Description of the report</td>
        </tr>
    
    
    
        <tr>
            <td><code>PATH</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Report path</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATA_OBJECT</code></td>
            <td>String (up to 38)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARMS_FLG_Y_N</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameters indication flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of the report</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARM_DEFINITION</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameter definition</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``rpt_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>401</code></td>
                <td>PUBLIC REPORTS</td>
            </tr>
        
            <tr>
                <td><code>402</code></td>
                <td>AUDITS</td>
            </tr>
        
            <tr>
                <td><code>403</code></td>
                <td>FINANCIAL REPORTS</td>
            </tr>
        
            <tr>
                <td><code>404</code></td>
                <td>AUDITS</td>
            </tr>
        
            <tr>
                <td><code>405</code></td>
                <td>MAILING LABELS</td>
            </tr>
        
            <tr>
                <td><code>406</code></td>
                <td>OTHER REPORTS</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`13 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p13>`_, `122 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p122>`_)






------------

*********************
FILER_TYPE_PERIODS_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "J M needs
to document. This is in his list of tables designed for future enhancements."


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPE_PERIODS_CD.TSV?footer=no&slice=0:10"></script>




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>ELECTION_TYPE</code></td>
        
            <td><code>FILER_TYPE</code></td>
        
            <td><code>PERIOD_ID</code></td>
        
        </tr>
    </tbody>
    </table>


Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
    
    
    
        <tr>
            <td><code>ELECTION_TYPE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_TYPE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td><code>PERIOD_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilingPeriodCd.period_id</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``election_type``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        
            <tr>
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>3001</code></td>
                <td>GENERAL</td>
            </tr>
        
            <tr>
                <td><code>3002</code></td>
                <td>PRIMARY</td>
            </tr>
        
            <tr>
                <td><code>3003</code></td>
                <td>RECALL</td>
            </tr>
        
            <tr>
                <td><code>3004</code></td>
                <td>SPECIAL ELECTION</td>
            </tr>
        
            <tr>
                <td><code>3005</code></td>
                <td>OFFICEHOLDER</td>
            </tr>
        
            <tr>
                <td><code>3006</code></td>
                <td>SPECIAL RUNOFF</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p3">3-4</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `71 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p71>`_)





