Other tables
================================


The CAL-ACCESS database contains 23 tables not categorized anywhere in the `official documentation <calaccess/officialdocumentation.html>`_ as being specific to campaign finance filings, specific to lobbyist disclosure or common to both domains. These tables are outlined below.



------------

AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Contains acronyms and their meaning.

**Sample:** `ACRONYMS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p16-thumbnail.gif'></a><p>p. 16</p></div></div>





Fields
^^^^^^

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
            <td>acronym</td>
            <td>String (up to 40)</td>
            <td>Yes</td>
            <td>Acronym text value</td>
        </tr>
    
    
    
        <tr>
            <td>stands_for</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Definition of the acronym</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for the acronym</td>
        </tr>
    
    
    
        <tr>
            <td>a_desc</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Description of the acronym</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

AddressCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table holds all addresses for the system. This table can be used
for address-based searches and formes the bases for address information
desplayed by the AMS.

**Sample:** `ADDRESS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ADDRESS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p16-thumbnail.gif'></a><p>p. 16</p></div></div>





Fields
^^^^^^

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
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address indentification number</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address city</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address state</td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address email</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

BallotMeasuresCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Ballot measure dates and times

**Sample:** `BALLOT_MEASURES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/BALLOT_MEASURES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p19-thumbnail.gif'></a><p>p. 19</p></div></div>





Fields
^^^^^^

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
            <td>election_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ballot measure election date</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>measure_no</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td>measure_name</td>
            <td>String (up to 163)</td>
            <td>No</td>
            <td>Ballot measure full name</td>
        </tr>
    
    
    
        <tr>
            <td>measure_short_name</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Ballot measure short name</td>
        </tr>
    
    
    
        <tr>
            <td>jurisdiction</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

EfsFilingLogCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Electronic Filing Subsystem Log. The EFS accepts and validates electronic filings.

**Sample:** `EFS_FILING_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EFS_FILING_LOG_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*Overview*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/1.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p1-thumbnail.gif'></a><p>p. 1</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p49-thumbnail.gif'></a><p>p. 49</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p50-thumbnail.gif'></a><p>p. 50</p></div></div>




Filing Forms
^^^^^^^^^^^^
EfsFilingLogCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
            <td>filing_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Date of filing</td>
        </tr>
    
    
    
        <tr>
            <td>filingstatus</td>
            <td>Integer</td>
            <td>No</td>
            <td>Status of filing. This field is described in the docs as beingVARCHAR. However, its distinct values are 0, 1, 2 and 7.</td>
        </tr>
    
    
    
        <tr>
            <td>vendor</td>
            <td>String (up to 250)</td>
            <td>Yes</td>
            <td>Software vendor who submitted the electronic filing</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>error_no</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Most records have a value of &quot;ACCEPTED&quot;. Other records include &quot;ERROR&quot;or &quot;BADFORMAT&quot; and a three-digit number.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


*Overview*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p4-thumbnail.gif'></a><p>p. 4</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p5-thumbnail.gif'></a><p>p. 5</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p6-thumbnail.gif'></a><p>p. 6</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p8-thumbnail.gif'></a><p>p. 8</p></div></div>




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
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
        <tr>
            <td>BADFORMAT 253</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>form</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links acronyms to filers

**Sample:** `FILER_ACRONYMS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ACRONYMS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p61-thumbnail.gif'></a><p>p. 61</p></div></div>





Fields
^^^^^^

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
            <td>acronym</td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>AMS acronym</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links filers and addresses. This table maintains a history of when
addresses change.

**Sample:** `FILER_ADDRESS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ADDRESS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p61-thumbnail.gif'></a><p>p. 61</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p62-thumbnail.gif'></a><p>p. 62</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address identification number</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Address effective date</td>
        </tr>
    
    
    
        <tr>
            <td>add_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Address type</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*add_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p5-thumbnail.gif'></a><p>p. 5</p></div></div>




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
            <td>51</td>
            <td>PERMANENT</td>
        </tr>
    
        <tr>
            <td>7026</td>
            <td>BUSINESS</td>
        </tr>
    
        <tr>
            <td>7027</td>
            <td>HOME</td>
        </tr>
    
        <tr>
            <td>7050</td>
            <td>NOT IN USE</td>
        </tr>
    
        <tr>
            <td>7051</td>
            <td>PERMANENT</td>
        </tr>
    
        <tr>
            <td>7082</td>
            <td>MAILING ADDRESS</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores lobbyist ethics training dates.

**Sample:** `FILER_ETHICS_CLASS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ETHICS_CLASS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p64-thumbnail.gif'></a><p>p. 64</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ethics_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Date ethics training was accomplished</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links a filer to their interest codes.

**Sample:** `FILER_INTERESTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_INTERESTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p66-thumbnail.gif'></a><p>p. 66</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Interest code linked to the filer</td>
        </tr>
    
    
    
        <tr>
            <td>effect_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*interest_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40301</td>
            <td>AGRICULTURE</td>
        </tr>
    
        <tr>
            <td>40302</td>
            <td>EDUCATION</td>
        </tr>
    
        <tr>
            <td>40303</td>
            <td>ENTERTAINMENT/RECREATION</td>
        </tr>
    
        <tr>
            <td>40304</td>
            <td>FINANCE/INSURANCE</td>
        </tr>
    
        <tr>
            <td>40305</td>
            <td>GOVERNMENT</td>
        </tr>
    
        <tr>
            <td>40306</td>
            <td>HEALTH</td>
        </tr>
    
        <tr>
            <td>40307</td>
            <td>LABOR UNIONS</td>
        </tr>
    
        <tr>
            <td>40308</td>
            <td>LEGAL</td>
        </tr>
    
        <tr>
            <td>40309</td>
            <td>LODGING/RESTAURANTS</td>
        </tr>
    
        <tr>
            <td>40310</td>
            <td>MANUFACTURING/INDUSTRIAL</td>
        </tr>
    
        <tr>
            <td>40311</td>
            <td>MERCHANDISE/RETAIL</td>
        </tr>
    
        <tr>
            <td>40312</td>
            <td>MISCELLANEOUS</td>
        </tr>
    
        <tr>
            <td>40313</td>
            <td>OIL AND GAS</td>
        </tr>
    
        <tr>
            <td>40314</td>
            <td>POLITICAL ORGANIZATIONS</td>
        </tr>
    
        <tr>
            <td>40315</td>
            <td>PROFESSIONAL/TRADE</td>
        </tr>
    
        <tr>
            <td>40316</td>
            <td>PUBLIC EMPLOYEES</td>
        </tr>
    
        <tr>
            <td>40317</td>
            <td>REAL ESTATE</td>
        </tr>
    
        <tr>
            <td>40318</td>
            <td>TRANSPORTATION</td>
        </tr>
    
        <tr>
            <td>40319</td>
            <td>UTILITIES</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links filers to each other and records their relationship type.

