Lobbying tables
================================


The CAL-ACCESS database contains 32 tables that, according to the official documentation (see `here <https://www.documentcloud.org/documents/2711617-ReadMe-Zip/pages/1.html>`_ and `here <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/4.html>`_), store information specific to lobbying disclosure filings. These tables are outlined below.

.. warning::

    Most definitions below are drawn from the spotty and incomplete `official documentation <officialdocumentation.html>`_ verbatim. As we continue our research, we plan to improve the descriptions.

    For the time being, to be absolutely certain about what each table and field contains, you should compare the electronic data back to the original paper records published by the state.


------------

Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Additional data from lobbyist disclosure forms (615, 625, 635, and 645)

**Sample:** `CVR2_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_LOBBY_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p43-thumbnail.gif'></a><p>p. 43</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p36-thumbnail.gif'></a><p>p. 36</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2LobbyDisclosureCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of partner, owner, officer, employer if the entity is an individual. Only required by Form 635.</td>
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
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms

**Sample:** `CVR2_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_REGISTRATION_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p44-thumbnail.gif'></a><p>p. 44</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p45-thumbnail.gif'></a><p>p. 45</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p37-thumbnail.gif'></a><p>p. 37</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p73-thumbnail.gif'></a><p>p. 73</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2RegistrationCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




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
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 10)</td>
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
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or suffix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page information for lobbying disclosure forms

**Sample:** `CVR_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_LOBBY_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p32-thumbnail.gif'></a><p>p. 32</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p34-thumbnail.gif'></a><p>p. 34</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/17.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p17-thumbnail.gif'></a><p>p. 17</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p21-thumbnail.gif'></a><p>p. 21</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p68-thumbnail.gif'></a><p>p. 68</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p70-thumbnail.gif'></a><p>p. 70</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p55-thumbnail.gif'></a><p>p. 55</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p56-thumbnail.gif'></a><p>p. 56</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrLobbyDisclosureCd contains data collected from the following filing forms, form parts and schedules:



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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_n_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_y_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>cum_beg_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning date</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
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
            <td>Filer last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition business city</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition business phone number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition business state</td>
        </tr>
    
    
    
        <tr>
            <td>firm_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Form, employer or coalition business ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Description of lobbying activity. Applies to forms 635 and 645. Additional description may be provided in text records.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_n_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity none&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_y_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity Form 630 attached&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
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
            <td>major_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Major donor first name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Major donor last name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor suffix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor title or prefix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>nopart1_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part I information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>nopart2_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part II information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>part1_1_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners Form 615 attached ...&#39; checkbox. Applies only to form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>part1_2_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners listed below ...&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>rcpcmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient committee or major donor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>rcpcmte_nm</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient committee name</td>
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
            <td>Amendment number. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>sender_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of lobbyist entity that is submitting this report. The field is used to authenticate the filer and allows the firm to submit forms for its lobbyists.</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p67-thumbnail.gif'></a><p>p. 67</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms (601, 602, 603, 604, 606, and 607)

**Sample:** `CVR_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_REGISTRATION_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p38-thumbnail.gif'></a><p>p. 38</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p39-thumbnail.gif'></a><p>p. 39</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p22-thumbnail.gif'></a><p>p. 22</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p23-thumbnail.gif'></a><p>p. 23</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p24-thumbnail.gif'></a><p>p. 24</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p26-thumbnail.gif'></a><p>p. 26</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p27-thumbnail.gif'></a><p>p. 27</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/83.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p83-thumbnail.gif'></a><p>p. 83</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p84-thumbnail.gif'></a><p>p. 84</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p85-thumbnail.gif'></a><p>p. 85</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrRegistrationCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)




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
            <td>a_b_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Individual or business entity city</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of individual or business entity</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Individual or business entity state</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Individual or business entity ZIP Code.</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>auth_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address city</td>
        </tr>
    
    
    
        <tr>
            <td>auth_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Authorized lobbying firm business name. Applies to Form 602.</td>
        </tr>
    
    
    
        <tr>
            <td>auth_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address state</td>
        </tr>
    
    
    
        <tr>
            <td>auth_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>bus_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Business included activity checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>bus_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer business address city</td>
        </tr>
    
    
    
        <tr>
            <td>bus_class</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classifiction values of business related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_descr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of business classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>bus_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer business address email</td>
        </tr>
    
    
    
        <tr>
            <td>bus_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address fax number</td>
        </tr>
    
    
    
        <tr>
            <td>bus_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>bus_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer business address state</td>
        </tr>
    
    
    
        <tr>
            <td>bus_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>c_less50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with fewer than 50 members check this box</td>
        </tr>
    
    
    
        <tr>
            <td>c_more50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with more than 50 check this box.</td>
        </tr>
    
    
    
        <tr>
            <td>complet_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ethics orientation class completion date. Applies to Form 604. As filed by the lobbyist.</td>
        </tr>
    
    
    
        <tr>
            <td>descrip_1</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of business activity, industry or other</td>
        </tr>
    
    
    
        <tr>
            <td>descrip_2</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of specific or other lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>eff_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date of authoarization or termination</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
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
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the lobbyist employer or firm. Applies to Forms 604, 606, 607.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>ind_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Individual checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>ind_class</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classification values to category industry related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>ind_descr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of industry classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>influen_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Attempt to influence state legislation</td>
        </tr>
    
    
    
        <tr>
            <td>l_firm_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying firm within the ... &#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>lby_604_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in this 604 statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>lby_reg_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in form 601/603 registration statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying within the meaning...&#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_int</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of Part III lobbying interests. Applies to Form 603</td>
        </tr>
    
    
    
        <tr>
            <td>ls_beg_yr</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative session begins</td>
        </tr>
    
    
    
        <tr>
            <td>ls_end_yr</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative sessions ends</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
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
            <td>newcert_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will require a new certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>oth_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>qual_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified. Applies to forms 601 and 603. Only occurs once in lobbying filings.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>rencert_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will take a renewel certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number as reported by the filer. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report or amendment is filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>sender_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the lobbyist entity submitting this report. This is equal to the filer ID if the filer is the submitting the report and the firm or employer if they are submitting the report.</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>st_agency</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>List of identified state agencies. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>st_leg_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will lobby state legislature checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_firm</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Lobby firm named in &#39;Statement of Responsible Officer&#39;This field only applies to Form 601.</td>
        </tr>
    
    
    
        <tr>
            <td>trade_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry, trade or professional checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*bus_class*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*ind_class*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p85-thumbnail.gif'></a><p>p. 85</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*influen_yn*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*st_leg_yn*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Amends lobbying disclosure filings (Form 690)

