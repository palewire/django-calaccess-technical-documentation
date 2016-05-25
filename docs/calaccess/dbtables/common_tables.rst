.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the common_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Common tables
================================


The CAL-ACCESS database contains 9 tables that, according to the official documentation (see `here <https://www.documentcloud.org/documents/2711617-ReadMe-Zip/pages/1.html>`_ and `here <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/5.html>`_), store information common to campaign finance and lobbyist disclosure filings.



------------

*********************
FILERNAME_CD
*********************

A combination of CAL-ACCESS tables to provide the analyst with
filer information.

Full name of all PACs, firms, and employers are in the last
name field.

Major donors can be split between first and last name fields, but usually
are contained in the last name field only. Individual names of lobbyists,
candidates/officeholders, treasurers/responsible officers, and major donors
(when they are only an individual's name) use both the first and last name
fields in conjunction.

**Sample:** `FILERNAME_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILERNAME_CD.TSV>`_




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>NAMID</code></td>
        
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
            <td><code>XREF_FILER_ID</code></td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_TYPE</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>The type of filer. These values are found FILER_TYPES_CD.DESCRIPTION</td>
        </tr>
    
    
    
        <tr>
            <td><code>STATUS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The status of the filer. Includes a mixture of values found in the STATUS_TYPE and STATUS_DESC columns on FILER_STATUS_TYPES_CD</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for status</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name, sometimes full name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMF</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMT</code></td>
            <td>String (up to 70)</td>
            <td>No</td>
            <td>Name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>NAMS</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADR1</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>First line of street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADR2</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Second line of street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>CITY</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>City address</td>
        </tr>
    
    
    
        <tr>
            <td><code>ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>State</td>
        </tr>
    
    
    
        <tr>
            <td><code>ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>PHON</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FAX</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``filer_type``
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
                <td><code>NOT DEFINED</code></td>
                <td>Undefined</td>
            </tr>
        
            <tr>
                <td><code>ALL FILERS</code></td>
                <td>All filers</td>
            </tr>
        
            <tr>
                <td><code>CANDIDATE/OFFICEHOLDER</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>CLIENT</code></td>
                <td>Client</td>
            </tr>
        
            <tr>
                <td><code>EMPLOYER</code></td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td><code>FIRM</code></td>
                <td>Firm</td>
            </tr>
        
            <tr>
                <td><code>INDIVIDUAL</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>INITIATIVE</code></td>
                <td>Initiative</td>
            </tr>
        
            <tr>
                <td><code>LOBBYIST</code></td>
                <td>Lobbyist</td>
            </tr>
        
            <tr>
                <td><code>MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE</code></td>
                <td>Major donor or indenpendent expenditure committee</td>
            </tr>
        
            <tr>
                <td><code>PAYMENT TO INFLUENCE</code></td>
                <td>Payment to influence</td>
            </tr>
        
            <tr>
                <td><code>PREPAID ACCOUNT</code></td>
                <td>Prepaid account</td>
            </tr>
        
            <tr>
                <td><code>PROPONENT</code></td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td><code>PROPOSITION</code></td>
                <td>Proposition</td>
            </tr>
        
            <tr>
                <td><code>RECIPIENT COMMITTEE</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>SLATE MAILER ORGANIZATIONS</code></td>
                <td>Slate mailer organization</td>
            </tr>
        
            <tr>
                <td><code>TREASURER/RESPONSIBLE OFFICER</code></td>
                <td>Treasurer/responsible officer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Filer-Types-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774536-Filer-Types-Cd.html#document/p1">1</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``status``
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
                <td><code></code></td>
                <td>Undefined</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td><code>P</code></td>
                <td>PENDING</td>
            </tr>
        
            <tr>
                <td><code>R</code></td>
                <td>REVOKED</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SUSPENDED</td>
            </tr>
        
            <tr>
                <td><code>W</code></td>
                <td>WITHDRAWN</td>
            </tr>
        
            <tr>
                <td><code>Y</code></td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>INACTIVE</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>TERMINATED</td>
            </tr>
        
            <tr>
                <td><code>ACTIVE</code></td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td><code>INACTIVE</code></td>
                <td>INACTIVE</td>
            </tr>
        
            <tr>
                <td><code>TERMINATED</code></td>
                <td>TERMINATED</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Filer-Status-Types-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774537-Filer-Status-Types-Cd.html#document/p1">1</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* FAQ (`2 <https://www.documentcloud.org/documents/2711615-FAQ.html#document/p2>`_)

* CAL-ACCESS Tables, Columns and Indexes (`9 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p9>`_, `67-68 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p67>`_)






------------

*********************
FILER_FILINGS_CD
*********************

Key table that links filers to their paper, key data entry, legacy,
and electronic filings. This table is used as an index to locate
filing information.

**Sample:** `FILER_FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_FILINGS_CD.TSV>`_


Filing forms
============



* `Electronic Form 530 <../filingforms/campaign_forms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)



* `Form 400 <../filingforms/campaign_forms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <../filingforms/campaign_forms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 405 <../filingforms/campaign_forms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



* `Form 410 <../filingforms/campaign_forms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 415 <../filingforms/deprecated_forms.html#form-415>`_ (Title Unknown)



* `Form 416 <../filingforms/deprecated_forms.html#form-416>`_ (Title Unknown)



* `Form 419 <../filingforms/deprecated_forms.html#form-419>`_ (Ballot Measure Committee Campaign Statement-Long Form)



* `Form 420 <../filingforms/deprecated_forms.html#form-420>`_ (Recipient Committee Campaign Statement-Long Form)



* `Form 425 <../filingforms/campaign_forms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 430 <../filingforms/deprecated_forms.html#form-430>`_ (Title Unknown)



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 470 <../filingforms/campaign_forms.html#form-470>`_ (Officeholder and Candidate Campaign Statement, Short Form)



* `Form 490 <../filingforms/deprecated_forms.html#form-490>`_ (Officeholder/Candidate Campaign Statement-Long Form)



* `Form 495 <../filingforms/campaign_forms.html#form-495>`_ (Supplemental Pre-Election Campaign Statement)



* `Form 496 <../filingforms/campaign_forms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <../filingforms/campaign_forms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <../filingforms/campaign_forms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 501 <../filingforms/campaign_forms.html#form-501>`_ (Candidate Intention Statement)



* `Form 502 <../filingforms/campaign_forms.html#form-502>`_ (Campaign Bank Account Statement)



* `Form 511 <../filingforms/campaign_forms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <../filingforms/lobbyist_forms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <../filingforms/lobbyist_forms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <../filingforms/lobbyist_forms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 605 <../filingforms/lobbyist_forms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <../filingforms/lobbyist_forms.html#form-606>`_ (Notice of Termination)



* `Form 607 <../filingforms/lobbyist_forms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Form 690 <../filingforms/lobbyist_forms.html#form-690>`_ (Amendment to Lobbying Disclosure Report)



* `Form 700 <../filingforms/financial disclosure_forms.html#form-700>`_ (Statement of Economic Interest)



* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 630 <../filingforms/lobbyist_forms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <../filingforms/lobbyist_forms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <../filingforms/lobbyist_forms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))





Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>FORM_ID</code></td>
        
            <td><code>FILING_SEQUENCE</code></td>
        
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>PERIOD_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the period when the filing was recieved.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_ID</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_SEQUENCE</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment number where 0 is an original filing and 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the filing entered into the system</td>
        </tr>
    
    
    
        <tr>
            <td><code>STMNT_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td><code>STMNT_STATUS</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>The status of the statement. If the filing has been reviewed or not reviewed.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>USER_ID</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>User identifier of the PRD user who logged the filing</td>
        </tr>
    
    
    
        <tr>
            <td><code>SPECIAL_AUDIT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Denotes whether the filing has been audited for money laundering or other special condition.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FINE_AUDIT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates whether a filing has been audited for a fine</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_START</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_END</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date filing received</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>F405</code></td>
                <td>Form 405: Amendment to Campaign Disclosure Statement</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>F415</code></td>
                <td>Form 415: Title Unknown</td>
            </tr>
        
            <tr>
                <td><code>F416</code></td>
                <td>Form 416: Title Unknown</td>
            </tr>
        
            <tr>
                <td><code>F419</code></td>
                <td>Form 419: Ballot Measure Committee Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td><code>F420</code></td>
                <td>Form 420: Recipient Committee Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td><code>F425</code></td>
                <td>Form 425: Semi-Annual Statement of no Activity</td>
            </tr>
        
            <tr>
                <td><code>F430</code></td>
                <td>Form 430: Title Unknown</td>
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
                <td><code>F470</code></td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
            <tr>
                <td><code>F490</code></td>
                <td>Form 490: Officeholder/Candidate Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td><code>F495</code></td>
                <td>Form 495: Supplemental Pre-Election Campaign Statement</td>
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
                <td><code>F501</code></td>
                <td>Form 501: Candidate Intention Statement</td>
            </tr>
        
            <tr>
                <td><code>F502</code></td>
                <td>Form 502: Campaign Bank Account Statement</td>
            </tr>
        
            <tr>
                <td><code>F511</code></td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td><code>E530</code></td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
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
                <td><code>F605</code></td>
                <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
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
                <td><code>S630</code></td>
                <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
            </tr>
        
            <tr>
                <td><code>F635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>S635-C</code></td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td><code>S640</code></td>
                <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
            </tr>
        
            <tr>
                <td><code>F645</code></td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
            <tr>
                <td><code>F690</code></td>
                <td>Form 690: Amendment to Lobbying Disclosure Report</td>
            </tr>
        
            <tr>
                <td><code>F700</code></td>
                <td>Form 700: Statement of Economic Interest</td>
            </tr>
        
            <tr>
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td><code>F111</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F410 AT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F410ATR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F421</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F440</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F470S</code></td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
            <tr>
                <td><code>F480</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F500</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F501502</code></td>
                <td>Forms 501 and/or 502 (Candidate Intention and/or Bank Account Statements)</td>
            </tr>
        
            <tr>
                <td><code>F555</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F666</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F777</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F888</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F999</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p65">65</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``stmnt_type``
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
                <td><code>10001</code></td>
                <td>ORIGINAL/INITIAL</td>
            </tr>
        
            <tr>
                <td><code>10002</code></td>
                <td>AMENDMENT</td>
            </tr>
        
            <tr>
                <td><code>10003</code></td>
                <td>TERMINATION</td>
            </tr>
        
            <tr>
                <td><code>10004</code></td>
                <td>REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE</td>
            </tr>
        
            <tr>
                <td><code>10005</code></td>
                <td>LOG</td>
            </tr>
        
            <tr>
                <td><code>10006</code></td>
                <td>LOG/AMENDMENT</td>
            </tr>
        
            <tr>
                <td><code>10007</code></td>
                <td>AS FILED BY COMMITTEE</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p6">6</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``stmnt_status``
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
                <td><code>11001</code></td>
                <td>COMPLETE</td>
            </tr>
        
            <tr>
                <td><code>11002</code></td>
                <td>INCOMPLETE</td>
            </tr>
        
            <tr>
                <td><code>11003</code></td>
                <td>NEEDS REVIEW</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p6">6</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``filing_type``
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
                <td><code>22001</code></td>
                <td>Electronic</td>
            </tr>
        
            <tr>
                <td><code>22006</code></td>
                <td>Cal Online</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 FAQ (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `64-66 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p64>`_)






