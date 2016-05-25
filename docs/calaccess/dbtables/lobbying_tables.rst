.. This document was generated programmatically via the createcalaccessrawdbtabledocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the lobbying_tables.rst file in ./src/toolbox/templates/ or in the commands internal logic.

================================
Lobbying tables
================================


The CAL-ACCESS database contains 32 tables that, according to the official documentation (see `here <https://www.documentcloud.org/documents/2711617-ReadMe-Zip/pages/1.html>`_ and `here <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/4.html>`_), store information specific to lobbying disclosure filings. These tables are outlined below.



------------

*********************
CVR_REGISTRATION_CD
*********************

Cover page of lobbying disclosure forms (601, 602, 603, 604, 606, and 607)

**Sample:** `CVR_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_REGISTRATION_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
            <td><code>A_B_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Individual or business entity city</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_B_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of individual or business entity</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_B_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Individual or business entity state</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_B_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Individual or business entity ZIP Code.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AUTH_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>AUTH_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Authorized lobbying firm business name. Applies to Form 602.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AUTH_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address state</td>
        </tr>
    
    
    
        <tr>
            <td><code>AUTH_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Business included activity checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer business address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_CLASS</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classifiction values of business related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_DESCR</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of business classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_EMAIL</code></td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer business address email</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_FAX</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address fax number</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer business address state</td>
        </tr>
    
    
    
        <tr>
            <td><code>BUS_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>C_LESS50</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with fewer than 50 members check this box</td>
        </tr>
    
    
    
        <tr>
            <td><code>C_MORE50</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with more than 50 check this box.</td>
        </tr>
    
    
    
        <tr>
            <td><code>COMPLET_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ethics orientation class completion date. Applies to Form 604. As filed by the lobbyist.</td>
        </tr>
    
    
    
        <tr>
            <td><code>DESCRIP_1</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of business activity, industry or other</td>
        </tr>
    
    
    
        <tr>
            <td><code>DESCRIP_2</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of specific or other lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFF_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date of authoarization or termination</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
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
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the lobbyist employer or firm. Applies to Forms 604, 606, 607.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>IND_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Individual checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>IND_CLASS</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classification values to category industry related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td><code>IND_DESCR</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of industry classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td><code>INFLUEN_YN</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Attempt to influence state legislation</td>
        </tr>
    
    
    
        <tr>
            <td><code>L_FIRM_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying firm within the ... &#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_604_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in this 604 statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_REG_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in form 601/603 registration statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBY_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying within the meaning...&#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBY_INT</code></td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of Part III lobbying interests. Applies to Form 603</td>
        </tr>
    
    
    
        <tr>
            <td><code>LS_BEG_YR</code></td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative session begins</td>
        </tr>
    
    
    
        <tr>
            <td><code>LS_END_YR</code></td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative sessions ends</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 2)</td>
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
            <td><code>NEWCERT_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will require a new certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTH_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>QUAL_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified. Applies to forms 601 and 603. Only occurs once in lobbying filings.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td><code>RENCERT_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will take a renewel certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>REPORT_NUM</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number as reported by the filer. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report or amendment is filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>SENDER_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the lobbyist entity submitting this report. This is equal to the filer ID if the filer is the submitting the report and the firm or employer if they are submitting the report.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date signed</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_LOC</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_TITLE</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td><code>ST_AGENCY</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>List of identified state agencies. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ST_LEG_YN</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will lobby state legislature checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td><code>STMT_FIRM</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Lobby firm named in &#39;Statement of Responsible Officer&#39;This field only applies to Form 601.</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRADE_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry, trade or professional checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``bus_class``
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
                <td><code>ENT</code></td>
                <td>Entertainment/Recreation</td>
            </tr>
        
            <tr>
                <td><code>FIN</code></td>
                <td>Finance/Insurance</td>
            </tr>
        
            <tr>
                <td><code>LOG</code></td>
                <td>Lodging/Restaurants</td>
            </tr>
        
            <tr>
                <td><code>MAN</code></td>
                <td>Manufacturing/Industrial</td>
            </tr>
        
            <tr>
                <td><code>MER</code></td>
                <td>Merchandise/Retail</td>
            </tr>
        
            <tr>
                <td><code>OIL</code></td>
                <td>Oil and Gas</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>PRO</code></td>
                <td>Professional/Trade</td>
            </tr>
        
            <tr>
                <td><code>REA</code></td>
                <td>Real Estate</td>
            </tr>
        
            <tr>
                <td><code>TRN</code></td>
                <td>Transportation</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p70">70</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82">82</a>)
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
                <td><code>BUS</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FRM</code></td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>LBY</code></td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td><code>LCO</code></td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>LEM</code></td>
                <td>Lobbying Employer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p68">68</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82">82</a>)
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p68">68</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82">82</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``ind_class``
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
                <td><code>AGR</code></td>
                <td>Agriculture</td>
            </tr>
        
            <tr>
                <td><code>EDU</code></td>
                <td>Education</td>
            </tr>
        
            <tr>
                <td><code>GOV</code></td>
                <td>Government</td>
            </tr>
        
            <tr>
                <td><code>HEA</code></td>
                <td>Health</td>
            </tr>
        
            <tr>
                <td><code>LAB</code></td>
                <td>Labor Unions</td>
            </tr>
        
            <tr>
                <td><code>LEG</code></td>
                <td>Legal</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>POL</code></td>
                <td>Political Organizations</td>
            </tr>
        
            <tr>
                <td><code>PUB</code></td>
                <td>Public Employees</td>
            </tr>
        
            <tr>
                <td><code>UTL</code></td>
                <td>Utilities</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p70">70</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p85">85</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``influen_yn``
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
                <td><code>Y</code></td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td><code>y</code></td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>No</td>
            </tr>
        
            <tr>
                <td><code>n</code></td>
                <td>No</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Yes</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p71">71</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p86">86</a>)
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
                <td>CVR</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p68">68</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82">82</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``st_leg_yn``
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
                <td><code>Y</code></td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td><code>y</code></td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td><code>N</code></td>
                <td>No</td>
            </tr>
        
            <tr>
                <td><code>n</code></td>
                <td>No</td>
            </tr>
        
            <tr>
                <td><code>X</code></td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td><code>x</code></td>
                <td>Yes</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p71">71</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p86">86</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`82-86 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82>`_)

* Map from .CAL Format to Database Table and Fields (`22-27 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p22>`_)

* .CAL Format Layout (Version 1.05.02) (`68-71 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p68>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `35-39 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p35>`_)






