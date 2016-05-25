.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the campaign_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Campaign tables
================================


The CAL-ACCESS database contains 16 tables that, according to the
:doc:`official documentation </calaccess/officialdocumentation>`,
store information specific to campaign finance disclosure filings.



------------

*********************
CVR_SO_CD
*********************

Cover page for a statement of organization creation or termination
form filed by a slate-mailer organization or recipient committee.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_SO_CD.TSV?slice=0:10"></script>


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
            <td>- Part 1, Slate Mailer Organization Information</td>
        </tr>
        
        <tr>
            <td>- Part 2, Treasurer And Other Principal Officers</td>
        </tr>
        
        <tr>
            <td>- Part 4, Is This Organization A "Committee" Pursuant To Government Code Section 82013?</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-402">Form 402</a>:
                Statement of Termination (Slate Mailer Organization)
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-410">Form 410</a>:
                Statement of Organization Recipient Committee
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Committee Information</td>
        </tr>
        
        <tr>
            <td>- Part 2, Treasurer and Other Principal Officers</td>
        </tr>
        
        <tr>
            <td>- Part 4, Type of Committee</td>
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
            <td><code>ACCT_OPENDT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Account Opened</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACTVTY_LVL</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Organization&#39;s level of activity</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_ADR1</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 1 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_ADR2</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 2 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_NAM</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BANK_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BRDBASE_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Based Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Optional Committee EMAIL address</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Optional Committee FAX number</td>
        </tr>
    
    
    
        <tr>
            <td><code>COM82013ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>ID of 82013 Committee (if Com82013Nm is a RCP cmtte)</td>
        </tr>
    
    
    
        <tr>
            <td><code>COM82013NM</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of 82013 Committee (F400; when Com82013YN=Y)</td>
        </tr>
    
    
    
        <tr>
            <td><code>COM82013YN</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Is this SMO a 82013 &quot;Committee&quot;? (Yes/No) (F400)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTROL_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Controlled Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>COUNTY_ACT</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County where Active (F410)</td>
        </tr>
    
    
    
        <tr>
            <td><code>COUNTY_RES</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County of Domicile, Residence, or Location</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Filer. Values: SMO - Slate Mailer Organization (F400,402) [COM|RCP] - Recipient Committee (F410)</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name title</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>GENPURP_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>General Purpose Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>GPC_DESCR</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Brief description of Activity of GPC</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - City</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - State</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td><code>PHONE</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone Number of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRIMFC_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>QUALFY_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified as an organization</td>
        </tr>
    
    
    
        <tr>
            <td><code>QUAL_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Qualified Committee check-box (Req. if SMO)</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number - Values: 000 - Original Report 001 thru 999 - Amended Rpt #1-#999</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td><code>SMCONT_QUALDT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Small Contributor Committee Qualified</td>
        </tr>
    
    
    
        <tr>
            <td><code>SPONSOR_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Sponsored Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td><code>SURPLUSDSP</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Disposition of Surplus Funds</td>
        </tr>
    
    
    
        <tr>
            <td><code>TERM_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination Effective Date (Req. if F402)</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name title</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer&#39;s street</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 for Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``actvty_lvl``
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
                <td><code>CI</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CO</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>ST</code></td>
                <td>State</td>
            </tr>
        
            <tr>
                <td><code>St</code></td>
                <td>State</td>
            </tr>
        
            <tr>
                <td><code>st</code></td>
                <td>State</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p60">60</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p30">30</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p47">47</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>BMC</code></td>
                <td>Ballot measure committee</td>
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
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>SMO</code></td>
                <td>Slate-mailer organization</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>)
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
                <td><code>F400</code></td>
                <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F402</code></td>
                <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>)
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
                <td><code>CVR</code></td>
                <td>Cover Page for Stmt of Organization / Slate Mailer Org, Stmt of Termination / Slate Mailer Org or Stmt of Organization / Recipient Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p28">28</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 2.01) (`59-61 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59>`_)

* Map from .CAL Format to Database Table and Fields (`28-31 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p28>`_)

* .CAL Format Layout (Version 1.05.02) (`46-47 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46>`_)

* CAL-ACCESS Tables, Columns and Indexes (`39-41 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p39>`_)






------------

*********************
CVR2_SO_CD
*********************