------------

*********************
FILINGS_CD
*********************

This table is the parent table from which all links and association to
a filing are derived.

**Sample:** `FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILINGS_CD.TSV>`_




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``filing_type``
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
                <td><code>22001</code></td>
                <td>Electronic</td>
            </tr>
        
            <tr>
                <td><code>22002</code></td>
                <td>Key data entry</td>
            </tr>
        
            <tr>
                <td><code>22003</code></td>
                <td>Historical lobby</td>
            </tr>
        
            <tr>
                <td><code>22004</code></td>
                <td>Historical campaign</td>
            </tr>
        
            <tr>
                <td><code>22005</code></td>
                <td>AMS</td>
            </tr>
        
            <tr>
                <td><code>22006</code></td>
                <td>Cal Online</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 FAQ (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`75-75 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p75>`_)






------------

*********************
HDR_CD
*********************

Electronic filing record header data. Contains information
identifying vendor and Cal Format version.

**Sample:** `HDR_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HDR_CD.TSV>`_




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAL_VER</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>CAL Version number the filing was made using</td>
        </tr>
    
    
    
        <tr>
            <td><code>EF_TYPE</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Electronic filing type. This will always have the         value of &quot;CAL&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>HDRCOMMENT</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Typically used for development and test filings</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type. Value: HDR</td>
        </tr>
    
    
    
        <tr>
            <td><code>SOFT_NAME</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Filing software name used to electronically file</td>
        </tr>
    
    
    
        <tr>
            <td><code>SOFT_VER</code></td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filing software version number</td>
        </tr>
    
    
    
        <tr>
            <td><code>STATE_CD</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>The state code value entered in the electronic filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``ef_type``
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
                <td><code>CAL</code></td>
                <td>.CAL format</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p4">4</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p5">5</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``rec_type``
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
                <td><code>HDR</code></td>
                <td>HDR</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p4">4</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p5">5</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``state_cd``
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
                <td><code>CA</code></td>
                <td>California</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p4">4</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p5">5</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`5 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p5>`_)