**Sample:** `FILER_LINKS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_LINKS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p67-thumbnail.gif'></a><p>p. 67</p></div></div>





Fields
^^^^^^

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
            <td>filer_id_a</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the first filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id_b</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the second filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>active_flg</td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Indicates if the link is active</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>link_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Denotes the type of the link</td>
        </tr>
    
    
    
        <tr>
            <td>link_desc</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the link became active</td>
        </tr>
    
    
    
        <tr>
            <td>dominate_filer</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*link_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p6-thumbnail.gif'></a><p>p. 6</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p7-thumbnail.gif'></a><p>p. 7</p></div></div>




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
            <td>-12019</td>
            <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>-12018</td>
            <td>PROPONENT</td>
        </tr>
    
        <tr>
            <td>-12016</td>
            <td>TREASURER/RESPONSIBLE OFFICER FOR</td>
        </tr>
    
        <tr>
            <td>-12015</td>
            <td>ASSOCIATED</td>
        </tr>
    
        <tr>
            <td>-12014</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>-12013</td>
            <td>OPPOSE</td>
        </tr>
    
        <tr>
            <td>-12011</td>
            <td>CONTROLLING CANDIDATE</td>
        </tr>
    
        <tr>
            <td>-12008</td>
            <td>FIRM OF A LOBBYIST</td>
        </tr>
    
        <tr>
            <td>-12005</td>
            <td>FIRM OF A CLIENT (WHO IS ALSO A FIRM)</td>
        </tr>
    
        <tr>
            <td>-12004</td>
            <td>FIRM OF A CLIENT (WHO IS AN EMPLOYER)</td>
        </tr>
    
        <tr>
            <td>-12002</td>
            <td>EMPLOYER OF  AN IN-HOUSE LOBBYIST</td>
        </tr>
    
        <tr>
            <td>-12001</td>
            <td>CLIENT OF A FIRM</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>12001</td>
            <td>FIRM OF A CLIENT</td>
        </tr>
    
        <tr>
            <td>12002</td>
            <td>IN-HOUSE LOBBYIST OF AN EMPLOYER</td>
        </tr>
    
        <tr>
            <td>12004</td>
            <td>CLIENT (WHO IS AN EMPLOYER) OF A FIRM</td>
        </tr>
    
        <tr>
            <td>12005</td>
            <td>CLIENT (WHO IS ALSO A FIRM) OF ANOTHER FIRM</td>
        </tr>
    
        <tr>
            <td>12008</td>
            <td>LOBBYIST OF A FIRM</td>
        </tr>
    
        <tr>
            <td>12011</td>
            <td>CANDIDATE CONTROLS THIS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>12013</td>
            <td>OPPOSE</td>
        </tr>
    
        <tr>
            <td>12014</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>12015</td>
            <td>ASSOCIATED</td>
        </tr>
    
        <tr>
            <td>12016</td>
            <td>TREASURER/RESPONSIBLE OFFICER</td>
        </tr>
    
        <tr>
            <td>12018</td>
            <td>PROPONENT</td>
        </tr>
    
        <tr>
            <td>12019</td>
            <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model that contains a small number
of codes and definitions that map to values in FILERNAME_CD.STATUS.

**Sample:** `FILER_STATUS_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_STATUS_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p69-thumbnail.gif'></a><p>p. 69</p></div></div>





Fields
^^^^^^

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
            <td>status_type</td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>status_desc</td>
            <td>String (up to 11)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table links a filer to a set of characteristics that describe the
filer. This table maintains a history of changes and allows the filer
to change characteristics over time.