------------

*********************
CVR2_REGISTRATION_CD
*********************

Cover page of lobbying disclosure forms

**Sample:** `CVR2_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_REGISTRATION_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 10)</td>
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
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
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
                <td><code>CVR2</code></td>
                <td>CVR2</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p72">72</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p87">87</a>)
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p72">72</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p87">87</a>)
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
                <td><code>AGY</code></td>
                <td>State Agency</td>
            </tr>
        
            <tr>
                <td><code>EMP</code></td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td><code>FRM</code></td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>LBY</code></td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td><code>MBR</code></td>
                <td>Member of Associaton</td>
            </tr>
        
            <tr>
                <td><code>SCL</code></td>
                <td>Subcontracted Client</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p72">72</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p87">87</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`87-88 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p87>`_)

* Map from .CAL Format to Database Table and Fields (`37-37 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p37>`_)

* .CAL Format Layout (Version 1.05.02) (`72-73 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p72>`_)

* CAL-ACCESS Tables, Columns and Indexes (`44-45 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p44>`_)






------------

*********************
CVR_LOBBY_DISCLOSURE_CD
*********************

Cover page information for lobbying disclosure forms

**Sample:** `CVR_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_LOBBY_DISCLOSURE_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_N_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_Y_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_BEG_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning date</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
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
            <td>Filer last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition business city</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition business phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition business state</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Form, employer or coalition business ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>FROM_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_ACTVTY</code></td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Description of lobbying activity. Applies to forms 635 and 645. Additional description may be provided in text records.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBY_N_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity none&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOBBY_Y_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity Form 630 attached&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAIL_ST</code></td>
            <td>String (up to 2)</td>
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
            <td><code>MAJOR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Major donor first name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAJOR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Major donor last name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAJOR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor suffix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>MAJOR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor title or prefix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td><code>NOPART1_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part I information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td><code>NOPART2_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part II information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PART1_1_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners Form 615 attached ...&#39; checkbox. Applies only to form 625.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PART1_2_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners listed below ...&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PRN_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>RCPCMTE_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient committee or major donor identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>RCPCMTE_NM</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient committee name</td>
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
            <td>Amendment number. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>RPT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>SENDER_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of lobbyist entity that is submitting this report. The field is used to authenticate the filer and allows the firm to submit forms for its lobbyists.</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_LOC</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>SIG_TITLE</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td><code>THRU_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>CLI</code></td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td><code>FRM</code></td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td><code>LBY</code></td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td><code>LCO</code></td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>LEM</code></td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p53">53</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p67">67</a>)
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
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p53">53</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p66">66</a>)
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
                <td>CVR</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p53">53</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p66">66</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`66-70 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p66>`_)

