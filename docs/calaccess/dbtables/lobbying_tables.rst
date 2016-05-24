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

The records in CVR_REGISTRATION_CD are unique by FILING_ID, AMEND_ID, REC_TYPE and FORM_TYPE.

**Sample:** `CVR_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_REGISTRATION_CD.TSV>`_


Filing forms
============



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <../filingforms/lobbyist_forms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <../filingforms/lobbyist_forms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <../filingforms/lobbyist_forms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <../filingforms/lobbyist_forms.html#form-606>`_ (Notice of Termination)



* `Form 607 <../filingforms/lobbyist_forms.html#form-607>`_ (Notice of Withdrawal)




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
            <td>A_B_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Individual or business entity city</td>
        </tr>
    
    
    
        <tr>
            <td>A_B_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of individual or business entity</td>
        </tr>
    
    
    
        <tr>
            <td>A_B_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Individual or business entity state</td>
        </tr>
    
    
    
        <tr>
            <td>A_B_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Individual or business entity ZIP Code.</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>AUTH_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address city</td>
        </tr>
    
    
    
        <tr>
            <td>AUTH_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Authorized lobbying firm business name. Applies to Form 602.</td>
        </tr>
    
    
    
        <tr>
            <td>AUTH_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address state</td>
        </tr>
    
    
    
        <tr>
            <td>AUTH_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Business included activity checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer business address city</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_CLASS</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classifiction values of business related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_DESCR</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of business classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_EMAIL</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer business address email</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_FAX</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address fax number</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer business address state</td>
        </tr>
    
    
    
        <tr>
            <td>BUS_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>C_LESS50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with fewer than 50 members check this box</td>
        </tr>
    
    
    
        <tr>
            <td>C_MORE50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with more than 50 check this box.</td>
        </tr>
    
    
    
        <tr>
            <td>COMPLET_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ethics orientation class completion date. Applies to Form 604. As filed by the lobbyist.</td>
        </tr>
    
    
    
        <tr>
            <td>DESCRIP_1</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of business activity, industry or other</td>
        </tr>
    
    
    
        <tr>
            <td>DESCRIP_2</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of specific or other lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>EFF_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date of authoarization or termination</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the lobbyist employer or firm. Applies to Forms 604, 606, 607.</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>IND_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Individual checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>IND_CLASS</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classification values to category industry related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>IND_DESCR</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of industry classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>INFLUEN_YN</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Attempt to influence state legislation</td>
        </tr>
    
    
    
        <tr>
            <td>L_FIRM_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying firm within the ... &#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_604_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in this 604 statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_REG_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in form 601/603 registration statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBY_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying within the meaning...&#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBY_INT</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of Part III lobbying interests. Applies to Form 603</td>
        </tr>
    
    
    
        <tr>
            <td>LS_BEG_YR</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative session begins</td>
        </tr>
    
    
    
        <tr>
            <td>LS_END_YR</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative sessions ends</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>NEWCERT_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will require a new certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>OTH_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>QUAL_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified. Applies to forms 601 and 603. Only occurs once in lobbying filings.</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>RENCERT_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will take a renewel certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>REPORT_NUM</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number as reported by the filer. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report or amendment is filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>SENDER_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the lobbyist entity submitting this report. This is equal to the filer ID if the filer is the submitting the report and the firm or employer if they are submitting the report.</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date signed</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_LOC</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_TITLE</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>ST_AGENCY</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>List of identified state agencies. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>ST_LEG_YN</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will lobby state legislature checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>STMT_FIRM</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Lobby firm named in &#39;Statement of Responsible Officer&#39;This field only applies to Form 601.</td>
        </tr>
    
    
    
        <tr>
            <td>TRADE_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry, trade or professional checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


bus_class
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
                <td>ENT</td>
                <td>Entertainment/Recreation</td>
            </tr>
        
            <tr>
                <td>FIN</td>
                <td>Finance/Insurance</td>
            </tr>
        
            <tr>
                <td>LOG</td>
                <td>Lodging/Restaurants</td>
            </tr>
        
            <tr>
                <td>MAN</td>
                <td>Manufacturing/Industrial</td>
            </tr>
        
            <tr>
                <td>MER</td>
                <td>Merchandise/Retail</td>
            </tr>
        
            <tr>
                <td>OIL</td>
                <td>Oil and Gas</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>PRO</td>
                <td>Professional/Trade</td>
            </tr>
        
            <tr>
                <td>REA</td>
                <td>Real Estate</td>
            </tr>
        
            <tr>
                <td>TRN</td>
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
                <td>BUS</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FRM</td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>LBY</td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td>LCO</td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>LEM</td>
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