**Sample:** `FILER_TO_FILER_TYPE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TO_FILER_TYPE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p70-thumbnail.gif'></a><p>p. 70</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td>active</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if the filer is currently active</td>
        </tr>
    
    
    
        <tr>
            <td>race</td>
            <td>Integer</td>
            <td>No</td>
            <td>If applicable indicates the race in which the filer is running</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>category</td>
            <td>Integer</td>
            <td>No</td>
            <td>Defines the filer&#39;s category such as controlled, jointly controlled, etc. (subset of filer&#39;s type)</td>
        </tr>
    
    
    
        <tr>
            <td>category_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable, the category type specifies additional information about the category. (e.g. state, local, etc.)</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies general purpose, primarily formed, etc.</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>The date the filer assumed the current class or type</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies broad based or small contributor</td>
        </tr>
    
    
    
        <tr>
            <td>election_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates type of election (general, primary, special)</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category_a</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if sponsored or not</td>
        </tr>
    
    
    
        <tr>
            <td>nyq_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Indicates the date when a committee reached its qualifying level of activity</td>
        </tr>
    
    
    
        <tr>
            <td>party_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s political party</td>
        </tr>
    
    
    
        <tr>
            <td>county_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s county code</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s district number for the office being sought. Populated for Senate, Assembly or Board of Equalization races</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*race*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p16-thumbnail.gif'></a><p>p. 16</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/17.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p17-thumbnail.gif'></a><p>p. 17</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p21-thumbnail.gif'></a><p>p. 21</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>30002</td>
            <td>GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30003</td>
            <td>LIEUTENANT GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30004</td>
            <td>SECRETARY OF STATE</td>
        </tr>
    
        <tr>
            <td>30005</td>
            <td>CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30006</td>
            <td>TREASURER</td>
        </tr>
    
        <tr>
            <td>30007</td>
            <td>ATTORNEY GENERAL</td>
        </tr>
    
        <tr>
            <td>30008</td>
            <td>SUPERINTENDENT OF PUBLIC INSTRUCTION</td>
        </tr>
    
        <tr>
            <td>30009</td>
            <td>MEMBER BOARD OF EQUALIZATION</td>
        </tr>
    
        <tr>
            <td>30010</td>
            <td>OXNARD HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30011</td>
            <td>CITY CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30012</td>
            <td>STATE SENATE</td>
        </tr>
    
        <tr>
            <td>30013</td>
            <td>ASSEMBLY</td>
        </tr>
    
        <tr>
            <td>30014</td>
            <td>INSURANCE COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30015</td>
            <td>JUDGE</td>
        </tr>
    
        <tr>
            <td>30016</td>
            <td>BOARD MEMBER</td>
        </tr>
    
        <tr>
            <td>30017</td>
            <td>TAX COLLECTOR</td>
        </tr>
    
        <tr>
            <td>30018</td>
            <td>TRUSTEE</td>
        </tr>
    
        <tr>
            <td>30019</td>
            <td>SUPERVISOR</td>
        </tr>
    
        <tr>
            <td>30020</td>
            <td>SHERIFF</td>
        </tr>
    
        <tr>
            <td>30021</td>
            <td>CORONER</td>
        </tr>
    
        <tr>
            <td>30022</td>
            <td>MARSHALL</td>
        </tr>
    
        <tr>
            <td>30023</td>
            <td>CITY CLERK</td>
        </tr>
    
        <tr>
            <td>30024</td>
            <td>SCHOOL BOARD</td>
        </tr>
    
        <tr>
            <td>30025</td>
            <td>HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30026</td>
            <td>DISTRICT ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30027</td>
            <td>COUNTY CLERK</td>
        </tr>
    
        <tr>
            <td>30028</td>
            <td>AUDITOR</td>
        </tr>
    
        <tr>
            <td>30029</td>
            <td>MAYOR</td>
        </tr>
    
        <tr>
            <td>30030</td>
            <td>CITY ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30031</td>
            <td>DEMOCRATIC COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30032</td>
            <td>TOWN COUNCIL</td>
        </tr>
    
        <tr>
            <td>30033</td>
            <td>ASSESSOR</td>
        </tr>
    
        <tr>
            <td>30034</td>
            <td>CITY TREASURER</td>
        </tr>
    
        <tr>
            <td>30035</td>
            <td>CITY COUNCIL</td>
        </tr>
    
        <tr>
            <td>30036</td>
            <td>COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30037</td>
            <td>REPUBLICAN COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30038</td>
            <td>DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30039</td>
            <td>DIRECTOR OF ZONE 7</td>
        </tr>
    
        <tr>
            <td>30040</td>
            <td>COMMUNITY COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30041</td>
            <td>POLICE CHIEF</td>
        </tr>
    
        <tr>
            <td>30042</td>
            <td>CHIEF OF POLICE</td>
        </tr>
    
        <tr>
            <td>30043</td>
            <td>CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30044</td>
            <td>BOARD OF EDUCATION</td>
        </tr>
    
        <tr>
            <td>30045</td>
            <td>BOARD OF DIRECTORS</td>
        </tr>
    
        <tr>
            <td>30046</td>
            <td>COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30047</td>
            <td>BART BOARD DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30048</td>
            <td>BOARD OF TRUSTEES</td>
        </tr>
    
        <tr>
            <td>30049</td>
            <td>IRRIGATION</td>
        </tr>
    
        <tr>
            <td>30050</td>
            <td>WATER BOARD</td>
        </tr>
    
        <tr>
            <td>30051</td>
            <td>COMMUNITY PLANNING GROUP</td>
        </tr>
    
        <tr>
            <td>30052</td>
            <td>BOARD OF SUPERVISORS</td>
        </tr>
    
        <tr>
            <td>30053</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30054</td>
            <td>DISTRICT ATTORNEY/PUBLIC DEFENDER</td>
        </tr>
    
        <tr>
            <td>30055</td>
            <td>MEASURE</td>
        </tr>
    
        <tr>
            <td>30056</td>
            <td>CITY PROSECUTOR</td>
        </tr>
    
        <tr>
            <td>30057</td>
            <td>SUPREME COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30058</td>
            <td>PUBLIC EMPLOYEES RETIREMENT BOARD</td>
        </tr>
    
        <tr>
            <td>30059</td>
            <td>APPELLATE COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>50001</td>
            <td>Ag</td>
        </tr>
    
        <tr>
            <td>50002</td>
            <td>Assembly</td>
        </tr>
    
        <tr>
            <td>50003</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>50004</td>
            <td>Assessor/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50005</td>
            <td>Assessor/County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50006</td>
            <td>Assessor/Recorder</td>
        </tr>
    
        <tr>
            <td>50007</td>
            <td>Associate Justice</td>
        </tr>
    
        <tr>
            <td>50008</td>
            <td>Auditor</td>
        </tr>
    
        <tr>
            <td>50009</td>
            <td>Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50010</td>
            <td>Auditor/Controller/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50011</td>
            <td>Auditor/Controller/Recorder</td>
        </tr>
    
        <tr>
            <td>50012</td>
            <td>Auditor/Controller/Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50013</td>
            <td>Auditor/Recorder</td>
        </tr>
    
        <tr>
            <td>50014</td>
            <td>Board Member</td>
        </tr>
    
        <tr>
            <td>50015</td>
            <td>Board Of Director</td>
        </tr>
    
        <tr>
            <td>50016</td>
            <td>Board Of Supervisor</td>
        </tr>
    
        <tr>
            <td>50017</td>
            <td>Boe</td>
        </tr>
    
        <tr>
            <td>50018</td>
            <td>Chief Justice</td>
        </tr>
    
        <tr>
            <td>50019</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>50020</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>50021</td>
            <td>City Auditor</td>
        </tr>
    
        <tr>
            <td>50022</td>
            <td>City Clerk</td>
        </tr>
    
        <tr>
            <td>50023</td>
            <td>City Council</td>
        </tr>
    
        <tr>
            <td>50024</td>
            <td>City Of Los Angeles</td>
        </tr>
    
        <tr>
            <td>50025</td>
            <td>City Of South El Monte</td>
        </tr>
    
        <tr>
            <td>50026</td>
            <td>City Prosecutor</td>
        </tr>
    
        <tr>
            <td>50027</td>
            <td>City Treasurer</td>
        </tr>
    
        <tr>
            <td>50028</td>
            <td>Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50029</td>
            <td>Clerk/Record/Public Admin</td>
        </tr>
    
        <tr>
            <td>50030</td>
            <td>Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50031</td>
            <td>Clerk/Recorder/Registar</td>
        </tr>
    
        <tr>
            <td>50032</td>
            <td>Clerk/Recorder/Registrar</td>
        </tr>
    
        <tr>
            <td>50033</td>
            <td>Commissioner</td>
        </tr>
    
        <tr>
            <td>50034</td>
            <td>Controller</td>
        </tr>
    
        <tr>
            <td>50035</td>
            <td>Costa Mesa</td>
        </tr>
    
        <tr>
            <td>50036</td>
            <td>Council Member</td>
        </tr>
    
        <tr>
            <td>50037</td>
            <td>County Clerk</td>
        </tr>
    
        <tr>
            <td>50038</td>
            <td>County Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50039</td>
            <td>County Clerk/Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50040</td>
            <td>County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50041</td>
            <td>County Clerk/Recorder/Assessor</td>
        </tr>
    
        <tr>
            <td>50042</td>
            <td>County Clerk/Recorder/Public Admin</td>
        </tr>
    
        <tr>
            <td>50043</td>
            <td>Democratic County Central Committee</td>
        </tr>
    
        <tr>
            <td>50044</td>
            <td>Director</td>
        </tr>
    
        <tr>
            <td>50045</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>50046</td>
            <td>District Attorney/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50047</td>
            <td>Gccc</td>
        </tr>
    
        <tr>
            <td>50048</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>50049</td>
            <td>Harbor Commissioner</td>
        </tr>
    
        <tr>
            <td>50050</td>
            <td>Ic</td>
        </tr>
    
        <tr>
            <td>50051</td>
            <td>Irrigation Dist</td>
        </tr>
    
        <tr>
            <td>50052</td>
            <td>Judge</td>
        </tr>
    
        <tr>
            <td>50053</td>
            <td>Justice</td>
        </tr>
    
        <tr>
            <td>50054</td>
            <td>Legislature</td>
        </tr>
    
        <tr>
            <td>50055</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>50056</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>50057</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>50058</td>
            <td>Placentia</td>
        </tr>
    
        <tr>
            <td>50059</td>
            <td>Public Administrator</td>
        </tr>
    
        <tr>
            <td>50060</td>
            <td>Public Administrator/Guardian</td>
        </tr>
    
        <tr>
            <td>50061</td>
            <td>Rent Stabilization Board</td>
        </tr>
    
        <tr>
            <td>50062</td>
            <td>Republican Central Committee</td>
        </tr>
    
        <tr>
            <td>50063</td>
            <td>San Francisco Dccc</td>
        </tr>
    
        <tr>
            <td>50064</td>
            <td>Sanger</td>
        </tr>
    
        <tr>
            <td>50065</td>
            <td>School Board</td>
        </tr>
    
        <tr>
            <td>50066</td>
            <td>Secretary Of State</td>
        </tr>
    
        <tr>
            <td>50067</td>
            <td>Senator</td>
        </tr>
    
        <tr>
            <td>50068</td>
            <td>Sheriff</td>
        </tr>
    
        <tr>
            <td>50069</td>
            <td>Sheriff/Coroner</td>
        </tr>
    
        <tr>
            <td>50070</td>
            <td>Sheriff/Coroner/Marshall</td>
        </tr>
    
        <tr>
            <td>50071</td>
            <td>Sheriff/Coroner/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50072</td>
            <td>Solana Beach</td>
        </tr>
    
        <tr>
            <td>50073</td>
            <td>Superintendent</td>
        </tr>
    
        <tr>
            <td>50074</td>
            <td>Supervisor</td>
        </tr>
    
        <tr>
            <td>50075</td>
            <td>Supt Of Schools</td>
        </tr>
    
        <tr>
            <td>50076</td>
            <td>Tax Collector</td>
        </tr>
    
        <tr>
            <td>50077</td>
            <td>Town Council</td>
        </tr>
    
        <tr>
            <td>50078</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>50079</td>
            <td>Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50080</td>
            <td>Treasurer/Tax Collector/Clerk</td>
        </tr>
    
        <tr>
            <td>50081</td>
            <td>Treasurer/Tax Collector/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50082</td>
            <td>Treasurer/Tax Collector/Public Administrator/County Clerk</td>
        </tr>
    
        <tr>
            <td>50083</td>
            <td>Treasurer/Tax Collector/Recorder</td>
        </tr>
    
        <tr>
            <td>50084</td>
            <td>Trustee</td>
        </tr>
    
        <tr>
            <td>50085</td>
            <td>Weed Recreation Board Member</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*category*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40000</td>
            <td>CATEGORY</td>
        </tr>
    
        <tr>
            <td>40001</td>
            <td>JOINTLY CONTROLLED</td>
        </tr>
    
        <tr>
            <td>40002</td>
            <td>CONTROLLED</td>
        </tr>
    
        <tr>
            <td>40003</td>
            <td>CAUCUS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>40004</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*category_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40501</td>
            <td>LOCAL</td>
        </tr>
    
        <tr>
            <td>40502</td>
            <td>STATE</td>
        </tr>
    
        <tr>
            <td>40503</td>
            <td>COUNTY</td>
        </tr>
    
        <tr>
            <td>40504</td>
            <td>MULTI-COUNTY</td>
        </tr>
    
        <tr>
            <td>40505</td>
            <td>CITY</td>
        </tr>
    
        <tr>
            <td>40506</td>
            <td>FEDERAL</td>
        </tr>
    
        <tr>
            <td>40507</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sub_category*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40101</td>
            <td>PRIMARILY FORMED MEASURE</td>
        </tr>
    
        <tr>
            <td>40102</td>
            <td>PRIMARILY FORMED CANDIDATE</td>
        </tr>
    
        <tr>
            <td>40103</td>
            <td>GENERAL PURPOSE</td>
        </tr>
    
        <tr>
            <td>40104</td>
            <td>GENERAL PURPOSE POLITICAL PARTY</td>
        </tr>
    
        <tr>
            <td>40105</td>
            <td>GENERAL PURPOSE MEASURE</td>
        </tr>
    
        <tr>
            <td>40112</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sub_category_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40202</td>
            <td>BROAD-BASED</td>
        </tr>
    
        <tr>
            <td>40203</td>
            <td>SMALL CONTRIBUTOR</td>
        </tr>
    
        <tr>
            <td>40204</td>
            <td>MPO - NON PROFIT</td>
        </tr>
    
        <tr>
            <td>40205</td>
            <td>MPO - NON PROFIT CY</td>
        </tr>
    
        <tr>
            <td>40206</td>
            <td>MPO - OTHER</td>
        </tr>
    
        <tr>
            <td>40207</td>
            <td>MPO - OTHER CY</td>
        </tr>
    
        <tr>
            <td>40208</td>
            <td>FEDERAL PAC</td>
        </tr>
    
        <tr>
            <td>40209</td>
            <td>OUT OF STATE PAC</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*election_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>3001</td>
            <td>GENERAL</td>
        </tr>
    
        <tr>
            <td>3002</td>
            <td>PRIMARY</td>
        </tr>
    
        <tr>
            <td>3003</td>
            <td>RECALL</td>
        </tr>
    
        <tr>
            <td>3004</td>
            <td>SPECIAL ELECTION</td>
        </tr>
    
        <tr>
            <td>3005</td>
            <td>OFFICEHOLDER</td>
        </tr>
    
        <tr>
            <td>3006</td>
            <td>SPECIAL RUNOFF</td>
        </tr>
    
        <tr>
            <td>3010</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>3007</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*party_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div></div>




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
            <td>16001</td>
            <td>DEMOCRATIC</td>
        </tr>
    
        <tr>
            <td>16002</td>
            <td>REPUBLICAN</td>
        </tr>
    
        <tr>
            <td>16003</td>
            <td>GREEN PARTY</td>
        </tr>
    
        <tr>
            <td>16004</td>
            <td>REFORM PARTY</td>
        </tr>
    
        <tr>
            <td>16005</td>
            <td>AMERICAN INDEPENDENT PARTY</td>
        </tr>
    
        <tr>
            <td>16006</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
        <tr>
            <td>16007</td>
            <td>INDEPENDENT</td>
        </tr>
    
        <tr>
            <td>16008</td>
            <td>LIBERTARIAN</td>
        </tr>
    
        <tr>
            <td>16009</td>
            <td>NON PARTISAN</td>
        </tr>
    
        <tr>
            <td>16010</td>
            <td>NATURAL LAW</td>
        </tr>
    
        <tr>
            <td>16011</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>16012</td>
            <td>NO PARTY PREFERENCE</td>
        </tr>
    
        <tr>
            <td>16013</td>
            <td>AMERICANS ELECT</td>
        </tr>
    
        <tr>
            <td>16020</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
        <tr>
            <td>16014</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>None</td>
            <td>NONE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*county_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p14-thumbnail.gif'></a><p>p. 14</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p15-thumbnail.gif'></a><p>p. 15</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>18001</td>
            <td>01</td>
        </tr>
    
        <tr>
            <td>18002</td>
            <td>12</td>
        </tr>
    
        <tr>
            <td>18003</td>
            <td>23</td>
        </tr>
    
        <tr>
            <td>18004</td>
            <td>34</td>
        </tr>
    
        <tr>
            <td>18005</td>
            <td>45</td>
        </tr>
    
        <tr>
            <td>18006</td>
            <td>55</td>
        </tr>
    
        <tr>
            <td>18007</td>
            <td>56</td>
        </tr>
    
        <tr>
            <td>18008</td>
            <td>57</td>
        </tr>
    
        <tr>
            <td>18009</td>
            <td>58</td>
        </tr>
    
        <tr>
            <td>18010</td>
            <td>02</td>
        </tr>
    
        <tr>
            <td>18011</td>
            <td>03</td>
        </tr>
    
        <tr>
            <td>18012</td>
            <td>04</td>
        </tr>
    
        <tr>
            <td>18013</td>
            <td>05</td>
        </tr>
    
        <tr>
            <td>18014</td>
            <td>06</td>
        </tr>
    
        <tr>
            <td>18015</td>
            <td>07</td>
        </tr>
    
        <tr>
            <td>18016</td>
            <td>08</td>
        </tr>
    
        <tr>
            <td>18017</td>
            <td>09</td>
        </tr>
    
        <tr>
            <td>18018</td>
            <td>10</td>
        </tr>
    
        <tr>
            <td>18019</td>
            <td>11</td>
        </tr>
    
        <tr>
            <td>18020</td>
            <td>13</td>
        </tr>
    
        <tr>
            <td>18021</td>
            <td>14</td>
        </tr>
    
        <tr>
            <td>18022</td>
            <td>15</td>
        </tr>
    
        <tr>
            <td>18023</td>
            <td>16</td>
        </tr>
    
        <tr>
            <td>18024</td>
            <td>17</td>
        </tr>
    
        <tr>
            <td>18025</td>
            <td>18</td>
        </tr>
    
        <tr>
            <td>18026</td>
            <td>19</td>
        </tr>
    
        <tr>
            <td>18027</td>
            <td>20</td>
        </tr>
    
        <tr>
            <td>18028</td>
            <td>21</td>
        </tr>
    
        <tr>
            <td>18029</td>
            <td>22</td>
        </tr>
    
        <tr>
            <td>18030</td>
            <td>24</td>
        </tr>
    
        <tr>
            <td>18031</td>
            <td>25</td>
        </tr>
    
        <tr>
            <td>18032</td>
            <td>26</td>
        </tr>
    
        <tr>
            <td>18033</td>
            <td>27</td>
        </tr>
    
        <tr>
            <td>18034</td>
            <td>28</td>
        </tr>
    
        <tr>
            <td>18035</td>
            <td>29</td>
        </tr>
    
        <tr>
            <td>18036</td>
            <td>30</td>
        </tr>
    
        <tr>
            <td>18037</td>
            <td>31</td>
        </tr>
    
        <tr>
            <td>18038</td>
            <td>32</td>
        </tr>
    
        <tr>
            <td>18039</td>
            <td>33</td>
        </tr>
    
        <tr>
            <td>18040</td>
            <td>35</td>
        </tr>
    
        <tr>
            <td>18041</td>
            <td>36</td>
        </tr>
    
        <tr>
            <td>18042</td>
            <td>37</td>
        </tr>
    
        <tr>
            <td>18043</td>
            <td>38</td>
        </tr>
    
        <tr>
            <td>18044</td>
            <td>39</td>
        </tr>
    
        <tr>
            <td>18045</td>
            <td>40</td>
        </tr>
    
        <tr>
            <td>18046</td>
            <td>41</td>
        </tr>
    
        <tr>
            <td>18047</td>
            <td>42</td>
        </tr>
    
        <tr>
            <td>18048</td>
            <td>43</td>
        </tr>
    
        <tr>
            <td>18049</td>
            <td>44</td>
        </tr>
    
        <tr>
            <td>18050</td>
            <td>46</td>
        </tr>
    
        <tr>
            <td>18051</td>
            <td>47</td>
        </tr>
    
        <tr>
            <td>18052</td>
            <td>48</td>
        </tr>
    
        <tr>
            <td>18053</td>
            <td>49</td>
        </tr>
    
        <tr>
            <td>18054</td>
            <td>50</td>
        </tr>
    
        <tr>
            <td>18055</td>
            <td>51</td>
        </tr>
    
        <tr>
            <td>18056</td>
            <td>52</td>
        </tr>
    
        <tr>
            <td>18057</td>
            <td>53</td>
        </tr>
    
        <tr>
            <td>18058</td>
            <td>54</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*district_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>17001</td>
            <td>01</td>
        </tr>
    
        <tr>
            <td>17002</td>
            <td>13</td>
        </tr>
    
        <tr>
            <td>17003</td>
            <td>24</td>
        </tr>
    
        <tr>
            <td>17004</td>
            <td>35</td>
        </tr>
    
        <tr>
            <td>17005</td>
            <td>46</td>
        </tr>
    
        <tr>
            <td>17006</td>
            <td>57</td>
        </tr>
    
        <tr>
            <td>17007</td>
            <td>68</td>
        </tr>
    
        <tr>
            <td>17008</td>
            <td>79</td>
        </tr>
    
        <tr>
            <td>17009</td>
            <td>02</td>
        </tr>
    
        <tr>
            <td>17010</td>
            <td>05</td>
        </tr>
    
        <tr>
            <td>17011</td>
            <td>04</td>
        </tr>
    
        <tr>
            <td>17013</td>
            <td>06</td>
        </tr>
    
        <tr>
            <td>17014</td>
            <td>07</td>
        </tr>
    
        <tr>
            <td>17015</td>
            <td>08</td>
        </tr>
    
        <tr>
            <td>17016</td>
            <td>19</td>
        </tr>
    
        <tr>
            <td>17017</td>
            <td>10</td>
        </tr>
    
        <tr>
            <td>17018</td>
            <td>11</td>
        </tr>
    
        <tr>
            <td>17019</td>
            <td>12</td>
        </tr>
    
        <tr>
            <td>17020</td>
            <td>14</td>
        </tr>
    
        <tr>
            <td>17021</td>
            <td>15</td>
        </tr>
    
        <tr>
            <td>17022</td>
            <td>16</td>
        </tr>
    
        <tr>
            <td>17023</td>
            <td>17</td>
        </tr>
    
        <tr>
            <td>17024</td>
            <td>18</td>
        </tr>
    
        <tr>
            <td>17026</td>
            <td>20</td>
        </tr>
    
        <tr>
            <td>17027</td>
            <td>21</td>
        </tr>
    
        <tr>
            <td>17028</td>
            <td>22</td>
        </tr>
    
        <tr>
            <td>17029</td>
            <td>23</td>
        </tr>
    
        <tr>
            <td>17030</td>
            <td>25</td>
        </tr>
    
        <tr>
            <td>17031</td>
            <td>26</td>
        </tr>
    
        <tr>
            <td>17032</td>
            <td>27</td>
        </tr>
    
        <tr>
            <td>17033</td>
            <td>28</td>
        </tr>
    
        <tr>
            <td>17034</td>
            <td>29</td>
        </tr>
    
        <tr>
            <td>17035</td>
            <td>30</td>
        </tr>
    
        <tr>
            <td>17036</td>
            <td>31</td>
        </tr>
    
        <tr>
            <td>17037</td>
            <td>32</td>
        </tr>
    
        <tr>
            <td>17038</td>
            <td>33</td>
        </tr>
    
        <tr>
            <td>17039</td>
            <td>34</td>
        </tr>
    
        <tr>
            <td>17040</td>
            <td>36</td>
        </tr>
    
        <tr>
            <td>17041</td>
            <td>37</td>
        </tr>
    
        <tr>
            <td>17042</td>
            <td>38</td>
        </tr>
    
        <tr>
            <td>17043</td>
            <td>39</td>
        </tr>
    
        <tr>
            <td>17044</td>
            <td>40</td>
        </tr>
    
        <tr>
            <td>17045</td>
            <td>41</td>
        </tr>
    
        <tr>
            <td>17046</td>
            <td>42</td>
        </tr>
    
        <tr>
            <td>17047</td>
            <td>43</td>
        </tr>
    
        <tr>
            <td>17048</td>
            <td>44</td>
        </tr>
    
        <tr>
            <td>17049</td>
            <td>45</td>
        </tr>
    
        <tr>
            <td>17050</td>
            <td>47</td>
        </tr>
    
        <tr>
            <td>17051</td>
            <td>48</td>
        </tr>
    
        <tr>
            <td>17052</td>
            <td>49</td>
        </tr>
    
        <tr>
            <td>17053</td>
            <td>50</td>
        </tr>
    
        <tr>
            <td>17054</td>
            <td>51</td>
        </tr>
    
        <tr>
            <td>17055</td>
            <td>52</td>
        </tr>
    
        <tr>
            <td>17056</td>
            <td>53</td>
        </tr>
    
        <tr>
            <td>17057</td>
            <td>54</td>
        </tr>
    
        <tr>
            <td>17058</td>
            <td>55</td>
        </tr>
    
        <tr>
            <td>17059</td>
            <td>56</td>
        </tr>
    
        <tr>
            <td>17060</td>
            <td>03</td>
        </tr>
    
        <tr>
            <td>17061</td>
            <td>59</td>
        </tr>
    
        <tr>
            <td>17062</td>
            <td>60</td>
        </tr>
    
        <tr>
            <td>17063</td>
            <td>61</td>
        </tr>
    
        <tr>
            <td>17064</td>
            <td>62</td>
        </tr>
    
        <tr>
            <td>17065</td>
            <td>63</td>
        </tr>
    
        <tr>
            <td>17066</td>
            <td>64</td>
        </tr>
    
        <tr>
            <td>17067</td>
            <td>65</td>
        </tr>
    
        <tr>
            <td>17068</td>
            <td>66</td>
        </tr>
    
        <tr>
            <td>17069</td>
            <td>67</td>
        </tr>
    
        <tr>
            <td>17070</td>
            <td>69</td>
        </tr>
    
        <tr>
            <td>17071</td>
            <td>70</td>
        </tr>
    
        <tr>
            <td>17072</td>
            <td>71</td>
        </tr>
    
        <tr>
            <td>17073</td>
            <td>72</td>
        </tr>
    
        <tr>
            <td>17074</td>
            <td>73</td>
        </tr>
    
        <tr>
            <td>17075</td>
            <td>74</td>
        </tr>
    
        <tr>
            <td>17076</td>
            <td>75</td>
        </tr>
    
        <tr>
            <td>17077</td>
            <td>76</td>
        </tr>
    
        <tr>
            <td>17078</td>
            <td>77</td>
        </tr>
    
        <tr>
            <td>17079</td>
            <td>78</td>
        </tr>
    
        <tr>
            <td>17080</td>
            <td>80</td>
        </tr>
    
        <tr>
            <td>17081</td>
            <td>09</td>
        </tr>
    
        <tr>
            <td>17090</td>
            <td>58</td>
        </tr>
    
        <tr>
            <td>17091</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17083</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17093</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17094</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17088</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17096</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17012</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17095</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17092</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17086</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17099</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17082</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17025</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17085</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17084</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17087</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17098</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17089</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerTypePeriodsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "J M needs
to document. This is in his list of tables designed for future enhancements."

**Sample:** `FILER_TYPE_PERIODS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPE_PERIODS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p71-thumbnail.gif'></a><p>p. 71</p></div></div>