* Map from .CAL Format to Database Table and Fields (`17-21 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p17>`_)

* .CAL Format Layout (Version 1.05.02) (`53-56 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p53>`_)

* CAL-ACCESS Tables, Columns and Indexes (`32-35 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p32>`_)






------------

*********************
CVR2_LOBBY_DISCLOSURE_CD
*********************

Additional data from lobbyist disclosure forms (615, 625, 635, and 645)

**Sample:** `CVR2_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_LOBBY_DISCLOSURE_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTY_TITLE</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of partner, owner, officer, employer if the entity is an individual. Only required by Form 635.</td>
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
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>EMP</code></td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td><code>OFF</code></td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td><code>OWN</code></td>
                <td>Owner</td>
            </tr>
        
            <tr>
                <td><code>PTN</code></td>
                <td>Partner</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p57">57</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p71">71</a>)
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
                <td><code>F625</code></td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>F635</code></td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p57">57</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p71">71</a>)
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
                <td>CVR2</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p57">57</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p71">71</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`71 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p71>`_)

* Map from .CAL Format to Database Table and Fields (`36 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p36>`_)

* .CAL Format Layout (Version 1.05.02) (`57 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p57>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `43-44 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p43>`_)






------------

*********************
LOBBY_AMENDMENTS_CD
*********************

Lobbyist registration amendment information (Form 605 Part I).

