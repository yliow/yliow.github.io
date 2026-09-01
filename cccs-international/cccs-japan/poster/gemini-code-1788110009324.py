"""
change "/tmp/..." to "tmp/..." 
"""

import zipfile
import xml.etree.ElementTree as ET
import os

# Create an ODT file (which is a zip archive containing XML files)
# Structure of ODT:
# mimetype
# META-INF/manifest.xml
# content.xml
# styles.xml

# Let's create the directories
os.makedirs('tmp/odt_build/META-INF', exist_ok=True)

# 1. mimetype
with open('tmp/odt_build/mimetype', 'w', encoding='utf-8') as f:
    f.write('application/vnd.oasis.opendocument.text')

# 2. META-INF/manifest.xml
manifest_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2">
 <manifest:file-entry manifest:full-path="/" manifest:version="1.2" manifest:media-type="application/vnd.oasis.opendocument.text"/>
 <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
</manifest:manifest>'''

with open('tmp/odt_build/META-INF/manifest.xml', 'w', encoding='utf-8') as f:
    f.write(manifest_xml)

# 3. styles.xml
styles_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
 xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
 xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
 xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
 xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
 xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 office:version="1.2">
 <office:font-face-decls>
  <style:font-face style:name="Arial" svg:font-family="Arial" style:font-family-generic="swiss"/>
  <style:font-face style:name="Meiryo" svg:font-family="Meiryo" style:font-family-generic="system"/>
 </office:font-face-decls>
 <office:styles>
  <style:default-style style:family="paragraph">
   <style:paragraph-properties fo:hyphenate="false"/>
   <style:text-properties style:font-name="Arial" fo:font-size="10.5pt" style:font-name-asian="Meiryo" style:font-size-asian="10.5pt"/>
  </style:default-style>
 </office:styles>
</office:document-styles>'''

with open('tmp/odt_build/styles.xml', 'w', encoding='utf-8') as f:
    f.write(styles_xml)

