<xsl:stylesheet version="1.0"
		xmlns:t="http://www.tei-c.org/ns/1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:regexp="http://exslt.org/regular-expressions">

  <!--MIT License

	Copyright (c) 2017 Karthikeyan Madathil

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE. 
  -->
  
  <!-- Using the Muenchian method to group vArtikas and paribhaShAs (q.v)-->
  <xsl:key name="vartika" match="t:div[@type='vārtika']" use="normalize-space(.)" />
  <xsl:key name="paribhasha" match="t:div[@type='paribhāṣā']" use="normalize-space(.)" />

  <!-- start for the TEI tag -->
  <xsl:template match="//t:TEI">
    <html>
      <head>
	<meta charset="utf-8" /> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<!-- Embedded CSS to control display of various classes of text -->
	<style>
	  body {
	  font-family: Siddhanta;
	  }
	  .center {
	  text-align: center;
	  }
	  .vartika {
	  font-style: italic;
	  }
	  .paribhasha {
	  text-decoration: underline;
	  }
	  .dhatu {
	  font-weight: bold;
	  }
	  .sutra {
	  font-weight: bold;
	  }
	  .trailer {
	  font-style: italic;
	  }
	  table, th, td {
	  border: 1px solid black;
	  }
	</style>
      </head>
      <body>
	<h1 class="center">सिद्धान्तकौमुदी</h1>
	<!-- Main body - this is where the action starts - see templates that follow -->
        <xsl:apply-templates/>
	<!-- Main body is done, move on to appendices -->

	<h2 class="index">प्रदर्शनदृष्टान्तसूचि:</h2>
	<!-- Table showing how various categories are displayed -->
	<table>
	  <tr> <td>सूत्रम्‌</td><td><span class="sutra" title="सूत्रम्‌"><span id="SK1">1:</span> हलन्त्यम् </span> (1-3-3)</td></tr>
	  <tr> <td>परिभाषा</td><td><span class="paribhasha">यत्रानेकविधमान्तर्यं तत्र स्थानत आन्तर्यं बलीयः</span></td></tr>
	  <tr> <td>वार्तिकम्‌</td><td><span class="vartika">यणः प्रतिषेधो वाच्यः</span></td>
	  </tr>
	  <tr> <td>धातु:</td><td><span class="dhatu"> <span id="D1" class="dhatu" title="धातुः">1 भू</span> सत्तायाम्</span></td>
	  </tr>
	</table>

	<!-- Appendixes of Sutras -->
	<h2 class="index">सूत्रसूचि: (संगणितः)</h2>
	<!-- Sutras in alphabetical order -->
	<h3 class="index">सूत्राणि वर्णक्रमेण</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
	  <!-- Workaround to handle the fact that RR and LL are encoded in the wrong place in Unicode, and hence sort has issues -->
	  <!-- first, sort up to ऋ . The inversion of logic is necessary to handle the way xsl:sort works.
	       XPATH1.0 does not support lexicographic comparisons of characters, else a simple &lt; would've worked
	  -->
          <xsl:sort select="substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='अ' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='आ' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='इ' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='ई' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='उ' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='ऊ' and
			    substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='ऋ' 
			    "/> 
 	  <!-- Second, sort  ॠ  . The inversion of logic is necessary to handle the way xsl:sort works -->
          <xsl:sort select="substring(normalize-space(./t:ab[@type='sūtra']/text()),1,1)!='ॠ'"/>
	  <!-- Everything else now. It helps that ॠ is placed beyond the consonants -->
	  <!-- We do not handle LL as there are no sutras starting with it -->
          <xsl:sort select="normalize-space(./t:ab[@type='sūtra']/text())"/>
	  <!-- we skip phiT and uNAdi as well as zero numbered sUtras -->
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='फ'
			  and substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='उ' and
			  substring(./t:ab[@type='sūtra']/t:label[@type='AS']/text(),1,1)!='0'
			  ">
	    <div class="indexelem">
	      <span>
		<!-- This gets the AS Number -->
		(<xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text())"/>)
		<xsl:text> </xsl:text>
		<!-- Sutra text -->
	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text>
	      <!-- Link to sUtra (based on SK number)" -->
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>  
	</xsl:for-each>
	<!-- Sutras sorted by AS order -->
	<h3 class="index">सूत्राणि पाठक्रमेण</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
	  <!-- AS Sutra number is given as X-Y-Z, where 0<X<9, 0<Y<5 and Z can be between 1 and 3 digits.
	       To sort this properly, strip out X and Y, pad Z with zeros to three digits,
	       then concatenate, and lexically sort -->
          <xsl:sort select="concat(
			    substring-before(normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text()),'-'),
			    substring-before(substring-after(normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text()),'-'),'-'),
			    substring(concat('00',
			    substring-after(substring-after(normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text()),'-'),'-')),
			    string-length(substring-after(substring-after(normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text()),
			    '-'),'-'))))			    
			    "/>
	  <!-- Skip phiT uNAdi, and 0 numbered sUtras -->
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='फ' and
			  substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='उ' and
			  substring(./t:ab[@type='sūtra']/t:label[@type='AS']/text(),1,1)!='0'
			  ">
	    <div class="indexelem"> <!-- Assemble index element -->
	      <span>
		<!-- AS Sutra Number in parantheses -->
		(<xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text())"/>)
		<xsl:text> </xsl:text> <!-- spacer -->
              <!-- sUtra text -->
	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text> <!-- spacer -->
	      <!-- Link to sUtra (based on SK number)" -->
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>  
	</xsl:for-each>
	
	<!-- uNAdi Sutras sorted lexicographically -->
	<!-- Similar to sUtra sort, except for looking for उ as first letter -->
	<h3 class="index">उणादिसूत्राणि</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
          <xsl:sort select="normalize-space(./t:ab[@type='sūtra']/text())"/>
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)='उ'">
	    <div class="indexelem">
	      <span>
	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text>
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>
	</xsl:for-each>
	
	<!-- phiT Sutras sorted lexicographically -->
	<!-- Similar to sUtra sort, except for looking for उ as first letter -->
	<h3 class="index">फिट्सूत्राणि</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
          <xsl:sort select="normalize-space(./t:ab[@type='sūtra']/text())"/>
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)='फ'">
	    <div class="indexelem">
	      <span>
	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text>
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>
	</xsl:for-each>
	
	<!-- vArtika apprendix -->
	<h2 class="index">वार्तिकसूचि: (संगणितः)</h2>
	<!-- Muenchian method (qv), selects each vArtika only once -->
	<xsl:for-each select="//t:div[@type='vārtika' and count(. | key('vartika', normalize-space(.))[1]) = 1]">
	  <!-- Sort lexicographically -->
          <xsl:sort select="normalize-space(.)"/>
	  <div class="indexelem">
	    <!-- Text -->
	    <span><xsl:value-of select="normalize-space(.)"/></span>
	    <!-- since each vArtika is selected onlly once, we need to find all other instances of the same,
		 which we do using the Muenchian method, then get the SK number of their contexts, and create a comma separated list
	    -->
	    <xsl:for-each select="key('vartika', normalize-space(.))">
	      <!-- Sort contexts by SK number -->
	      <xsl:sort select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()" />
	      <xsl:text> </xsl:text>
	      <!-- Link to SK context through SK number tag -->
	      <a href="#SK{ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>	
	      <!-- XSLT pattern to skip the final comma -->
	      <xsl:if test="position() != last()">
		<xsl:text>,</xsl:text>
	      </xsl:if>
	    </xsl:for-each>	    
	  </div>	 
	</xsl:for-each>

	<!-- paribhAShA apprendix -->
	<h2 class="index">परिभाषासूचि: (संगणितः)</h2>
	<!-- Muenchian method (qv), selects each paribhAShA only once -->
	<xsl:for-each select="//t:div[@type='paribhāṣā' and count(. | key('paribhasha', normalize-space(.))[1]) = 1]">
	  <!-- Sort lexicographically -->
          <xsl:sort select="normalize-space(.)"/>
	  <div class="indexelem">
	    <!-- Text -->
	    <span><xsl:value-of select="normalize-space(.)"/></span>
	    <!-- since each paribhAShA is selected onlly once, we need to find all other instances of the same,
		 which we do using the Muenchian method, then get the SK number of their contexts, and create a comma separated list
		 -->
	    <xsl:for-each select="key('paribhasha', normalize-space(.))">
	      <!-- Sort contexts by SK number -->
	      <xsl:sort select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()" />
	      <xsl:text> </xsl:text>
	      <!-- Link to SK context through SK number tag -->
	      <a href="#SK{ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	      <!-- XSLT pattern to skip the final comma -->
	      <xsl:if test="position() != last()">
		<xsl:text>,</xsl:text>
	      </xsl:if>
	    </xsl:for-each>	    
	  </div>
	</xsl:for-each>

	<!-- appendix of dhAtus -->
	<h2 class="index">धातुसूचि: (संगणितः)</h2>
	
	<!-- substring-after(./text(),' ') strips the sutra number and spaces before the Sutra name -->
	<xsl:for-each select="//t:div[@type='dhātuḥ']">
          <!-- Workaround to handle the fact that RR and LL are encoded in the wrong place in Unicode, and hence sort has issues -->
	  <!-- first, sort up to ऋ . The inversion of logic is necessary to handle the way xsl:sort works -->
          <xsl:sort select="substring(substring-after(./text(),' '),1,1)!='अ' and
			    substring(substring-after(./text(),' '),1,1)!='आ' and
			    substring(substring-after(./text(),' '),1,1)!='इ' and
			    substring(substring-after(./text(),' '),1,1)!='ई' and
			    substring(substring-after(./text(),' '),1,1)!='उ' and
			    substring(substring-after(./text(),' '),1,1)!='ऊ' and
			    substring(substring-after(./text(),' '),1,1)!='ऋ' 
			    "/> 
 	  <!-- Second, sort  ॠ  . The inversion of logic is necessary to handle the way xsl:sort works -->
          <xsl:sort select="substring(substring-after(./text(),' '),1,1)!='ॠ'"/>
	  <!-- Everything else now. It helps that ॠ is placed beyond the consonants -->
	  <!-- We do not handle LL as there are no sutras starting with it -->
	  <xsl:sort select="substring-after(./text(),' ')"/>
	  <!-- Now that we're all sorted, we can start with introducing the dhAtus one by one -->
	  <div class="indexelem">
	    <!-- first, the dhatu itself -->
	    <span class="dhatu" title="धातुः"><xsl:value-of select="substring-after(./text(),' ')"/></span><xsl:text> </xsl:text>
	    <!-- Next, each of the meanings separated by space - there can be more than one! -->
	    <xsl:for-each select="parent::t:div[@type='dhātvarthaḥ']/text()">
	      <xsl:value-of select="normalize-space(.)"/><xsl:text> </xsl:text>
	    </xsl:for-each>
	    <!-- gaNa - sUtra numbers are monotonic with gaNas. -->
	    <!-- substring-before(./text(),' ') gets the sUtra number -->
	    <!-- bounds given by Dr. Dhaval Patel
		 upperbounds = [1011,1083,1107,1248,1282,1439,1464,1474,1535,1993]
		 i.e.
		 भ्वादिः - ०-१०१०
		 अदादिः - १०११-१०८२
		 जुहोत्यादिः - १०८३-११०६
		 दिवादिः - ११०७-१२४७
		 स्वादिः - १२४८-१२८१
		 तुदादिः - १२८२-१४३८
		 रुधादिः - १४३९-१४६३
		 तनादिः - १४६४-१४७३
		 क्र्यादिः - १४७४-१५३४
		 चुरादिः - १५३५-१९९३
		 -->
	    <xsl:choose>
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1011">
		भ्वादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1083">
		अदादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1107">
		जुहोत्यादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1248">
		दिवादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1282">
		स्वादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1439">
		तुदादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1464">
		रुधादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1474">
		तनादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1535">
		क्र्यादिः
	      </xsl:when> 
	      <xsl:when test="number(substring-before(./text(),' '))&lt;1994">
		चुरादिः
	      </xsl:when> 
	    </xsl:choose>
	    <xsl:text> </xsl:text>
	    <!-- Hyperlink to dhatu reference -->
	    <!-- substring-before(./text(),' ') gets the sUtra number -->
	    <a href="#D{substring-before(./text(),' ')}">
	    <xsl:value-of select="substring-before(./text(),' ')"/></a>
	  </div>
	</xsl:for-each>
	<!-- Document Information -->
	<h2 class="index">Document Information</h2>
	<h3>Licence</h3>
	<xsl:apply-templates select="//t:teiHeader/t:fileDesc//t:availability"/>
	<h3>Original Source</h3>
	<xsl:apply-templates select="//t:teiHeader/t:fileDesc/t:notesStmt/t:note"/>
	<h3>Revision History</h3>
	<!-- We cast the revision history found under change tags into a table based on the following format -->
	<table border="1">
	  <tr>
            <th>Date</th>
	    <th>Person</th>
            <th>Version</th>
	    <th>Changelog</th>
	  </tr>
	  <xsl:for-each select="//t:teiHeader/t:revisionDesc/t:change">
            <tr>
              <td><xsl:value-of select="./@when"/></td>
              <td><xsl:value-of select="./@who"/></td>
              <td><xsl:value-of select="./t:version"/></td>
              <td><xsl:apply-templates select="."/></td>
            </tr>
	  </xsl:for-each>
	</table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="t:teiHeader">
  </xsl:template>

  <!-- Dig in deeper when you find a text tag -->
  <xsl:template match="t:text">
    <xsl:apply-templates/> 
  </xsl:template>

  <!-- Ditto -->
  <xsl:template match="t:body">
    <xsl:apply-templates/> 
  </xsl:template>

  <!-- 'prakaraṇa' tag: -->
  <xsl:template match="t:div[@type='prakaraṇa']">
    <!-- Create a Chapter header -->
    <h2 class="center chapter"><xsl:value-of select="./t:head"/></h2>
    <!-- Dig into the Sutras -->
    <xsl:apply-templates select="t:div[@type='sūtra_with_explanation']"/>
    <!-- Insert the trailer after all sUtras -->
    <div class="center trailer"><xsl:value-of select="./t:trailer"/></div>
  </xsl:template>

  <!-- sUtra with explanation: Wrap with a div and dig in further -->
  <xsl:template match="t:div[@type='sūtra_with_explanation']">
    <div>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <!-- sUtra tags-->
  <xsl:template match="t:ab[@type='sūtra']">
    <!--Apply the sutra class and dig in. Note that we'll suppress the AS number while digging in -->
    <span class="sutra" title="सूत्रम्‌"><xsl:apply-templates/></span>
    <!-- AS number was earlier suppressed, add it at the end -->
    <xsl:choose>
      <!-- Suppress links for non AshTAdhyAyI sutras - paribhAShA, uNAdi, phiT -->
      <xsl:when test="substring-before(t:label[@type='AS'],'-')=0 or substring-before(t:label[@type='AS'],'-')>8">
	(<xsl:value-of select="./t:label[@type='AS']"/>)
      </xsl:when>
      <!-- For AshTAdhyAyI sutras,  add link to avg-sanskrit.org. target=_blank results in the link opening in a new tab -->
      <xsl:otherwise>
        (<a href="http://avg-sanskrit.org/sutras/{t:label[@type='AS']}.html" title="AVG {./t:label[@type='AS']}" target="_blank"><xsl:value-of select="./t:label[@type='AS']"/></a>)
      </xsl:otherwise>
    </xsl:choose>   
  </xsl:template>

  <!-- SK number under sutra. Insert a tag which can be linked to. Useful for internal references and appendices -->
  <xsl:template match="t:label[@type='SK']">
    <span id="SK{.}"><xsl:value-of select="."/>:</span>
  </xsl:template>

  <!-- Suppress AS number as described above-->
  <xsl:template match="t:label[@type='AS']">
  </xsl:template>

  <!-- Convert TEI p tag into HTML p tag -->
  <xsl:template match="t:p">
    <p><xsl:apply-templates/></p>
  </xsl:template>

  <!-- Insert classes for vartika paribhasha to control their display -->
  <xsl:template match="t:div[@type='vārtika']">
    <span class="vartika" title="वार्तिकम्‌"><xsl:value-of select="."/></span>
  </xsl:template>
  <xsl:template match="t:div[@type='paribhāṣā']">
    <span class="paribhasha" title="परिभाषा"><xsl:value-of select="."/></span>
  </xsl:template>
  
  <!-- dhAtu + meaning - insert class and dig deeper -->
  <xsl:template match="t:div[@type='dhātvarthaḥ']">
    <span class="dhatu" >
      <xsl:apply-templates/>
    </span>
  </xsl:template>

  <!-- dhAtu tag. Insert linkable tag -->
  <xsl:template match="t:div[@type='dhātuḥ']">
    <span id="D{substring-before(./text(),' ')}" class="dhatu" title="धातुः"><xsl:value-of select="."/></span>
  </xsl:template>

  <!-- Internal reference. Link to SK context and style as sup (deliberately not done in css) -->
  <xsl:template match="t:div[@type='SKsandarbhaḥ']">
    <a href="#SK{.}" title="{//t:ab[t:label=current()]/text()}" ><sup><xsl:value-of select="."/></sup></a>
  </xsl:template>

  <!-- Convert TEI ref tags to HTML a tags -->
  <xsl:template match="t:ref">
    <a href="{./@target}"><xsl:value-of select="."/></a>
  </xsl:template>

  <!-- Convert TEI list tags into HTML ul/ol tags as appropriate -->
  <xsl:template match="t:list">
    <xsl:choose>
      <xsl:when test="@rend='numbered'">
	<ol>
	  <xsl:apply-templates/>
	</ol>
      </xsl:when>
      <xsl:otherwise>
	<ul>
	  <xsl:apply-templates/>
	</ul>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- TEI item tag. Since the covering list tag decides the list type, this can
       be directly transformed into HTML li -->
  <xsl:template match="t:item">
    <li>
      <xsl:apply-templates/>
    </li>
  </xsl:template>
  
  <!-- suppress output for version tag, as it's taken care of separately -->
  <xsl:template match="t:version">
  </xsl:template>


</xsl:stylesheet>

