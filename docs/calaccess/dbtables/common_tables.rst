================================
Common tables
================================


The CAL-ACCESS database contains 9 tables that, according to the official documentation (see `here <https://www.documentcloud.org/documents/2711617-ReadMe-Zip/pages/1.html>`_ and `here <https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/5.html>`_), store information common to campaign finance and lobbyist disclosure filings.



------------

*********************
CVR_E530_CD
*********************

Probably Cover Pages for Electronic Form 530. This table is listed in the record
layouts, but neither table nor any of its columns are labeled.

**Sample:** `CVR_E530_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_E530_CD.TSV>`_


Filing forms
============



* `Electronic Form 530 <filingforms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)




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
            <td>entity_cd</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filer city</td>
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
            <td>occupation</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 13)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 46)</td>
            <td>No</td>
            <td>Candidate last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 21)</td>
            <td>No</td>
            <td>Candidate first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate suffix</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>District Code</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>pmnt_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>pmnt_amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_literature</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_printads</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_radio</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_tv</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_it</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_billboards</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_other</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>other_desc</td>
            <td>String (up to 49)</td>
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
        
        </tbody>
        
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html">9</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html">10</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html">11</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html">8</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html">9</a>)
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
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html">11</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/12.html">12</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html">13</a>)
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
            Sources: Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/16.html">16</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/17.html">17</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html">18</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html">20</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/21.html">21</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/22.html">22</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p30-thumbnail.gif'></a><p>p. 30</p></div></div>







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



* `Electronic Form 530 <filingforms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 405 <filingforms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 415 <filingforms.html#form-415>`_ (Title Unknown)



* `Form 416 <filingforms.html#form-416>`_ (Title Unknown)



* `Form 419 <filingforms.html#form-419>`_ (Ballot Measure Committee Campaign Statement-Long Form)



* `Form 420 <filingforms.html#form-420>`_ (Recipient Committee Campaign Statement-Long Form)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 430 <filingforms.html#form-430>`_ (Title Unknown)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 470 <filingforms.html#form-470>`_ (Officeholder and Candidate Campaign Statement, Short Form)



* `Form 490 <filingforms.html#form-490>`_ (Officeholder/Candidate Campaign Statement-Long Form)



* `Form 495 <filingforms.html#form-495>`_ (Supplemental Pre-Election Campaign Statement)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 501 <filingforms.html#form-501>`_ (Candidate Intention Statement)



* `Form 502 <filingforms.html#form-502>`_ (Campaign Bank Account Statement)



* `Form 511 <filingforms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 605 <filingforms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Form 690 <filingforms.html#form-690>`_ (Amendment to Lobbying Disclosure Report)



* `Form 700 <filingforms.html#form-700>`_ (Statement of Economic Interest)



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




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
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>period_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the period when the filing was recieved.</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment number where 0 is an original filing and 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>filing_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the filing entered into the system</td>
        </tr>
    
    
    
        <tr>
            <td>stmnt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>stmnt_status</td>
            <td>Integer</td>
            <td>No</td>
            <td>The status of the statement. If the filing has been reviewed or not reviewed.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>user_id</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>User identifier of the PRD user who logged the filing</td>
        </tr>
    
    
    
        <tr>
            <td>special_audit</td>
            <td>Integer</td>
            <td>No</td>
            <td>Denotes whether the filing has been audited for money laundering or other special condition.</td>
        </tr>
    
    
    
        <tr>
            <td>fine_audit</td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates whether a filing has been audited for a fine</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date filing received</td>
        </tr>
    
    
    
        <tr>
            <td>filing_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