**Sample:** `LOBBY_AMENDMENTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBY_AMENDMENTS_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-601">Form 601</a>:
                Lobbying Firm Registration Statement
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-603">Form 603</a>:
                Lobbyist Employer or Lobbying Coalition Registration Statement
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
            <td>Yes</td>
            <td>Record Type Value: F605</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXEC_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this amendment executed on</td>
        </tr>
    
    
    
        <tr>
            <td><code>FROM_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td><code>THRU_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting date to/through date of original</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_L_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_L_EFF</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_L_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_L_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_L_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_L_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_L_CB</code></td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Delete lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_L_EFF</code></td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_L_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_L_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_L_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_L_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyiest suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_LE_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyiest employer checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_LE_EFF</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_LE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_LE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist or employer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_LE_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_LE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_LE_CB</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Delete lobbyist employer check box</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_LE_EFF</code></td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_LE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_LE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyiest employer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_LE_NAMT</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Delete lobbyist employer name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_LE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist employer name</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_LF_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADD_LF_EFF</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>A_LF_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_LF_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Delete lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>DEL_LF_EFF</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Delete lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>D_LF_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_CB</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other amendments checkbox</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_EFF</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Other amendments effective date</td>
        </tr>
    
    
    
        <tr>
            <td><code>OTHER_DESC</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of changes</td>
        </tr>
    
    
    
        <tr>
            <td><code>F606_YES</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing all activity</td>
        </tr>
    
    
    
        <tr>
            <td><code>F606_NO</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing employment but staying active</td>
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
                <td><code>F605</code></td>
                <td>F605</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p74">74</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p88">88</a>)
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
                <td><code>F601</code></td>
                <td>Form 601: Lobbying Firm Registration Statement</td>
            </tr>
        
            <tr>
                <td><code>F603</code></td>
                <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p74">74</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p88">88</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`88-89 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p88>`_)

* Map from .CAL Format to Database Table and Fields (`64-66 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p64>`_)

* .CAL Format Layout (Version 1.05.02) (`74 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p74>`_)

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `90-91 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p90>`_)






------------

*********************
F690P2_CD
*********************

Amends lobbying disclosure filings (Form 690)

**Sample:** `F690P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F690P2_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
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
            <td>Record Type Value: F690</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXEC_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the original report (or prior amendment to the original report) was executed on.</td>
        </tr>
    
    
    
        <tr>
            <td><code>FROM_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td><code>THRU_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Report period to/through date of original.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CHG_PARTS</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on part(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CHG_SECTS</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on sections(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_TXT1</code></td>
            <td>String (up to 330)</td>
            <td>No</td>
            <td>Description of changes to the filing</td>
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
                <td><code>F690</code></td>
                <td>F690</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p58">58</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p72">72</a>)
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
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p58">58</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p72">72</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`72 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p72>`_)

* Map from .CAL Format to Database Table and Fields (`50-51 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p50>`_)

* .CAL Format Layout (Version 1.05.02) (`58 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p58>`_)

* CAL-ACCESS Tables, Columns and Indexes (`8 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p8>`_, `59-60 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p59>`_)






------------

*********************
LATT_CD
*********************

Lobbyist disclosure attachment schedules for payments

**Sample:** `LATT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LATT_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#schedule-630">Schedule 630</a>:
                Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) 
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#schedule-635c">Schedule 635C</a>:
                Payments Received by Lobbying Coalitions
            </td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#schedule-640">Schedule 640</a>:
                Governmental Agencies Reporting (Attachment to Form 635 or Form 645)
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
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_AMT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUMBEG_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payment Recipient/Payee</td>
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
            <td><code>LINE_ITEM</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
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
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>PMT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LATT</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>FRM</code></td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>IND</code></td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td><code>LBY</code></td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td><code>LCO</code></td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>LEM</code></td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>RCP</code></td>
                <td>Recipient Committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p65">65</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p80">80</a>)
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p79">79</a>),  Map from .CAL Format to Database Table and Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p52">52</a>),  .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p65">65</a>)
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
                <td><code>LATT</code></td>
                <td>LATT</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p65">65</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p79">79</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`79-80 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p79>`_)

* Map from .CAL Format to Database Table and Fields (`52-53 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p52>`_)

* .CAL Format Layout (Version 1.05.02) (`65 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p65>`_)

* CAL-ACCESS Tables, Columns and Indexes (`81-82 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p81>`_)






------------

*********************
LEXP_CD
*********************

Lobbying activity expenditures schedule information, reported in
Forms 615 Part 1, 625 Part 3A, 635 Part 3C, and 645 Part 2A.

**Sample:** `LEXP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEXP_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-615">Form 615</a>:
                Lobbyist Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        <tr>
            <td>- Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-635">Form 635</a>:
                Report of Lobbyist Employer or Report of Lobbying Coalition
            </td>
        </tr>
        
        <tr>
            <td>- Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-645">Form 645</a>:
                Report of Person Spending $5,000 or More
            </td>
        </tr>
        
        <tr>
            <td>- Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
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
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to the tranaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td><code>BENE_AMT</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Amount benefiting benficiary</td>
        </tr>
    
    
    
        <tr>
            <td><code>BENE_NAME</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Name of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td><code>BENE_POSIT</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official position of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td><code>CREDCARDCO</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the credit card company, if paid using a card</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payee</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of expenditure</td>
        </tr>
    
    
    
        <tr>
            <td><code>EXPN_DSCR</code></td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of the expense and a description or explanation</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee city</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state</td>
        </tr>
    
    
    
        <tr>
            <td><code>PAYEE_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEXP</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECSUBTYPE</code></td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Record Subtype</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>IND</code></td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p61">61</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p75">75</a>)
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
                <td><code>F615P1</code></td>
                <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
            </tr>
        
            <tr>
                <td><code>F625P3A</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F635P3C</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td><code>F645P2A</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p61">61</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p74">74</a>)
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
                <td><code>LEXP</code></td>
                <td>LEXP</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p61">61</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p74">74</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


