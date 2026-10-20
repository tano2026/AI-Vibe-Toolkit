# Auto-push local skills to GitHub & Local Sync
$ErrorActionPreference = "Stop"
# Repo = thu muc cha cua configs/ (khong hard-code duong dan may); fallback ve duong dan cu neu chay tu noi khac
$RepoPath = if ($PSScriptRoot) { Split-Path -Parent $PSScriptRoot } else { "C:\Users\Nguyen Ngoc Tan\AI-Vibe-Toolkit" }
if (!(Test-Path "$RepoPath\.git")) { throw "Khong phai git repo: $RepoPath" }
Set-Location $RepoPath

# 1. Sync skills locally to Hermes & OpenClaw
$RootSkills = Get-ChildItem -Path "$RepoPath\skills" -Directory
foreach ($dir in $RootSkills) {
    $name = $dir.Name
    if (Test-Path "$($dir.FullName)\SKILL.md") {
        # Hermes
        $hermesDir = "C:\Users\Nguyen Ngoc Tan\AppData\Local\hermes\skills\$name"
        if (!(Test-Path $hermesDir)) { New-Item -ItemType Directory -Path $hermesDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$hermesDir\SKILL.md" -Force
        # OpenClaw
        $openclawDir = "C:\Users\Nguyen Ngoc Tan\.openclaw\skills\$name"
        if (!(Test-Path $openclawDir)) { New-Item -ItemType Directory -Path $openclawDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$openclawDir\SKILL.md" -Force
    }
}

$AgentSkills = Get-ChildItem -Path "$RepoPath\agents\*\skills\*" -Directory
foreach ($dir in $AgentSkills) {
    $name = $dir.Name
    if (Test-Path "$($dir.FullName)\SKILL.md") {
        # Hermes
        $hermesDir = "C:\Users\Nguyen Ngoc Tan\AppData\Local\hermes\skills\$name"
        if (!(Test-Path $hermesDir)) { New-Item -ItemType Directory -Path $hermesDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$hermesDir\SKILL.md" -Force
        # OpenClaw
        $openclawDir = "C:\Users\Nguyen Ngoc Tan\.openclaw\skills\$name"
        if (!(Test-Path $openclawDir)) { New-Item -ItemType Directory -Path $openclawDir -Force | Out-Null }
        Copy-Item -Path "$($dir.FullName)\SKILL.md" -Destination "$openclawDir\SKILL.md" -Force
    }
}

# 2. Chi stage thu muc skill (khong `git add .` de tranh commit nham file khac/bi mat), roi push
git add -- skills agents

$status = git status --porcelain -- skills agents
if ($status) {
    $branch = (git rev-parse --abbrev-ref HEAD).Trim()
    if ($branch -ne "main") { throw "Dang o nhanh '$branch', khong phai main - khong tu commit/push." }
    $date = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    git commit -m "Auto-sync skills: $date"
    if ($LASTEXITCODE -ne 0) { throw "git commit that bai" }
    git push origin main
    if ($LASTEXITCODE -ne 0) { throw "git push that bai" }
}