# 4. content.xml
content_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
 xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
 xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
 xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
 xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
 xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
 office:version="1.2">
 <office:font-face-decls>
  <style:font-face style:name="Arial" svg:font-family="Arial" style:font-family-generic="swiss"/>
  <style:font-face style:name="Hiragino Kaku Gothic ProN" svg:font-family="Hiragino Kaku Gothic ProN"/>
  <style:font-face style:name="Meiryo" svg:font-family="Meiryo"/>
 </office:font-face-decls>
 <office:automatic-styles>
  <style:style style:name="Poster_Title" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:text-align="center" fo:margin-top="0cm" fo:margin-bottom="0.2cm" fo:background-color="#5c0612" fo:padding="0.4cm"/>
   <style:text-properties fo:color="#ffffff" fo:font-size="20pt" fo:font-weight="bold" style:font-size-asian="20pt" style:font-weight-asian="bold"/>
  </style:style>
  <style:style style:name="Poster_Subtitle" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:text-align="center" fo:margin-top="0cm" fo:margin-bottom="0.4cm"/>
   <style:text-properties fo:color="#5c0612" fo:font-size="14pt" fo:font-weight="bold" style:font-size-asian="14pt" style:font-weight-asian="bold"/>
  </style:style>
  <style:style style:name="Section_Header" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:text-align="left" fo:margin-top="0.4cm" fo:margin-bottom="0.2cm" fo:background-color="#002d62" fo:padding="0.2cm"/>
   <style:text-properties fo:color="#ffffff" fo:font-size="13pt" fo:font-weight="bold" style:font-size-asian="13pt" style:font-weight-asian="bold"/>
  </style:style>
  <style:style style:name="Bullet_Text" style:family="paragraph" style:parent-style-name="Standard">
   <style:paragraph-properties fo:margin-left="0.5cm" fo:margin-top="0.1cm" fo:margin-bottom="0.1cm"/>
   <style:text-properties fo:font-size="11pt" style:font-size-asian="11pt"/>
  </style:style>
  <style:style style:name="Box_Style" style:family="table">
   <style:table-properties table:align="center" style:width="100%"/>
  </style:style>
  <style:style style:name="Box_Cell" style:family="table-cell">
   <style:table-cell-properties fo:background-color="#fdf6e3" fo:padding="0.25cm" fo:border="0.03cm solid #d3d3d3"/>
  </style:style>
  <style:style style:name="Bold_Text" style:family="text">
   <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold"/>
  </style:style>
  <style:style style:name="Highlight_Text" style:family="text">
   <style:text-properties fo:color="#5c0612" fo:font-weight="bold" style:font-weight-asian="bold"/>
  </style:style>
 </office:automatic-styles>
 <office:body>
  <office:text>
   
   <!-- Title Header -->
   <text:p text:style-name="Poster_Title">STUDY COMPUTER SCIENCE IN THE USA<text:line-break/>アメリカでCSを学ぼう！</text:p>
   <text:p text:style-name="Poster_Subtitle">CCCS-Japan (Columbia College CS)-Japan Scholarship Program<text:line-break/>日本人限定奨学金プログラム</text:p>

   <!-- Section 1 -->
   <text:p text:style-name="Section_Header">🏛️ Columbia College in Columbia, Missouri, USA / 米国ミズーリ州コロンビア・カレッジ</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Rigorous, elite, and small classes</text:span> / 少人数制の徹底したエリート教育</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">For high-achieving analytical minds</text:span> / 高い分析力を持つ優秀な学生向け</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">No prior programming experience required</text:span> / プログラミング未経験者歓迎・事前知識不問</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Proven elite career outcomes for international graduates</text:span> / 圧倒的な就職・キャリア実績</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Top-tier campus safety</text:span> / 全米トップクラスの治安・安全性</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">On-campus CS positions</text:span> / 学内CS有給ワークの機会あり</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">3-Year US STEM-designated B.Sc. degree OPT Work Authorization</text:span> / 3年間の卒業後就労許可（OPT）対象</text:p>

   <!-- Section 2 -->
   <text:p text:style-name="Section_Header">✨ Elite Career Outcomes / 圧倒的な就職実績</text:p>
   <text:p text:style-name="Bullet_Text" text:align="center"><text:span text:style-name="Bold_Text">Google | Meta | Amazon | Microsoft | IBM | Dell | Netflix | JPMorgan Chase</text:span></text:p>

   <!-- Section 3 -->
   <text:p text:style-name="Section_Header">💰 Scholarships / 奨学金</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Target:</text:span> GCE A-Levels/CIE/IAL/IB track / 対象：GCE A-Level/CIE/IAL/IB 取得・見込み者</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">GCE/IB Cutoffs &amp; Program Details:</text:span> Visit our website / GCE/IB採用基準スコア＆プログラム詳細：公式ウェブサイトをご覧ください。</text:p>
   
   <table:table table:name="ScholarshipTable" table:style-name="Box_Style">
    <table:table-column/>
    <table:table-column/>
    <table:table-row>
     <table:table-cell table:style-name="Box_Cell">
      <text:p text:style-name="Standard" text:align="center"><text:span text:style-name="Highlight_Text">Tier 1: $21K/yr | $84K Total</text:span><text:line-break/>ティア1：年$21K（4年総額:$84K）</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="Box_Cell">
      <text:p text:style-name="Standard" text:align="center"><text:span text:style-name="Highlight_Text">Tier 2: $19K/yr | $76K Total</text:span><text:line-break/>ティア2：年$19K（4年総額:$76K）</text:p>
     </table:table-cell>
    </table:table-row>
    <table:table-row>
     <table:table-cell table:style-name="Box_Cell">
      <text:p text:style-name="Standard"><text:span text:style-name="Bold_Text">Alan Turing Scholarship:</text:span> Extra +$3K/yr. Paid CS position starts 2nd year.<text:line-break/>アラン・チューリング奨学金：年+$3K追加・2年次より学内CS有給就労確約</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="Box_Cell">
      <text:p text:style-name="Standard"><text:span text:style-name="Bold_Text">Ada Lovelace Scholarship:</text:span> Extra +$3K/yr. Female STEM scholars.<text:line-break/>エイダ・ラブレス奨学金：年+$3K追加（女性STEM特待生向け）</text:p>
     </table:table-cell>
    </table:table-row>
   </table:table>

   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">High School Cohort Bonus:</text:span> Extra +$500 to +$2K/yr / 高校同時入学ボーナス：年+$500〜$2K追加（同校から同時期に入学する場合）</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Extra Merit Scholarship &amp; Need-Based Aid available</text:span> / 追加の成績優秀者枠・給付型支援あり</text:p>
   <text:p text:style-name="Bullet_Text">• <text:span text:style-name="Bold_Text">Tuition:</text:span> ~$29K/yr, <text:span text:style-name="Bold_Text">Room &amp; Board:</text:span> ~$12K/yr. / 学費：約$29K/年 | 寮・食費：約$12K/年</text:p>

   <!-- Section 4 -->
   <text:p text:style-name="Section_Header">📌 Contact &amp; Information / お問い合わせ・公式WEB</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">CCCS-Japan Website / 公式WEB:</text:span> https://bit.ly/cccs-japan</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">Name / 氏名:</text:span> Dr. Yihsiang Liow (Associate Professor of CS) / リョウ・イーシャン コンピュータサイエンス学科准教授</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">Email / メール:</text:span> yliow@ccis.edu</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">Profile / 教授紹介:</text:span> https://www.ccis.edu/faculty/profiles/yihsiang-liow</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">Full Sheet URL:</text:span> https://yliow.github.io/cccs-international/cccs-japan/docs/cccs-japan-summary-sheet.pdf</text:p>
   <text:p text:style-name="Bullet_Text"><text:span text:style-name="Bold_Text">The scholarship website is:</text:span> https://bit.ly/cccs-japan</text:p>

  </office:text>
 </office:body>
</office:document-content>'''

with open('tmp/odt_build/content.xml', 'w', encoding='utf-8') as f:
    f.write(content_xml)

# Create the zip archive named output.odt
output_odt_path = 'tmp/cccs_japan_scholarship_poster.odt'
with zipfile.ZipFile(output_odt_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # mimetype must be the first file and uncompressed according to ODF spec
    zip_file.write('tmp/odt_build/mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
    zip_file.write('tmp/odt_build/META-INF/manifest.xml', 'META-INF/manifest.xml')
    zip_file.write('tmp/odt_build/styles.xml', 'styles.xml')
    zip_file.write('tmp/odt_build/content.xml', 'content.xml')

print(f"Generated ODT file successfully at: {output_odt_path}")