``recsubtype``
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
                <td><code>1</code></td>
                <td>Main</td>
            </tr>
        
            <tr>
                <td><code>2</code></td>
                <td>Detail</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p61">61</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p74">74</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`74-75 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p74>`_)

* Map from .CAL Format to Database Table and Fields (`58-59 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p58>`_)

* .CAL Format Layout (Version 1.05.02) (`61 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p61>`_)

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `86-87 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p86>`_)






------------

*********************
LCCM_CD
*********************

Lobbying campaign contributions reported on Forms 615 Part 2,
625 Part 4B, 635 Part 4B and the 645 Part 3B.

**Sample:** `LCCM_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LCCM_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-615">Form 615</a>:
                Lobbyist Report
            </td>
        </tr>
        
        <tr>
            <td>- Part 2, Campaign Contributions Made or Delivered</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        <tr>
            <td>- Part 4: Campaign Contributions Made</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-635">Form 635</a>:
                Report of Lobbyist Employer or Report of Lobbying Coalition
            </td>
        </tr>
        
        <tr>
            <td>- Part 4: Campaign Contributions Made</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-645">Form 645</a>:
                Report of Person Spending $5,000 or More
            </td>
        </tr>
        
        <tr>
            <td>- Part 3: Campaign Contributions Made</td>
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
            <td>Amount of contribution</td>
        </tr>
    
    
    
        <tr>
            <td><code>BAKREF_TID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CTRIB_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code for Recipient of the Campaign Contribution Value</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LCCM</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td><code>RECIP_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>RCP</code></td>
                <td>Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>CTL</code></td>
                <td>Controlled committee</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p64">64</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p78">78</a>)
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
                <td><code>F615P2</code></td>
                <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
            </tr>
        
            <tr>
                <td><code>F625P4B</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td><code>F635P4B</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td><code>F645P3B</code></td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p64">64</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p78">78-79</a>)
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
                <td><code>LCCM</code></td>
                <td>LCCM</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p64">64</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p78">78</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`78-79 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p78>`_)

* Map from .CAL Format to Database Table and Fields (`54-55 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p54>`_)

* .CAL Format Layout (Version 1.05.02) (`64 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p64>`_)

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `83-84 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p83>`_)






------------

*********************
LEMP_CD
*********************

Lobbyist employers and subcontracted clients (Form 601)

**Sample:** `LEMP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEMP_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-601">Form 601</a>:
                Lobbying Firm Registration Statement
            </td>
        </tr>
        
        <tr>
            <td>- Part 2: Section A, Lobbyist Employers</td>
        </tr>
        
        <tr>
            <td>- Part 2: Section B: Subcontracted Clients</td>
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
            <td><code>AGENCYLIST</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agencies to be lobbied</td>
        </tr>
    
    
    
        <tr>
            <td><code>AMEND_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employing client city</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employing client first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employing client last name</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employing client phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employing client state</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLI_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>CLIENT_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the Part 2A employer or Part 2B Client/Employer</td>
        </tr>
    
    
    
        <tr>
            <td><code>CON_PERIOD</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Period of the contract</td>
        </tr>
    
    
    
        <tr>
            <td><code>DESCRIP</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of employer/client lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFF_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective Date of Lobbying Contract</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Record Type Value: LEMP</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm city</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Subcontracting lobbying firms name</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm state</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUB_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUBFIRM_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of subcontracting lobbying firm</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>F601P2A</code></td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
            </tr>
        
            <tr>
                <td><code>F601P2B</code></td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section B: Subcontracted Clients</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p75">75</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p90">90</a>)
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
                <td><code>LEMP</code></td>
                <td>LEMP</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p75">75</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p90">90</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`90-91 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p90>`_)