ind_class
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
                <td>AGR</td>
                <td>Agriculture</td>
            </tr>
        
            <tr>
                <td>EDU</td>
                <td>Education</td>
            </tr>
        
            <tr>
                <td>GOV</td>
                <td>Government</td>
            </tr>
        
            <tr>
                <td>HEA</td>
                <td>Health</td>
            </tr>
        
            <tr>
                <td>LAB</td>
                <td>Labor Unions</td>
            </tr>
        
            <tr>
                <td>LEG</td>
                <td>Legal</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>POL</td>
                <td>Political Organizations</td>
            </tr>
        
            <tr>
                <td>PUB</td>
                <td>Public Employees</td>
            </tr>
        
            <tr>
                <td>UTL</td>
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


influen_yn
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
                <td>Y</td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td>y</td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>No</td>
            </tr>
        
            <tr>
                <td>n</td>
                <td>No</td>
            </tr>
        
            <tr>
                <td>X</td>
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
                 .CAL Format Layout (Version 1.05.02) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p68">68</a>),  .CAL Format Layout (Version 2.01) (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p82">82</a>)
            </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


st_leg_yn
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
                <td>Y</td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td>y</td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>No</td>
            </tr>
        
            <tr>
                <td>n</td>
                <td>No</td>
            </tr>
        
            <tr>
                <td>X</td>
                <td>Yes</td>
            </tr>
        
            <tr>
                <td>x</td>
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