* Map from .CAL Format to Database Table and Fields (`1 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p1>`_, `51 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p51>`_)

* .CAL Format Layout (Version 1.05.02) (`4 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p4>`_)

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `79 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p79>`_)






------------

*********************
HEADER_CD
*********************

Lookup table used to report Form 460 information in the Agency Management System.

**Sample:** `HEADER_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HEADER_CD.TSV>`_




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>LINE_NUMBER</code></td>
        
            <td><code>FORM_ID</code></td>
        
            <td><code>REC_TYPE</code></td>
        
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
            <td><code>LINE_NUMBER</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_ID</code></td>
            <td>String (up to 5)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td><code>SECTION_LABEL</code></td>
            <td>String (up to 58)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>COMMENTS1</code></td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>COMMENTS2</code></td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>LABEL</code></td>
            <td>String (up to 98)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>COLUMN_A</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>COLUMN_B</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>COLUMN_C</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>SHOW_C</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>SHOW_B</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>AF490</code></td>
                <td>Form 490, Part A</td>
            </tr>
        
            <tr>
                <td><code>AP1</code></td>
                <td>Allocation Part 1</td>
            </tr>
        
            <tr>
                <td><code>AP2</code></td>
                <td>Allocation Part 2</td>
            </tr>
        
            <tr>
                <td><code>BF490</code></td>
                <td>Form 490, Part B</td>
            </tr>
        
            <tr>
                <td><code>CF490</code></td>
                <td>Form 490, Part C</td>
            </tr>
        
            <tr>
                <td><code>DF490</code></td>
                <td>Form 490, Part D</td>
            </tr>
        
            <tr>
                <td><code>EF490</code></td>
                <td>Form 490, Part E</td>
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
                <td><code>FF490</code></td>
                <td>Form 490, Part F</td>
            </tr>
        
            <tr>
                <td><code>HF490</code></td>
                <td>Form 490, Part H</td>
            </tr>
        
            <tr>
                <td><code>IF490</code></td>
                <td>Form 490, Part I</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>