Fields
^^^^^^

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
            <td>election_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td>period_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing FilingPeriodCd.period_id</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*election_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




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
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>3001</td>
            <td>GENERAL</td>
        </tr>
    
        <tr>
            <td>3002</td>
            <td>PRIMARY</td>
        </tr>
    
        <tr>
            <td>3003</td>
            <td>RECALL</td>
        </tr>
    
        <tr>
            <td>3004</td>
            <td>SPECIAL ELECTION</td>
        </tr>
    
        <tr>
            <td>3005</td>
            <td>OFFICEHOLDER</td>
        </tr>
    
        <tr>
            <td>3006</td>
            <td>SPECIAL RUNOFF</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This lookup table describes filer types.

**Sample:** `FILER_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p71-thumbnail.gif'></a><p>p. 71</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p72-thumbnail.gif'></a><p>p. 72</p></div></div>





Fields
^^^^^^

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
            <td>filer_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer type identification number</td>
        </tr>
    
    
    
        <tr>
            <td>description</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Description of the filer type</td>
        </tr>
    
    
    
        <tr>
            <td>grp_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Group type assocated with the filer type</td>
        </tr>
    
    
    
        <tr>
            <td>calc_use</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Use checkbox flag</td>
        </tr>
    
    
    
        <tr>
            <td>grace_period</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*grp_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




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
            <td>58</td>
            <td>LOBBY PERIODS</td>
        </tr>
    
        <tr>
            <td>59</td>
            <td>CAMPAIGN PERIODS</td>
        </tr>
    
        <tr>
            <td>60</td>
            <td>DEFAULT PERIOD FOR ERRONEOUS DATA</td>
        </tr>
    
        <tr>
            <td>61</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

FilerXrefCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table maps legacy filer identification numbers to the system's filer
identification numbers. Although 60 percent of the FILER_ID and XREF_ID values
are equal.

**Sample:** `FILER_XREF_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_XREF_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p72-thumbnail.gif'></a><p>p. 72</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>xref_id</td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date</td>
        </tr>
    
    
    
        <tr>
            <td>migration_source</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Source of the XREF_ID. Migration or generated by the AMS.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

FilersCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is the parent table from which all links and associations
to a filer are derived.

**Sample:** `FILERS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILERS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p73-thumbnail.gif'></a><p>p. 73</p></div></div>





Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~~~

An undocumented table that contains metadata for a variety
of filing periods.

**Sample:** `FILING_PERIOD_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILING_PERIOD_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p74-thumbnail.gif'></a><p>p. 74</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p75-thumbnail.gif'></a><p>p. 75</p></div></div>





Fields
^^^^^^

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
            <td>period_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique period identification number</td>
        </tr>
    
    
    
        <tr>
            <td>start_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for period</td>
        </tr>
    
    
    
        <tr>
            <td>end_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date of period</td>
        </tr>
    
    
    
        <tr>
            <td>period_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>per_grp_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Period group type</td>
        </tr>
    
    
    
        <tr>
            <td>period_desc</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Period description</td>
        </tr>
    
    
    
        <tr>
            <td>deadline</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Deadline date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*period_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div></div>




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
            <td>1500</td>
            <td>Standard period</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*per_grp_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div></div>




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
            <td>1500</td>
            <td>STANDARD PERIOD</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This lookup table stores group type information. Most (but not all) of the GRP_ID/
GRP_NAME value pairs in this table match the FILER_TYPE/DESCRIPTION value pairs in
the FILER_TYPE_CD table.

