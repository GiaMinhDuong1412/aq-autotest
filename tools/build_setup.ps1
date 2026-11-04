# Tạo bộ cài AQ-AutoTest-Setup-<ver>.exe từ AQ-AutoTest-<ver>-windows.zip (chạy trên Windows, GitHub Actions gọi).
#   pwsh tools/build_setup.ps1 -Ver 2026.11.04-2 [-Dist dist]
param([Parameter(Mandatory = $true)][string]$Ver, [string]$Dist = "dist")
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$dist = Resolve-Path (Join-Path $root $Dist)
$build = Join-Path $root "build"
if (Test-Path $build) { Remove-Item $build -Recurse -Force }
Expand-Archive (Join-Path $dist "AQ-AutoTest-$Ver-windows.zip") -DestinationPath $build
$iscc = Join-Path ${env:ProgramFiles(x86)} "Inno Setup 6\ISCC.exe"
if (-not (Test-Path $iscc)) {
  Write-Host "Cài Inno Setup…"
  choco install innosetup --no-progress -y | Out-Null
}
& $iscc /Qp "/DMyVer=$Ver" "/DSrcDir=$build\AQ-AutoTest" "/DOutDir=$dist" (Join-Path $root "app\aq-autotest.iss")
if ($LASTEXITCODE) { throw "ISCC lỗi $LASTEXITCODE" }
Get-ChildItem $dist "AQ-AutoTest-Setup-*.exe" | ForEach-Object { Write-Host ("Bộ cài: {0} ({1:N0} KB)" -f $_.Name, ($_.Length / 1KB)) }