``rec_type``
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
                <td><code>AP1</code></td>
                <td>AP1</td>
            </tr>
        
            <tr>
                <td><code>AP2</code></td>
                <td>AP2</td>
            </tr>
        
            <tr>
                <td><code>SMRY_HEADER</code></td>
                <td>SMRY_HEADER</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `79-80 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p79>`_)






------------

*********************
SMRY_CD
*********************

Summary totals from filings.

**Sample:** `SMRY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SMRY_CD.TSV>`_


Filing forms
============



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)

    * Schedule A, Payments Received

    * Schedule B, Payments Made

    * Schedule B-1, Payments Made by Agent or Independent Contractor




* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule B - Part 3, Outstanding Bal

    * Schedule C, Non-Monetary Contributions Received

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule E, Payments Made

    * Schedule F, Accrued Expenses (Unpaid Bills)

    * Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)

    * Schedule H, Loans Made to Others

    * Schedule H - Part 1, Loans Made

    * Schedule H- Part 2, Repayments Rcvd

    * Schedule H - Part 3, Outstanding Loans

    * Schedule I, miscellanous increases to cash




* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)

    * Part 2, Payments Received in Connection with Lobbying Activity

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission




* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More)

    * Part 2 (Payments Made this Period), Section A: Activity Expenses

    * Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action

    * Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission




* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 640 <../filingforms/lobbyist_forms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))





Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
            <td><code>LINE_ITEM</code></td>
        
            <td><code>REC_TYPE</code></td>
        
            <td><code>FORM_TYPE</code></td>
        
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: SMRY</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT_A</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column A</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT_B</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column B</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT_C</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column C</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Election date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``rec_type``
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
                <td><code>SMRY</code></td>
                <td>SMRY</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p27">27</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p59">59</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35">35</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p72">72</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


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
                <td><code>F401</code></td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F401A</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td><code>F401B</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F401B-1</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
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
                <td><code>A</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>B1</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
            </tr>
        
            <tr>
                <td><code>B2</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
            </tr>
        
            <tr>
                <td><code>B3</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 3, Outstanding Bal</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>D</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
            </tr>
        
            <tr>
                <td><code>E</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule E, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
            </tr>
        
            <tr>
                <td><code>H1</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 1, Loans Made</td>
            </tr>
        
            <tr>
                <td><code>H2</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H- Part 2, Repayments Rcvd</td>
            </tr>
        
            <tr>
                <td><code>H3</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 3, Outstanding Loans</td>
            </tr>
        
            <tr>
                <td><code>I</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
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
                <td><code>F625</code></td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>F625P2</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td><code>F625P3A</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F625P3B</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>F635P3A</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists</td>
            </tr>
        
            <tr>
                <td><code>F635P3B</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
            </tr>
        
            <tr>
                <td><code>F635P3C</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F635P3D</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action</td>
            </tr>
        
            <tr>
                <td><code>F635P3E</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission</td>
            </tr>
        
            <tr>
                <td><code>S640</code></td>
                <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
            </tr>
        
            <tr>
                <td><code>F645</code></td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
            <tr>
                <td><code>F645P2A</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F645P2B</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action</td>
            </tr>
        
            <tr>
                <td><code>F645P2C</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission</td>
            </tr>
        
            <tr>
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td><code>401A</code></td>
                <td>A</td>
            </tr>
        
            <tr>
                <td><code>401B</code></td>
                <td>B</td>
            </tr>
        
            <tr>
                <td><code>401B-1</code></td>
                <td>B-1</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p27">27-28</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p59">59-60</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p36">36-37</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p73">73-74</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p86">86</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 1.05.02) (`27-28 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p27>`_, `59-60 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p59>`_)

* .CAL Format Layout (Version 2.01) (`35-37 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35>`_, `72-74 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p72>`_)

* CAL-ACCESS Tables, Columns and Indexes (`131-132 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p131>`_)

* Map from .CAL Format to Database Table and Fields (`86-87 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p86>`_)






------------

*********************
CVR_E530_CD
*********************

Probably Cover Pages for Electronic Form 530. This table is listed in the record
layouts, but neither table nor any of its columns are labeled.

**Sample:** `CVR_E530_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_E530_CD.TSV>`_


Filing forms
============