Additional names and committee information included on the second page
of a statement of organization creation form filed
by a slate-mailer organization or recipient committee.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_SO_CD.TSV?slice=0:10"></script>


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
            <td>- Part 3, Individuals Who Authorize Contents Of Slate Mailers</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-410">Form 410</a>:
                Statement of Organization Recipient Committee
            </td>
        </tr>
        
        <tr>
            <td>- Part 4, Type of Committee</td>
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
            <td>Type of record. This column will always contain &quot;CVR2&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Form type of the filing the record is included in. This must equal the form_type of the parent filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity&#39;s business name or last name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity&#39;s first name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name prefix or title if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name suffix if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ITEM_CD</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Section of the Statement of Organization this itemization relates to. See CAL document for the definition of legal values for this column.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>State portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zipcode portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td><code>DAY_PHONE</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s daytime phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FAX_PHONE</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMAIL_ADR</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address. Not contained in current forms.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>IND_GROUP</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Industry group/affiliation description</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office sought code (OFFICE_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office jurisdiction code. See CAL document for a list of legal values.</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description provided if the         jurisdiction code (JURIS_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office district number for Senate, Assembly, and Board of Equalization districts.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office sought/held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held</td>
        </tr>
    
    
    
        <tr>
            <td><code>NON_PTY_CB</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Non-partisan check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARTY_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of party (if partisan)</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>YEAR_ELECT</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td><code>POF_TITLE</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Position/title of the principal officer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>CVR2</code></td>
                <td>Cover Page; Additional Names &amp; Addresses</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p58">58</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p45">45</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>)
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
                <td><code>F400</code></td>
                <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 3, Individuals Who Authorize Contents Of Slate Mailers</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410 (Statement of Organization Recipient Committee): Part 4, Type of Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p58">58-59</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p45">45-46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>OFF</code></td>
                <td>Officer</td>
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
                <td><code>SPO</code></td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td><code>BMN</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48">48</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62">62</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``item_cd``
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
                <td><code>ATR</code></td>
                <td>Assistant Treasurer (F410)</td>
            </tr>
        
            <tr>
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>CTL</code></td>
                <td>Controlled Committee (F410)</td>
            </tr>
        
            <tr>
                <td><code>P5B</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PFC</code></td>
                <td>Primarily Formed Committee Item (F410)</td>
            </tr>
        
            <tr>
                <td><code>Pfc</code></td>
                <td>Primarily Formed Committee Item (F410)</td>
            </tr>
        
            <tr>
                <td><code>POF</code></td>
                <td>Principal Officer (F400, F410</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td><code>SMA</code></td>
                <td>Slate Mailer Authorizer (F400)</td>
            </tr>
        
            <tr>
                <td><code>SPO</code></td>
                <td>Sponsored Committee Itemization (F410)</td>
            </tr>
        
            <tr>
                <td><code>n/a</code></td>
                <td>Not Applicable</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CST</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48">48</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p10">10</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62">62</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>Asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>OF</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>REP</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>05</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>PAC</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td><code>JR</code></td>
                <td>N/A</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p63">63</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p39">39</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p63">63</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p39">39</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p40">40</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 2.01) (`62-64 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62>`_)

* Map from .CAL Format to Database Table and Fields (`38-40 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38>`_)

* .CAL Format Layout (Version 1.05.02) (`48-49 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `45-46 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p45>`_)






------------

*********************
CVR_CAMPAIGN_DISCLOSURE_CD
*********************

Cover page information from campaign disclosure forms. This data comes from
the electronic filing. The data contained herein is "as filed" by the entity
making the filing.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_CAMPAIGN_DISCLOSURE_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-425">Form 425</a>:
                Semi-Annual Statement of no Activity
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Committee Information</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        <tr>
            <td>- Type of Recipient Committee</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-461">Form 461</a>:
                Independent Expenditure Committee & Major Donor Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Name and Address of Filer</td>
        </tr>
        
        <tr>
            <td>- Part 2, Nature and Interests of Filer</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Committee/Filer Information</td>
        </tr>
        
        <tr>
            <td>- Part 2, Name of Candidate or Measure Supported or Opposed</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-496">Form 496</a>:
                Late Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, List Only One Candidate or Ballot Measure</td>
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
                <a href="../filingforms/campaign_forms.html#form-511">Form 511</a>:
                Paid Spokesperson Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-900">Form 900</a>:
                Public employee's retirement board, candidate campaign statement
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
        
            <td><code>filing_id</code></td>
        
            <td><code>amend_id</code></td>
        
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
            <td>No</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMENDEXP_1</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 1</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMENDEXP_2</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 2</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMENDEXP_3</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 3</td>
        </tr>
    
    
    
        <tr>
            <td><code>ASSOC_CB</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Association Interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ASSOC_INT</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of association interests</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td><code>BRDBASE_YN</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Base Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer/business address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_INTER</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Employer/business interest description</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of employer/business. Applies to the form 461.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer/business address state</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer/business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUSACT_CB</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Business activity info included check-box. Valid values are &#39;X&#39; and null</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUSACTVITY</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Business activity description</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officeholder city</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder fax. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Applies to forms 460, 465, and 496.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (Filer_id) of recipient Committee who&#39;s campaign statement is attached. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTTE_TYPE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Type of Recipient Committee. Applies to the 450/460.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTROL_YN</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLBUS_CB</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Employer/Business Info included check-box. Legal values are &#39;X&#39; or null. Applies to the Form 461.</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>The entity type of the filer. These codes vary by form type.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILE_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer&#39;s email address</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer&#39;s fax</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>The committee&#39;s or organization&#39;s name or if an individual the filer&#39;s last name.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s title or prefix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer phone number</td>
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
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>FROM_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction description if the field JURIS_CD is set to city (CIT), county (CTY), local (LOC), or other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td><code>LATE_RPTNO</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Identifying Report Number used to distinguish multiple reports filed during the same filing period. For example, this field allows for multiple form 497s to be filed on the same day.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OCCUPATION</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description if the field OFFICE_CD is set to other (OTH)</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other entity interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_INT</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Other entity interests description</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRIMFRM_YN</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number, as reported by the filer Report Number 000 represents an original filing. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORTNAME</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement type. Legal values are 450, 460, and 461.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_ATT_CB</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Committee Report Attached check-box. Legal values are &#39;X&#39; or null. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, according to the filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPTFROMDT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period from date.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPTTHRUDT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period through date.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SELFEMP_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self employed check-box. CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td><code>SPONSOR_YN</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Sponsored Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>STMT_TYPE</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>THRU_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s email</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


``cmtte_type``
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
                <td><code>C</code></td>
                <td>Candidate or officeholder controlled committee</td>
            </tr>
        
            <tr>
                <td><code>P</code></td>
                <td>Candidate or officeholder primarily formed committee</td>
            </tr>
        
            <tr>
                <td><code>B</code></td>
                <td>Ballot-measure committee</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>General-purpose committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p24">24</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p10">10</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p19">19</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>BMC</code></td>
                <td>Ballot measure committee</td>
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
                <td><code>OTH</code></td>
                <td>Other</td>
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6">6</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
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
                <td><code>F511</code></td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>Gov</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>46</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>55</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>APP</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SD</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>OC</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>AD</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28-29</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p13">13</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21-22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>h</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>Gov</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>Sen</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>REP</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>Mem</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>PAC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>)
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
                <td><code>CVR</code></td>
                <td>Cover Page</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6">6</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p25">25</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``reportname``
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
                <td><code>450</code></td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td><code>460</code></td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td><code>461</code></td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p15">15</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p20">20</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p19">19</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p26">26</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``stmt_type``
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
                <td><code>PE</code></td>
                <td>Pre-Election (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>QT</code></td>
                <td>Quarterly Stmt (F450,F460)</td>
            </tr>
        
            <tr>
                <td><code>SA</code></td>
                <td>Semi-annual (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>SE</code></td>
                <td>Supplemental Pre-elect (F450, F460, F495)</td>
            </tr>
        
            <tr>
                <td><code>SY</code></td>
                <td>Special Odd-Yr. Campaign (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>S1</code></td>
                <td>Semi-Annual (Jan1-Jun30) (F425)</td>
            </tr>
        
            <tr>
                <td><code>S2</code></td>
                <td>Semi-Annual (Jul1-Dec31) (F425)</td>
            </tr>
        
            <tr>
                <td><code>TS</code></td>
                <td>Termination Statement (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>pe</code></td>
                <td>Pre-Election (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>qt</code></td>
                <td>Quarterly Stmt (F450,F460)</td>
            </tr>
        
            <tr>
                <td><code>sa</code></td>
                <td>Semi-annual (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>se</code></td>
                <td>Supplemental Pre-elect (F450, F460, F495)</td>
            </tr>
        
            <tr>
                <td><code>sy</code></td>
                <td>Special Odd-Yr. Campaign (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>ts</code></td>
                <td>Termination Statement (F450, F460)</td>
            </tr>
        
            <tr>
                <td><code>**</code></td>
                <td>Amendment</td>
            </tr>
        
            <tr>
                <td><code>1</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>2</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MD</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>QS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>x</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>YE</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p23">23</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p7">7</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>o</code></td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p14">14</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p28">28</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 2.01) (`22-30 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22>`_)

* Map from .CAL Format to Database Table and Fields (`6-14 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6>`_)

* .CAL Format Layout (Version 1.05.02) (`18-22 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18>`_)

* CAL-ACCESS Tables, Columns and Indexes (`7 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p7>`_, `25-29 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p25>`_)






------------

*********************
CVR2_CAMPAIGN_DISCLOSURE_CD
*********************

Record used to carry additional names (e.g., Assistant Treasurers) for the
campaign disclosure forms below.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_CAMPAIGN_DISCLOSURE_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-425">Form 425</a>:
                Semi-Annual Statement of no Activity
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Committee Information</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        <tr>
            <td>- Part 3, Committee Information</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page - Part 2</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 5, Filing Officers</td>
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Commitee identification number, when the entity is a committee</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTROL_YN</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) checkbox. Legal values are &quot;Y&quot; or &quot;N&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code used to identify the type of entity being described with in the record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity city</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Entity email address</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity name, or last name if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity prefix or title, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Entity state</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity ZIP code</td>
        </tr>
    
    
    
        <tr>
            <td><code>F460_PART</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Part of 460 cover page coded on ths cvr2 record</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s mailing city</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s mailing state</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s mailing ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>TITLE</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official title of filing officer. Applies to the form 465.</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>ATR</code></td>
                <td>Assistant treasurer</td>
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
                <td><code>OFF</code></td>
                <td>Officer</td>
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
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>FIL</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PEX</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RDP</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23-24</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p32">32</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``f460_part``
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
                <td><code>3</code></td>
                <td>Part 3: Committee Information</td>
            </tr>
        
            <tr>
                <td><code>4a</code></td>
                <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td><code>4A</code></td>
                <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td><code>4b</code></td>
                <td>Part 4b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td><code>4B</code></td>
                <td>Part 4b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td><code>5a</code></td>
                <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td><code>5A</code></td>
                <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td><code>5b</code></td>
                <td>Part 5b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td><code>5B</code></td>
                <td>Part 5b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td><code>6</code></td>
                <td>Part 6: Primarily Formed Committee</td>
            </tr>
        
            <tr>
                <td><code>6a</code></td>
                <td>Part 6a: Name of Ballot Measure</td>
            </tr>
        
            <tr>
                <td><code>6A</code></td>
                <td>Part 6a: Name of Ballot Measure</td>
            </tr>
        
            <tr>
                <td><code>6b</code></td>
                <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
            </tr>
        
            <tr>
                <td><code>6B</code></td>
                <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
            </tr>
        
            <tr>
                <td><code>7</code></td>
                <td>Part 7: Primarily Formed Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p32">32</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>)
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
                <td><code>F425</code></td>
                <td>Form 425 (Semi-Annual Statement of no Activity): Part 1, Committee Information</td>
            </tr>
        
            <tr>
                <td><code>F450</code></td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 3, Committee Information</td>
            </tr>
        
            <tr>
                <td><code>F460</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Cover Page - Part 2</td>
            </tr>
        
            <tr>
                <td><code>F465</code></td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 5, Filing Officers</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31">31</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>SD</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>se</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>LBC</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Statewide</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p33">33</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>CTL</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ST</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>PAC</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
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
                <td><code>CVR2</code></td>
                <td>Cover, Page 2</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31">31</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41">41</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>o</code></td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>),  CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41">41</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`23-24 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23>`_)

* .CAL Format Layout (Version 2.01) (`31-34 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `41-43 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41>`_)

* Map from .CAL Format to Database Table and Fields (`32-35 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32>`_)






------------

*********************
CVR3_VERIFICATION_INFO_CD
*********************

Cover page verification information from campaign disclosure forms


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR3_VERIFICATION_INFO_CD.TSV?slice=0:10"></script>


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
            <td>- Part 5, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-402">Form 402</a>:
                Statement of Termination (Slate Mailer Organization)
            </td>
        </tr>
        
        <tr>
            <td>- Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-410">Form 410</a>:
                Statement of Organization Recipient Committee
            </td>
        </tr>
        
        <tr>
            <td>- Part 3, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-425">Form 425</a>:
                Semi-Annual Statement of no Activity
            </td>
        </tr>
        
        <tr>
            <td>- Part 3, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        <tr>
            <td>- Part 4, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Cover Page</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-461">Form 461</a>:
                Independent Expenditure Committee & Major Donor Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Part 4, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 6, Verification</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-511">Form 511</a>:
                Paid Spokesperson Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-900">Form 900</a>:
                Public employee's retirement board, candidate campaign statement
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
            <td>Record Type Value: CVR3</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_LOC</code></td>
            <td>String (up to 39)</td>
            <td>No</td>
            <td>City and state where signed</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAML</code></td>
            <td>String (up to 56)</td>
            <td>No</td>
            <td>Last name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Title of the signer</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMS</code></td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Suffix of the signer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>CVR3</code></td>
                <td>Cover Page 3, Verification Information</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25">25</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50">50</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>)
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
                <td><code>F400</code></td>
                <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 5, Verification</td>
            </tr>
        
            <tr>
                <td><code>F401</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Cover Page</td>
            </tr>
        
            <tr>
                <td><code>F402</code></td>
                <td>Form 402 (Statement of Termination (Slate Mailer Organization)): Verification</td>
            </tr>
        
            <tr>
                <td><code>F410</code></td>
                <td>Form 410 (Statement of Organization Recipient Committee): Part 3, Verification</td>
            </tr>
        
            <tr>
                <td><code>F425</code></td>
                <td>Form 425 (Semi-Annual Statement of no Activity): Part 3, Verification</td>
            </tr>
        
            <tr>
                <td><code>F450</code></td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 4, Verification</td>
            </tr>
        
            <tr>
                <td><code>F460</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Cover Page</td>
            </tr>
        
            <tr>
                <td><code>F461</code></td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 4, Verification</td>
            </tr>
        
            <tr>
                <td><code>F465</code></td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 6, Verification</td>
            </tr>
        
            <tr>
                <td><code>F511</code></td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50">50</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>ATR</code></td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td><code>SPO</code></td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td><code>atr</code></td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td><code>tre</code></td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td><code>cao</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>MDI</code></td>
                <td>Major Donor/Ind Expenditure</td>
            </tr>
        
            <tr>
                <td><code>POF</code></td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>COA</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BBB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MAI</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p9">9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25">25</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p11">11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`25 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25>`_, `50 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50>`_)

