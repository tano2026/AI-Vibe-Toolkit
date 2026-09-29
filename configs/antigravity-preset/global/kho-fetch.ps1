<#
  kho-fetch.ps1 — đọc kho AI-Vibe-Toolkit (repo private) bằng token READ-ONLY.
  Token lấy từ biến môi trường KHO_READONLY_TOKEN. Agent KHÔNG cần thấy giá trị token.

  Dùng:
    kho-fetch.ps1 KHO-INDEX.md                 # đọc 1 file
    kho-fetch.ps1 repos                        # liệt kê 1 thư mục
    kho-fetch.ps1 -Search "design|taste"       # tìm đường dẫn khớp regex (bỏ qua /content)
#>
param(
  [Parameter(Position=0)][string]$Path,
  [string]$Search,
  [int]$Max = 40
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$Repo = 'tano2026/AI-Vibe-Toolkit'
$Tok = $env:KHO_READONLY_TOKEN
if (-not $Tok) { Write-Error 'Chua set KHO_READONLY_TOKEN. Bao Nobitano lam theo README (buoc 3).'; exit 1 }
$H = @{ Authorization = "token $Tok"; Accept = 'application/vnd.github.v3+json'; 'User-Agent' = 'antigravity-kho' }

if ($Search) {
  $t = Invoke-RestMethod -Headers $H -Uri "https://api.github.com/repos/$Repo/git/trees/main?recursive=1"
  $t.tree | Where-Object { $_.type -eq 'blob' -and $_.path -match $Search -and $_.path -notlike 'content/*' } |
    Select-Object -First $Max -ExpandProperty path
  exit 0
}
if (-not $Path) { Write-Error 'Dung: kho-fetch.ps1 <path>  hoac  kho-fetch.ps1 -Search <regex>'; exit 1 }

$r = Invoke-RestMethod -Headers $H -Uri "https://api.github.com/repos/$Repo/contents/$Path"
if ($r -is [array]) { $r | ForEach-Object { "$($_.type)`t$($_.path)" }; exit 0 }
[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(($r.content -replace '\s','')))