The records in CVR2_REGISTRATION_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR2_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_REGISTRATION_CD.TSV>`_


Filing forms
============



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <../filingforms/lobbyist_forms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <../filingforms/lobbyist_forms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




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
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 10)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
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
                <td>AGY</td>
                <td>State Agency</td>
            </tr>
        
            <tr>
                <td>EMP</td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td>FRM</td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>LBY</td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td>MBR</td>
                <td>Member of Associaton</td>
            </tr>
        
            <tr>
                <td>SCL</td>
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

The records in CVR_LOBBY_DISCLOSURE_CD are unique by FILING_ID, AMEND_ID, REC_TYPE and FORM_TYPE.

**Sample:** `CVR_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_LOBBY_DISCLOSURE_CD.TSV>`_


Filing forms
============



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More)




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_N_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_Y_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_BEG_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning date</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition business city</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition business phone number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition business state</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Form, employer or coalition business ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>FROM_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_ACTVTY</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Description of lobbying activity. Applies to forms 635 and 645. Additional description may be provided in text records.</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBY_N_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity none&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBY_Y_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity Form 630 attached&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>MAIL_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>MAJOR_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Major donor first name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>MAJOR_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Major donor last name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>MAJOR_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor suffix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>MAJOR_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor title or prefix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>NOPART1_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part I information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>NOPART2_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part II information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>PART1_1_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners Form 615 attached ...&#39; checkbox. Applies only to form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>PART1_2_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners listed below ...&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>PRN_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>RCPCMTE_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient committee or major donor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>RCPCMTE_NM</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient committee name</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>REPORT_NUM</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>SENDER_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of lobbyist entity that is submitting this report. The field is used to authenticate the filer and allows the firm to submit forms for its lobbyists.</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_LOC</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>SIG_TITLE</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>THRU_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
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
                <td>CLI</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>FRM</td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td>LBY</td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td>LCO</td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>LEM</td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td>OTH</td>
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

The records in CVR2_LOBBY_DISCLOSURE_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `CVR2_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_LOBBY_DISCLOSURE_CD.TSV>`_


Filing forms
============



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>ENTY_TITLE</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of partner, owner, officer, employer if the entity is an individual. Only required by Form 635.</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
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
                <td>EMP</td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td>OFF</td>
                <td>Officer</td>
            </tr>
        
            <tr>
                <td>OWN</td>
                <td>Owner</td>
            </tr>
        
            <tr>
                <td>PTN</td>
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
                <td>F625</td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>F635</td>
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

The records in LOBBY_AMENDMENTS_CD are unique by FILING_ID, AMEND_ID, REC_TYPE and FORM_TYPE.

**Sample:** `LOBBY_AMENDMENTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBY_AMENDMENTS_CD.TSV>`_


Filing forms
============



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 603 <../filingforms/lobbyist_forms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




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
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: F605</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>EXEC_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this amendment executed on</td>
        </tr>
    
    
    
        <tr>
            <td>FROM_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>THRU_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting date to/through date of original</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_L_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_L_EFF</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>A_L_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>A_L_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>A_L_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>A_L_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist suffix</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_L_CB</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Delete lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_L_EFF</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>D_L_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>D_L_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>D_L_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>D_L_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyiest suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_LE_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyiest employer checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_LE_EFF</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>A_LE_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>A_LE_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist or employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>A_LE_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>A_LE_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_LE_CB</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Delete lobbyist employer check box</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_LE_EFF</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>D_LE_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>D_LE_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyiest employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>D_LE_NAMT</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Delete lobbyist employer name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>D_LE_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist employer name</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_LF_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>ADD_LF_EFF</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>A_LF_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_LF_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Delete lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>DEL_LF_EFF</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Delete lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>D_LF_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>OTHER_CB</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other amendments checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>OTHER_EFF</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Other amendments effective date</td>
        </tr>
    
    
    
        <tr>
            <td>OTHER_DESC</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of changes</td>
        </tr>
    
    
    
        <tr>
            <td>F606_YES</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing all activity</td>
        </tr>
    
    
    
        <tr>
            <td>F606_NO</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing employment but staying active</td>
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
                <td>F605</td>
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
                <td>F601</td>
                <td>Form 601: Lobbying Firm Registration Statement</td>
            </tr>
        
            <tr>
                <td>F603</td>
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

The records in F690P2_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `F690P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F690P2_CD.TSV>`_


Filing forms
============



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More)




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
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: F690</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>EXEC_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the original report (or prior amendment to the original report) was executed on.</td>
        </tr>
    
    
    
        <tr>
            <td>FROM_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>THRU_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Report period to/through date of original.</td>
        </tr>
    
    
    
        <tr>
            <td>CHG_PARTS</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on part(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>CHG_SECTS</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on sections(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_TXT1</td>
            <td>String (up to 330)</td>
            <td>No</td>
            <td>Description of changes to the filing</td>
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
                <td>F690</td>
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

The records in LATT_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LATT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LATT_CD.TSV>`_


Filing forms
============



* `Schedule 630 <../filingforms/lobbyist_forms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <../filingforms/lobbyist_forms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <../filingforms/lobbyist_forms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_AMT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>CUMBEG_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning to date</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payment Recipient/Payee</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_CODE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_REFNO</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>PMT_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LATT</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient suffix</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
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
                <td>FRM</td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>IND</td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td>LBY</td>
                <td>Lobbyist (an individual)</td>
            </tr>
        
            <tr>
                <td>LCO</td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>LEM</td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>RCP</td>
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
                <td>S630</td>
                <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
            </tr>
        
            <tr>
                <td>S635-C</td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td>S640</td>
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
                <td>LATT</td>
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

The records in LEXP_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LEXP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEXP_CD.TSV>`_


Filing forms
============



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>BAKREF_TID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to the tranaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>BENE_AMT</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Amount benefiting benficiary</td>
        </tr>
    
    
    
        <tr>
            <td>BENE_NAME</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Name of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>BENE_POSIT</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official position of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>CREDCARDCO</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the credit card company, if paid using a card</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payee</td>
        </tr>
    
    
    
        <tr>
            <td>EXPN_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of expenditure</td>
        </tr>
    
    
    
        <tr>
            <td>EXPN_DSCR</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of the expense and a description or explanation</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_CODE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_REFNO</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee city</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee first name</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee suffix</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state</td>
        </tr>
    
    
    
        <tr>
            <td>PAYEE_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEXP</td>
        </tr>
    
    
    
        <tr>
            <td>RECSUBTYPE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Record Subtype</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
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
                <td>IND</td>
                <td>Person (spending &gt; $5000)</td>
            </tr>
        
            <tr>
                <td>OTH</td>
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
                <td>F615P1</td>
                <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
            </tr>
        
            <tr>
                <td>F625P3A</td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F635P3C</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F645P2A</td>
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
                <td>LEXP</td>
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