**Sample:** `GROUP_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/GROUP_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div></div>





Fields
^^^^^^

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
            <td>grp_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Group identification number</td>
        </tr>
    
    
    
        <tr>
            <td>grp_name</td>
            <td>String (up to 28)</td>
            <td>No</td>
            <td>Group name. Many of the values in this column are empty strings.</td>
        </tr>
    
    
    
        <tr>
            <td>grp_desc</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Group Description. This column contains only empty strings.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table links images to filers and accounts.

**Sample:** `IMAGE_LINKS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/IMAGE_LINKS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p80-thumbnail.gif'></a><p>p. 80</p></div></div>





Fields
^^^^^^

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
            <td>img_link_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image link identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_link_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of image link</td>
        </tr>
    
    
    
        <tr>
            <td>img_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of image</td>
        </tr>
    
    
    
        <tr>
            <td>img_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Image date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*img_link_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p5-thumbnail.gif'></a><p>p. 5</p></div></div>




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
            <td>6501</td>
            <td>FILING ID</td>
        </tr>
    
        <tr>
            <td>6502</td>
            <td>FILER ID</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*img_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




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
            <td>6001</td>
            <td>FAX</td>
        </tr>
    
        <tr>
            <td>6002</td>
            <td>PERSONAL PHOTO</td>
        </tr>
    
        <tr>
            <td>6004</td>
            <td>SCANNED CHECK</td>
        </tr>
    
        <tr>
            <td>6005</td>
            <td>SCANNED LETTER</td>
        </tr>
    
        <tr>
            <td>6007</td>
            <td>IMAGE TYPES</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Legislative session, begin and end dates look up table.

