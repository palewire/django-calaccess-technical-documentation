.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the campaign_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Campaign tables
================================


The CAL-ACCESS database contains 16 tables that, according to the official documentation (see `here <https://www.documentcloud.org/documents/2711617-ReadMe-Zip/pages/1.html>`_ and `here <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/3.html>`_), store information specific to campaign finance disclosure filings. These tables are outlined below.



------------

*********************
CVR_SO_CD
*********************

Cover page for a statement of organization creation or termination
form filed by a slate-mailer organization or recipient committee.

The records in CVR_SO_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR_SO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_SO_CD.TSV>`_


Filing forms
============



* `Form 400 <../filingforms/campaign_forms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))

    * Part 1, Slate Mailer Organization Information

    * Part 2, Treasurer And Other Principal Officers

    * Part 4, Is This Organization A "Committee" Pursuant To Government Code Section 82013?




* `Form 402 <../filingforms/campaign_forms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization)): Cover Page



* `Form 410 <../filingforms/campaign_forms.html#form-410>`_ (Statement of Organization Recipient Committee)

    * Part 1, Committee Information

    * Part 2, Treasurer and Other Principal Officers

    * Part 4, Type of Committee





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
            <td>acct_opendt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Account Opened</td>
        </tr>
    
    
    
        <tr>
            <td>actvty_lvl</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Organization&#39;s level of activity</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr1</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 1 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr2</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 2 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_nam</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>brdbase_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Based Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Optional Committee EMAIL address</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Optional Committee FAX number</td>
        </tr>
    
    
    
        <tr>
            <td>com82013id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>ID of 82013 Committee (if Com82013Nm is a RCP cmtte)</td>
        </tr>
    
    
    
        <tr>
            <td>com82013nm</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of 82013 Committee (F400; when Com82013YN=Y)</td>
        </tr>
    
    
    
        <tr>
            <td>com82013yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Is this SMO a 82013 &quot;Committee&quot;? (Yes/No) (F400)</td>
        </tr>
    
    
    
        <tr>
            <td>control_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Controlled Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>county_act</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County where Active (F410)</td>
        </tr>
    
    
    
        <tr>
            <td>county_res</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County of Domicile, Residence, or Location</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Filer. Values: SMO - Slate Mailer Organization (F400,402) [COM|RCP] - Recipient Committee (F410)</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name title</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>genpurp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>General Purpose Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>gpc_descr</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Brief description of Activity of GPC</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - City</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - State</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone Number of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>primfc_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>qualfy_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified as an organization</td>
        </tr>
    
    
    
        <tr>
            <td>qual_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Qualified Committee check-box (Req. if SMO)</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number - Values: 000 - Original Report 001 thru 999 - Amended Rpt #1-#999</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td>smcont_qualdt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Small Contributor Committee Qualified</td>
        </tr>
    
    
    
        <tr>
            <td>sponsor_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Sponsored Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>surplusdsp</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Disposition of Surplus Funds</td>
        </tr>
    
    
    
        <tr>
            <td>term_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination Effective Date (Req. if F402)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer&#39;s street</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 for Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


actvty_lvl
----------------

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
                <td>CI</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CO</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>ST</td>
                <td>State</td>
            </tr>
        
            <tr>
                <td>St</td>
                <td>State</td>
            </tr>
        
            <tr>
                <td>st</td>
                <td>State</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p30">30</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p60">60</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p47">47</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>BMC</td>
                <td>Ballot measure committee</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SMO</td>
                <td>Slate-mailer organization</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F402</td>
                <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td>F410</td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>CVR</td>
                <td>Cover Page for Stmt of Organization / Slate Mailer Org, Stmt of Termination / Slate Mailer Org or Stmt of Organization / Recipient Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p28">28</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59">59</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46">46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`39-41 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p39>`_)

* MapCalFormat2Fields (`28-31 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p28>`_)

* Cal-Format-201 (`59-61 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p59>`_)

* Cal-Format-1-05-02 (`46-47 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p46>`_)






------------

*********************
CVR2_SO_CD
*********************

Additional names and committee information included on the second page
of a statement of organization creation form filed
by a slate-mailer organization or recipient committee.

The records in CVR2_SO_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR2_SO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_SO_CD.TSV>`_


Filing forms
============



* `Form 400 <../filingforms/campaign_forms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization)): Part 3, Individuals Who Authorize Contents Of Slate Mailers



* `Form 410 <../filingforms/campaign_forms.html#form-410>`_ (Statement of Organization Recipient Committee): Part 4, Type of Committee




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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Type of record. This column will always contain &quot;CVR2&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Form type of the filing the record is included in. This must equal the form_type of the parent filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record.</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity&#39;s business name or last name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity&#39;s first name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name prefix or title if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name suffix if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>item_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Section of the Statement of Organization this itemization relates to. See CAL document for the definition of legal values for this column.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>State portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zipcode portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>day_phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s daytime phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax_phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email_adr</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address. Not contained in current forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ind_group</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Industry group/affiliation description</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office sought code (OFFICE_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office jurisdiction code. See CAL document for a list of legal values.</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description provided if the         jurisdiction code (JURIS_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office district number for Senate, Assembly, and Board of Equalization districts.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office sought/held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held</td>
        </tr>
    
    
    
        <tr>
            <td>non_pty_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Non-partisan check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>party_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of party (if partisan)</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>year_elect</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td>pof_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Position/title of the principal officer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>CVR2</td>
                <td>Cover Page; Additional Names &amp; Addresses</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p58">58</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p45">45</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 3, Individuals Who Authorize Contents Of Slate Mailers</td>
            </tr>
        
            <tr>
                <td>F410</td>
                <td>Form 410 (Statement of Organization Recipient Committee): Part 4, Type of Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p58">58-59</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p45">45-46</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>ATH</td>
                <td>Authorizing individual</td>
            </tr>
        
            <tr>
                <td>ATR</td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>POF</td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>SPO</td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td>BMN</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38">38</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62">62</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48">48</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


