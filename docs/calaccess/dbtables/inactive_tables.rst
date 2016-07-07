.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the inactive_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Inactive tables
================================


We've classifed the following 22 tables because:

1. An empty .TSV file of the same name is included in the daily CAL-ACCESS exports; or
2. The date field on the table indicating when each record was created contains only dates older than three years ago.



------------

*********************
BALLOT_MEASURES_CD
*********************

Ballot measure dates and times.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=BALLOT_MEASURES_CD.TSV"></script>




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
CVR_F470_CD
*********************

Cover page information for Officeholder and Candidate Short and Supplement Forms.

An empty file of the same name is included in the Secretary of State's daily
CAL-ACCESS database exports.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=CVR_F470_CD.TSV"></script>


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
FILER_TYPE_PERIODS_CD
*********************

Listed in the official CAL-ACCESS documentation, but not fully explained.

The table's description contains this note: "J M needs to document. This is
in his list of tables designed for future enhancements."


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=FILER_TYPE_PERIODS_CD.TSV"></script>




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






------------

*********************
LOBBYIST_CONTRIBUTIONS1_CD
*********************

Lobbyist contribution disclosure table.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_CONTRIBUTIONS1_CD.TSV"></script>





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
            <td><code>FILING_PERIOD_START_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_PERIOD_END_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTION_DT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_NAME</code></td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_CONTRIBUTIONS2_CD
*********************

Lobbyist contribution disclosure table.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_CONTRIBUTIONS2_CD.TSV"></script>





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
            <td><code>FILING_PERIOD_START_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_PERIOD_END_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTION_DT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_NAME</code></td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_CONTRIBUTIONS3_CD
*********************

Lobbyist contribution disclosure table.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_CONTRIBUTIONS3_CD.TSV"></script>





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
            <td><code>FILING_PERIOD_START_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_PERIOD_END_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTION_DT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_NAME</code></td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIPIENT_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMOUNT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_EMP_LOBBYIST1_CD
*********************

This table is identical to LOBBYIST_EMP_LOBBYIST2_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the distinct SESSION_ID values span from 1995 to 2001, so probably this
table is no longer in use.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMP_LOBBYIST1_CD.TSV"></script>





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
            <td><code>LOBBYIST_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_LAST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_FIRST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
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




------------

*********************
LOBBYIST_EMP_LOBBYIST2_CD
*********************

This table is identical to LOBBYIST_EMP_LOBBYIST2_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the distinct SESSION_ID values span from 1995 to 2001, so probably this
table is no longer in use.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMP_LOBBYIST2_CD.TSV"></script>





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
            <td><code>LOBBYIST_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_LAST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_FIRST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
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




------------

*********************
LOBBYIST_EMPLOYER1_CD
*********************

This table is 99 percent identical to LOBBYIST_EMPLOYER2_CD and LOBBYIST_EMPLOYER3_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
observed in SESSION_YR_2 is 2000.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER1_CD.TSV"></script>





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
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_NAME</code></td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
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

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `97-98 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p97>`_)






------------

*********************
LOBBYIST_EMPLOYER2_CD
*********************

This table is 99 percent identical to LOBBYIST_EMPLOYER1_CD and LOBBYIST_EMPLOYER3_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
observed in SESSION_YR_2 is 2000.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER2_CD.TSV"></script>





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
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_NAME</code></td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7 total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8 total amount</td>
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

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `98-99 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p98>`_)






------------

*********************
LOBBYIST_EMPLOYER3_CD
*********************

This table is 99 percent identical to LOBBYIST_EMPLOYER1_CD and LOBBYIST_EMPLOYER2_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
observed in SESSION_YR_2 is 2000.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER3_CD.TSV"></script>





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
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_NAME</code></td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
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

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `99 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p99>`_)






------------

*********************
LOBBYIST_EMPLOYER_FIRMS1_CD
*********************

This table is identical to LOBBYIST_EMPLOYER_FIRMS2_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also the distinct SESSION_ID values span from 1995 to 2001, so probably this
table is no longer in use.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER_FIRMS1_CD.TSV"></script>





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
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>TERMINATION_DT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_EMPLOYER_FIRMS2_CD
*********************

