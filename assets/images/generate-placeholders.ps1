# Load System.Drawing assembly
[System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") | Out-Null

$base = "c:\xampp\htdocs\abynsstudio\fotografer-videografer\assets\images"
$dirs = @("hero","portfolio","gallery","about","services","articles","activities","testimonials","clients","og")
foreach ($d in $dirs) {
  $path = Join-Path $base $d
  if (-not (Test-Path $path)) { New-Item -ItemType Directory -Path $path -Force | Out-Null }
}

function MakeRealJpeg {
  param(
    [string]$filePath,
    [int]$w,
    [int]$h,
    [string]$label,
    [string]$bgColorHex
  )
  
  $bmp = New-Object System.Drawing.Bitmap($w, $h)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  
  # Set background color
  $bg = [System.Drawing.ColorTranslator]::FromHtml($bgColorHex)
  $brush = New-Object System.Drawing.SolidBrush($bg)
  $g.FillRectangle($brush, 0, 0, $w, $h)
  
  # Draw gold border
  $penColor = [System.Drawing.ColorTranslator]::FromHtml("#C7A66A")
  $pen = New-Object System.Drawing.Pen($penColor, 4)
  $g.DrawRectangle($pen, 2, 2, ($w - 4), ($h - 4))
  
  # Draw text "ABYNSS STUDIO"
  $font = New-Object System.Drawing.Font("Georgia", 24, [System.Drawing.FontStyle]::Bold)
  $textBrush = New-Object System.Drawing.SolidBrush($penColor)
  
  # Center text
  $sf = New-Object System.Drawing.StringFormat
  $sf.Alignment = [System.Drawing.StringAlignment]::Center
  $sf.LineAlignment = [System.Drawing.StringAlignment]::Center
  
  $rect = New-Object System.Drawing.RectangleF(0, 0, $w, $h)
  $g.DrawString($label, $font, $textBrush, $rect, $sf)
  
  # Save as JPEG
  $bmp.Save($filePath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
  
  # Dispose resources
  $brush.Dispose()
  $textBrush.Dispose()
  $pen.Dispose()
  $font.Dispose()
  $g.Dispose()
  $bmp.Dispose()
}

# Hero
MakeRealJpeg -filePath "$base\hero\hero-poster.jpg" -w 1920 -h 1080 -label "ABYNSS STUDIO - Hero Poster" -bgColorHex "#0D0D0D"

# Portfolio
$pNames = @('wedding-01','wedding-01-2','wedding-01-3','wedding-01-4','wedding-01-5','wedding-01-6','commercial-01','commercial-01-2','commercial-01-3','wedding-film-01','wedding-film-01-2','wedding-film-01-3','fashion-01','fashion-01-2','fashion-01-3','food-01','food-01-2','food-01-3','corporate-01','corporate-01-2','corporate-01-3','graduation-01','graduation-01-2','prewedding-01','prewedding-01-2','prewedding-01-3')
foreach ($n in $pNames) { 
  MakeRealJpeg -filePath "$base\portfolio\$n.jpg" -w 1200 -h 800 -label "ABYNSS STUDIO - $n" -bgColorHex "#111111" 
}

# Gallery
for ($i = 1; $i -le 12; $i++) {
  $num = $i.ToString('D2')
  MakeRealJpeg -filePath "$base\gallery\gallery-$num.jpg" -w 800 -h 800 -label "ABYNSS - Gallery $num" -bgColorHex "#111111"
}

# Services
$sNames = @('photography','videography','wedding','corporate','drone','editing')
foreach ($n in $sNames) { 
  MakeRealJpeg -filePath "$base\services\$n.jpg" -w 1200 -h 800 -label "ABYNSS - $n" -bgColorHex "#111111" 
}

# Articles
for ($i = 1; $i -le 3; $i++) {
  $num = $i.ToString('D2')
  MakeRealJpeg -filePath "$base\articles\article-$num.jpg" -w 1200 -h 800 -label "ABYNSS - Article $num" -bgColorHex "#111111"
}

# Activities
for ($i = 1; $i -le 3; $i++) {
  $num = $i.ToString('D2')
  MakeRealJpeg -filePath "$base\activities\activity-$num.jpg" -w 1200 -h 800 -label "ABYNSS - Activity $num" -bgColorHex "#111111"
  MakeRealJpeg -filePath "$base\activities\activity-$num-2.jpg" -w 1200 -h 800 -label "ABYNSS - Activity $num B" -bgColorHex "#111111"
}

# Testimonials
for ($i = 1; $i -le 6; $i++) {
  $num = $i.ToString('D2')
  MakeRealJpeg -filePath "$base\testimonials\avatar-$num.jpg" -w 200 -h 200 -label "AV $num" -bgColorHex "#181818"
}

# About
MakeRealJpeg -filePath "$base\about\author.jpg" -w 200 -h 200 -label "Author" -bgColorHex "#181818"
MakeRealJpeg -filePath "$base\about\studio.jpg" -w 1200 -h 1500 -label "Studio" -bgColorHex "#111111"
MakeRealJpeg -filePath "$base\about\photographer.jpg" -w 1200 -h 1500 -label "Photographer" -bgColorHex "#111111"

# OG
MakeRealJpeg -filePath "$base\og\og-home.jpg" -w 1200 -h 630 -label "ABYNSS STUDIO" -bgColorHex "#0D0D0D"

Write-Host "All placeholder images regenerated as REAL JPEGs!"