item_cd
----------------

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
                <td>ATR</td>
                <td>Assistant Treasurer (F410)</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled Committee (F410)</td>
            </tr>
        
            <tr>
                <td>P5B</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PFC</td>
                <td>Primarily Formed Committee Item (F410)</td>
            </tr>
        
            <tr>
                <td>Pfc</td>
                <td>Primarily Formed Committee Item (F410)</td>
            </tr>
        
            <tr>
                <td>POF</td>
                <td>Principal Officer (F400, F410</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>SMA</td>
                <td>Slate Mailer Authorizer (F400)</td>
            </tr>
        
            <tr>
                <td>SPO</td>
                <td>Sponsored Committee Itemization (F410)</td>
            </tr>
        
            <tr>
                <td>n/a</td>
                <td>Not Applicable</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CST</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p10">10</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62">62</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48">48</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>Asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>OF</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>REP</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>05</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td>PAC</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>N/A</td>
            </tr>
        
            <tr>
                <td>JR</td>
                <td>N/A</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p39">39</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p63">63</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p39">39</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p63">63</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46">46</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p40">40</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p49">49</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `45-46 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p45>`_)

* MapCalFormat2Fields (`38-40 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p38>`_)

* Cal-Format-201 (`62-64 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p62>`_)

* Cal-Format-1-05-02 (`48-49 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p48>`_)






------------

*********************
CVR_CAMPAIGN_DISCLOSURE_CD
*********************

Cover page information from campaign disclosure forms. This data comes from
the electronic filing. The data contained herein is "as filed" by the entity
making the filing.

The records in CVR_CAMPAIGN_DISCLOSURE_CD are unique by filing_id and amend_id.

**Sample:** `CVR_CAMPAIGN_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_CAMPAIGN_DISCLOSURE_CD.TSV>`_


Filing forms
============



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Cover Page



* `Form 425 <../filingforms/campaign_forms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 1, Committee Information



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Type of Recipient Committee



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page



* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)

    * Part 1, Name and Address of Filer

    * Part 2, Nature and Interests of Filer




* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report)

    * Part 1, Committee/Filer Information

    * Part 2, Name of Candidate or Measure Supported or Opposed




* `Form 496 <../filingforms/campaign_forms.html#form-496>`_ (Late Independent Expenditure Report): Part 1, List Only One Candidate or Ballot Measure



* `Form 497 <../filingforms/campaign_forms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <../filingforms/campaign_forms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 511 <../filingforms/campaign_forms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_1</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 1</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_2</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 2</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_3</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 3</td>
        </tr>
    
    
    
        <tr>
            <td>assoc_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Association Interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>assoc_int</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of association interests</td>
        </tr>
    
    
    
        <tr>
            <td>bal_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>brdbase_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Base Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer/business address city</td>
        </tr>
    
    
    
        <tr>
            <td>bus_inter</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Employer/business interest description</td>
        </tr>
    
    
    
        <tr>
            <td>bus_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of employer/business. Applies to the form 461.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer/business address state</td>
        </tr>
    
    
    
        <tr>
            <td>bus_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer/business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>busact_cb</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Business activity info included check-box. Valid values are &#39;X&#39; and null</td>
        </tr>
    
    
    
        <tr>
            <td>busactvity</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Business activity description</td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officeholder city</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder fax. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Applies to forms 460, 465, and 496.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>cmtte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (Filer_id) of recipient Committee who&#39;s campaign statement is attached. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td>cmtte_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Type of Recipient Committee. Applies to the 450/460.</td>
        </tr>
    
    
    
        <tr>
            <td>control_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election</td>
        </tr>
    
    
    
        <tr>
            <td>emplbus_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Employer/Business Info included check-box. Legal values are &#39;X&#39; or null. Applies to the Form 461.</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>The entity type of the filer. These codes vary by form type.</td>
        </tr>
    
    
    
        <tr>
            <td>file_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer&#39;s email address</td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>filer_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer&#39;s fax</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>The committee&#39;s or organization&#39;s name or if an individual the filer&#39;s last name.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s title or prefix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer state</td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction description if the field JURIS_CD is set to city (CIT), county (CTY), local (LOC), or other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>late_rptno</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Identifying Report Number used to distinguish multiple reports filed during the same filing period. For example, this field allows for multiple form 497s to be filed on the same day.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>occupation</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description if the field OFFICE_CD is set to other (OTH)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>other_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other entity interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>other_int</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Other entity interests description</td>
        </tr>
    
    
    
        <tr>
            <td>primfrm_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number, as reported by the filer Report Number 000 represents an original filing. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>reportname</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement type. Legal values are 450, 460, and 461.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_att_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Committee Report Attached check-box. Legal values are &#39;X&#39; or null. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, according to the filer</td>
        </tr>
    
    
    
        <tr>
            <td>rptfromdt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period from date.</td>
        </tr>
    
    
    
        <tr>
            <td>rptthrudt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period through date.</td>
        </tr>
    
    
    
        <tr>
            <td>selfemp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self employed check-box. CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>sponsor_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Sponsored Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_type</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td>tres_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s email</td>
        </tr>
    
    
    
        <tr>
            <td>tres_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


cmtte_type
----------------

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
                <td>C</td>
                <td>Candidate or officeholder controlled committee</td>
            </tr>
        
            <tr>
                <td>P</td>
                <td>Candidate or officeholder primarily formed committee</td>
            </tr>
        
            <tr>
                <td>B</td>
                <td>Ballot-measure committee</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>General-purpose committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p10">10</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p24">24</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p19">19</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>BMC</td>
                <td>Ballot measure committee</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>MDI</td>
                <td>Major Donor/Ind Expenditure</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td>SMO</td>
                <td>Slate-mailer organization</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6">6</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F401</td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
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
                <td>F511</td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>Gov</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>46</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>55</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>APP</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SD</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>OC</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>AD</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p13">13</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28-29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21-22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>h</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>Gov</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>Sen</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>REP</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>Mem</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>PAC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>CVR</td>
                <td>Cover Page</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p25">25</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6">6</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22">22</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


reportname
----------------

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
                <td>450</td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td>460</td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td>461</td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p19">19</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p26">26</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p15">15</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p20">20</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


stmt_type
----------------

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
                <td>PE</td>
                <td>Pre-Election (F450, F460)</td>
            </tr>
        
            <tr>
                <td>QT</td>
                <td>Quarterly Stmt (F450,F460)</td>
            </tr>
        
            <tr>
                <td>SA</td>
                <td>Semi-annual (F450, F460)</td>
            </tr>
        
            <tr>
                <td>SE</td>
                <td>Supplemental Pre-elect (F450, F460, F495)</td>
            </tr>
        
            <tr>
                <td>SY</td>
                <td>Special Odd-Yr. Campaign (F450, F460)</td>
            </tr>
        
            <tr>
                <td>S1</td>
                <td>Semi-Annual (Jan1-Jun30) (F425)</td>
            </tr>
        
            <tr>
                <td>S2</td>
                <td>Semi-Annual (Jul1-Dec31) (F425)</td>
            </tr>
        
            <tr>
                <td>TS</td>
                <td>Termination Statement (F450, F460)</td>
            </tr>
        
            <tr>
                <td>pe</td>
                <td>Pre-Election (F450, F460)</td>
            </tr>
        
            <tr>
                <td>qt</td>
                <td>Quarterly Stmt (F450,F460)</td>
            </tr>
        
            <tr>
                <td>sa</td>
                <td>Semi-annual (F450, F460)</td>
            </tr>
        
            <tr>
                <td>se</td>
                <td>Supplemental Pre-elect (F450, F460, F495)</td>
            </tr>
        
            <tr>
                <td>sy</td>
                <td>Special Odd-Yr. Campaign (F450, F460)</td>
            </tr>
        
            <tr>
                <td>ts</td>
                <td>Termination Statement (F450, F460)</td>
            </tr>
        
            <tr>
                <td>**</td>
                <td>Amendment</td>
            </tr>
        
            <tr>
                <td>1</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>2</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MD</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>QS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>x</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>YE</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p7">7</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p23">23</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18">18</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>o</td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p28">28</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p14">14</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p28">28</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p21">21</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`7 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p7>`_, `25-29 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p25>`_)

* MapCalFormat2Fields (`6-14 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p6>`_)

* Cal-Format-201 (`22-30 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p22>`_)

* Cal-Format-1-05-02 (`18-22 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p18>`_)






------------

*********************
CVR2_CAMPAIGN_DISCLOSURE_CD
*********************

Record used to carry additional names (e.g., Assistant Treasurers) for the
campaign disclosure forms below.

The records in CVR2_CAMPAIGN_DISCLOSURE_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR2_CAMPAIGN_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_CAMPAIGN_DISCLOSURE_CD.TSV>`_


Filing forms
============



* `Form 425 <../filingforms/campaign_forms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 1, Committee Information



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 3, Committee Information



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page - Part 2



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 5, Filing Officers




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Commitee identification number, when the entity is a committee</td>
        </tr>
    
    
    
        <tr>
            <td>control_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) checkbox. Legal values are &quot;Y&quot; or &quot;N&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code used to identify the type of entity being described with in the record.</td>
        </tr>
    
    
    
        <tr>
            <td>enty_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity city</td>
        </tr>
    
    
    
        <tr>
            <td>enty_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Entity email address</td>
        </tr>
    
    
    
        <tr>
            <td>enty_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity fax number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity name, or last name if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity prefix or title, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Entity state</td>
        </tr>
    
    
    
        <tr>
            <td>enty_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity ZIP code</td>
        </tr>
    
    
    
        <tr>
            <td>f460_part</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Part of 460 cover page coded on ths cvr2 record</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s mailing city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s mailing state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s mailing ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>title</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official title of filing officer. Applies to the form 465.</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>ATR</td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>POF</td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>FIL</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PEX</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RDP</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p32">32</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23-24</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


f460_part
----------------

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
                <td>3</td>
                <td>Part 3: Committee Information</td>
            </tr>
        
            <tr>
                <td>4a</td>
                <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td>4A</td>
                <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td>4b</td>
                <td>Part 4b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td>4B</td>
                <td>Part 4b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td>5a</td>
                <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td>5A</td>
                <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
            </tr>
        
            <tr>
                <td>5b</td>
                <td>Part 5b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td>5B</td>
                <td>Part 5b: Related Committees Not Included in this Statement</td>
            </tr>
        
            <tr>
                <td>6</td>
                <td>Part 6: Primarily Formed Committee</td>
            </tr>
        
            <tr>
                <td>6a</td>
                <td>Part 6a: Name of Ballot Measure</td>
            </tr>
        
            <tr>
                <td>6A</td>
                <td>Part 6a: Name of Ballot Measure</td>
            </tr>
        
            <tr>
                <td>6b</td>
                <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
            </tr>
        
            <tr>
                <td>6B</td>
                <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
            </tr>
        
            <tr>
                <td>7</td>
                <td>Part 7: Primarily Formed Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p32">32</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F425</td>
                <td>Form 425 (Semi-Annual Statement of no Activity): Part 1, Committee Information</td>
            </tr>
        
            <tr>
                <td>F450</td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 3, Committee Information</td>
            </tr>
        
            <tr>
                <td>F460</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Cover Page - Part 2</td>
            </tr>
        
            <tr>
                <td>F465</td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 5, Filing Officers</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31">31</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>SD</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>se</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>LBC</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Statewide</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p33">33</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p24">24</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ST</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>PAC</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>CVR2</td>
                <td>Cover, Page 2</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41">41</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32">32</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31">31</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23">23</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>o</td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41">41</a>),  MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `41-43 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p41>`_)

* MapCalFormat2Fields (`32-35 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p32>`_)

* Cal-Format-201 (`31-34 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p31>`_)

* Cal-Format-1-05-02 (`23-24 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p23>`_)






------------

*********************
RCPT_CD
*********************

Contribution records from receipts schedules for Slate Mailer Organization
and Recipient Committee Campaign Statements.

The records in RCPT_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `RCPT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RCPT_CD.TSV>`_


Filing forms
============



* `Electronic Form 530 <../filingforms/campaign_forms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule A-1, Contributions Transferred to Special Election Commitee

    * Schedule C, Non-Monetary Contributions Received

    * Schedule I, miscellanous increases to cash




* `Form 496 <../filingforms/campaign_forms.html#form-496>`_ (Late Independent Expenditure Report): Part 3, Contributions > $100 Received



* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount Received (Monetary, Inkkind, Promise)</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a transaction identifier of a parent record</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name prefix or title. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee Identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Contributor&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of goods/services received</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self Employed Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Contributor&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>cum_oth</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Other (Sched A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_ytd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative year to date amount (Form 460 Schedule A and Form 401 Schedule A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the contributor</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>int_rate</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>intr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td>intr_cmteid</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>intr_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Employer</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Last Name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>intr_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Intermediary&#39;s Occupation</td>
        </tr>
    
    
    
        <tr>
            <td>intr_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Intermediary&#39;s self employed check box</td>
        </tr>
    
    
    
        <tr>
            <td>intr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>intr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code. See the CAL document for the list of legal values. Used on Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>rcpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tran_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Transaction Type</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &#39;X&#39; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Sched &#39;B2&#39; or &#39;F&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td>Com</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PTH</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RFD</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MBR</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71">71</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37">37</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>E530</td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td>F401A</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td>A-1</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A-1, Contributions Transferred to Special Election Commitee</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td>I</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
            </tr>
        
            <tr>
                <td>F496P3</td>
                <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37">37</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CLB</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>CO</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SAC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AL</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>4</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p74">74</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p75">75</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>gov</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>OTh</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>oth</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>csu</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>HOU</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ASS</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>E530</td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
            </tr>
        
            <tr>
                <td>RCPT</td>
                <td>Receipt</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71">71</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p37">37</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p74">74</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p40">40</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p30">30</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


tran_type
----------------

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
                <td>F</td>
                <td>Forgiven Loan</td>
            </tr>
        
            <tr>
                <td>I</td>
                <td>Intermediary</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>Returned (Negative Amount?)</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>Third Party Repayment</td>
            </tr>
        
            <tr>
                <td>X</td>
                <td>Transfer</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>I</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>M</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p72">72</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p38">38</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29">29</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`13 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p13>`_, `118-121 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p118>`_)

* MapCalFormat2Fields (`71-75 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p71>`_)

* Cal-Format-201 (`37-41 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p37>`_)

* Cal-Format-1-05-02 (`29-30 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p29>`_)






------------

*********************
CVR3_VERIFICATION_INFO_CD
*********************

Cover page verification information from campaign disclosure forms

The records in CVR3_VERIFICATION_INFO_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR3_VERIFICATION_INFO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR3_VERIFICATION_INFO_CD.TSV>`_


Filing forms
============



* `Form 400 <../filingforms/campaign_forms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization)): Part 5, Verification



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Cover Page



* `Form 402 <../filingforms/campaign_forms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization)): Verification



* `Form 410 <../filingforms/campaign_forms.html#form-410>`_ (Statement of Organization Recipient Committee): Part 3, Verification



* `Form 425 <../filingforms/campaign_forms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 3, Verification



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 4, Verification



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page



* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement): Part 4, Verification



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 6, Verification



* `Form 511 <../filingforms/campaign_forms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR3</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 39)</td>
            <td>No</td>
            <td>City and state where signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 56)</td>
            <td>No</td>
            <td>Last name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Title of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Suffix of the signer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>CVR3</td>
                <td>Cover Page 3, Verification Information</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25">25</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50">50</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 5, Verification</td>
            </tr>
        
            <tr>
                <td>F401</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Cover Page</td>
            </tr>
        
            <tr>
                <td>F402</td>
                <td>Form 402 (Statement of Termination (Slate Mailer Organization)): Verification</td>
            </tr>
        
            <tr>
                <td>F410</td>
                <td>Form 410 (Statement of Organization Recipient Committee): Part 3, Verification</td>
            </tr>
        
            <tr>
                <td>F425</td>
                <td>Form 425 (Semi-Annual Statement of no Activity): Part 3, Verification</td>
            </tr>
        
            <tr>
                <td>F450</td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 4, Verification</td>
            </tr>
        
            <tr>
                <td>F460</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Cover Page</td>
            </tr>
        
            <tr>
                <td>F461</td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 4, Verification</td>
            </tr>
        
            <tr>
                <td>F465</td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 6, Verification</td>
            </tr>
        
            <tr>
                <td>F511</td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64">64</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50">50</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>ATR</td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>SPO</td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td>atr</td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td>tre</td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td>cao</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>MDI</td>
                <td>Major Donor/Ind Expenditure</td>
            </tr>
        
            <tr>
                <td>POF</td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>COA</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BBB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MAI</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p11">11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34">34</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p9">9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25">25</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`46-47 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p46>`_)