* `Electronic Form 530 <../filingforms/campaign_forms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)





Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMF</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMS</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_CITY</code></td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filer city</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer state</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OCCUPATION</code></td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER</code></td>
            <td>String (up to 13)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 46)</td>
            <td>No</td>
            <td>Candidate last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 21)</td>
            <td>No</td>
            <td>Candidate first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>DISTRICT_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>District Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>PMNT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>PMNT_AMOUNT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_LITERATURE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_PRINTADS</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_RADIO</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_TV</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_IT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_BILLBOARDS</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>TYPE_OTHER</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_DESC</code></td>
            <td>String (up to 49)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``rec_type``
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
                <td><code>CVR</code></td>
                <td>CVR</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>


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
                <td><code>E530</code></td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>


``entity_cd``
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
                <td><code>ATH</code></td>
                <td>Authorizing individual</td>
            </tr>
        
            <tr>
                <td><code>ATR</code></td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td><code>BMC</code></td>
                <td>Ballot measure committee</td>
            </tr>
        
            <tr>
                <td><code>BNM</code></td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>CTL</code></td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>MDI</code></td>
                <td>Major Donor/Ind Expenditure</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>POF</code></td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td><code>PTY</code></td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>SCC</code></td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td><code>SMO</code></td>
                <td>Slate-mailer organization</td>
            </tr>
        
            <tr>
                <td><code>SPO</code></td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>Treasurer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>)
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


``office_cd``
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
                <td><code>30001</code></td>
                <td>PRESIDENT</td>
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



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`29-30 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p29>`_)






------------

*********************
SPLT_CD
*********************

Split Transaction Record - Used as a child record for schedules:
A, B1, B2, C, D, H and/or F450P5 when disclosing Per Election to Date information.

**Sample:** `SPLT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SPLT_CD.TSV>`_


Filing forms
============



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule C, Non-Monetary Contributions Received

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule H, Loans Made to Others






Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
            <td><code>LINE_ITEM</code></td>
        
            <td><code>PFORM_TYPE</code></td>
        
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Per Election to Date Amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_CODE</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Per Election to Date Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Election</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>PFORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Parent Schedule Type</td>
        </tr>
    
    
    
        <tr>
            <td><code>PTRAN_ID</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Parent transaction ID</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``elec_code``
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
                <td><code>P</code></td>
                <td>Primary</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>General</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Special</td>
            </tr>
        
            <tr>
                <td><code>R</code></td>
                <td>Runoff</td>
            </tr>
        
            <tr>
                <td><code>g</code></td>
                <td>General</td>
            </tr>
        
            <tr>
                <td><code>p</code></td>
                <td>primary</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>D</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>M</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>1</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>2</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``pform_type``
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
                <td><code>A</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>B1</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
            </tr>
        
            <tr>
                <td><code>B2</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>D</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
            </tr>
        
            <tr>
                <td><code>F450P5</code></td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`18 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p18>`_)

* Map from .CAL Format to Database Table and Fields (`88 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p88>`_)

* CAL-ACCESS Tables, Columns and Indexes (`132 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p132>`_)






------------

*********************
TEXT_MEMO_CD
*********************

Text memos attached to electronic filings

**Sample:** `TEXT_MEMO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/TEXT_MEMO_CD.TSV>`_


Filing forms
============



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 405 <../filingforms/campaign_forms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



* `Form 410 <../filingforms/campaign_forms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <../filingforms/campaign_forms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <../filingforms/campaign_forms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <../filingforms/campaign_forms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <../filingforms/campaign_forms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <../filingforms/lobbyist_forms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <../filingforms/lobbyist_forms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <../filingforms/lobbyist_forms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 605 <../filingforms/lobbyist_forms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <../filingforms/lobbyist_forms.html#form-606>`_ (Notice of Termination)



