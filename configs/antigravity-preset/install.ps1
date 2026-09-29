<#
.SYNOPSIS
  Cài Tano preset vào Google Antigravity: luật toàn cục + 1 project.
.EXAMPLE
  .\install.ps1 -Project D:\tano-tuvi-platform -DryRun     # xem trước, không ghi gì
  .\install.ps1 -Project D:\tano-tuvi-platform             # cài thật
  .\install.ps1 -Project D:\tano-tuvi-platform -AgentDir .agents   # nếu bản Antigravity của mày dùng .agents
#>
param(
  [Parameter(Mandatory=$true)][string]$Project,
  [string]$AgentDir = '.agent',
  [switch]$Force,
  [switch]$DryRun,
  [switch]$SkipGlobal
)
$ErrorActionPreference = 'Stop'
$Here  = Split-Path -Parent $MyInvocation.MyCommand.Path
$Stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$Begin = '<!-- TANO-PRESET:BEGIN'
$End   = '<!-- TANO-PRESET:END -->'
$Utf8  = New-Object Text.UTF8Encoding($false)

function Say($m) { Write-Host $m }
function Do-Copy($src, $dst) {
  if (Test-Path $dst) {
    if (-not $Force) { Say "  bo qua (da co): $dst"; return }
    if (-not $DryRun) { Copy-Item $dst "$dst.bak-$Stamp" }
    Say "  ghi de (co backup): $dst"
  } else { Say "  tao: $dst" }
  if (-not $DryRun) {
    New-Item -ItemType Directory -Force -Path (Split-Path $dst) | Out-Null
    Copy-Item $src $dst -Force
  }
}

if (-not (Test-Path $Project)) { throw "Khong thay project: $Project" }
$Project = (Resolve-Path $Project).Path
$Gem = Join-Path $HOME '.gemini'
if ($DryRun) { Say '*** DRY RUN: khong ghi gi ca ***' }

# ---------- GLOBAL ----------
if (-not $SkipGlobal) {
  Say "[GLOBAL] $Gem"
  $block  = (Get-Content (Join-Path $Here 'global\GEMINI.md') -Raw -Encoding UTF8).Trim()
  $target = Join-Path $Gem 'GEMINI.md'
  if (Test-Path $target) {
    $cur = Get-Content $target -Raw -Encoding UTF8
    if (-not $DryRun) { Copy-Item $target "$target.bak-$Stamp" }
    $i = $cur.IndexOf($Begin); $j = $cur.IndexOf($End)
    if ($i -ge 0 -and $j -gt $i) {
      $new = $cur.Substring(0, $i) + $block + $cur.Substring($j + $End.Length)
      Say '  cap nhat block Tano trong GEMINI.md (co backup)'
    } else {
      $new = $cur.TrimEnd() + "`r`n`r`n" + $block + "`r`n"
      Say '  them block Tano vao cuoi GEMINI.md (co backup)'
    }
  } else { $new = $block + "`r`n"; Say '  tao GEMINI.md' }
  if (-not $DryRun) {
    New-Item -ItemType Directory -Force -Path $Gem | Out-Null
    [IO.File]::WriteAllText($target, $new, $Utf8)
  }
  Do-Copy (Join-Path $Here 'global\kho-fetch.ps1') (Join-Path $Gem 'scripts\kho-fetch.ps1')
}

# ---------- PROJECT ----------
Say "[PROJECT] $Project"
$src = Join-Path $Here 'project'
$ad  = Join-Path $Project $AgentDir

$agentsDst = Join-Path $Project 'AGENTS.md'
if (Test-Path $agentsDst) {
  $agentsDst = Join-Path $Project 'AGENTS.tano-preset.md'
  Say '  AGENTS.md da co -> ghi mau vao AGENTS.tano-preset.md, tu gop tay'
}
Do-Copy (Join-Path $src 'AGENTS.md') $agentsDst

$srcAgent = Join-Path $src '.agent'
foreach ($f in Get-ChildItem $srcAgent -Recurse -File) {
  $rel = $f.FullName.Substring($srcAgent.Length).TrimStart('\', '/')
  Do-Copy $f.FullName (Join-Path $ad $rel)
}

# config.yml: khong tu commit (Antigravity va DSH dung chung repo)
$cfg = Join-Path $ad 'config.yml'
if (-not (Test-Path $cfg)) {
  Say "  tao: $cfg (auto_commit: false)"
  if (-not $DryRun) { [IO.File]::WriteAllText($cfg, "auto_commit: false`r`n", $Utf8) }
}

# .gitignore: bao dam .env khong bi commit
$gi = Join-Path $Project '.gitignore'
$giText = ''
if (Test-Path $gi) { $giText = Get-Content $gi -Raw -Encoding UTF8 }
$need = @()
foreach ($line in @('.env', '.env.*')) {
  if ($giText -notmatch ('(?m)^' + [regex]::Escape($line) + '\s*$')) { $need += $line }
}
if ($need.Count -gt 0) {
  Say ('  .gitignore: them ' + ($need -join ', '))
  if (-not $DryRun) { [IO.File]::AppendAllText($gi, "`r`n" + ($need -join "`r`n") + "`r`n", $Utf8) }
}

Say ''
Say 'XONG. Buoc tiep theo:'
Say '  1) Mo lai Antigravity, mo project, vao Customizations kiem tra Rules / Workflows / Skills da hien.'
Say '  2) Tao token READ-ONLY cho kho (xem README buoc 3), tu chay lenh dat bien moi truong.'
Say '  3) Test: go /kho design-md trong chat cua Antigravity.'