* MapCalFormat2Fields (`41-42 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p41>`_)

* Cal-Format-201 (`34 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p34>`_, `64 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p64>`_)

* Cal-Format-1-05-02 (`25 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p25>`_, `50 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p50>`_)






------------

*********************
LOAN_CD
*********************

Loans received and made by recepient committees

The records in LOAN_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LOAN_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOAN_CD.TSV>`_


Filing forms
============



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule B - Part 3, Outstanding Bal

    * Schedule H, Loans Made to Others

    * Schedule H - Part 1, Loans Made

    * Schedule H- Part 2, Repayments Rcvd

    * Schedule H - Part 3, Outstanding Loans





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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the lender</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 2)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>intr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>intr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Lender&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Lender&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt1</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Repaid or forgiven amount; Original loan amount. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt2</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding Principal; unpaid balance. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt3</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Interest Paid; Unpaid interest; Interest received. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt4</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Amount/Other. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt5</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt6</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt7</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt8</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Lender&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>loan_date1</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the loan was made or recieved. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_date2</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date repaid/forgiven; date loan due. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Loan employer. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Loan occupation. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_rate</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Interest Rate. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>loan_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Lender&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>loan_type</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Type of loan</td>
        </tr>
    
    
    
        <tr>
            <td>loan_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOAN</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &quot;X&quot; indicates this condition is true.</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Form 460 Schedule &#39;A&#39; or &#39;E&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>B1</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
            </tr>
        
            <tr>
                <td>B2</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
            </tr>
        
            <tr>
                <td>B3</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 3, Outstanding Bal</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
            </tr>
        
            <tr>
                <td>H1</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 1, Loans Made</td>
            </tr>
        
            <tr>
                <td>H2</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H- Part 2, Repayments Rcvd</td>
            </tr>
        
            <tr>
                <td>H3</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 3, Outstanding Loans</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


loan_type
----------------

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
                <td>H2T</td>
                <td>Third party payment</td>
            </tr>
        
            <tr>
                <td>H2F</td>
                <td>Forgiven</td>
            </tr>
        
            <tr>
                <td>H2R</td>
                <td>Repay</td>
            </tr>
        
            <tr>
                <td>B2T</td>
                <td>Third party payment</td>
            </tr>
        
            <tr>
                <td>B2F</td>
                <td>Forgiven</td>
            </tr>
        
            <tr>
                <td>B2R</td>
                <td>Repay</td>
            </tr>
        
            <tr>
                <td>B1G</td>
                <td>Guarantor</td>
            </tr>
        
            <tr>
                <td>B1L</td>
                <td>Lender</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>LOAN</td>
                <td>LOAN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47">47</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35">35</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`87-90 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p87>`_)

* MapCalFormat2Fields (`60-63 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p60>`_)

* Cal-Format-201 (`47-50 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p47>`_)

* Cal-Format-1-05-02 (`35-39 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p35>`_)






------------

*********************
S401_CD
*********************

Form 401 (Slate Mailer Organization) payment and other
disclosure schedules (F401B, F401B-1, F401C, F401D) information. Does not
include Form 401, Schedule A (Payments Received).

The records in S401_CD are unique by FILING_ID, AMEND_ID, LINE_ID, REC_TYPE and FORM_TYPE.

**Sample:** `S401_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S401_CD.TSV>`_


Filing forms
============



* `Form 401 <../filingforms/campaign_forms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)

    * Schedule B, Payments Made

    * Schedule B-1, Payments Made by Agent or Independent Contractor

    * Schedule C, Persons Receiving $1,000 or More

    * Schedule D, Candidates and Measures Not Listed on Schedule A





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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>No</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S401</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>agent_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namt</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>agent_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s title or prefix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee&#39;s city address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount (Sched F401B, 401B-1, 401C)</td>
        </tr>
    
    
    
        <tr>
            <td>aggregate</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Aggregate year-to-date amount (Sched 401C)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>S401</td>
                <td>S401</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51">51</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F401B</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td>F401B-1</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
            </tr>
        
            <tr>
                <td>F401C</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule C, Persons Receiving $1,000 or More</td>
            </tr>
        
            <tr>
                <td>F401D</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule D, Candidates and Measures Not Listed on Schedule A</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51">51</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ltg</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>OTh</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>att</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>oth</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>tre</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>con</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>boe</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>sos</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>sup</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>SAC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ca</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CAL</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AL</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>10</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p77">77</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>HELD</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p52">52</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39">39</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`123-124 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p123>`_)

