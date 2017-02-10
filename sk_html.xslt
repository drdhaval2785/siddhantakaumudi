<xsl:stylesheet version="1.0"
		xmlns:t="http://www.tei-c.org/ns/1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:regexp="http://exslt.org/regular-expressions">

<xsl:template match="//t:TEI">
  <html>
    <head>
      <style>
	.center {
	text-align: center;
	}
      </style>
    </head>
    <body>
      <h1 class="center">सिद्धान्तकौमुदी</h1>
      <xsl:apply-templates/>
      
      <h2 class="index">धतुसूचि: (संगणितः)</h2>
      <xsl:for-each select="//t:div[@type='dhātukramaḥ']">
        <xsl:sort select="./following-sibling::text()[1]"/>
	<div class="indexelem">
	<xsl:choose>
	  <xsl:when test="contains(./following-sibling::text()[1], '।')">
	    <xsl:value-of select="substring-before(./following-sibling::text()[1],'।')"/>
	  </xsl:when>
	  <xsl:when test="contains(./following-sibling::text()[1], '॥')">
	    <xsl:value-of select="substring-before(./following-sibling::text()[1],'॥')"/>
	  </xsl:when>
	  <xsl:otherwise>
	    <xsl:value-of select="./following-sibling::text()[1]"/>
	  </xsl:otherwise>
	</xsl:choose>
	<a href="#D{.}"><xsl:value-of select="."/></a>
	</div>
      </xsl:for-each>
      <h2 class="index">Document Information</h2>
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
  <b><xsl:apply-templates/></b>
   (<a href="http://avg-sanskrit.org/sutras/{.}.html" title="AVG {./t:label[@type='AS']}" target="_blank"><xsl:value-of select="./t:label[@type='AS']"/></a>)
</xsl:template>

<xsl:template match="t:label[@type='SK']">
   <span id="SK{.}"><b><xsl:value-of select="."/>:</b></span>
</xsl:template>
<xsl:template match="t:label[@type='AS']">
</xsl:template>
<xsl:template match="t:p">
  <p><xsl:apply-templates/></p>
</xsl:template>
<xsl:template match="t:div[@type='vārtika']">
   <em><xsl:value-of select="."/></em>
</xsl:template>
<xsl:template match="t:div[@type='dhātukramaḥ']">
   <span id="D{.}"><b><xsl:value-of select="."/></b></span>
</xsl:template>
<xsl:template match="t:div[@type='SKsandarbhaḥ']">
   <a href="#SK{.}" title="{//t:ab[t:label=current()]/text()}" ><sup><xsl:value-of select="."/></sup></a>
</xsl:template>
</xsl:stylesheet>

