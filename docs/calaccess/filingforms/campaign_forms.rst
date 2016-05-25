.. This document was generated programmatically via the createcalaccessrawformdocs command. Any edits you make to this file will be overwritten the next time that command is called. Changes to this doc should instead be made either in the campaign_forms.rst file in ./src/toolbox/templates/ or in the commands internal logic.

===============================
Campaign forms
===============================


California's Political Reform Act requires that political candidates and campaign committees disclose their contributions and expenditures by filing the forms outlined below. The data collected on these 20 forms are stored in the CAL-ACCESS database. Where possible, we have also mapped each form to the specific database tables.

You can read more about these forms and the disclosure requirements in the `Campaign Forms <http://www.fppc.ca.gov/learn/campaign-rules/campaign-forms.html>`_ and `Campaign Disclosure Manuals <http://www.fppc.ca.gov/learn/campaign-rules/campaign-disclosure-manuals.html>`_ sections of the Fair Political Practices Commission (FPPC) website as well as the `Campaign Forms and Instructions <http://www.sos.ca.gov/campaign-lobbying/campaign-disclosure-and-requirements/campaign-forms-and-instructions/>`_ and `Campaign Filing Requirements <http://www.sos.ca.gov/campaign-lobbying/campaign-disclosure-and-requirements/campaign-filing-requirements/>`_ sections of the California Secretary of State's website.




------------

Form 400
---------------

Statement of Organization (Slate Mailer Organization)

Form 400 must be filed within 10 days after the slate mailer organization receives, or is promised to receive, $500 or more for producing one or more slate mailers.

Sections
````````

* Part 1, Slate Mailer Organization Information (`p. 2 <https://www.documentcloud.org/documents/2781370-400-2016-01.html#document/p2>`_)


* Part 2, Treasurer And Other Principal Officers (`p. 2 <https://www.documentcloud.org/documents/2781370-400-2016-01.html#document/p2>`_)


* Part 3, Individuals Who Authorize Contents Of Slate Mailers (`p. 3 <https://www.documentcloud.org/documents/2781370-400-2016-01.html#document/p3>`_)


* Part 4, Is This Organization A "Committee" Pursuant To Government Code Section 82013? (`p. 3 <https://www.documentcloud.org/documents/2781370-400-2016-01.html#document/p3>`_)