* MapCalFormat2Fields (`76-78 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p76>`_)

* Cal-Format-201 (`51-52 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p51>`_)

* Cal-Format-1-05-02 (`39 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p39>`_)






------------

*********************
EXPN_CD
*********************

Campaign expenditures from a variety of forms, excluding Late Independent
Expenditures (from Form 496)

The records in EXPN_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `EXPN_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EXPN_CD.TSV>`_


Filing forms
============



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule E, Payments Made

    * Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)




* `Form 461 <../filingforms/campaign_forms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made



* `Form 465 <../filingforms/campaign_forms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made



* `Form 900 <../filingforms/campaign_forms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




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
            <td>agent_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Last name (Sched G)</td>
        </tr>
    
    
    
        <tr>
            <td>agent_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of Payment</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a Tran_ID of a &#39;parent&#39; record</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot Measure Name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot Number or Letter</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (If [COM|RCP] &amp; no ID#, Treas info Req.)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_oth</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / &#39;Other&#39; (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_ytd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / Year-to-date amount         (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_chkno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Check Number (Optional)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_code</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>CTB &amp; IND need explanation &amp; listing on Sched D TRC &amp; TRS require explanation</td>
        </tr>
    
    
    
        <tr>
            <td>expn_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Expenditure (Note: Date not on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>g_from_e_f</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Back Reference from Sched G to Sched &#39;E&#39; or &#39;F&#39;?</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description         (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo Amount? (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (Req. if Office_Cd=OTH)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee City</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State code</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip+4</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: EXPN</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer City</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s First name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s Last name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer State</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>X = Related item on other Sched has same Tran_ID</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related item is included on Sched &#39;C&#39; or &#39;H2&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>MBR</td>
                <td>Member of Associaton</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PTH</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RFD</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


expn_code
----------------

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
                <td>CMP</td>
                <td>campaign paraphernalia/miscellaneous</td>
            </tr>
        
            <tr>
                <td>CNS</td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td>CTB</td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td>CVC</td>
                <td>civic donations</td>
            </tr>
        
            <tr>
                <td>FIL</td>
                <td>candidate filing/ballot feeds</td>
            </tr>
        
            <tr>
                <td>FND</td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td>IKD</td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>independent expenditure supporting/opposing others (explain)*</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>legal defense</td>
            </tr>
        
            <tr>
                <td>LIT</td>
                <td>campaign literature and mailings</td>
            </tr>
        
            <tr>
                <td>LON</td>
                <td>loan</td>
            </tr>
        
            <tr>
                <td>MBR</td>
                <td>member communications</td>
            </tr>
        
            <tr>
                <td>MON</td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td>MTG</td>
                <td>meetings and appearances</td>
            </tr>
        
            <tr>
                <td>OFC</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td>PET</td>
                <td>petition circulating</td>
            </tr>
        
            <tr>
                <td>PHO</td>
                <td>phone banks</td>
            </tr>
        
            <tr>
                <td>POL</td>
                <td>polling and survey research</td>
            </tr>
        
            <tr>
                <td>POS</td>
                <td>postage, delivery and messenger services</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>professional services (legal, accounting)</td>
            </tr>
        
            <tr>
                <td>PRT</td>
                <td>print ads</td>
            </tr>
        
            <tr>
                <td>RAD</td>
                <td>radio airtime and production costs</td>
            </tr>
        
            <tr>
                <td>RFD</td>
                <td>returned contributions</td>
            </tr>
        
            <tr>
                <td>SAL</td>
                <td>campaign workers salaries</td>
            </tr>
        
            <tr>
                <td>TEL</td>
                <td>T.V. or cable airtime and production costs</td>
            </tr>
        
            <tr>
                <td>TRC</td>
                <td>candidate travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>staff/spouse travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td>TSF</td>
                <td>transfer between committees of the same candidate/sponsor</td>
            </tr>
        
            <tr>
                <td>VOT</td>
                <td>voter registration</td>
            </tr>
        
            <tr>
                <td>WEB</td>
                <td>information technology costs (internet, e-mail)</td>
            </tr>
        
            <tr>
                <td>ctb</td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td>ikd</td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td>Mon</td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td>ofc</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td>OFc</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td>Ofc</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>*</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>001</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>011</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>200</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>401</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ADV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ANN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>APR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AUG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AUT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Ban</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BAN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BOO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BOX</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CHE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CIV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CNT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>COP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CRE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CSN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>,CT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>.CT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CTN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CVD</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DEC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Dem</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DIN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Don</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Ear</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>EIM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>EMP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FAX</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FDN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FEE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FIN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Fun</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FUN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GGG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GOT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>IEs</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>IN-</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Ina</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>INK</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ITE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JAN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JUL</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JUN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>KIC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>L</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LEV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Lit</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LN#</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LOG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>M</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MAI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Mar</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MAR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MEE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MGT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Mis</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MRB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NGP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NOT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NOV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OCT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>.OF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OPE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>P</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Pac</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PAI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PAR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PAY</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PMT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>.PO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Pos</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PRE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PRI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PRP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>.Re</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>.RE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>REF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>REI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RFP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S-A</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Sal</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S C</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S.C</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SCU</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SEE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SEP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S.M.</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SOF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SWI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TAX</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TB,</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TIC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Tor</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TRA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TRF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TRV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>UN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>UTI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>V</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>VEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>-VO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>VOI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>VOY</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>WI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>x</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>X</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S-6</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S.M</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S-4</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SA:</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>100</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RFN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>REN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>003</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S-1</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>08</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p13">13-14</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p11">11</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F450P5</td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
            </tr>
        
            <tr>
                <td>D</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
            </tr>
        
            <tr>
                <td>E</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule E, Payments Made</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
            </tr>
        
            <tr>
                <td>F461P5</td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made</td>
            </tr>
        
            <tr>
                <td>F465P3</td>
                <td>Form 465 (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>Cit</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>Sen</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>stw</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>APP</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>ES</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>SM</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>12</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>4</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>8</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>27</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>93</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>98</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>CLB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Boa</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>Sta</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SAN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ES </td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LBC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>WES</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>(Lo</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>(Ci</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>vty</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SM </td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ASS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ADM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SAC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>US</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>J</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LOS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>IRV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JRS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NEV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>IB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Ass</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SD</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>D</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SEC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>RB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>h</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>a</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>8</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>Cou</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>AtT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>May</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>Sen</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>gov</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>Gov</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>LA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>HOU</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LAD</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>11A</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>001</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AS1</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ASS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>73</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>HSE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CO</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PAC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>REP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>031</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ASB</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>NAT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SWE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>ST</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PRE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>/S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>U S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>8</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>C:S</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>EXPN</td>
                <td>Expense</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42">42</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31">31</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SUPPORT</td>
            </tr>
        
            <tr>
                <td>o</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>X</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>Y</td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p44">44</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p32">32</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `53-56 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p53>`_)

* MapCalFormat2Fields (`45-48 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p45>`_)

* Cal-Format-201 (`42-44 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p42>`_)

* Cal-Format-1-05-02 (`31-32 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p31>`_)






------------

*********************
F495P2_CD
*********************

Form 495 Supplemental Pre-Election Campaign Statement, attached to
Recipient Committee Campaign Statements (Forms 450 and 460).

The records in F495P2_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_ITEM and FORM_TYPE.

**Sample:** `F495P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F495P2_CD.TSV>`_


Filing forms
============



* `Form 450 <../filingforms/campaign_forms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement)




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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type Value: F495</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form to which the Form 495 is attached (must equal Form_Type in CVR record)</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election This date will be the same as on the filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td>electjuris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of the election</td>
        </tr>
    
    
    
        <tr>
            <td>contribamt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Contribution amount (For the period of 6 months prior to 17 days before the election)</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>F495</td>
                <td>F495</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35">35</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26">26</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F450</td>
                <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
            </tr>
        
            <tr>
                <td>F460</td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35">35</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26">26</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`56-57 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p56>`_)