recsubtype
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
                <td>1</td>
                <td>Main</td>
            </tr>
        
            <tr>
                <td>2</td>
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

The records in LCCM_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LCCM_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LCCM_CD.TSV>`_


Filing forms
============



* `Form 615 <../filingforms/lobbyist_forms.html#form-615>`_ (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm): Part 4: Campaign Contributions Made



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made



* `Form 645 <../filingforms/lobbyist_forms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>BAKREF_TID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor first name</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor suffix</td>
        </tr>
    
    
    
        <tr>
            <td>CTRIB_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code for Recipient of the Campaign Contribution Value</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_CODE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_REFNO</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LCCM</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient identification number</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>RECIP_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
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
                <td>RCP</td>
                <td>Recipient Committee</td>
            </tr>
        
            <tr>
                <td>CTL</td>
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
                <td>F615P2</td>
                <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
            </tr>
        
            <tr>
                <td>F625P4B</td>
                <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td>F635P4B</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td>F645P3B</td>
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
                <td>LCCM</td>
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

The records in LEMP_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LEMP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEMP_CD.TSV>`_


Filing forms
============



* `Form 601 <../filingforms/lobbyist_forms.html#form-601>`_ (Lobbying Firm Registration Statement)

    * Part 2: Section A, Lobbyist Employers

    * Part 2: Section B: Subcontracted Clients





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
            <td>AGENCYLIST</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agencies to be lobbied</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employing client city</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employing client first name</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employing client last name</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client suffix</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employing client phone number</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employing client state</td>
        </tr>
    
    
    
        <tr>
            <td>CLI_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>CLIENT_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the Part 2A employer or Part 2B Client/Employer</td>
        </tr>
    
    
    
        <tr>
            <td>CON_PERIOD</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Period of the contract</td>
        </tr>
    
    
    
        <tr>
            <td>DESCRIP</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of employer/client lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>EFF_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective Date of Lobbying Contract</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEMP</td>
        </tr>
    
    
    
        <tr>
            <td>SUB_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm city</td>
        </tr>
    
    
    
        <tr>
            <td>SUB_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Subcontracting lobbying firms name</td>
        </tr>
    
    
    
        <tr>
            <td>SUB_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm phone number</td>
        </tr>
    
    
    
        <tr>
            <td>SUB_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm state</td>
        </tr>
    
    
    
        <tr>
            <td>SUB_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>SUBFIRM_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of subcontracting lobbying firm</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td>F601P2A</td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
            </tr>
        
            <tr>
                <td>F601P2B</td>
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
                <td>LEMP</td>
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

The records in LOBBYING_CHG_LOG_CD are unique by FILER_ID and CHANGE_NO.

**Sample:** `LOBBYING_CHG_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYING_CHG_LOG_CD.TSV>`_



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
            <td>FILER_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>CHANGE_NO</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Number of changes this session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>LOG_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_TYPE</td>
            <td>Integer</td>
            <td>No</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td>CORRECTION_FLG</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ACTION</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ATTRIBUTE_CHANGED</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ETHICS_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>INTERESTS</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_FULL_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name of filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_CITY</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>City address of filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_ST</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>State address of filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_ZIP</td>
            <td>Integer</td>
            <td>No</td>
            <td>ZIP Code of filer</td>
        </tr>
    
    
    
        <tr>
            <td>FILER_PHONE</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Phone number of filer</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_TYPE</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented. The values might refer to either FILER_TYPES_CD.FILER_TYPE or GROUP_TYPES_CD.GRP_ID, but that&#39;s just a guess.</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_NAME</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CITY</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_ST</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_ZIP</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_PHONE</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>RESPONSIBLE_OFFICER</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>EFFECT_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


entity_type
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
                <td>n/a</td>
            </tr>
        
            <tr>
                <td>1</td>
                <td>Client</td>
            </tr>
        
            <tr>
                <td>2</td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td>3</td>
                <td>Firm</td>
            </tr>
        
            <tr>
                <td>4</td>
                <td>Lobbyist</td>
            </tr>
        
            <tr>
                <td>10</td>
                <td>Major Donor</td>
            </tr>
        
            <tr>
                <td>16</td>
                <td>Recipient Committee</td>
            </tr>
        
            <tr>
                <td>20</td>
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
            <td>FILER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_START_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_END_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTION_DT</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_NAME</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
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
            <td>FILER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_START_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_END_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTION_DT</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_NAME</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
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
            <td>FILER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_START_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_PERIOD_END_DT</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTION_DT</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_NAME</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>RECIPIENT_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
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
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_CD</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_NAME</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


