<xsl:stylesheet version="1.0"
		xmlns:t="http://www.tei-c.org/ns/1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:regexp="http://exslt.org/regular-expressions">

  <!-- Using the Muenchian method to group vArtikas and paribhaShAs (q.v)-->
  <xsl:key name="vartika" match="t:div[@type='vārtika']" use="normalize-space(.)" />
  <xsl:key name="paribhasha" match="t:div[@type='paribhāṣā']" use="normalize-space(.)" />
  
  <xsl:template match="//t:TEI">
    <html>
      <head>
	<meta charset="utf-8" /> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
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
	  table, th, td {
	  border: 1px solid black;
	  }
	</style>
      </head>
      <body>
	<h1 class="center">सिद्धान्तकौमुदी</h1>
	<xsl:apply-templates/>
	<h2 class="index">प्रदर्शनदृष्टान्तसूचि:</h2>
	<table>
	  <tr> <td>सूत्रम्‌</td><td><span class="sutra" title="सूत्रम्‌"><span id="SK1">1:</span> हलन्त्यम् </span> (1-3-3)</td></tr>
	  <tr> <td>परिभाषा</td><td><span class="paribhasha">यत्रानेकविधमान्तर्यं तत्र स्थानत आन्तर्यं बलीयः</span></td></tr>
	  <tr> <td>वार्तिकम्‌</td><td><span class="vartika">यणः प्रतिषेधो वाच्यः</span></td>
	  </tr>
	  <tr> <td>धातु:</td><td><span class="dhatu"> <span id="D1" class="dhatu" title="धातुः">1 भू</span> सत्तायाम्</span></td>
	  </tr>
	</table>
	<h2 class="index">सूत्रसूचि: (संगणितः)</h2>
	<h3 class="index">सूत्राणि वर्णक्रमेण</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
          <xsl:sort select="normalize-space(./t:ab[@type='sūtra']/text())"/>
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='फ' and substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='उ'">
	    <div class="indexelem">
	      <span>
		(<xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text())"/>)
		<xsl:text> </xsl:text>
	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text>
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>  
	</xsl:for-each>
	<h3 class="index">सूत्राणि पाठक्रमेण</h3>
	<xsl:for-each select="//t:div[@type='sūtra_with_explanation']">
          <xsl:sort select="number(translate(normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text()),'-',''))"/>
          <xsl:if   test="substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='फ' and substring(./t:ab[@type='sūtra']/t:label[@type='SK']/text(),1,1)!='उ'">
	    <div class="indexelem">
	      <span>
		(<xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/t:label[@type='AS']/text())"/>)
		<xsl:text> </xsl:text>

	      <xsl:value-of select="normalize-space(./t:ab[@type='sūtra']/text())"/></span>
	      <xsl:text> </xsl:text>
	      <a href="#SK{./t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="./t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	      </a>
	    </div>
	  </xsl:if>  
	</xsl:for-each>
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
	<h2 class="index">वार्तिकसूचि: (संगणितः)</h2>
	<xsl:for-each select="//t:div[@type='vārtika' and count(. | key('vartika', normalize-space(.))[1]) = 1]">
          <xsl:sort select="normalize-space(.)"/>
	  <div class="indexelem">
	    <span><xsl:value-of select="normalize-space(.)"/></span>
	    <xsl:for-each select="key('vartika', normalize-space(.))">
	      <xsl:sort select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()" />
		<xsl:text> </xsl:text>
	    <a href="#SK{ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
	      <xsl:value-of select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	    </a>	
	    <xsl:if test="position() != last()">
	      <xsl:text>,</xsl:text>
	    </xsl:if>
	    </xsl:for-each>	    
	  </div>	 
	</xsl:for-each>

	<h2 class="index">परिभाषासूचि: (संगणितः)</h2>
	<xsl:for-each select="//t:div[@type='paribhāṣā' and count(. | key('paribhasha', normalize-space(.))[1]) = 1]">
          <xsl:sort select="normalize-space(.)"/>
	  <div class="indexelem">
	    <span><xsl:value-of select="normalize-space(.)"/></span>
	    <xsl:for-each select="key('paribhasha', normalize-space(.))">
	      <xsl:sort select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()" />
	      <xsl:text> </xsl:text>
	      <a href="#SK{ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()}">
		<xsl:value-of select="ancestor::t:div[@type='sūtra_with_explanation']/t:ab[@type='sūtra']/t:label[@type='SK']/text()"/>
	    </a>
	    <xsl:if test="position() != last()">
	      <xsl:text>,</xsl:text>
	    </xsl:if>
	    </xsl:for-each>	    
	  </div>
	</xsl:for-each>
	
	<h2 class="index">धातुसूचि: (संगणितः)</h2>
	<xsl:for-each select="//t:div[@type='dhātuḥ']">
          <xsl:sort select="substring-after(./text(),' ')"/>
	  <div class="indexelem">
	    <span class="dhatu" title="धातुः"><xsl:value-of select="substring-after(./text(),' ')"/></span><xsl:text> </xsl:text>
	    <xsl:for-each select="parent::t:div[@type='dhātvarthaḥ']/text()">
	      <xsl:value-of select="normalize-space(.)"/><xsl:text> </xsl:text>
	    </xsl:for-each>
	    <!-- gaNa -->
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
	    <a href="#D{substring-before(./text(),' ')}">
	    <xsl:value-of select="substring-before(./text(),' ')"/></a>
	  </div>
	</xsl:for-each>
	<h2 class="index">Document Information</h2>
	<h3>Licence</h3>
	<xsl:apply-templates select="//t:teiHeader/t:fileDesc//t:availability"/>
	<h3>Original Source</h3>
	<xsl:apply-templates select="//t:teiHeader/t:fileDesc/t:notesStmt/t:note"/>
	<h3>Revision History</h3>
	<table border="1">
	  <tr>
            <th>Date</th>
	    <th>Person</th>
	    <th>Changelog</th>
	  </tr>
	  <xsl:for-each select="//t:teiHeader/t:revisionDesc/t:change">
            <tr>
              <td><xsl:value-of select="./@when"/></td>
              <td><xsl:value-of select="./@who"/></td>
              <td><xsl:value-of select="."/></td>
            </tr>
	  </xsl:for-each>
	</table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="t:teiHeader">
  </xsl:template>

  <xsl:template match="t:text">
    <xsl:apply-templates/> 
  </xsl:template>

  <xsl:template match="t:body">
    <xsl:apply-templates/> 
  </xsl:template>

  <xsl:template match="t:div[@type='prakaraṇa']">
    <h2 class="center chapter"><xsl:value-of select="./t:head"/></h2>
    <xsl:apply-templates select="t:div[@type='sūtra_with_explanation']"/>
    <div class="center"><em><xsl:value-of select="./t:trailer"/></em></div>
  </xsl:template>

  <xsl:template match="t:div[@type='sūtra_with_explanation']">
    <div>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

  <xsl:template match="t:ab[@type='sūtra']">
    <span class="sutra" title="सूत्रम्‌"><xsl:apply-templates/></span>
    <xsl:choose>
      <xsl:when test="substring-before(t:label[@type='AS'],'-')=0 orsubstring-before(t:label[@type='AS'],'-')>8">
	(<xsl:value-of select="./t:label[@type='AS']"/>)
      </xsl:when>
      <xsl:otherwise>
        (<a href="http://avg-sanskrit.org/sutras/{t:label[@type='AS']}.html" title="AVG {./t:label[@type='AS']}" target="_blank"><xsl:value-of select="./t:label[@type='AS']"/></a>)
      </xsl:otherwise>
    </xsl:choose>   
  </xsl:template>

  <xsl:template match="t:label[@type='SK']">
    <span id="SK{.}"><xsl:value-of select="."/>:</span>
  </xsl:template>
  <xsl:template match="t:label[@type='AS']">
  </xsl:template>
  <xsl:template match="t:p">
    <p><xsl:apply-templates/></p>
  </xsl:template>
  <xsl:template match="t:div[@type='vārtika']">
    <span class="vartika" title="वार्तिकम्‌"><xsl:value-of select="."/></span>
  </xsl:template>
  <xsl:template match="t:div[@type='paribhāṣā']">
    <span class="paribhasha" title="परिभाषा"><xsl:value-of select="."/></span>
  </xsl:template>
  <xsl:template match="t:div[@type='dhātvarthaḥ']">
    <span class="dhatu" >
      <xsl:apply-templates/>
    </span>
  </xsl:template>
  <xsl:template match="t:div[@type='dhātuḥ']">
    <span id="D{substring-before(./text(),' ')}" class="dhatu" title="धातुः"><xsl:value-of select="."/></span>
  </xsl:template>
  <xsl:template match="t:div[@type='SKsandarbhaḥ']">
    <a href="#SK{.}" title="{//t:ab[t:label=current()]/text()}" ><sup><xsl:value-of select="."/></sup></a>
  </xsl:template>

  <xsl:template match="t:ref">
    <a href="{./@target}"><xsl:value-of select="."/></a>
  </xsl:template>

  <xsl:template match="t:list">
    <ul>
      <xsl:apply-templates/>
    </ul>
  </xsl:template>
  <xsl:template match="t:item">
    <li>
      <xsl:apply-templates/>
    </li>
  </xsl:template>


</xsl:stylesheet>