**Sample:** `F690P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F690P2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p60-thumbnail.gif'></a><p>p. 60</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p50-thumbnail.gif'></a><p>p. 50</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




Filing Forms
^^^^^^^^^^^^
F690P2Cd contains data collected from the following filing forms, form parts and schedules:



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
            <td>Record Type Value: F690</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>exec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the original report (or prior amendment to the original report) was executed on.</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Report period to/through date of original.</td>
        </tr>
    
    
    
        <tr>
            <td>chg_parts</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on part(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>chg_sects</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on sections(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>amend_txt1</td>
            <td>String (up to 330)</td>
            <td>No</td>
            <td>Description of changes to the filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LattCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist disclosure attachment schedules for payments

**Sample:** `LATT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LATT_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/81.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p81-thumbnail.gif'></a><p>p. 81</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p52-thumbnail.gif'></a><p>p. 52</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p53-thumbnail.gif'></a><p>p. 53</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p80-thumbnail.gif'></a><p>p. 80</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




Filing Forms
^^^^^^^^^^^^
LattCd contains data collected from the following filing forms, form parts and schedules:



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>cum_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>cumbeg_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning to date</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payment Recipient/Payee</td>
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
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
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
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>pmt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LATT</td>
        </tr>
    
    
    
        <tr>
            <td>recip_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient suffix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>recip_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p80-thumbnail.gif'></a><p>p. 80</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LccmCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbying campaign contributions reported on Forms 615 Part 2,
625 Part 4B, 635 Part 4B and the 645 Part 3B.

**Sample:** `LCCM_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LCCM_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/83.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p83-thumbnail.gif'></a><p>p. 83</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p84-thumbnail.gif'></a><p>p. 84</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p55-thumbnail.gif'></a><p>p. 55</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




Filing Forms
^^^^^^^^^^^^
LccmCd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 4: Campaign Contributions Made



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor first name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code for Recipient of the Campaign Contribution Value</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LCCM</td>
        </tr>
    
    
    
        <tr>
            <td>recip_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>recip_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient identification number</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>recip_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>recip_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LempCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist employers and subcontracted clients (Form 601)

**Sample:** `LEMP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEMP_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p85-thumbnail.gif'></a><p>p. 85</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p56-thumbnail.gif'></a><p>p. 56</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p91-thumbnail.gif'></a><p>p. 91</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




