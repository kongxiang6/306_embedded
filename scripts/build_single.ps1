param(
    [Parameter(Mandatory = $true)]
    [string]$PayloadDir,

    [string]$SpecPath = "packaging/306_single.spec"
)

$ErrorActionPreference = "Stop"

$resolvedPayload = Resolve-Path -LiteralPath $PayloadDir
$env:APP_PAYLOAD_DIR = $resolvedPayload.Path

pyinstaller --clean --noconfirm $SpecPath