* .CAL Format Layout (Version 2.01) (`34 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34>`_, `64 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64>`_)

* CAL-ACCESS Tables, Columns and Indexes (`46-47 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46>`_)

* Map from .CAL Format to Database Table and Fields (`41-42 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p41>`_)






------------

*********************
CVR_F470_CD
*********************

Cover page information for Officeholder and Candidate Short and Supplement Forms
(Form 470)


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_F470_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-470">Form 470</a>:
                Officeholder and Candidate Campaign Statement, Short Form
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
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment Identification number. A number of 0 is an original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ADR1</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First line of the filer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ADR2</code></td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Second line of the filer&#39;s street address. </td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s City.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s EMail address. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s FAX Phone Number. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s zipcode</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATE_1000</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date contributions totaling $1,000 or more. (For the 470-S)</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the general election. Required for filings in even years.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>The filer&#39;s entity code. The value of this column will always be Candidate/Office Holder (CAO) for this table.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s First Name(s) - required for individuals</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer&#39;s Last Name/Committee name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s Name Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The filer&#39;s prefix or title that preceeds their name if they are an individual.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Type of Filing or Formset. The value of this column will always be equal to F470.</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description text reqired if the jurisdiction code (Juris_cd) is equal to CIT, CTY, LOC, or OTH.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office Sought/Held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office code is other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Code that identifies the office being sought. See the CAL document for a list of valid codes.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 3)</td>
            <td>Yes</td>
            <td>Type of CAL record. This column will always contain CVR.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended as reported in the filing.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed as reported by the filer.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>)
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
                <td><code>F470</code></td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p30">30</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>)
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
                <td><code>CVR</code></td>
                <td>Cover Page</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 2.01) (`29-30 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29>`_)

