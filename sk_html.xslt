<xsl:transform version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <head>
      <style>
	.center {
	text-align: center;
	}
      </style>
    </head>
    <body>
      <h1 class="center">सिद्धान्तकौमुदिः</h1>
      <xsl:apply-templates/>
    </body>
  </html>
</xsl:template>

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
   (<a href="http://avg-sanskrit.org/sutras/{.}.html"><xsl:value-of select="."/></a>)
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
   <a href="#SK{.}"><sup><xsl:value-of select="."/></sup></a>
</xsl:template>



</xsl:transform>