**Sample:** `LEGISLATIVE_SESSIONS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEGISLATIVE_SESSIONS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p84-thumbnail.gif'></a><p>p. 84</p></div></div>





Fields
^^^^^^

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
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>begin_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session start date</td>
        </tr>
    
    
    
        <tr>
            <td>end_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session end date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LookupCodesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

The description of some lookup codes in the system.

**Sample:** `LOOKUP_CODES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOOKUP_CODES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/106.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p106-thumbnail.gif'></a><p>p. 106</p></div></div>





Fields
^^^^^^

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
            <td>code_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>code_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>The code&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>code_desc</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Code description</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

NamesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

The name of all entities in the system. Used for searches when
the name has an identification number.

**Sample:** `NAMES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/NAMES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/112.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p112-thumbnail.gif'></a><p>p. 112</p></div></div>





Fields
^^^^^^

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
            <td>namid</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number unique to the name</td>
        </tr>
    
    
    
        <tr>
            <td>naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    
        <tr>
            <td>namf</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td>namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>nams</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>moniker</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>moniker_pos</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Location of the entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>namm</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Middle name</td>
        </tr>
    
    
    
        <tr>
            <td>fullname</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name</td>
        </tr>
    
    
    
        <tr>
            <td>naml_search</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

ReceivedFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is undocumented.

**Sample:** `RECEIVED_FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RECEIVED_FILINGS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/121.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p121-thumbnail.gif'></a><p>p. 121</p></div></div>




