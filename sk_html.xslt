<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:regexp="http://exslt.org/regular-expressions">

<xsl:template match="/">
  <html xmlns="http://www.w3.org/1999/xhtml" lang="sa" xml:lang="sa">
    <head>
      <meta charset="UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <style>
	.center {
	text-align: center;
	}
	label {
	display: inline-block;
	width: 5em;
	}
      </style>
    </head>
    <body>
      <h1 class="center">सिद्धान्तकौमुदी</h1>
      <xsl:apply-templates/>
      
      <h2 class="index">धतुसूचि: (संगणितः)</h2>
      <xsl:for-each select="//DAtukramaH">
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
	<a href="#D{.}" title="#D{.}"><xsl:value-of select="."/></a>
	</div>
      </xsl:for-each>
      <h2 class="index" lang="en">Document Information</h2>
      <h3>Revision History</h3>
      <table border="1">
      <tr>
        <th>Version</th>
        <th>Date</th>
	<th>Person</th>
	<th>Email</th>
	<th>Changelog</th>
      </tr>
      <xsl:for-each select="//header/revHistory">
        <tr>
          <td><xsl:value-of select="version"/></td>
          <td><xsl:value-of select="date"/></td>
          <td><xsl:value-of select="person"/></td>
          <td><xsl:value-of select="email"/></td>
          <td><xsl:value-of select="changelog"/></td>
        </tr>
      </xsl:for-each>
      </table>
      <h3>Original Source</h3>
         <xsl:value-of select="//header/sourceDesc"/>
    </body>
  </html>
</xsl:template>

<xsl:template match="header"/>


<xsl:template match="prakaraRa">
  <h2 class="center chapter">अथ <xsl:value-of select="./@prakaraRanAman"/></h2>
  <xsl:apply-templates select="sUtra"/>
  <xsl:apply-templates select="prakaraRAnta"/>
</xsl:template>


<xsl:template match="prakaraRAnta">
  <div class="center"><em>इति <xsl:value-of select="."/></em></div>
</xsl:template>

<xsl:template match="sUtra">
  <div>
    <xsl:apply-templates/>
  </div>
</xsl:template>

<xsl:template match="sUtramUlam">
  <b><xsl:value-of select="."/></b>
</xsl:template>

<xsl:template match="SK">
   <span id="SK{.}"><b><xsl:value-of select="."/>:</b></span>
</xsl:template>
<xsl:template match="AS">
   (<a title="AVG {.}" href="http://avg-sanskrit.org/sutras/{.}.html" target="_blank"><xsl:value-of select="."/></a>)
</xsl:template>
<xsl:template match="vivaraRam">
  <div><xsl:apply-templates/></div>
</xsl:template>
<xsl:template match="vArtika">
   <em><xsl:value-of select="."/></em>
</xsl:template>
<xsl:template match="DAtukramaH">
   <span id="D{.}"><b><xsl:value-of select="."/></b></span>
</xsl:template>
<xsl:template match="SKsandarBaH">
   <a href="#SK{.}" title="{//sUtra[SK=current()]/sUtramUlam}"><sup><xsl:value-of select="."/></sup></a>
</xsl:template>



</xsl:stylesheet>