Filing Forms
^^^^^^^^^^^^
LempCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)

    * Part 2: Section A, Lobbyist Employers

    * Part 2: Section B: Subcontracted Clients





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
            <td>agencylist</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agencies to be lobbied</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>cli_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employing client city</td>
        </tr>
    
    
    
        <tr>
            <td>cli_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employing client first name</td>
        </tr>
    
    
    
        <tr>
            <td>cli_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employing client last name</td>
        </tr>
    
    
    
        <tr>
            <td>cli_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cli_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>cli_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employing client phone number</td>
        </tr>
    
    
    
        <tr>
            <td>cli_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employing client state</td>
        </tr>
    
    
    
        <tr>
            <td>cli_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>client_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the Part 2A employer or Part 2B Client/Employer</td>
        </tr>
    
    
    
        <tr>
            <td>con_period</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Period of the contract</td>
        </tr>
    
    
    
        <tr>
            <td>descrip</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of employer/client lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>eff_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective Date of Lobbying Contract</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Record Type Value: LEMP</td>
        </tr>
    
    
    
        <tr>
            <td>sub_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm city</td>
        </tr>
    
    
    
        <tr>
            <td>sub_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Subcontracting lobbying firms name</td>
        </tr>
    
    
    
        <tr>
            <td>sub_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm phone number</td>
        </tr>
    
    
    
        <tr>
            <td>sub_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm state</td>
        </tr>
    
    
    
        <tr>
            <td>sub_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>subfirm_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of subcontracting lobbying firm</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LexpCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbying activity expenditures schedule information, reported in
Forms 615 Part 1, 625 Part 3A, 635 Part 3C, and 645 Part 2A.

**Sample:** `LEXP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEXP_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p86-thumbnail.gif'></a><p>p. 86</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p58-thumbnail.gif'></a><p>p. 58</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




Filing Forms
^^^^^^^^^^^^
LexpCd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to the tranaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>bene_amt</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Amount benefiting benficiary</td>
        </tr>
    
    
    
        <tr>
            <td>bene_name</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Name of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>bene_posit</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official position of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>credcardco</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the credit card company, if paid using a card</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of expenditure</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of the expense and a description or explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee city</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee first name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEXP</td>
        </tr>
    
    
    
        <tr>
            <td>recsubtype</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Record Subtype</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*recsubtype*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist registration amendment information (Form 605 Part I).

**Sample:** `LOBBY_AMENDMENTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBY_AMENDMENTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p90-thumbnail.gif'></a><p>p. 90</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p91-thumbnail.gif'></a><p>p. 91</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p64-thumbnail.gif'></a><p>p. 64</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p65-thumbnail.gif'></a><p>p. 65</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/89.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p89-thumbnail.gif'></a><p>p. 89</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




Filing Forms
^^^^^^^^^^^^
LobbyAmendmentsCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




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
            <td>Yes</td>
            <td>Record Type Value: F605</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>exec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this amendment executed on</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting date to/through date of original</td>
        </tr>
    
    
    
        <tr>
            <td>add_l_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_l_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist suffix</td>
        </tr>
    
    
    
        <tr>
            <td>del_l_cb</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Delete lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>del_l_eff</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyiest suffix</td>
        </tr>
    
    
    
        <tr>
            <td>add_le_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyiest employer checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_le_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist or employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>del_le_cb</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Delete lobbyist employer check box</td>
        </tr>
    
    
    
        <tr>
            <td>del_le_eff</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyiest employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_namt</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Delete lobbyist employer name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist employer name</td>
        </tr>
    
    
    
        <tr>
            <td>add_lf_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_lf_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_lf_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>del_lf_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Delete lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>del_lf_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Delete lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_lf_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>other_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other amendments checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>other_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Other amendments effective date</td>
        </tr>
    
    
    
        <tr>
            <td>other_desc</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of changes</td>
        </tr>
    
    
    
        <tr>
            <td>f606_yes</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing all activity</td>
        </tr>
    
    
    
        <tr>
            <td>f606_no</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing employment but staying active</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Holds lobbyist log data for web display