* MapCalFormat2Fields (`49 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p49>`_)

* Cal-Format-201 (`35 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p35>`_)

* Cal-Format-1-05-02 (`26 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p26>`_)






------------

*********************
DEBT_CD
*********************

Records of unpaid bills accrued by Recipient Campaigns, as listed on
Form 460, Schedule F (Accrued Expenses).

The records in DEBT_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `DEBT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/DEBT_CD.TSV>`_


Filing forms
============



* `Form 460 <../filingforms/campaign_forms.html#form-460>`_ (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amt_incur</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount incurred this period</td>
        </tr>
    
    
    
        <tr>
            <td>amt_paid</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount paid this period.</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to a transaction identifier of a parent record.</td>
        </tr>
    
    
    
        <tr>
            <td>beg_bal</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at beginning of period</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>end_bal</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at close of this period</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_code</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Expense Code</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number of the parent filing</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Schedule Name/ID: (F - Sched F / Accrued Expenses)</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Record line item number</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>First line of the payee&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual.</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s name suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Payee&#39;s prefix or title if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type value: DEBT</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction identifier - permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. /&quot;X/&quot; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Schedule C.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


expn_code
----------------

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
                <td>CMP</td>
                <td>campaign paraphernalia/miscellaneous</td>
            </tr>
        
            <tr>
                <td>CNS</td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td>CTB</td>
                <td>contribution (if nonmonetary, explain)*</td>
            </tr>
        
            <tr>
                <td>CVC</td>
                <td>civic donations</td>
            </tr>
        
            <tr>
                <td>FIL</td>
                <td>candidate filing/ballot feeds</td>
            </tr>
        
            <tr>
                <td>FND</td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td>IKD</td>
                <td>In-kind contribution (nonmonetary)</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>independent expenditure supporting/opposing others (explain)*</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>legal defense</td>
            </tr>
        
            <tr>
                <td>LIT</td>
                <td>campaign literature and mailings</td>
            </tr>
        
            <tr>
                <td>LON</td>
                <td>loan</td>
            </tr>
        
            <tr>
                <td>MBR</td>
                <td>member communications</td>
            </tr>
        
            <tr>
                <td>MON</td>
                <td>monetary contribution</td>
            </tr>
        
            <tr>
                <td>MTG</td>
                <td>meetings and appearances</td>
            </tr>
        
            <tr>
                <td>OFC</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td>PET</td>
                <td>petition circulating</td>
            </tr>
        
            <tr>
                <td>PHO</td>
                <td>phone banks</td>
            </tr>
        
            <tr>
                <td>POL</td>
                <td>polling and survey research</td>
            </tr>
        
            <tr>
                <td>POS</td>
                <td>postage, delivery and messenger services</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>professional services (legal, accounting)</td>
            </tr>
        
            <tr>
                <td>PRT</td>
                <td>print ads</td>
            </tr>
        
            <tr>
                <td>RAD</td>
                <td>radio airtime and production costs</td>
            </tr>
        
            <tr>
                <td>RFD</td>
                <td>returned contributions</td>
            </tr>
        
            <tr>
                <td>SAL</td>
                <td>campaign workers salaries</td>
            </tr>
        
            <tr>
                <td>TEL</td>
                <td>T.V. or cable airtime and production costs</td>
            </tr>
        
            <tr>
                <td>TRC</td>
                <td>candidate travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>staff/spouse travel, lodging and meals (explain)</td>
            </tr>
        
            <tr>
                <td>TSF</td>
                <td>transfer between committees of the same candidate/sponsor</td>
            </tr>
        
            <tr>
                <td>VOT</td>
                <td>voter registration</td>
            </tr>
        
            <tr>
                <td>WEB</td>
                <td>information technology costs (internet, e-mail)</td>
            </tr>
        
            <tr>
                <td>Fnd</td>
                <td>fundraising events</td>
            </tr>
        
            <tr>
                <td>ofc</td>
                <td>office expenses</td>
            </tr>
        
            <tr>
                <td>&#39;CN</td>
                <td>campaign consultants</td>
            </tr>
        
            <tr>
                <td>*</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>AIR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>BUS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CAM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CSN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>DEP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>EVE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>fns</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>GGG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>HOT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>L</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LDF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>MEE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>P</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>PEN</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>SPE</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TAX</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>TRA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>V</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>X</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p13">13-14</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p11">11</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>DEBT</td>
                <td>DEBT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45">45-46</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33">33-34</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`47-49 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p47>`_)