interest_cd
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
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_CD</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_NAME</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8 total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


interest_cd
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
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_CD</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_NAME</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


interest_cd
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
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>TERMINATION_DT</td>
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
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>TERMINATION_DT</td>
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
            <td>LOBBYIST_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_LAST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_FIRST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
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
            <td>LOBBYIST_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_LAST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_FIRST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
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
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
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
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
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
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
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
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_SEQUENCE</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_START</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_END</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>PER_TOTAL</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_TOTAL</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_ACTVTY</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>EXT_LBY_ACTVTY</td>
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
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_SEQUENCE</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_START</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>RPT_END</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>PER_TOTAL</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_TOTAL</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_ACTVTY</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>EXT_LBY_ACTVTY</td>
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
            <td>LOBBYIST_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_LAST_NAME</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_FIRST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
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
            <td>LOBBYIST_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_LAST_NAME</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>LOBBYIST_FIRST_NAME</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
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

The records in LOTH_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LOTH_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOTH_CD.TSV>`_


Filing forms
============



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




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
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>AMOUNT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_AMT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_CODE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_REFNO</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>PMT_DATE</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOTH</td>
        </tr>
    
    
    
        <tr>
            <td>SUBJ_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>SUBJ_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>SUBJ_NAMS</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Suffix of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>SUBJ_NAMT</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Prefix or title of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


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
                <td>F625P3B</td>
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
                <td>LOTH</td>
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

The records in LPAY_CD are unique by FILING_ID, AMEND_ID, LINE_ITEM, REC_TYPE and FORM_TYPE.

**Sample:** `LPAY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LPAY_CD.TSV>`_


Filing forms
============



* `Form 625 <../filingforms/lobbyist_forms.html#form-625>`_ (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity



* `Form 635 <../filingforms/lobbyist_forms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms




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
            <td>ADVAN_AMT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Advance and other payments amount</td>
        </tr>
    
    
    
        <tr>
            <td>ADVAN_DSCR</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of advance and other payments</td>
        </tr>
    
    
    
        <tr>
            <td>AMEND_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>BAKREF_TID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to transaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>CUM_TOTAL</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_CITY</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer city</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_ID</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_NAMF</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_NAML</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_NAMS</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_NAMT</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_PHON</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_ST</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer state</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLR_ZIP4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>ENTITY_CD</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Employer Values</td>
        </tr>
    
    
    
        <tr>
            <td>FEES_AMT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Fees and retainers amount</td>
        </tr>
    
    
    
        <tr>
            <td>FILING_ID</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>FORM_TYPE</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>LBY_ACTVTY</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>LINE_ITEM</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_CODE</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>MEMO_REFNO</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>PER_TOTAL</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>REC_TYPE</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LPAY</td>
        </tr>
    
    
    
        <tr>
            <td>REIMB_AMT</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Reimbursements of expense amount</td>
        </tr>
    
    
    
        <tr>
            <td>TRAN_ID</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
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
                <td>FRM</td>
                <td>Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>LCO</td>
                <td>Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>LEM</td>
                <td>Lobbying Employer</td>
            </tr>
        
            <tr>
                <td>OTH</td>
                <td>Other</td>
            </tr>
        
            <tr>
                <td>128</td>
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
                <td>F625P2</td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td>F635P3B</td>
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
                <td>LPAY</td>
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
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>EMPLOYER_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer Name</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_CD</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>INTEREST_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Interest name.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 1 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 2 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 3 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 4 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 5 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 6 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 7 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 8 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


interest_cd
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
            <td>CONTRIBUTOR_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>CURRENT_QTR_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the Firm/Employer/Coalition.</td>
        </tr>
    
    
    
        <tr>
            <td>FIRM_NAME</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Name of Firm/Employer/Coalition</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>QTR_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_ID</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_TOTAL_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>SESSION_YR_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>YR_1_YTD_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td>YR_2_YTD_AMT</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