form_id
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
                <td>F401</td>
                <td>Form 401: Slate Mailer Organization Campaign Statement</td>
            </tr>
        
            <tr>
                <td>F402</td>
                <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
            </tr>
        
            <tr>
                <td>F405</td>
                <td>Form 405: Amendment to Campaign Disclosure Statement</td>
            </tr>
        
            <tr>
                <td>F410</td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td>F415</td>
                <td>Form 415: Title Unknown</td>
            </tr>
        
            <tr>
                <td>F416</td>
                <td>Form 416: Title Unknown</td>
            </tr>
        
            <tr>
                <td>F419</td>
                <td>Form 419: Ballot Measure Committee Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td>F420</td>
                <td>Form 420: Recipient Committee Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td>F425</td>
                <td>Form 425: Semi-Annual Statement of no Activity</td>
            </tr>
        
            <tr>
                <td>F430</td>
                <td>Form 430: Title Unknown</td>
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
                <td>F470</td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
            <tr>
                <td>F490</td>
                <td>Form 490: Officeholder/Candidate Campaign Statement-Long Form</td>
            </tr>
        
            <tr>
                <td>F495</td>
                <td>Form 495: Supplemental Pre-Election Campaign Statement</td>
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
                <td>F501</td>
                <td>Form 501: Candidate Intention Statement</td>
            </tr>
        
            <tr>
                <td>F502</td>
                <td>Form 502: Campaign Bank Account Statement</td>
            </tr>
        
            <tr>
                <td>F511</td>
                <td>Form 511: Paid Spokesperson Report</td>
            </tr>
        
            <tr>
                <td>E530</td>
                <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
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
                <td>F605</td>
                <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
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
                <td>S630</td>
                <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
            </tr>
        
            <tr>
                <td>F635</td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>S635-C</td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td>S640</td>
                <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
            </tr>
        
            <tr>
                <td>F645</td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
            <tr>
                <td>F690</td>
                <td>Form 690: Amendment to Lobbying Disclosure Report</td>
            </tr>
        
            <tr>
                <td>F700</td>
                <td>Form 700: Statement of Economic Interest</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td>F111</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F410 AT</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F410ATR</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F421</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F440</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F470S</td>
                <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
            </tr>
        
            <tr>
                <td>F480</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F500</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F501502</td>
                <td>Forms 501 and/or 502 (Candidate Intention and/or Bank Account Statements)</td>
            </tr>
        
            <tr>
                <td>F555</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F666</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F777</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F888</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F999</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: CalAccessTablesWeb (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/65.html">65</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


stmnt_type
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
            Sources: Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html">6</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


stmnt_status
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
                <td>11001</td>
                <td>COMPLETE</td>
            </tr>
        
            <tr>
                <td>11002</td>
                <td>INCOMPLETE</td>
            </tr>
        
            <tr>
                <td>11003</td>
                <td>NEEDS REVIEW</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Lookup-Codes-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html">6</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


filing_type
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
                <td>22001</td>
                <td>Electronic</td>
            </tr>
        
            <tr>
                <td>22006</td>
                <td>Cal Online</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: FAQ (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html">2</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p64-thumbnail.gif'></a><p>p. 64</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p65-thumbnail.gif'></a><p>p. 65</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p66-thumbnail.gif'></a><p>p. 66</p></div></div>







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
            <td>xref_filer_id</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>The type of filer. These values are found FILER_TYPES_CD.DESCRIPTION</td>
        </tr>
    
    
    
        <tr>
            <td>status</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The status of the filer. Includes a mixture of values found in the STATUS_TYPE and STATUS_DESC columns on FILER_STATUS_TYPES_CD</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for status</td>
        </tr>
    
    
    
        <tr>
            <td>naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name, sometimes full name</td>
        </tr>
    
    
    
        <tr>
            <td>namf</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td>namt</td>
            <td>String (up to 70)</td>
            <td>No</td>
            <td>Name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>adr1</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>First line of street address</td>
        </tr>
    
    
    
        <tr>
            <td>adr2</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Second line of street address</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>City address</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>State</td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>phon</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


filer_type
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
                <td>NOT DEFINED</td>
                <td>Undefined</td>
            </tr>
        
            <tr>
                <td>ALL FILERS</td>
                <td>All filers</td>
            </tr>
        
            <tr>
                <td>CANDIDATE/OFFICEHOLDER</td>
                <td>Candidate/officeholder</td>
            </tr>
        
            <tr>
                <td>CLIENT</td>
                <td>Client</td>
            </tr>
        
            <tr>
                <td>EMPLOYER</td>
                <td>Employer</td>
            </tr>
        
            <tr>
                <td>FIRM</td>
                <td>Firm</td>
            </tr>
        
            <tr>
                <td>INDIVIDUAL</td>
                <td>Individual</td>
            </tr>
        
            <tr>
                <td>INITIATIVE</td>
                <td>Initiative</td>
            </tr>
        
            <tr>
                <td>LOBBYIST</td>
                <td>Lobbyist</td>
            </tr>
        
            <tr>
                <td>MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE</td>
                <td>Major donor or indenpendent expenditure committee</td>
            </tr>
        
            <tr>
                <td>PAYMENT TO INFLUENCE</td>
                <td>Payment to influence</td>
            </tr>
        
            <tr>
                <td>PREPAID ACCOUNT</td>
                <td>Prepaid account</td>
            </tr>
        
            <tr>
                <td>PROPONENT</td>
                <td>Proponent</td>
            </tr>
        
            <tr>
                <td>PROPOSITION</td>
                <td>Proposition</td>
            </tr>
        
            <tr>
                <td>RECIPIENT COMMITTEE</td>
                <td>Recipient committee</td>
            </tr>
        
            <tr>
                <td>SLATE MAILER ORGANIZATIONS</td>
                <td>Slate mailer organization</td>
            </tr>
        
            <tr>
                <td>TREASURER/RESPONSIBLE OFFICER</td>
                <td>Treasurer/responsible officer</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Filer-Types-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774536-Filer-Types-Cd/pages/1.html">1</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


status
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
                <td></td>
                <td>Undefined</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td>P</td>
                <td>PENDING</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>REVOKED</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>SUSPENDED</td>
            </tr>
        
            <tr>
                <td>W</td>
                <td>WITHDRAWN</td>
            </tr>
        
            <tr>
                <td>Y</td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td>N</td>
                <td>INACTIVE</td>
            </tr>
        
            <tr>
                <td>T</td>
                <td>TERMINATED</td>
            </tr>
        
            <tr>
                <td>ACTIVE</td>
                <td>ACTIVE</td>
            </tr>
        
            <tr>
                <td>INACTIVE</td>
                <td>INACTIVE</td>
            </tr>
        
            <tr>
                <td>TERMINATED</td>
                <td>TERMINATED</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Filer-Status-Types-Cd (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774537-Filer-Status-Types-Cd/pages/1.html">1</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p68-thumbnail.gif'></a><p>p. 68</p></div></div>


*FAQ*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711615/pages/FAQ-p2-thumbnail.gif'></a><p>p. 2</p></div></div>







------------

*********************
FILINGS_CD
*********************

This table is the parent table from which all links and association to
a filing are derived.

**Sample:** `FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILINGS_CD.TSV>`_



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
            <td>filing_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


filing_type
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
                <td>22001</td>
                <td>Electronic</td>
            </tr>
        
            <tr>
                <td>22002</td>
                <td>Key data entry</td>
            </tr>
        
            <tr>
                <td>22003</td>
                <td>Historical lobby</td>
            </tr>
        
            <tr>
                <td>22004</td>
                <td>Historical campaign</td>
            </tr>
        
            <tr>
                <td>22005</td>
                <td>AMS</td>
            </tr>
        
            <tr>
                <td>22006</td>
                <td>Cal Online</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: FAQ (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html">2</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p75-thumbnail.gif'></a><p>p. 75</p></div></div>







------------

*********************
HDR_CD
*********************

Electronic filing record header data. Contains information
identifying vendor and Cal Format version.

**Sample:** `HDR_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HDR_CD.TSV>`_



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
            <td>cal_ver</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>CAL Version number the filing was made using</td>
        </tr>
    
    
    
        <tr>
            <td>ef_type</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Electronic filing type. This will always have the         value of &quot;CAL&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>hdr_comment</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Typically used for development and test filings</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type. Value: HDR</td>
        </tr>
    
    
    
        <tr>
            <td>soft_name</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Filing software name used to electronically file</td>
        </tr>
    
    
    
        <tr>
            <td>soft_ver</td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filing software version number</td>
        </tr>
    
    
    
        <tr>
            <td>state_cd</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>The state code value entered in the electronic filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


ef_type
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
                <td>CAL</td>
                <td>.CAL format</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html">5</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html">4</a>)
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
                <td>HDR</td>
                <td>HDR</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html">5</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html">4</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


state_cd
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
                <td>CA</td>
                <td>California</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html">5</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html">4</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/1.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p1-thumbnail.gif'></a><p>p. 1</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p5-thumbnail.gif'></a><p>p. 5</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p4-thumbnail.gif'></a><p>p. 4</p></div></div>







------------

*********************
HEADER_CD
*********************

Lookup table used to report Form 460 information in the Agency Management System.

**Sample:** `HEADER_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HEADER_CD.TSV>`_



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
            <td>line_number</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 5)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td>section_label</td>
            <td>String (up to 58)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>comments1</td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>comments2</td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>label</td>
            <td>String (up to 98)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_a</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_b</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_c</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>show_c</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>show_b</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


form_id
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
                <td>AF490</td>
                <td>Form 490, Part A</td>
            </tr>
        
            <tr>
                <td>AP1</td>
                <td>Allocation Part 1</td>
            </tr>
        
            <tr>
                <td>AP2</td>
                <td>Allocation Part 2</td>
            </tr>
        
            <tr>
                <td>BF490</td>
                <td>Form 490, Part B</td>
            </tr>
        
            <tr>
                <td>CF490</td>
                <td>Form 490, Part C</td>
            </tr>
        
            <tr>
                <td>DF490</td>
                <td>Form 490, Part D</td>
            </tr>
        
            <tr>
                <td>EF490</td>
                <td>Form 490, Part E</td>
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
                <td>FF490</td>
                <td>Form 490, Part F</td>
            </tr>
        
            <tr>
                <td>HF490</td>
                <td>Form 490, Part H</td>
            </tr>
        
            <tr>
                <td>IF490</td>
                <td>Form 490, Part I</td>
            </tr>
        
        </tbody>
        
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
                <td>AP1</td>
                <td>AP1</td>
            </tr>
        
            <tr>
                <td>AP2</td>
                <td>AP2</td>
            </tr>
        
            <tr>
                <td>SMRY_HEADER</td>
                <td>SMRY_HEADER</td>
            </tr>
        
        </tbody>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p80-thumbnail.gif'></a><p>p. 80</p></div></div>







------------

*********************
SMRY_CD
*********************

Summary totals from filings.

**Sample:** `SMRY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SMRY_CD.TSV>`_


Filing forms
============



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)

    * Schedule A, Payments Received

    * Schedule B, Payments Made

    * Schedule B-1, Payments Made by Agent or Independent Contractor




* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

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




* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)

    * Part 2, Payments Received in Connection with Lobbying Activity

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission




* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)

    * Part 2 (Payments Made this Period), Section A: Activity Expenses

    * Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action

    * Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission




* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




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
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: SMRY</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>amount_a</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column A</td>
        </tr>
    
    
    
        <tr>
            <td>amount_b</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column B</td>
        </tr>
    
    
    
        <tr>
            <td>amount_c</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column C</td>
        </tr>
    
    
    
        <tr>
            <td>elec_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Election date</td>
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
                <td>SMRY</td>
                <td>SMRY</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html">35</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html">72</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html">27</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html">59</a>)
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
                <td>F401A</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td>F401B</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td>F401B-1</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
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
                <td>A</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
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
                <td>C</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
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
                <td>F</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
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
        
            <tr>
                <td>I</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
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
                <td>F625</td>
                <td>Form 625: Report of Lobbying Firm</td>
            </tr>
        
            <tr>
                <td>F625P2</td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td>F625P3A</td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F625P3B</td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
            </tr>
        
            <tr>
                <td>F635</td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>F635P3A</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists</td>
            </tr>
        
            <tr>
                <td>F635P3B</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
            </tr>
        
            <tr>
                <td>F635P3C</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F635P3D</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action</td>
            </tr>
        
            <tr>
                <td>F635P3E</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission</td>
            </tr>
        
            <tr>
                <td>S640</td>
                <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
            </tr>
        
            <tr>
                <td>F645</td>
                <td>Form 645: Report of Person Spending $5,000 or More</td>
            </tr>
        
            <tr>
                <td>F645P2A</td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F645P2B</td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action</td>
            </tr>
        
            <tr>
                <td>F645P2C</td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission</td>
            </tr>
        
            <tr>
                <td>F900</td>
                <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
            </tr>
        
            <tr>
                <td>401A</td>
                <td>A</td>
            </tr>
        
            <tr>
                <td>401B</td>
                <td>B</td>
            </tr>
        
            <tr>
                <td>401B-1</td>
                <td>B-1</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/86.html">86</a>), Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/36.html">36</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html">37</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/73.html">73</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html">74</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html">27</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/28.html">28</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html">59</a>, <a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/60.html">60</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/131.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p131-thumbnail.gif'></a><p>p. 131</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/132.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p132-thumbnail.gif'></a><p>p. 132</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p86-thumbnail.gif'></a><p>p. 86</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p73-thumbnail.gif'></a><p>p. 73</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p60-thumbnail.gif'></a><p>p. 60</p></div></div>