* Map from .CAL Format to Database Table and Fields (`15-16 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p15>`_)

* .CAL Format Layout (Version 1.05.02) (`22 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `30-32 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p30>`_)






------------

*********************
DEBT_CD
*********************

Records of unpaid bills accrued by Recipient Campaigns, as listed on
Form 460, Schedule F (Accrued Expenses).


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/DEBT_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule F, Accrued Expenses (Unpaid Bills)</td>
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMT_INCUR</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount incurred this period</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMT_PAID</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount paid this period.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to a transaction identifier of a parent record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BEG_BAL</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at beginning of period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>END_BAL</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at close of this period</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the payee</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_CODE</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Expense Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DSCR</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number of the parent filing</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Schedule Name/ID: (F - Sched F / Accrued Expenses)</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Record line item number</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>First line of the payee&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s name suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMT</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Payee&#39;s prefix or title if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type value: DEBT</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction identifier - permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_MATCH</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. /&quot;X/&quot; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_SCHNM</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Schedule C.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>BNM</code></td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``expn_code``
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
                <td><code>CMP</code></td>
                <td>campaign paraphernalia/miscellaneous</td>
            </tr>
        
            <tr>
                <td><code>CNS</code></td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td><code>CTB</code></td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td><code>CVC</code></td>
                <td>civic donations</td>
            </tr>
        
            <tr>
                <td><code>FIL</code></td>
                <td>candidate filing/ballot feeds</td>
            </tr>
        
            <tr>
                <td><code>FND</code></td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td><code>IKD</code></td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>independent expenditure supporting/opposing others (explain)*</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>legal defense</td>
            </tr>
        
            <tr>
                <td><code>LIT</code></td>
                <td>campaign literature and mailings</td>
            </tr>
        
            <tr>
                <td><code>LON</code></td>
                <td>loan</td>
            </tr>
        
            <tr>
                <td><code>MBR</code></td>
                <td>member communications</td>
            </tr>
        
            <tr>
                <td><code>MON</code></td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td><code>MTG</code></td>
                <td>meetings and appearances</td>
            </tr>
        
            <tr>
                <td><code>OFC</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code>PET</code></td>
                <td>petition circulating</td>
            </tr>
        
            <tr>
                <td><code>PHO</code></td>
                <td>phone banks</td>
            </tr>
        
            <tr>
                <td><code>POL</code></td>
                <td>polling and survey research</td>
            </tr>
        
            <tr>
                <td><code>POS</code></td>
                <td>postage, delivery and messenger services</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>professional services (legal, accounting)</td>
            </tr>
        
            <tr>
                <td><code>PRT</code></td>
                <td>print ads</td>
            </tr>
        
            <tr>
                <td><code>RAD</code></td>
                <td>radio airtime and production costs</td>
            </tr>
        
            <tr>
                <td><code>RFD</code></td>
                <td>returned contributions</td>
            </tr>
        
            <tr>
                <td><code>SAL</code></td>
                <td>campaign workers salaries</td>
            </tr>
        
            <tr>
                <td><code>TEL</code></td>
                <td>T.V. or cable airtime and production costs</td>
            </tr>
        
            <tr>
                <td><code>TRC</code></td>
                <td>candidate travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>staff/spouse travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td><code>TSF</code></td>
                <td>transfer between committees of the same candidate/sponsor</td>
            </tr>
        
            <tr>
                <td><code>VOT</code></td>
                <td>voter registration</td>
            </tr>
        
            <tr>
                <td><code>WEB</code></td>
                <td>information technology costs (internet, e-mail)</td>
            </tr>
        
            <tr>
                <td><code>Fnd</code></td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td><code>ofc</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code>&#39;CN</code></td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td><code>*</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AIR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BUS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CAM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CSN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DEP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>EVE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>fns</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GGG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>HOT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>L</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LDF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MEE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>P</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SPE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TAX</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TRA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>V</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p11">11</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p13">13-14</a>)
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
                <td><code>F</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45</a>)
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
                <td><code>DEBT</code></td>
                <td>DEBT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33-34</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45-46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`33-34 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33>`_)

* .CAL Format Layout (Version 2.01) (`45-46 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45>`_)

* CAL-ACCESS Tables, Columns and Indexes (`47-49 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p47>`_)

* Map from .CAL Format to Database Table and Fields (`49-48 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p49>`_)






------------

*********************
EXPN_CD
*********************

Campaign expenditures from a variety of forms, excluding Late Independent
Expenditures (from Form 496)


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EXPN_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-450">Form 450</a>:
                Recipient Committee Campaign Disclosure Statement - Short Form
            </td>
        </tr>
        
        <tr>
            <td>- Part 5, Payments Made</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
        </tr>
        
        <tr>
            <td>- Schedule E, Payments Made</td>
        </tr>
        
        <tr>
            <td>- Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-461">Form 461</a>:
                Independent Expenditure Committee & Major Donor Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-465">Form 465</a>:
                Supplemental Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 3, Independent Expenditures Made</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-900">Form 900</a>:
                Public employee's retirement board, candidate campaign statement
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
            <td><code>AGENT_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Last name (Sched G)</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of Payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a Tran_ID of a &#39;parent&#39; record</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot Measure Name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot Number or Letter</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (If [COM|RCP] &amp; no ID#, Treas info Req.)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_OTH</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / &#39;Other&#39; (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_YTD</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / Year-to-date amount         (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing payee</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_CHKNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Check Number (Optional)</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_CODE</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>CTB &amp; IND need explanation &amp; listing on Sched D TRC &amp; TRS require explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Expenditure (Note: Date not on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DSCR</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>G_FROM_E_F</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Back Reference from Sched G to Sched &#39;E&#39; or &#39;F&#39;?</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description         (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo Amount? (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (Req. if Office_Cd=OTH)</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee City</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State code</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip+4</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: EXPN</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer City</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s First name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s Last name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer State</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_MATCH</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>X = Related item on other Sched has same Tran_ID</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_SCHNM</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related item is included on Sched &#39;C&#39; or &#39;H2&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PTY</code></td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td><code>SCC</code></td>
                <td>Small Contributor Committee</td>
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
                <td><code>MBR</code></td>
                <td>Member of Associaton</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PTH</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RFD</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``expn_code``
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
                <td><code>CMP</code></td>
                <td>campaign paraphernalia/miscellaneous</td>
            </tr>
        
            <tr>
                <td><code>CNS</code></td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td><code>CTB</code></td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td><code>CVC</code></td>
                <td>civic donations</td>
            </tr>
        
            <tr>
                <td><code>FIL</code></td>
                <td>candidate filing/ballot feeds</td>
            </tr>
        
            <tr>
                <td><code>FND</code></td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td><code>IKD</code></td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>independent expenditure supporting/opposing others (explain)*</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>legal defense</td>
            </tr>
        
            <tr>
                <td><code>LIT</code></td>
                <td>campaign literature and mailings</td>
            </tr>
        
            <tr>
                <td><code>LON</code></td>
                <td>loan</td>
            </tr>
        
            <tr>
                <td><code>MBR</code></td>
                <td>member communications</td>
            </tr>
        
            <tr>
                <td><code>MON</code></td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td><code>MTG</code></td>
                <td>meetings and appearances</td>
            </tr>
        
            <tr>
                <td><code>OFC</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code>PET</code></td>
                <td>petition circulating</td>
            </tr>
        
            <tr>
                <td><code>PHO</code></td>
                <td>phone banks</td>
            </tr>
        
            <tr>
                <td><code>POL</code></td>
                <td>polling and survey research</td>
            </tr>
        
            <tr>
                <td><code>POS</code></td>
                <td>postage, delivery and messenger services</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>professional services (legal, accounting)</td>
            </tr>
        
            <tr>
                <td><code>PRT</code></td>
                <td>print ads</td>
            </tr>
        
            <tr>
                <td><code>RAD</code></td>
                <td>radio airtime and production costs</td>
            </tr>
        
            <tr>
                <td><code>RFD</code></td>
                <td>returned contributions</td>
            </tr>
        
            <tr>
                <td><code>SAL</code></td>
                <td>campaign workers salaries</td>
            </tr>
        
            <tr>
                <td><code>TEL</code></td>
                <td>T.V. or cable airtime and production costs</td>
            </tr>
        
            <tr>
                <td><code>TRC</code></td>
                <td>candidate travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>staff/spouse travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td><code>TSF</code></td>
                <td>transfer between committees of the same candidate/sponsor</td>
            </tr>
        
            <tr>
                <td><code>VOT</code></td>
                <td>voter registration</td>
            </tr>
        
            <tr>
                <td><code>WEB</code></td>
                <td>information technology costs (internet, e-mail)</td>
            </tr>
        
            <tr>
                <td><code>ctb</code></td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td><code>ikd</code></td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td><code>Mon</code></td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td><code>ofc</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code>OFc</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code>Ofc</code></td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td><code></code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>*</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>001</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>011</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>200</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>401</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ADV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ANN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>APR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AUG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AUT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Ban</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BAN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BOO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BOX</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CHE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CIV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CNT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>COP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CRE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CSN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>,CT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>.CT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CTN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CVD</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DEC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Dem</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DIN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Don</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Ear</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>EIM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>EMP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FAX</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FDN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FEE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FIN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Fun</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FUN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>G</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GGG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GOT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>IEs</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>IN-</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Ina</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>INK</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ITE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JAN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JUL</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JUN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>KIC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>L</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LEV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Lit</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LN#</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LOG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>M</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MAI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Mar</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MAR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MEE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MGT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Mis</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MRB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NGP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NOT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NOV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OCT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>.OF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OPE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>P</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Pac</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PAI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PAR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PAY</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PMT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>.PO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Pos</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PRE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PRI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PRP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>R</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>.Re</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>.RE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>REF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>REI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RFP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S-A</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Sal</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S C</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S.C</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SCU</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SEE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SEP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S.M.</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SOF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SWI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TAX</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TB,</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TIC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Tor</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TRA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TRF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>TRV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>UN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>UTI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>V</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>VEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>-VO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>VOI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>VOY</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>WI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>x</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S-6</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S.M</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S-4</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SA:</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>100</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RFN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>REN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>003</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S-1</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>08</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p11">11</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p13">13-14</a>)
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
                <td><code>F450P5</code></td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
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
                <td><code>G</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
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
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>Cit</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>Sen</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>stw</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>APP</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>ES</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>SM</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>12</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>4</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>8</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>27</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>93</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>98</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>CLB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Boa</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>Sta</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SAN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ES </code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LBC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>WES</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>(Lo</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>(Ci</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>vty</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SM </code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ASS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ADM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SAC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>US</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>J</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LOS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>IRV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JRS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NEV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>IB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>Ass</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SD</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>D</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SEC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GEN</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>R</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>h</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>a</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>8</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>Cou</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>AtT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>May</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>Sen</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>gov</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>Gov</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>LA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>HOU</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LAD</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>11A</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>001</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>BM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AS1</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ASS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>73</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>HSE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>GO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CO</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PAC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>REP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>031</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ASB</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>NAT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SWE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>DA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ST</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PRE</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>/S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>U S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>8</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>C:S</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
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
                <td><code>EXPN</code></td>
                <td>Expense</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>o</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>Y</code></td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`31-32 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31>`_)

* .CAL Format Layout (Version 2.01) (`42-44 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `53-56 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p53>`_)