This table is identical to LOBBYIST_EMPLOYER_FIRMS1_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also the distinct SESSION_ID values span from 1995 to 2001, so probably this
table is no longer in use.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER_FIRMS2_CD.TSV"></script>





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
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>TERMINATION_DT</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_EMPLOYER_HISTORY_CD
*********************

An empty file of the same name is included in the Secretary of State's daily CAL-ACCESS database exports.

This table is documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation
on these tables. Cox 5/11/2000".

Also, the columns on this table are identical to the columns on the
LOBBYIST_EMPLOYER1_CD, LOBBYIST_EMPLOYER2_CD and LOBBYIST_EMPLOYER3_CD
tables.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_EMPLOYER_HISTORY_CD.TSV"></script>





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
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer Name</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_CD</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTEREST_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Interest name.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 1 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 2 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 3 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 4 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 5 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 6 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 7 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 8 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount.</td>
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

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `96-97 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p96>`_)






------------

*********************
LOBBYIST_FIRM1_CD
*********************

This table is identical to LOBBYIST_FIRM2_CD and LOBBYIST_FIRM3_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
are 2002.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM1_CD.TSV"></script>





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
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM2_CD
*********************

This table is identical to LOBBYIST_FIRM1_CD and LOBBYIST_FIRM3_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
are 2002.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM2_CD.TSV"></script>





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
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM3_CD
*********************

This table is identical to LOBBYIST_FIRM1_CD and LOBBYIST_FIRM2_CD.

All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
with this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
are 2002.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM3_CD.TSV"></script>





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
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM_EMPLOYER1_CD
*********************

This table is identical to LOBBYIST_FIRM_EMPLOYER2_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also RPT_START and RPT_END each contain only one distinct value, "2001-04-01"
and "2001-06-30", respectively.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM_EMPLOYER1_CD.TSV"></script>





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
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_SEQUENCE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_START</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_END</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td><code>PER_TOTAL</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_TOTAL</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_ACTVTY</code></td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXT_LBY_ACTVTY</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM_EMPLOYER2_CD
*********************

This table is identical to LOBBYIST_FIRM_EMPLOYER1_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also RPT_START and RPT_END each contain only one distinct value, "2001-04-01"
and "2001-06-30", respectively.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM_EMPLOYER2_CD.TSV"></script>





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
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_SEQUENCE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLOYER_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_START</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_END</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td><code>PER_TOTAL</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_TOTAL</code></td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_ACTVTY</code></td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXT_LBY_ACTVTY</code></td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM_HISTORY_CD
*********************

An empty file of the same name is included in the Secretary of State's daily CAL-ACCESS database exports.

This table is documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation
on these tables. Cox 5/11/2000".

Also, the columns on this table are identical to the columns on the
LOBBYIST_FIRM1_CD, LOBBYIST_FIRM2_CD and LOBBYIST_FIRM3_CD tables.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM_HISTORY_CD.TSV"></script>





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
            <td><code>CONTRIBUTOR_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CURRENT_QTR_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the Firm/Employer/Coalition.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Name of Firm/Employer/Coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_3</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_4</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_5</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_6</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_7</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>QTR_8</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_TOTAL_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_1</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_YR_2</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_1_YTD_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td><code>YR_2_YTD_AMT</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




------------

*********************
LOBBYIST_FIRM_LOBBYIST1_CD
*********************

This table is identical to LOBBYIST_FIRM_LOBBYIST1_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, all rows have the same SESSION_ID value: 2001.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM_LOBBYIST1_CD.TSV"></script>





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
            <td><code>LOBBYIST_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_LAST_NAME</code></td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_FIRST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
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




------------

*********************
LOBBYIST_FIRM_LOBBYIST2_CD
*********************

This table is identical to LOBBYIST_FIRM_LOBBYIST1_CD.

Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
this cryptic note: "Matt needs to describe the relationship between the
multiple tables. Documentation should be cloned from D H's documentation on
these tables. Cox 5/11/2000".

Also, all rows have the same SESSION_ID value: 2001.


Sample
======

.. raw:: html

    <script src="https://gist.github.com/palewire/66bed097ddca855c36506da4b7c0d349.js?file=LOBBYIST_FIRM_LOBBYIST2_CD.TSV"></script>





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
            <td><code>LOBBYIST_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_LAST_NAME</code></td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBYIST_FIRST_NAME</code></td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
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