------------

*********************
SPLT_CD
*********************

Split Transaction Record - Used as a child record for schedules:
A, B1, B2, C, D, H and/or F450P5 when disclosing Per Election to Date information.

**Sample:** `SPLT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SPLT_CD.TSV>`_


Filing forms
============



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule C, Non-Monetary Contributions Received

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule H, Loans Made to Others





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
            <td>elec_amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Per Election to Date Amount</td>
        </tr>
    
    
    
        <tr>
            <td>elec_code</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Per Election to Date Code</td>
        </tr>
    
    
    
        <tr>
            <td>elec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Election</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>pform_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Parent Schedule Type</td>
        </tr>
    
    
    
        <tr>
            <td>ptran_id</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Parent transaction ID</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Look-up Codes
=============


elec_code
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
                <td>P</td>
                <td>Primary</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>General</td>
            </tr>
        
            <tr>
                <td>S</td>
                <td>Special</td>
            </tr>
        
            <tr>
                <td>R</td>
                <td>Runoff</td>
            </tr>
        
            <tr>
                <td>g</td>
                <td>General</td>
            </tr>
        
            <tr>
                <td>p</td>
                <td>primary</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>D</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>F</td>
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
                <td>X</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>O</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>0</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>1</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>2</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html">18</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>


pform_type
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
                <td>A</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td>B1</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
            </tr>
        
            <tr>
                <td>B2</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
            </tr>
        
            <tr>
                <td>D</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
            </tr>
        
            <tr>
                <td>F450P5</td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html">18</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/132.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p132-thumbnail.gif'></a><p>p. 132</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p18-thumbnail.gif'></a><p>p. 18</p></div></div>