* MapCalFormat2Fields (`49-48 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p49>`_)

* Cal-Format-201 (`45-46 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p45>`_)

* Cal-Format-1-05-02 (`33-34 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p33>`_)






------------

*********************
S496_CD
*********************

Records of expenditures made by Independent Expenditure Committees in the 90
days preceding an election.

The records in S496_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `S496_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S496_CD.TSV>`_


Filing forms
============



* `Form 496 <../filingforms/campaign_forms.html#form-496>`_ (Late Independent Expenditure Report)




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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S496</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Expenditure amount</td>
        </tr>
    
    
    
        <tr>
            <td>exp_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Expenditure dates</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items paid</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>S496</td>
                <td>S496</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53">53</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40">40</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F496</td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53">53</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40">40</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `124-125 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p124>`_)

* MapCalFormat2Fields (`79 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p79>`_)

* Cal-Format-201 (`53 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p53>`_)

* Cal-Format-1-05-02 (`40 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p40>`_)






------------

*********************
S497_CD
*********************

Campaign Committee contributions received or made in the 90 days before an
election, as reported on Form 497.

The records in S497_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `S497_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S497_CD.TSV>`_


Filing forms
============



* `Form 497 <../filingforms/campaign_forms.html#form-497>`_ (Late Contribution Report)

    * Part 1, Contribution(s) Received

    * Part 2, Contribution(s) Made





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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S497</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name title or prefix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name suffix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Contributor self-employed checkbox. &quot;X&quot; indicates the contributor is self-employed.</td>
        </tr>
    
    
    
        <tr>
            <td>elec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received/made</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received/made</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Jurisdiction code describing the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in TEXT code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cand_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>sup_off_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>S497</td>
                <td>S497</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F497P1</td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td>F497P2</td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>com</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54">54</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41">41</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>Asm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>May</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>ASm</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>oth</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>csu</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>Oth</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>HOU</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>P</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LTV</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>LT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>REP</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>N/A</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>asm</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>sen</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>cit</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>CLB</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>IRV</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>Fon</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>JRS</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>CO</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>Riv</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>SNE</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>83</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FED</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>CA</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>JR</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p55">55</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p42">42</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>s</td>
                <td>SOUGHT</td>
            </tr>
        
            <tr>
                <td>h</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>UNKNOWN</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p55">55</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p42">42</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p82">82</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `125-127 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p125>`_)