* Map from .CAL Format to Database Table and Fields (`45-48 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p45>`_)






------------

*********************
LOAN_CD
*********************

Loans received and made by recepient committees


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOAN_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule B - Part 1, Loans Received</td>
        </tr>
        
        <tr>
            <td>- Schedule B - Part 2, Loan Guarantors</td>
        </tr>
        
        <tr>
            <td>- Schedule B - Part 3, Outstanding Bal</td>
        </tr>
        
        <tr>
            <td>- Schedule H, Loans Made to Others</td>
        </tr>
        
        <tr>
            <td>- Schedule H - Part 1, Loans Made</td>
        </tr>
        
        <tr>
            <td>- Schedule H- Part 2, Repayments Rcvd</td>
        </tr>
        
        <tr>
            <td>- Schedule H - Part 3, Outstanding Loans</td>
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the lender</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 2)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>LNDR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Lender&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LNDR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Lender&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LNDR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>LNDR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT1</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Repaid or forgiven amount; Original loan amount. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT2</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding Principal; unpaid balance. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT3</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Interest Paid; Unpaid interest; Interest received. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT4</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Amount/Other. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT5</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT6</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT7</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_AMT8</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Lender&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_DATE1</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the loan was made or recieved. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_DATE2</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date repaid/forgiven; date loan due. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_EMP</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Loan employer. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_OCC</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Loan occupation. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_RATE</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Interest Rate. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_SELF</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Lender&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_TYPE</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Type of loan</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOAN_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOAN</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_MATCH</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &quot;X&quot; indicates this condition is true.</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_SCHNM</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Form 460 Schedule &#39;A&#39; or &#39;E&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>)
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``loan_type``
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
                <td><code>H2T</code></td>
                <td>Third party payment</td>
            </tr>
        
            <tr>
                <td><code>H2F</code></td>
                <td>Forgiven</td>
            </tr>
        
            <tr>
                <td><code>H2R</code></td>
                <td>Repay</td>
            </tr>
        
            <tr>
                <td><code>B2T</code></td>
                <td>Third party payment</td>
            </tr>
        
            <tr>
                <td><code>B2F</code></td>
                <td>Forgiven</td>
            </tr>
        
            <tr>
                <td><code>B2R</code></td>
                <td>Repay</td>
            </tr>
        
            <tr>
                <td><code>B1G</code></td>
                <td>Guarantor</td>
            </tr>
        
            <tr>
                <td><code>B1L</code></td>
                <td>Lender</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>)
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
                <td><code>LOAN</code></td>
                <td>LOAN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`35-39 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35>`_)