* Map from .CAL Format to Database Table and Fields (`56-57 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p56>`_)

* .CAL Format Layout (Version 1.05.02) (`75 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p75>`_)

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `85-86 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p85>`_)






------------

*********************
LOBBYING_CHG_LOG_CD
*********************

Holds lobbyist log data for web display

**Sample:** `LOBBYING_CHG_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYING_CHG_LOG_CD.TSV>`_




Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        
            <td><code>FILER_ID</code></td>
        
            <td><code>CHANGE_NO</code></td>
        
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
            <td><code>CHANGE_NO</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Number of changes this session</td>
        </tr>
    
    
    
        <tr>
            <td><code>SESSION_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>LOG_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td><code>CORRECTION_FLG</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ACTION</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ATTRIBUTE_CHANGED</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ETHICS_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>INTERESTS</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_FULL_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name of filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_CITY</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>City address of filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ST</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>State address of filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_ZIP</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>ZIP Code of filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILER_PHONE</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Phone number of filer</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_TYPE</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented. The values might refer to either FILER_TYPES_CD.FILER_TYPE or GROUP_TYPES_CD.GRP_ID, but that&#39;s just a guess.</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_NAME</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CITY</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_ST</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_ZIP</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_PHONE</code></td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_ID</code></td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td><code>RESPONSIBLE_OFFICER</code></td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>EFFECT_DT</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


``entity_type``
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
                <td>n/a</td>
            </tr>
        
            <tr>
                <td><code>1</code></td>
                <td>Client</td>
            </tr>
        
            <tr>
                <td><code>2</code></td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td><code>3</code></td>
                <td>Firm</td>
            </tr>
        
            <tr>
                <td><code>4</code></td>
                <td>Lobbyist</td>
            </tr>
        
            <tr>
                <td><code>10</code></td>
                <td>Major Donor</td>
            </tr>
        
            <tr>
                <td><code>16</code></td>
                <td>Recipient Committee</td>
            </tr>
        
            <tr>
                <td><code>20</code></td>
                <td>Treasurer/Responsible Officer</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`10 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p10>`_, `91-92 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p91>`_)






------------

*********************
LOBBYIST_CONTRIBUTIONS1_CD
*********************

Lobbyist contribution disclosure table.

**Sample:** `LOBBYIST_CONTRIBUTIONS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS1_CD.TSV>`_





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

Lobbyist contribution disclosure table. Temporary table used to generate
disclosure table (Lobbyist Contributions 3)

**Sample:** `LOBBYIST_CONTRIBUTIONS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS2_CD.TSV>`_





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

**Sample:** `LOBBYIST_CONTRIBUTIONS3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS3_CD.TSV>`_





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
LOBBYIST_EMPLOYER1_CD
*********************

Information for lobbyist's primary employer

**Sample:** `LOBBYIST_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER1_CD.TSV>`_





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


Look-up Codes
=============


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



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `97-98 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p97>`_)






------------

*********************
LOBBYIST_EMPLOYER2_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER2_CD.TSV>`_





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


Look-up Codes
=============


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



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `98-99 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p98>`_)






------------

*********************
LOBBYIST_EMPLOYER3_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER3_CD.TSV>`_





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


Look-up Codes
=============


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



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `99 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p99>`_)






------------