* MapCalFormat2Fields (`80-82 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p80>`_)

* Cal-Format-201 (`54-55 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p54>`_)

* Cal-Format-1-05-02 (`41-42 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p41>`_)






------------

*********************
F501_502_CD
*********************

Candidate Intention Statements (Forms 501 and 502), including a record
for the original filing and each amendment.

The records in F501_502_CD are unique by FILING_ID and AMEND_ID.

**Sample:** `F501_502_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F501_502_CD.TSV>`_


Filing forms
============



* `Form 501 <../filingforms/campaign_forms.html#form-501>`_ (Candidate Intention Statement)



* `Form 502 <../filingforms/campaign_forms.html#form-502>`_ (Campaign Bank Account Statement)




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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>committee_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>can_namm</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder middle name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>moniker_pos</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Location of the candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>moniker</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officerholder city</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder state</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder zip +4</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone number</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officerholder fax</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email address</td>
        </tr>
    
    
    
        <tr>
            <td>fin_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Financial institution&#39;s business name</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s title.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Financial institution&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Financial institution&#39;s state.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Financial institution&#39;s zip code.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s FAX Number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Financial institution&#39;s e-mail address.</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 80)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>agency_nam</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agency name</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>party</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Political party</td>
        </tr>
    
    
    
        <tr>
            <td>yr_of_elec</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td>elec_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td>execute_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Execution date</td>
        </tr>
    
    
    
        <tr>
            <td>can_sig</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate signature</td>
        </tr>
    
    
    
        <tr>
            <td>account_no</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Account number</td>
        </tr>
    
    
    
        <tr>
            <td>acct_op_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Account open date</td>
        </tr>
    
    
    
        <tr>
            <td>party_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Party code</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>accept_limit_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>did_exceed_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cntrb_prsnl_fnds_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>CVR</td>
                <td>CVR</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p58">58</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F501</td>
                <td>Form 501: Candidate Intention Statement</td>
            </tr>
        
            <tr>
                <td>F502</td>
                <td>Form 502: Campaign Bank Account Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p58">58</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>ATH</td>
                <td>Authorizing individual</td>
            </tr>
        
            <tr>
                <td>ATR</td>
                <td>Assistant treasurer</td>
            </tr>
        
            <tr>
                <td>BMC</td>
                <td>Ballot measure committee</td>
            </tr>
        
            <tr>
                <td>BNM</td>
                <td>Ballot measure&#39;s name/title</td>
            </tr>
        
            <tr>
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
                <td>Controlled committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>MDI</td>
                <td>Major Donor/Ind Expenditure</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>POF</td>
                <td>Principal officer</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>PTY</td>
                <td>Political Party</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SCC</td>
                <td>Small Contributor Committee</td>
            </tr>
        
            <tr>
                <td>SMO</td>
                <td>Slate-mailer organization</td>
            </tr>
        
            <tr>
                <td>SPO</td>
                <td>Sponsor</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>Treasurer</td>
            </tr>
        
            <tr>
                <td>8</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


stmt_type
----------------

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
                <td>10001</td>
                <td>ORIGINAL/INITIAL</td>
            </tr>
        
            <tr>
                <td>10002</td>
                <td>AMENDMENT</td>
            </tr>
        
            <tr>
                <td>10003</td>
                <td>TERMINATION</td>
            </tr>
        
            <tr>
                <td>10004</td>
                <td>REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE</td>
            </tr>
        
            <tr>
                <td>10005</td>
                <td>LOG</td>
            </tr>
        
            <tr>
                <td>10006</td>
                <td>LOG/AMENDMENT</td>
            </tr>
        
            <tr>
                <td>10007</td>
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


office_cd
----------------

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
                <td>30001</td>
                <td>PRESIDENT</td>
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


juris_cd
----------------

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
                <td>40507</td>
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


elec_type
----------------

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
                <td>3007</td>
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


party_cd
----------------

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
                <td>16014</td>
                <td>UNKNOWN</td>
            </tr>
        
            <tr>
                <td>16020</td>
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


district_cd
----------------

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
                <td>17012</td>
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



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `57-59 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p57>`_)






------------

*********************
S498_CD
*********************

Payments received by Slate Mailer Organizations within 90 days of an election,
as reported on Form 498.

The records in S498_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `S498_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S498_CD.TSV>`_


Filing forms
============