* Part 5, Verification (`p. 3 <https://www.documentcloud.org/documents/2781370-400-2016-01.html#document/p3>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-so-cd">
                    CVR_SO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-so-cd">
                    CVR2_SO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781370-400-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781370-400-2016-01.js", {
      container: "#DV-viewer-2781370-400-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781370/400-2016-01.pdf>400-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781370/400-2016-01.txt>400-2016-01 (Text)</a>
    </noscript>





------------

Form 401
---------------

Slate Mailer Organization Campaign Statement

Form 401 is filed by slate mailer organizations to disclose payments made and received in connection with producing slate mailers.

Sections
````````

* Cover Page (`p. 3-4 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p3>`_)


* Schedule A, Payments Received (`p. 5-7 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p5>`_)


* Schedule B, Payments Made (`p. 8-9 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p8>`_)


* Schedule B-1, Payments Made by Agent or Independent Contractor (`p. 10 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p10>`_)


* Schedule C, Persons Receiving $1,000 or More (`p. 11-12 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p11>`_)


* Schedule D, Candidates and Measures Not Listed on Schedule A (`p. 13-14 <https://www.documentcloud.org/documents/2781366-401-2005-01.html#document/p13>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#rcpt-cd">
                    RCPT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#s401-cd">
                    S401_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781366-401-2005-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781366-401-2005-01.js", {
      container: "#DV-viewer-2781366-401-2005-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781366/401-2005-01.pdf>401-2005-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781366/401-2005-01.txt>401-2005-01 (Text)</a>
    </noscript>





------------

Form 402
---------------

Statement of Termination (Slate Mailer Organization)

Form 402 is filed by slate mailer organizations to terminate the organization.

Sections
````````

* Cover Page (`p. 2 <https://www.documentcloud.org/documents/2781369-402-2005-01.html#document/p2>`_)


* Verification (`p. 2 <https://www.documentcloud.org/documents/2781369-402-2005-01.html#document/p2>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-so-cd">
                    CVR_SO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781369-402-2005-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781369-402-2005-01.js", {
      container: "#DV-viewer-2781369-402-2005-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781369/402-2005-01.pdf>402-2005-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781369/402-2005-01.txt>402-2005-01 (Text)</a>
    </noscript>





------------

Form 405
---------------

Amendment to Campaign Disclosure Statement

Form 405 must be used to amend campaign disclosure statements,except for Statement of Organization, Candidate Intention or Campaign Bank Account (Forms 410, 501, 502).



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2811582-405-1994" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2811582-405-1994.js", {
      container: "#DV-viewer-2811582-405-1994",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2811582/405-1994.pdf>405-1994 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2811582/405-1994.txt>405-1994 (Text)</a>
    </noscript>





------------

Form 410
---------------

Statement of Organization Recipient Committee

Form 410 must be filed within 10 days of receiving $2,000 in contributions. If the committee has not yet reached the $2,000 threshold, the not yet qualified box should be checked.

Sections
````````

* Part 1, Committee Information (`p. 2 <https://www.documentcloud.org/documents/2781368-410-2016-01.html#document/p2>`_)


* Part 2, Treasurer and Other Principal Officers (`p. 2 <https://www.documentcloud.org/documents/2781368-410-2016-01.html#document/p2>`_)


* Part 3, Verification (`p. 2 <https://www.documentcloud.org/documents/2781368-410-2016-01.html#document/p2>`_)


* Part 4, Type of Committee (`p. 2-3 <https://www.documentcloud.org/documents/2781368-410-2016-01.html#document/p2>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-so-cd">
                    CVR_SO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-so-cd">
                    CVR2_SO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781368-410-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781368-410-2016-01.js", {
      container: "#DV-viewer-2781368-410-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781368/410-2016-01.pdf>410-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781368/410-2016-01.txt>410-2016-01 (Text)</a>
    </noscript>





------------

Form 425
---------------

Semi-Annual Statement of no Activity

Form 425 is filed by recipient committees that have not received any contributions and have not made any expenditures during the six-month period covered by a semi-annual statement.

Sections
````````

* Part 1, Committee Information (`p. 1 <https://www.documentcloud.org/documents/2781365-425-2001-01.html#document/p1>`_)


* Part 2, Period of No Activity (`p. 1 <https://www.documentcloud.org/documents/2781365-425-2001-01.html#document/p1>`_)


* Part 3, Verification (`p. 1 <https://www.documentcloud.org/documents/2781365-425-2001-01.html#document/p1>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-campaign-disclosure-cd">
                    CVR2_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781365-425-2001-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781365-425-2001-01.js", {
      container: "#DV-viewer-2781365-425-2001-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781365/425-2001-01.pdf>425-2001-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781365/425-2001-01.txt>425-2001-01 (Text)</a>
    </noscript>





------------

Form 450
---------------

Recipient Committee Campaign Disclosure Statement - Short Form

Form 450 is filed by recipient committees that meet certain specific criteria listed in the Form 450.

Sections
````````

* Type of Recipient Committee (`p. 3 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p3>`_)


* Part 1, Payments Made (`p. 3 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p3>`_)


* Part 2, Type of Statement (`p. 3 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p3>`_)


* Part 3, Committee Information (`p. 3 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p3>`_)


* Part 4, Verification (`p. 3 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p3>`_)


* Summary Page (`p. 5 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p5>`_)


* Part 5, Payments Made (`p. 6-7 <https://www.documentcloud.org/documents/2781364-450-2016-01.html#document/p6>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-campaign-disclosure-cd">
                    CVR2_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#expn-cd">
                    EXPN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#f495p2-cd">
                    F495P2_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#splt-cd">
                    SPLT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781364-450-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781364-450-2016-01.js", {
      container: "#DV-viewer-2781364-450-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781364/450-2016-01.pdf>450-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781364/450-2016-01.txt>450-2016-01 (Text)</a>
    </noscript>





------------

Form 460
---------------

Recipient Committee Campaign Statement

Form 460 is filed by recipient committees to report expenditures and contributions. It can be used to file a pre-election statement, semi-annual statement, quarterly statement, termination statement, special odd-year report, or an amendment to a previously filed statement.

Sections
````````

* Cover Page (`p. 3-4 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p3>`_)


* Cover Page - Part 2 (`p. 2 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p2>`_)


* Summary Page (`p. 7-8 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p7>`_)


* Schedule A, Monetary Contributions Received (`p. 9-11 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p9>`_)


* Schedule A-1, Contributions Transferred to Special Election Commitee 


* Schedule B - Part 1, Loans Received (`p. 12-13 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p12>`_)


* Schedule B - Part 2, Loan Guarantors (`p. 14-15 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p14>`_)


* Schedule B - Part 3, Outstanding Bal 


* Schedule C, Non-Monetary Contributions Received (`p. 16-17 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p16>`_)


* Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees (`p. 18-20 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p18>`_)


* Schedule E, Payments Made (`p. 21-24 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p21>`_)


* Schedule F, Accrued Expenses (Unpaid Bills) (`p. 25-27 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p25>`_)


* Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee) (`p. 28-29 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p28>`_)


* Schedule H, Loans Made to Others (`p. 29-30 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p29>`_)


* Schedule H - Part 1, Loans Made 


* Schedule H- Part 2, Repayments Rcvd 


* Schedule H - Part 3, Outstanding Loans 


* Schedule I, miscellanous increases to cash (`p. 31-32 <https://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p31>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-campaign-disclosure-cd">
                    CVR2_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#debt-cd">
                    DEBT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#expn-cd">
                    EXPN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#loan-cd">
                    LOAN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#rcpt-cd">
                    RCPT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#f495p2-cd">
                    F495P2_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#splt-cd">
                    SPLT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781363-460-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781363-460-2016-01.js", {
      container: "#DV-viewer-2781363-460-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781363/460-2016-01.pdf>460-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781363/460-2016-01.txt>460-2016-01 (Text)</a>
    </noscript>





------------

Form 461
---------------

Independent Expenditure Committee & Major Donor Committee Campaign Statement

Form 461 is filed by major donors, independent expenditure committees, and multipurpose organizations including nonprofits.

Sections
````````

* Part 1, Name and Address of Filer (`p. 3 <https://www.documentcloud.org/documents/2781361-461-2016-01.html#document/p3>`_)


* Part 2, Nature and Interests of Filer (`p. 3 <https://www.documentcloud.org/documents/2781361-461-2016-01.html#document/p3>`_)


* Part 3, Summary (`p. 3 <https://www.documentcloud.org/documents/2781361-461-2016-01.html#document/p3>`_)


* Part 4, Verification (`p. 3 <https://www.documentcloud.org/documents/2781361-461-2016-01.html#document/p3>`_)


* Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made (`p. 5-6 <https://www.documentcloud.org/documents/2781361-461-2016-01.html#document/p5>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#expn-cd">
                    EXPN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781361-461-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781361-461-2016-01.js", {
      container: "#DV-viewer-2781361-461-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781361/461-2016-01.pdf>461-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781361/461-2016-01.txt>461-2016-01 (Text)</a>
    </noscript>





------------

Form 465
---------------

Supplemental Independent Expenditure Report

Form 465 is filed by officeholders, candidates, recipient committees, major donor committees, and independent expenditure committees that make independent expenditures totaling $1,000 or more in a calendar year to support or oppose: a single candidate, a single measure, or the qualification of one single measure. Form 465s are filed in the same period(s) the candidate or committee supported or opposed by the independent expenditure(s) is required to file.

Sections
````````

* Part 1, Committee/Filer Information (`p. 2 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p2>`_)


* Part 2, Name of Candidate or Measure Supported or Opposed (`p. 2 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p2>`_)


* Part 3, Independent Expenditures Made (`p. 2 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p2>`_)


* Part 4, Summary (`p. 4 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p4>`_)


* Part 5, Filing Officers (`p. 4 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p4>`_)


* Part 6, Verification (`p. 4 <https://www.documentcloud.org/documents/2781358-465-2009-06.html#document/p4>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr2-campaign-disclosure-cd">
                    CVR2_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#expn-cd">
                    EXPN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781358-465-2009-06" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781358-465-2009-06.js", {
      container: "#DV-viewer-2781358-465-2009-06",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781358/465-2009-06.pdf>465-2009-06 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781358/465-2009-06.txt>465-2009-06 (Text)</a>
    </noscript>





------------

Form 470
---------------

Officeholder and Candidate Campaign Statement, Short Form

Form 470 is filed by officeholders and candidates who do not have a controlled committee, do not receive contributions totaling $2,000 or more during the calendar year, and do not spend $2,000 or more during the calendar year.



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-f470-cd">
                    CVR_F470_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781357-470-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781357-470-2016-01.js", {
      container: "#DV-viewer-2781357-470-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781357/470-2016-01.pdf>470-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781357/470-2016-01.txt>470-2016-01 (Text)</a>
    </noscript>





------------

Form 495
---------------

Supplemental Pre-Election Campaign Statement

Form 495 is filed by recipient committees that make contributions totaling $10,000 or more in connection with an election in which the committee is not required to file regular preelection reports. Form 495 is filed as an attachment to a campaign disclosure statement (Form 450 or 460).



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781356-495-2005-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781356-495-2005-01.js", {
      container: "#DV-viewer-2781356-495-2005-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781356/495-2005-01.pdf>495-2005-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781356/495-2005-01.txt>495-2005-01 (Text)</a>
    </noscript>





------------

Form 496
---------------

Late Independent Expenditure Report

Form 496 is filed by committees that make independent expenditures whose combined total is $1,000 or more to support or oppose a single candidate for elective office, or a single ballot measure. Form 496 should be filed within 24-hours of making the expenditure during the 90 days immediately preceding the election.

Sections
````````

* Part 1, List Only One Candidate or Ballot Measure (`p. 3 <https://www.documentcloud.org/documents/2781355-496-2016-01.html#document/p3>`_)


* Part 2, Independent Expenditures Made (`p. 3 <https://www.documentcloud.org/documents/2781355-496-2016-01.html#document/p3>`_)


* Part 3, Contributions > $100 Received (`p. 3 <https://www.documentcloud.org/documents/2781355-496-2016-01.html#document/p3>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#rcpt-cd">
                    RCPT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#s496-cd">
                    S496_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781355-496-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781355-496-2016-01.js", {
      container: "#DV-viewer-2781355-496-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781355/496-2016-01.pdf>496-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781355/496-2016-01.txt>496-2016-01 (Text)</a>
    </noscript>





------------

Form 497
---------------

Late Contribution Report

Form 497 is filed by state and local committees making or receiving contribution(s) whose combined total is $1,000 or more in the 90 days before an election, committees reporting contributions of $5,000 or more in connection with a state ballot measure, and state candidates as well as state ballot measure committees that receive $5,000 or more at any time other than a 90-day election cycle.

Sections
````````

* Part 1, Contribution(s) Received (`p. 2 <https://www.documentcloud.org/documents/2781353-497-2016-01.html#document/p2>`_)


* Part 2, Contribution(s) Made (`p. 4 <https://www.documentcloud.org/documents/2781353-497-2016-01.html#document/p4>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#s497-cd">
                    S497_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781353-497-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781353-497-2016-01.js", {
      container: "#DV-viewer-2781353-497-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781353/497-2016-01.pdf>497-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781353/497-2016-01.txt>497-2016-01 (Text)</a>
    </noscript>





------------

Form 498
---------------

Slate Mailer Late Payment Report

Form 498 is filed by a slate mailer organization upon receipt of a late payment.

Sections
````````

* Part A, Late Payments Attributed To 


* Part R, Late Payments Received From (`p. 2 <https://www.documentcloud.org/documents/2781352-498-2016-01.html#document/p2>`_)





Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#s498-cd">
                    S498_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#text-memo-cd">
                    TEXT_MEMO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#efs-filing-log-cd">
                    EFS_FILING_LOG_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/other_tables.html#received-filings-cd">
                    RECEIVED_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781352-498-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781352-498-2016-01.js", {
      container: "#DV-viewer-2781352-498-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781352/498-2016-01.pdf>498-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781352/498-2016-01.txt>498-2016-01 (Text)</a>
    </noscript>





------------

Form 501
---------------

Candidate Intention Statement

Form 501 is filed each election by candidates for state or local office.



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#f501-502-cd">
                    F501_502_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781351-501-2016-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781351-501-2016-01.js", {
      container: "#DV-viewer-2781351-501-2016-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781351/501-2016-01.pdf>501-2016-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781351/501-2016-01.txt>501-2016-01 (Text)</a>
    </noscript>





------------

Form 502
---------------

Campaign Bank Account Statement

Form 502 must be filed within 10 days of opening a campaign bank account at a financial institution in California.



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#f501-502-cd">
                    F501_502_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>







------------

Form 511
---------------

Paid Spokesperson Report

Form 511 is filed by committees that make expenditures totaling $5,000 or more to an individual for his or her appearance in a printed, televised, or radio advertisement, or in a telephone message, to support or oppose the qualification, passage, or defeat of a state or local ballot measure.



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781350-511-2015-01" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781350-511-2015-01.js", {
      container: "#DV-viewer-2781350-511-2015-01",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781350/511-2015-01.pdf>511-2015-01 (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781350/511-2015-01.txt>511-2015-01 (Text)</a>
    </noscript>





------------

Electronic Form 530
---------------

Electronic Issue Advocacy Report

On-line Form E-530 reports must be filed by anyone spending or promising to pay $50,000 or more for a communication disseminated within 45 days of an election, if the communication clearly identifies a candidate for state elective office but does not expressly advocate the election or defeat of that candidate.



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#rcpt-cd">
                    RCPT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#cvr-e530-cd">
                    CVR_E530_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>




Sample
``````

.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-2781349-E530-Instructions" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/2781349-E530-Instructions.js", {
      container: "#DV-viewer-2781349-E530-Instructions",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href=https://assets.documentcloud.org/documents/2781349/E530-Instructions.pdf>E530-Instructions (PDF)</a>
      <br />
      <a href=https://assets.documentcloud.org/documents/2781349/E530-Instructions.txt>E530-Instructions (Text)</a>
    </noscript>





------------

Form 900
---------------

Public employee's retirement board, candidate campaign statement

None



Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr-campaign-disclosure-cd">
                    CVR_CAMPAIGN_DISCLOSURE_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#cvr3-verification-info-cd">
                    CVR3_VERIFICATION_INFO_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#expn-cd">
                    EXPN_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/campaign_tables.html#rcpt-cd">
                    RCPT_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#filer-filings-cd">
                    FILER_FILINGS_CD
                </a>
            </td>
        </tr>
    
        <tr>
            <td>
                <a href="../dbtables/common_tables.html#smry-cd">
                    SMRY_CD
                </a>
            </td>
        </tr>
    
    </tbody>
    </table>
    </div>