Filing Forms
^^^^^^^^^^^^
ReceivedFilingsCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_file_name</td>
            <td>String (up to 14)</td>
            <td>No</td>
            <td>The field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>received_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td>filing_directory</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>receive_comment</td>
            <td>String (up to 51)</td>
            <td>No</td>
            <td>A comment</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_id*


*Overview*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p4-thumbnail.gif'></a><p>p. 4</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p5-thumbnail.gif'></a><p>p. 5</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p6-thumbnail.gif'></a><p>p. 6</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711624-Overview/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711624/pages/Overview-p8-thumbnail.gif'></a><p>p. 8</p></div></div>




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
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
    </tbody>
    </table>
    </div>





------------

ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Sample:** `REPORTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/REPORTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/122.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p122-thumbnail.gif'></a><p>p. 122</p></div></div>





Fields
^^^^^^

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
            <td>rpt_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_name</td>
            <td>String (up to 74)</td>
            <td>No</td>
            <td>Name of the report</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_desc_field</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Description of the report</td>
        </tr>
    
    
    
        <tr>
            <td>path</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Report path</td>
        </tr>
    
    
    
        <tr>
            <td>data_object</td>
            <td>String (up to 38)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>parms_flg_y_n</td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameters indication flag</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of the report</td>
        </tr>
    
    
    
        <tr>
            <td>parm_definition</td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameter definition</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rpt_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p2-thumbnail.gif'></a><p>p. 2</p></div></div>




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
            <td>401</td>
            <td>PUBLIC REPORTS</td>
        </tr>
    
        <tr>
            <td>402</td>
            <td>AUDITS</td>
        </tr>
    
        <tr>
            <td>403</td>
            <td>FINANCIAL REPORTS</td>
        </tr>
    
        <tr>
            <td>404</td>
            <td>AUDITS</td>
        </tr>
    
        <tr>
            <td>405</td>
            <td>MAILING LABELS</td>
        </tr>
    
        <tr>
            <td>406</td>
            <td>OTHER REPORTS</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
    </tbody>
    </table>
    </div>