* `Form 498 <../filingforms/campaign_forms.html#form-498>`_ (Slate Mailer Late Payment Report)

    * Part A, Late Payments Attributed To

    * Part R, Late Payments Received From





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
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S498</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>payor_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>payor_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payor&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s Prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payor&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payor&#39;s State.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td>date_rcvd</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td>amt_rcvd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Description of office sought</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter.</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>amt_attrib</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount attributed (only if Form_type = &#39;F498-A&#39;)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flat</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference text contained in TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>occupation</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>selfemp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


rec_type
----------------

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
                <td>S498</td>
                <td>S498</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F498-A</td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
            </tr>
        
            <tr>
                <td>F498-R</td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


entity_cd
----------------

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
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>COM</td>
                <td>Committee</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>RCP</td>
                <td>Recipient committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p9">9-11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56">56</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p8">8-9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
            <tr>
                <td>gov</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>oth</td>
                <td>Other</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Errata-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201.html#document/p2">2</a>),  Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p12">12</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p10">10</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Statewide</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p44">44</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


sup_opp_cd
----------------

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
                <td>O</td>
                <td>OPPOSITION</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SUPPORT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p57">57</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43">43</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`12 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p12>`_, `127-129 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p127>`_)

* MapCalFormat2Fields (`83-85 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p83>`_)

* Cal-Format-201 (`56-57 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p56>`_)

* Cal-Format-1-05-02 (`43-44 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p43>`_)






------------

*********************
CVR_F470_CD
*********************

Cover page information for Officeholder and Candidate Short and Supplement Forms
(Form 470)

The records in CVR_F470_CD are unique by FILING_ID, AMEND_ID, REC_TYPE and FORM_TYPE.

**Sample:** `CVR_F470_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_F470_CD.TSV>`_


Filing forms
============



* `Form 470 <../filingforms/campaign_forms.html#form-470>`_ (Officeholder and Candidate Campaign Statement, Short Form)




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment Identification number. A number of 0 is an original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_adr1</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First line of the filer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_adr2</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Second line of the filer&#39;s street address. </td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s City.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s EMail address. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s FAX Phone Number. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s zipcode</td>
        </tr>
    
    
    
        <tr>
            <td>date_1000</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date contributions totaling $1,000 or more. (For the 470-S)</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the general election. Required for filings in even years.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>The filer&#39;s entity code. The value of this column will always be Candidate/Office Holder (CAO) for this table.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s First Name(s) - required for individuals</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer&#39;s Last Name/Committee name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s Name Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The filer&#39;s prefix or title that preceeds their name if they are an individual.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Type of Filing or Formset. The value of this column will always be equal to F470.</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description text reqired if the jurisdiction code (Juris_cd) is equal to CIT, CTY, LOC, or OTH.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office Sought/Held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held.</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office code is other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Code that identifies the office being sought. See the CAL document for a list of valid codes.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 3)</td>
            <td>Yes</td>
            <td>Type of CAL record. This column will always contain CVR.</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended as reported in the filing.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed as reported by the filer.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_cd
----------------

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
                <td>CAO</td>
                <td>Candidate/officeholder</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


form_type
----------------

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
                <td>F470</td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


juris_cd
----------------

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
                <td>ASM</td>
                <td>Assembly District</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization District</td>
            </tr>
        
            <tr>
                <td>CIT</td>
                <td>City</td>
            </tr>
        
            <tr>
                <td>CTY</td>
                <td>County</td>
            </tr>
        
            <tr>
                <td>LOC</td>
                <td>Local</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>Senate District</td>
            </tr>
        
            <tr>
                <td>STW</td>
                <td>Statewide</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


off_s_h_cd
----------------

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
                <td>H</td>
                <td>HELD</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SOUGHT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p30">30</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


office_cd
----------------

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
                <td>APP</td>
                <td>State Appellate Court Justice</td>
            </tr>
        
            <tr>
                <td>ASM</td>
                <td>State Assembly Person</td>
            </tr>
        
            <tr>
                <td>ASR</td>
                <td>Assessor</td>
            </tr>
        
            <tr>
                <td>ATT</td>
                <td>Attorney General</td>
            </tr>
        
            <tr>
                <td>BED</td>
                <td>Board of Education</td>
            </tr>
        
            <tr>
                <td>BOE</td>
                <td>Board of Equalization Member</td>
            </tr>
        
            <tr>
                <td>BSU</td>
                <td>Board of Supervisors</td>
            </tr>
        
            <tr>
                <td>CAT</td>
                <td>City Attorney</td>
            </tr>
        
            <tr>
                <td>CCB</td>
                <td>Community College Board</td>
            </tr>
        
            <tr>
                <td>CCM</td>
                <td>City Council Member</td>
            </tr>
        
            <tr>
                <td>CON</td>
                <td>State Controller</td>
            </tr>
        
            <tr>
                <td>COU</td>
                <td>County Counsel</td>
            </tr>
        
            <tr>
                <td>CSU</td>
                <td>County Supervisor</td>
            </tr>
        
            <tr>
                <td>CTR</td>
                <td>Local Controller</td>
            </tr>
        
            <tr>
                <td>DAT</td>
                <td>District Attorney</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Governor</td>
            </tr>
        
            <tr>
                <td>INS</td>
                <td>Insurance Commissioner</td>
            </tr>
        
            <tr>
                <td>LTG</td>
                <td>Lieutenant Governor</td>
            </tr>
        
            <tr>
                <td>MAY</td>
                <td>Mayor</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PDR</td>
                <td>Public Defender</td>
            </tr>
        
            <tr>
                <td>PER</td>
                <td>Public Employees Retirement System</td>
            </tr>
        
            <tr>
                <td>PLN</td>
                <td>Planning Commissioner</td>
            </tr>
        
            <tr>
                <td>SCJ</td>
                <td>Superior Court Judge</td>
            </tr>
        
            <tr>
                <td>SEN</td>
                <td>State Senator</td>
            </tr>
        
            <tr>
                <td>SHC</td>
                <td>Sheriff-Coroner</td>
            </tr>
        
            <tr>
                <td>SOS</td>
                <td>Secretary of State</td>
            </tr>
        
            <tr>
                <td>SPM</td>
                <td>Supreme Court Justice</td>
            </tr>
        
            <tr>
                <td>SUP</td>
                <td>Superintendent of Public Instruction</td>
            </tr>
        
            <tr>
                <td>TRE</td>
                <td>State Treasurer</td>
            </tr>
        
            <tr>
                <td>TRS</td>
                <td>Local Treasurer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


rec_type
----------------

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
                <td>CVR</td>
                <td>Cover Page</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: 
                 Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29">29</a>),  Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22">22</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CalAccessTablesWeb (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `30-32 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p30>`_)

* MapCalFormat2Fields (`15-16 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p15>`_)

* Cal-Format-201 (`29-30 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p29>`_)

* Cal-Format-1-05-02 (`22 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p22>`_)





