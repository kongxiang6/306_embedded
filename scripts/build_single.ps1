param(
    [Parameter(Mandatory = $true)]
    [string]$PayloadDir,

    [string]$SpecPath = "packaging/306_single.spec"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$resolvedPayload = Resolve-Path -LiteralPath $PayloadDir
$env:APP_PAYLOAD_DIR = $resolvedPayload.Path
$resolvedSpec = if ([System.IO.Path]::IsPathRooted($SpecPath)) {
    $SpecPath
} else {
    Join-Path $RepoRoot $SpecPath
}

Push-Location $RepoRoot
try {
    pyinstaller --clean --noconfirm $resolvedSpec
}
finally {
    Pop-Location
}