* .CAL Format Layout (Version 2.01) (`47-50 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47>`_)

* CAL-ACCESS Tables, Columns and Indexes (`87-90 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p87>`_)

* Map from .CAL Format to Database Table and Fields (`60-63 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p60>`_)






------------

*********************
RCPT_CD
*********************

Contribution records from receipts schedules for Slate Mailer Organization
and Recipient Committee Campaign Statements.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RCPT_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#electronic-form-530">Electronic Form 530</a>:
                Electronic Issue Advocacy Report
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule A, Payments Received</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-460">Form 460</a>:
                Recipient Committee Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule A, Monetary Contributions Received</td>
        </tr>
        
        <tr>
            <td>- Schedule A-1, Contributions Transferred to Special Election Commitee</td>
        </tr>
        
        <tr>
            <td>- Schedule C, Non-Monetary Contributions Received</td>
        </tr>
        
        <tr>
            <td>- Schedule I, miscellanous increases to cash</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-496">Form 496</a>:
                Late Independent Expenditure Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 3, Contributions > $100 Received</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-900">Form 900</a>:
                Public employee's retirement board, candidate campaign statement
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
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount Received (Monetary, Inkkind, Promise)</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a transaction identifier of a parent record</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name prefix or title. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee Identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Contributor&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_DSCR</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of goods/services received</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_EMP</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_OCC</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_SELF</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self Employed Check-box</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Contributor&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_OTH</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Other (Sched A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_YTD</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative year to date amount (Form 460 Schedule A and Form 401 Schedule A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATE_THRU</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the contributor</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>INT_RATE</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_CMTEID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_EMP</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Employer</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Last Name</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_OCC</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Intermediary&#39;s Occupation</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_SELF</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Intermediary&#39;s self employed check box</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTR_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code. See the CAL document for the list of legal values. Used on Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>RCPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_TYPE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Transaction Type</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRES_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_MATCH</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &#39;X&#39; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td><code>XREF_SCHNM</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Sched &#39;B2&#39; or &#39;F&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>PTY</code></td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
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
                <td><code>Com</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>BNM</code></td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PTH</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>RFD</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>MBR</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37">37</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71">71</a>)
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
                <td><code>E530</code></td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
            </tr>
        
            <tr>
                <td><code>F900</code></td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td><code>F401A</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td><code>A</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>A-1</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A-1, Contributions Transferred to Special Election Commitee</td>
            </tr>
        
            <tr>
                <td><code>C</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td><code>I</code></td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
            </tr>
        
            <tr>
                <td><code>F496P3</code></td>
                <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37">37</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CLB</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>CO</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SAC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>SF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AL</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>4</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p74">74</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p75">75</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>gov</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>OTh</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>oth</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>csu</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>HOU</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ASS</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
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
                <td><code>E530</code></td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
            </tr>
        
            <tr>
                <td><code>RCPT</code></td>
                <td>Receipt</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p37">37</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71">71</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p74">74</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``tran_type``
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
                <td><code>F</code></td>
                <td>Forgiven Loan</td>
            </tr>
        
            <tr>
                <td><code>I</code></td>
                <td>Intermediary</td>
            </tr>
        
            <tr>
                <td><code>R</code></td>
                <td>Returned (Negative Amount?)</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>Third Party Repayment</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Transfer</td>
            </tr>
        
            <tr>
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>I</code></td>
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
                <td><code>R</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p38">38</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p72">72</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`29-30 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29>`_)