------------

*********************
TEXT_MEMO_CD
*********************

Text memos attached to electronic filings

**Sample:** `TEXT_MEMO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/TEXT_MEMO_CD.TSV>`_


Filing forms
============



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 405 <filingforms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



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



* `Form 605 <filingforms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




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
            <td>Record Type Value: TEXT</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>ref_no</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Links text memo to a specific record</td>
        </tr>
    
    
    
        <tr>
            <td>text4000</td>
            <td>String (up to 4000)</td>
            <td>No</td>
            <td>Contents of the text memo</td>
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
                <td>TEXT</td>
                <td>TEXT</td>
            </tr>
        
            <tr>
                <td>MEMO</td>
                <td>MEMO</td>
            </tr>
        
            <tr>
                <td>trun</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Unde</td>
                <td>Under</td>
            </tr>
        
            <tr>
                <td>am</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>sele</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>Term</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>re</td>
                <td>Unknown</td>
            </tr>
        
            <tr>
                <td>i</td>
                <td>Unknown</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html">16</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html">13</a>)
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
                <td>F405</td>
                <td>Form 405: Amendment to Campaign Disclosure Statement</td>
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
                <td>F605</td>
                <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
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
        
            <tr>
                <td>410</td>
                <td>Form 410: Statement of Organization Recipient Committee</td>
            </tr>
        
            <tr>
                <td>460</td>
                <td>Form 460: Recipient Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td>461</td>
                <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
            </tr>
        
            <tr>
                <td>465</td>
                <td>Form 465: Supplemental Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td>496</td>
                <td>Form 496: Late Independent Expenditure Report</td>
            </tr>
        
            <tr>
                <td>497</td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td>497P1</td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td>497P2</td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
            <tr>
                <td>F401A</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
            </tr>
        
            <tr>
                <td>F401B</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
            </tr>
        
            <tr>
                <td>F401B-1</td>
                <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
            </tr>
        
            <tr>
                <td>F450P5</td>
                <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
            </tr>
        
            <tr>
                <td>F461P1</td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 1, Name and Address of Filer</td>
            </tr>
        
            <tr>
                <td>F461P2</td>
                <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 2, Nature and Interests of Filer</td>
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
                <td>F496P3</td>
                <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
            </tr>
        
            <tr>
                <td>F497P1</td>
                <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
            </tr>
        
            <tr>
                <td>F497P2</td>
                <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
            </tr>
        
            <tr>
                <td>F498-A</td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
            </tr>
        
            <tr>
                <td>F498-R</td>
                <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
            </tr>
        
            <tr>
                <td>F601P2A</td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
            </tr>
        
            <tr>
                <td>F601P2B</td>
                <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section B: Subcontracted Clients</td>
            </tr>
        
            <tr>
                <td>F615P1</td>
                <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
            </tr>
        
            <tr>
                <td>F615P2</td>
                <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
            </tr>
        
            <tr>
                <td>F625P2</td>
                <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
            </tr>
        
            <tr>
                <td>F625P3A</td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F625P3B</td>
                <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
            </tr>
        
            <tr>
                <td>F625P4B</td>
                <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td>S635</td>
                <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
            </tr>
        
            <tr>
                <td>F635P3B</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
            </tr>
        
            <tr>
                <td>F635P3C</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F635P4B</td>
                <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td>F645P2A</td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
            </tr>
        
            <tr>
                <td>F645P3B</td>
                <td>Form 645 (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made</td>
            </tr>
        
            <tr>
                <td>S497</td>
                <td>Form 497: Late Contribution Report</td>
            </tr>
        
            <tr>
                <td>S635C</td>
                <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
            </tr>
        
            <tr>
                <td>A</td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td>A4</td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td>A6</td>
                <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td>B</td>
                <td>Schedule B of any form (e.g., Forms 401 or 460)</td>
            </tr>
        
            <tr>
                <td>B1</td>
                <td>Schedule B, Part 1 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td>B2</td>
                <td>Schedule B, Part 2 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td>B3</td>
                <td>Schedule B, Part 3 of Forms 401 or 460</td>
            </tr>
        
            <tr>
                <td>C</td>
                <td>Schedule C of any form (e.g., Forms 401 or F460)</td>
            </tr>
        
            <tr>
                <td>COMMENTS</td>
                <td>Possibly comments by FPPC for any form?</td>
            </tr>
        
            <tr>
                <td>CVR</td>
                <td>Cover page for any form (e.g., Forms 460, 461 or 497)</td>
            </tr>
        
            <tr>
                <td>D</td>
                <td>Schedule D of any form (e.g., Forms 401, 460 or 461)</td>
            </tr>
        
            <tr>
                <td>DEBTF</td>
                <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
            </tr>
        
            <tr>
                <td>E</td>
                <td>Schedule E of any form (e.g., Forms 460, 461 or 465)</td>
            </tr>
        
            <tr>
                <td>EXPNT</td>
                <td>Expenditures outlined on any form (e.g. Form 460)</td>
            </tr>
        
            <tr>
                <td>F</td>
                <td>Schedule F of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>G</td>
                <td>Schedule G of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>H</td>
                <td>Schedule H of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>H1</td>
                <td>Schedule H, Part 1 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>H2</td>
                <td>Schedule H2, Part 2 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>H3</td>
                <td>Schedule H3, Part 3 of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>I</td>
                <td>Schedule I of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>PT5</td>
                <td>Part 5 of any form (e.g., Form 461</td>
            </tr>
        
            <tr>
                <td>RCPTB1</td>
                <td>Schedule B, Part 1 of any form (e.g., Form 460</td>
            </tr>
        
            <tr>
                <td>RCPTC</td>
                <td>Schedule C of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>RCPTI</td>
                <td>Schedule I of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>SCH A</td>
                <td>Schedule A of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>SF</td>
                <td>Schedule F of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>SPLT</td>
                <td>A memo that applies to multiple items?</td>
            </tr>
        
            <tr>
                <td>SMRY</td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>SUM</td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
            <tr>
                <td>SUMMARY</td>
                <td>Summary section of any form (e.g., Form 460)</td>
            </tr>
        
        </tbody>
        
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources: MapCalFormat2Fields (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/90.html">90</a>), Cal-Format-201 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html">16</a>), Cal-Format-1-05-02 (<a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html">13</a>)
           </small>
        </td>
        </tr>
        </tfoot>
        
        </table>
    </div>



Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p14-thumbnail.gif'></a><p>p. 14</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/133.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p133-thumbnail.gif'></a><p>p. 133</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/134.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p134-thumbnail.gif'></a><p>p. 134</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/89.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p89-thumbnail.gif'></a><p>p. 89</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p15-thumbnail.gif'></a><p>p. 15</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p16-thumbnail.gif'></a><p>p. 16</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p13-thumbnail.gif'></a><p>p. 13</p></div></div>






