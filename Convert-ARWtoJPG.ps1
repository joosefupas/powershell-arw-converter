param (
    [string]$inputDir = $(throw "Input directory parameter required."),
    [string]$outputDir = $(throw "Output directory parameter required.")
)

# Check that the ImageMagick "convert" command is available
if (!(Test-Path "magick.exe")) {
    Write-Host "Error: ImageMagick is not installed or the 'magick.exe' command is not in the system path." -ForegroundColor Red
    Exit
}

# Check that the input and output directories exist
if (!(Test-Path $inputDir -PathType Container)) {
    Write-Host "Error: Input directory not found." -ForegroundColor Red
    Exit
}
if (!(Test-Path $outputDir -PathType Container)) {
    Write-Host "Error: Output directory not found." -ForegroundColor Red
    Exit
}

# Get the list of ARW files in the input directory
$arw_files = Get-ChildItem -Path $inputDir -Filter *.arw

# Convert each ARW file to JPG format with quality 100
foreach ($arw_file in $arw_files) {
    $jpg_file = Join-Path $outputDir ($arw_file.BaseName + ".jpg")
    $convert_command = "magick.exe `"$($arw_file.FullName)`" -quality 100 `"$jpg_file`""
    Write-Host "Converting $($arw_file.FullName) to $($jpg_file)..."
    Invoke-Expression $convert_command
}

Write-Host "Conversion complete." -ForegroundColor Green