* .CAL Format Layout (Version 2.01) (`37-41 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37>`_)

* CAL-ACCESS Tables, Columns and Indexes (`13 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p13>`_, `118-121 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p118>`_)

* Map from .CAL Format to Database Table and Fields (`71-75 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71>`_)






------------

*********************
S401_CD
*********************

Form 401 (Slate Mailer Organization) payment and other
disclosure schedules (F401B, F401B-1, F401C, F401D) information. Does not
include Form 401, Schedule A (Payments Received).


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S401_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-401">Form 401</a>:
                Slate Mailer Organization Campaign Statement
            </td>
        </tr>
        
        <tr>
            <td>- Schedule B, Payments Made</td>
        </tr>
        
        <tr>
            <td>- Schedule B-1, Payments Made by Agent or Independent Contractor</td>
        </tr>
        
        <tr>
            <td>- Schedule C, Persons Receiving $1,000 or More</td>
        </tr>
        
        <tr>
            <td>- Schedule D, Candidates and Measures Not Listed on Schedule A</td>
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
        
            <td><code>FILING_ID</code></td>
        
            <td><code>AMEND_ID</code></td>
        
            <td><code>LINE_ID</code></td>
        
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
            <td>No</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S401</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAMT</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENT_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s title or prefix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee&#39;s city address</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state address</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount (Sched F401B, 401B-1, 401C)</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGGREGATE</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Aggregate year-to-date amount (Sched 401C)</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DSCR</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>S401</code></td>
                <td>S401</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51">51</a>)
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
                <td><code>F401B</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td><code>F401B-1</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
            </tr>
        
            <tr>
                <td><code>F401C</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule C, Persons Receiving $1,000 or More</td>
            </tr>
        
            <tr>
                <td><code>F401D</code></td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule D, Candidates and Measures Not Listed on Schedule A</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51">51</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ltg</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>OTh</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>att</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>oth</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>tre</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>con</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>boe</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>sos</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>sup</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>SAC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>ca</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CAL</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OR</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>AL</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>10</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p77">77</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`39 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39>`_)

* .CAL Format Layout (Version 2.01) (`51-52 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51>`_)

* CAL-ACCESS Tables, Columns and Indexes (`123-124 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p123>`_)

* Map from .CAL Format to Database Table and Fields (`76-78 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p76>`_)






------------

*********************
F495P2_CD
*********************

Form 495 Supplemental Pre-Election Campaign Statement, attached to
Recipient Committee Campaign Statements (Forms 450 and 460).


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F495P2_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
        
        
    </tbody>
    </table>



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
        
            <td><code>REC_ITEM</code></td>
        
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
            <td>No</td>
            <td>Record Type Value: F495</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form to which the Form 495 is attached (must equal Form_Type in CVR record)</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election This date will be the same as on the filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECTJURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of the election</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBAMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Contribution amount (For the period of 6 months prior to 17 days before the election)</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>F495</code></td>
                <td>F495</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26">26</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35">35</a>)
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
                <td><code>F450</code></td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td><code>F460</code></td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26">26</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`26 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26>`_)

* .CAL Format Layout (Version 2.01) (`35 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35>`_)

* CAL-ACCESS Tables, Columns and Indexes (`56-57 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p56>`_)

* Map from .CAL Format to Database Table and Fields (`49 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p49>`_)






------------

*********************
S496_CD
*********************

Records of expenditures made by Independent Expenditure Committees in the 90
days preceding an election.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S496_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-496">Form 496</a>:
                Late Independent Expenditure Report
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
            <td>Record Type Value: S496</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Expenditure amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXP_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Expenditure dates</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DSCR</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATE_THRU</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items paid</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>S496</code></td>
                <td>S496</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40">40</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53">53</a>)
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
                <td><code>F496</code></td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40">40</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53">53</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`40 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40>`_)

* .CAL Format Layout (Version 2.01) (`53 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53>`_)

* CAL-ACCESS Tables, Columns and Indexes (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `124-125 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p124>`_)

* Map from .CAL Format to Database Table and Fields (`79 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p79>`_)






------------

*********************
S497_CD
*********************

Campaign Committee contributions received or made in the 90 days before an
election, as reported on Form 497.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S497_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-497">Form 497</a>:
                Late Contribution Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Contribution(s) Received</td>
        </tr>
        
        <tr>
            <td>- Part 2, Contribution(s) Made</td>
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
            <td>Record Type Value: S497</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name title or prefix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name suffix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_EMP</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_OCC</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_SELF</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Contributor self-employed checkbox. &quot;X&quot; indicates the contributor is self-employed.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received/made</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATE_THRU</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received/made</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Jurisdiction code describing the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in TEXT code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OFF_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>S497</code></td>
                <td>S497</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>)
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
                <td><code>F497P1</code></td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td><code>F497P2</code></td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>BNM</code></td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>CTL</code></td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>com</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
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
                <td><code>0</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>Asm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>May</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>ASm</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>oth</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>csu</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>Oth</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>H</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>HOU</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>P</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LTV</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>LT</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>REP</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>N/A</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>asm</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>sen</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>cit</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>CLB</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>IRV</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>Fon</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>JRS</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>CO</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>Riv</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>SNE</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>83</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FED</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>CA</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>JR</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p42">42</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p55">55</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>s</code></td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td><code>h</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>F</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>T</code></td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p42">42</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p55">55</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p82">82</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`41-42 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41>`_)