* `Form 607 <../filingforms/lobbyist_forms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Schedule 630 <../filingforms/lobbyist_forms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <../filingforms/lobbyist_forms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <../filingforms/lobbyist_forms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))





Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
            <td><code>LINE_ITEM</code></td>
        
            <td><code>REC_TYPE</code></td>
        
            <td><code>FORM_TYPE</code></td>
        
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: TEXT</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>REF_NO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Links text memo to a specific record</td>
        </tr>
    
    
    
        <tr>
            <td><code>TEXT4000</code></td>
            <td>String (up to 4000)</td>
            <td>No</td>
            <td>Contents of the text memo</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``rec_type``
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
                <td><code>TEXT</code></td>
                <td>TEXT</td>
            </tr>
        
            <tr>
                <td><code>MEMO</code></td>
                <td>MEMO</td>
            </tr>
        
            <tr>
                <td><code>trun</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Unde</code></td>
                <td>Under</td>
            </tr>
        
            <tr>
                <td><code>am</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>sele</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Term</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>re</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>i</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p13">13</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p16">16</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


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
                <td><code>F401</code></td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>F405</code></td>
                <td>Form 405: Amendment to Campaign Disclosure Statement</td>
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
                <td><code>F605</code></td>
                <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
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
                <td><code>S630</code></td>
                <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
            </tr>
        
            <tr>
                <td><code>S635-C</code></td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td><code>S640</code></td>
                <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
            </tr>
        
            <tr>
                <td><code>410</code></td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>460</code></td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>461</code></td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>465</code></td>
                <td>Form 465: Supplemental Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>496</code></td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td><code>497</code></td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td><code>497P1</code></td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td><code>497P2</code></td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
            <tr>
                <td><code>F401A</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td><code>F401B</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F401B-1</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
            </tr>
        
            <tr>
                <td><code>F450P5</code></td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F461P1</code></td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 1, Name and Address of Filer</td>
            </tr>
        
            <tr>
                <td><code>F461P2</code></td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 2, Nature and Interests of Filer</td>
            </tr>
        
            <tr>
                <td><code>F461P5</code></td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made</td>
            </tr>
        
            <tr>
                <td><code>F465P3</code></td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made</td>
            </tr>
        
            <tr>
                <td><code>F496P3</code></td>
                <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
            </tr>
        
            <tr>
                <td><code>F497P1</code></td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td><code>F497P2</code></td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
            <tr>
                <td><code>F498-A</code></td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
            </tr>
        
            <tr>
                <td><code>F498-R</code></td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
            </tr>
        
            <tr>
                <td><code>F601P2A</code></td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
            </tr>
        
            <tr>
                <td><code>F601P2B</code></td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section B: Subcontracted Clients</td>
            </tr>
        
            <tr>
                <td><code>F615P1</code></td>
                <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
            </tr>
        
            <tr>
                <td><code>F615P2</code></td>
                <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
            </tr>
        
            <tr>
                <td><code>F625P2</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td><code>F625P3A</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F625P3B</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F625P4B</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td><code>S635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>F635P3B</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
            </tr>
        
            <tr>
                <td><code>F635P3C</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F635P4B</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td><code>F645P2A</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F645P3B</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td><code>S497</code></td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td><code>S635C</code></td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td><code>A4</code></td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td><code>A6</code></td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td><code>B</code></td>
                <td>Schedule B of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td><code>B1</code></td>
                <td>Schedule B, Part 1 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td><code>B2</code></td>
                <td>Schedule B, Part 2 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td><code>B3</code></td>
                <td>Schedule B, Part 3 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Schedule C of any form (e.g., Forms 401 or F460)</td>
            </tr>
        
            <tr>
                <td><code>COMMENTS</code></td>
                <td>Possibly comments by FPPC for any form?</td>
            </tr>
        
            <tr>
                <td><code>CVR</code></td>
                <td>Cover page for any form (e.g., Forms 460, 461 or 497)</td>
            </tr>
        
            <tr>
                <td><code>D</code></td>
                <td>Schedule D of any form (e.g., Forms 401, 460 or 461)</td>
            </tr>
        
            <tr>
                <td><code>DEBTF</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
            <tr>
                <td><code>E</code></td>
                <td>Schedule E of any form (e.g., Forms 460, 461 or 465)</td>
            </tr>
        
            <tr>
                <td><code>EXPNT</code></td>
                <td>Expenditures outlined on any form (e.g. Form 460)</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Schedule F of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>Schedule G of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Schedule H of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>H1</code></td>
                <td>Schedule H, Part 1 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>H2</code></td>
                <td>Schedule H2, Part 2 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>H3</code></td>
                <td>Schedule H3, Part 3 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>I</code></td>
                <td>Schedule I of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>PT5</code></td>
                <td>Part 5 of any form (e.g., Form 461</td>
            </tr>
        
            <tr>
                <td><code>RCPTB1</code></td>
                <td>Schedule B, Part 1 of any form (e.g., Form 460</td>
            </tr>
        
            <tr>
                <td><code>RCPTC</code></td>
                <td>Schedule C of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>RCPTI</code></td>
                <td>Schedule I of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>SCH A</code></td>
                <td>Schedule A of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>SF</code></td>
                <td>Schedule F of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>SPLT</code></td>
                <td>A memo that applies to multiple items?</td>
            </tr>
        
            <tr>
                <td><code>SMRY</code></td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>SUM</code></td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td><code>SUMMARY</code></td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p13">13</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p16">16</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p90">90</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 1.05.02) (`13 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p13>`_)

* .CAL Format Layout (Version 2.01) (`15-16 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p15>`_)

* CAL-ACCESS Tables, Columns and Indexes (`14 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p14>`_, `133-134 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p133>`_)

* Map from .CAL Format to Database Table and Fields (`89-90 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p89>`_)