*********************
LOBBYIST_EMPLOYER_FIRMS1_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS1_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS2_CD.TSV>`_





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
LOBBYIST_EMP_LOBBYIST1_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST1_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST2_CD.TSV>`_





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
LOBBYIST_FIRM1_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM1_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM2_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM3_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER1_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER2_CD.TSV>`_





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
LOBBYIST_FIRM_LOBBYIST1_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST1_CD.TSV>`_





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

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST2_CD.TSV>`_





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
LOTH_CD
*********************

Payment to other lobbying firms listed of Form 625 Part 3B

**Sample:** `LOTH_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOTH_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        <tr>
            <td>- Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
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
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_AMT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_NAME</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>FIRM_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>PMT_DATE</code></td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOTH</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUBJ_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUBJ_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUBJ_NAMS</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Suffix of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td><code>SUBJ_NAMT</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Prefix or title of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>F625P3B</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p63">63</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p77">77</a>)
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
                <td><code>LOTH</code></td>
                <td>LOTH</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p63">63</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p77">77</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`77-78 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p77>`_)

* .CAL Format Layout (Version 1.05.02) (`63 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p63>`_)

* Map from .CAL Format to Database Table and Fields (`67-68 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p67>`_)

* CAL-ACCESS Tables, Columns and Indexes (`106-107 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p106>`_)






------------

*********************
LPAY_CD
*********************

Payments made or received by lobbying firms, reported on
Form 625 Part 2 and 635 Part 3B

**Sample:** `LPAY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LPAY_CD.TSV>`_


Filing forms
============

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-625">Form 625</a>:
                Report of Lobbying Firm
            </td>
        </tr>
        
        <tr>
            <td>- Part 2, Payments Received in Connection with Lobbying Activity</td>
        </tr>
        
        
        <tr>
            <td>
                <a href="../filingforms/lobbyist_forms.html#form-635">Form 635</a>:
                Report of Lobbyist Employer or Report of Lobbying Coalition
            </td>
        </tr>
        
        <tr>
            <td>- Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
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
            <td><code>ADVAN_AMT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Advance and other payments amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>ADVAN_DSCR</code></td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of advance and other payments</td>
        </tr>
    
    
    
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
            <td>Backreference to transaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td><code>CUM_TOTAL</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_CITY</code></td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer city</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_ID</code></td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_NAMF</code></td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employer first name</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_NAML</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_NAMS</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_NAMT</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_PHON</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employer phone number</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_ST</code></td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer state</td>
        </tr>
    
    
    
        <tr>
            <td><code>EMPLR_ZIP4</code></td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td><code>ENTITY_CD</code></td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Employer Values</td>
        </tr>
    
    
    
        <tr>
            <td><code>FEES_AMT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Fees and retainers amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>FILING_ID</code></td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td><code>FORM_TYPE</code></td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td><code>LBY_ACTVTY</code></td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td><code>MEMO_REFNO</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td><code>PER_TOTAL</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td><code>REC_TYPE</code></td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LPAY</td>
        </tr>
    
    
    
        <tr>
            <td><code>REIMB_AMT</code></td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Reimbursements of expense amount</td>
        </tr>
    
    
    
        <tr>
            <td><code>TRAN_ID</code></td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td><code>FRM</code></td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td><code>LCO</code></td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td><code>LEM</code></td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td><code>OTH</code></td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td><code>128</code></td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p62">62</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p76">76</a>)
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
                <td><code>F625P2</code></td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td><code>F635P3B</code></td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p62">62</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p76">76</a>)
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
                <td><code>LPAY</code></td>
                <td>LPAY</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p62">62</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p76">76</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

* .CAL Format Layout (Version 2.01) (`76-77 <https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p76>`_)

* .CAL Format Layout (Version 1.05.02) (`62 <https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p62>`_)

* Map from .CAL Format to Database Table and Fields (`69-70 <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p69>`_)

* CAL-ACCESS Tables, Columns and Indexes (`107-109 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p107>`_)






------------

*********************
LOBBYIST_EMPLOYER_HISTORY_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_HISTORY_CD.TSV>`_





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


Look-up Codes
=============


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



Source Docs
^^^^^^^^^^^

* CAL-ACCESS Tables, Columns and Indexes (`11 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p11>`_, `96-97 <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p96>`_)






------------

*********************
LOBBYIST_FIRM_HISTORY_CD
*********************

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_HISTORY_CD.TSV>`_





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