* .CAL Format Layout (Version 2.01) (`54-55 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54>`_)

* CAL-ACCESS Tables, Columns and Indexes (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `125-127 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p125>`_)

* Map from .CAL Format to Database Table and Fields (`80-82 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p80>`_)






------------

*********************
S498_CD
*********************

Payments received by Slate Mailer Organizations within 90 days of an election,
as reported on Form 498.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S498_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-498">Form 498</a>:
                Slate Mailer Late Payment Report
            </td>
        </tr>
        
        <tr>
            <td>- Part A, Late Payments Attributed To</td>
        </tr>
        
        <tr>
            <td>- Part R, Late Payments Received From</td>
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
            <td>Record Type Value: S498</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td><code>CMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payor&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s Prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payor&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payor&#39;s State.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYOR_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td><code>DATE_RCVD</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMT_RCVD</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Description of office sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFF_S_H_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_NUM</code></td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAL_JURIS</code></td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUP_OPP_CD</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMT_ATTRIB</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount attributed (only if Form_type = &#39;F498-A&#39;)</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_CODE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flat</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference text contained in TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>OCCUPATION</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>SELFEMP_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
                <td><code>S498</code></td>
                <td>S498</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>)
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
                <td><code>F498-A</code></td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
            </tr>
        
            <tr>
                <td><code>F498-R</code></td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
                <td><code>CAO</code></td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td><code>COM</code></td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>RCP</code></td>
                <td>Recipient committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>)
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
                <td><code>APP</code></td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td><code>ASM</code></td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td><code>ASR</code></td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td><code>ATT</code></td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td><code>BED</code></td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td><code>BSU</code></td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td><code>CAT</code></td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td><code>CCB</code></td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td><code>CCM</code></td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td><code>CON</code></td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td><code>CSU</code></td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td><code>CTR</code></td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td><code>DAT</code></td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>INS</code></td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td><code>LTG</code></td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td><code>MAY</code></td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PDR</code></td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td><code>PER</code></td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td><code>PLN</code></td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td><code>SCJ</code></td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td><code>SHC</code></td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td><code>SOS</code></td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td><code>SPM</code></td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td><code>SUP</code></td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td><code>TRE</code></td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td><code>TRS</code></td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td><code>gov</code></td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td><code>oth</code></td>
                <td>Other</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  .CAL Version 2.01 Errata (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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
                <td><code>ASM</code></td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td><code>BOE</code></td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td><code>CIT</code></td>
                <td>City</td>
            </tr>
        
            <tr>
                <td><code>CTY</code></td>
                <td>County</td>
            </tr>
        
            <tr>
                <td><code>LOC</code></td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>SEN</code></td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td><code>STW</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td><code>COU</code></td>
                <td>County</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``off_s_h_cd``
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
                <td><code>H</code></td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p44">44</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``sup_opp_cd``
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
                <td><code>O</code></td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td><code>S</code></td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



References
==========

* .CAL Format Layout (Version 1.05.02) (`43-44 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43>`_)

* .CAL Format Layout (Version 2.01) (`56-57 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56>`_)

* CAL-ACCESS Tables, Columns and Indexes (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `127-129 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p127>`_)

* Map from .CAL Format to Database Table and Fields (`83-85 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p83>`_)






------------

*********************
F501_502_CD
*********************

Candidate Intention Statements (Forms 501 and 502), including a record
for the original filing and each amendment.


Sample
======

.. raw:: html

    <script src="https://gist-it.appspot.com/github/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F501_502_CD.TSV?slice=0:10"></script>


Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-501">Form 501</a>:
                Candidate Intention Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/campaign_forms.html#form-502">Form 502</a>:
                Campaign Bank Account Statement
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
            <td><code>FILER_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>COMMITTEE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td><code>STMT_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td><code>FROM_DATE</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td><code>THRU_DATE</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELECT_DATE</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAN_NAMM</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder middle name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMT</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>MONIKER_POS</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Location of the candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td><code>MONIKER</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officerholder city</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder state</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder zip +4</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officerholder fax</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAND_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email address</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Financial institution&#39;s business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_NAMT</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s title.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_NAMS</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Financial institution&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_ST</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Financial institution&#39;s state.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Financial institution&#39;s zip code.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s FAX Number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIN_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Financial institution&#39;s e-mail address.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFICE_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td><code>OFFIC_DSCR</code></td>
            <td>String (up to 80)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td><code>AGENCY_NAM</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agency name</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td><code>JURIS_DSCR</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td><code>DIST_NO</code></td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARTY</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Political party</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_OF_ELEC</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td><code>ELEC_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXECUTE_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Execution date</td>
        </tr>
    
    
    
        <tr>
            <td><code>CAN_SIG</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate signature</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACCOUNT_NO</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Account number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACCT_OP_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Account open date</td>
        </tr>
    
    
    
        <tr>
            <td><code>PARTY_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Party code</td>
        </tr>
    
    
    
        <tr>
            <td><code>DISTRICT_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACCEPT_LIMIT_YN</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>DID_EXCEED_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>CNTRB_PRSNL_FNDS_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lookup codes
============


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
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p58">58</a>)
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
                <td><code>F501</code></td>
                <td>Form 501: Candidate Intention Statement</td>
            </tr>
        
            <tr>
                <td><code>F502</code></td>
                <td>Form 502: Campaign Bank Account Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 CAL-ACCESS Tables, Columns and Indexes (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p58">58</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
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
        
            <tr>
                <td><code>8</code></td>
                <td>Unknown</td>
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


``stmt_type``
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
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
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
                 Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd.html#document/p20">20-22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``juris_cd``
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


``elec_type``
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
                <td><code>3007</code></td>
                <td>UNKNOWN</td>
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
                <td><code>0</code></td>
                <td>N/A</td>
            </tr>
        
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
                <td><code>16014</code></td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td><code>16020</code></td>
                <td>PEACE AND FREEDOM</td>
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
                <td><code>17012</code></td>
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

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `57-59 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p57>`_)