**Sample:** `LOBBYING_CHG_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYING_CHG_LOG_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p91-thumbnail.gif'></a><p>p. 91</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/92.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p92-thumbnail.gif'></a><p>p. 92</p></div></div>





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
            <td>change_no</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Number of changes this session</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>log_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Foreign key referencing FilerTypesCd.filer_type</td>
        </tr>
    
    
    
        <tr>
            <td>correction_flag</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>action</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>attribute_changed</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ethics_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>interests</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_full_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name of filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>City address of filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_st</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>State address of filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip</td>
            <td>Integer</td>
            <td>No</td>
            <td>ZIP Code of filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_phone</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Phone number of filer</td>
        </tr>
    
    
    
        <tr>
            <td>entity_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented. The values might refer to either FILER_TYPES_CD.FILER_TYPE or GROUP_TYPES_CD.GRP_ID, but that&#39;s just a guess.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_name</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_city</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_st</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_zip</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_phone</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>responsible_officer</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_type*


.. raw:: html

    <div class="wy-table-responsive">
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





------------

LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table.

**Sample:** `LOBBYIST_CONTRIBUTIONS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/92.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p92-thumbnail.gif'></a><p>p. 92</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/93.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p93-thumbnail.gif'></a><p>p. 93</p></div></div>





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
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistContributions2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table. Temporary table used to generate
disclosure table (Lobbyist Contributions 3)

**Sample:** `LOBBYIST_CONTRIBUTIONS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/93.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p93-thumbnail.gif'></a><p>p. 93</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div></div>





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
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistContributions3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table.

**Sample:** `LOBBYIST_CONTRIBUTIONS3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div></div>





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
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Start date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End date of filing period</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistEmpLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div></div>





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
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
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



------------

LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div></div>





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
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
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



------------

LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Information for lobbyist's primary employer

**Sample:** `LOBBYIST_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/97.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p97-thumbnail.gif'></a><p>p. 97</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/98.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p98-thumbnail.gif'></a><p>p. 98</p></div></div>





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
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
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

LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/98.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p98-thumbnail.gif'></a><p>p. 98</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/99.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p99-thumbnail.gif'></a><p>p. 99</p></div></div>





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
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7 total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8 total amount</td>
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

LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/99.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p99-thumbnail.gif'></a><p>p. 99</p></div></div>





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
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
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

LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div></div>





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
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div></div>





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
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistEmployerHistoryCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_HISTORY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/97.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p97-thumbnail.gif'></a><p>p. 97</p></div></div>





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
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer Name</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest Code</td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Interest name.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 1 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 2 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 3 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 4 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 5 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 6 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 7 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter 8 total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount.</td>
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

LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/103.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p103-thumbnail.gif'></a><p>p. 103</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/104.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p104-thumbnail.gif'></a><p>p. 104</p></div></div>





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
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/104.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p104-thumbnail.gif'></a><p>p. 104</p></div></div>





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
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/105.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p105-thumbnail.gif'></a><p>p. 105</p></div></div>





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
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/100.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p100-thumbnail.gif'></a><p>p. 100</p></div></div>





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
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>ext_lby_actvty</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirmEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/100.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p100-thumbnail.gif'></a><p>p. 100</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/101.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p101-thumbnail.gif'></a><p>p. 101</p></div></div>





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
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>ext_lby_actvty</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirmHistoryCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_HISTORY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/101.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p101-thumbnail.gif'></a><p>p. 101</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div></div>





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
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the Firm/Employer/Coalition.</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Name of Firm/Employer/Coalition</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>



------------

LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div></div>





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
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
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



------------

LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/103.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p103-thumbnail.gif'></a><p>p. 103</p></div></div>





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
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
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



------------

LothCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Payment to other lobbying firms listed of Form 625 Part 3B

**Sample:** `LOTH_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOTH_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/106.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p106-thumbnail.gif'></a><p>p. 106</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/107.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p107-thumbnail.gif'></a><p>p. 107</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p68-thumbnail.gif'></a><p>p. 68</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




Filing Forms
^^^^^^^^^^^^
LothCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




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
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>cum_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>firm_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>pmt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOTH</td>
        </tr>
    
    
    
        <tr>
            <td>subj_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_nams</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Suffix of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_namt</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Prefix or title of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>





------------

LpayCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Payments made or received by lobbying firms, reported on
Form 625 Part 2 and 635 Part 3B

**Sample:** `LPAY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LPAY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/107.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p107-thumbnail.gif'></a><p>p. 107</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/108.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p108-thumbnail.gif'></a><p>p. 108</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/109.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p109-thumbnail.gif'></a><p>p. 109</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p70-thumbnail.gif'></a><p>p. 70</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




Filing Forms
^^^^^^^^^^^^
LpayCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms




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
            <td>advan_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Advance and other payments amount</td>
        </tr>
    
    
    
        <tr>
            <td>advan_dscr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of advance and other payments</td>
        </tr>
    
    
    
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
            <td>Backreference to transaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer city</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer state</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Employer Values</td>
        </tr>
    
    
    
        <tr>
            <td>fees_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Fees and retainers amount</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
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
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LPAY</td>
        </tr>
    
    
    
        <tr>
            <td>reimb_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Reimbursements of expense amount</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
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
    </table>
    </div>




